class Pulse:
    HIGH = True
    LOW = False

    def __init__(self, origin, destination, magnitude):
        self.origin = origin
        self.destination = destination
        self.magnitude = magnitude

    def is_low(self):
        return not self.magnitude

    def is_high(self):
        return self.magnitude

    def __str__(self):
        return f"{self.origin} [{self.magnitude}] -> {self.destination}"


class Module:
    def __init__(self, name: str, destinations_list: [str]):
        self.name = name
        self.destinations_list = destinations_list

    def send(self, pulse_magnitude):
        return [Pulse(self.name, destination, pulse_magnitude) for destination in self.destinations_list]


class FlipFlopModule(Module):
    def __init__(self, name: str, destinations_list: [str]):
        super().__init__(name, destinations_list)
        
        self.state = False

    def receive(self, pulse: Pulse):
        if pulse.is_low():
            self.state = not self.state
            return self.send(self.state)    

        return []


class BroadcastModule(Module):
    def receive(self, pulse: Pulse):
        return self.send(pulse.magnitude)


class ConjunctionModule(Module):
    def __init__(self, name: str, destinations_list: [str], input_list: [str] = []):
        super().__init__(name, destinations_list)

        self.mem = {input_name: Pulse.LOW for input_name in input_list}
        
    def receive(self, pulse: Pulse):
        self.mem[pulse.origin] = pulse.magnitude

        magnitude = Pulse.LOW

        for name in self.mem:
            if self.mem[name] == Pulse.LOW:
                magnitude = Pulse.HIGH

        return self.send(magnitude)


# Mapping Modules
modules_list = {}

with open("2023/day20/input.txt", 'r') as src:
    line = src.readline()

    while line:
        name, destinations_list = line.replace('\n', '').split(" -> ")
        destinations_list = destinations_list.split(", ")

        match name[0]:
            case 'b':
                modules_list[name] = BroadcastModule(name, destinations_list)
            
            case '%':
                modules_list[name[1:]] = FlipFlopModule(name[1:], destinations_list)

            case '&':
                modules_list[name[1:]] = ConjunctionModule(name[1:], destinations_list)

        line = src.readline()

# Initiating Conjunction Modules
queue = []

for name in modules_list:
    queue += modules_list[name].send(Pulse.LOW)  # Every module emits a low pulse

for pulse in queue:
    if pulse.destination in modules_list and type(modules_list[pulse.destination]) == ConjunctionModule:
        # Each pulse for a Conjunction Module is treated : at the end each Conjunction Module knows its input modules
        modules_list[pulse.destination].receive(pulse)  

# Simulating
sum_high = 0
sum_low = 0

for _ in range(1000):
    queue = [Pulse("button", "broadcaster", Pulse.LOW)]

    while queue:
        pulse = queue.pop(0)

        if pulse.magnitude:
            sum_high += 1
        else:
            sum_low += 1

        if pulse.destination != "rx":
            queue += modules_list[pulse.destination].receive(pulse)

print(sum_high * sum_low)