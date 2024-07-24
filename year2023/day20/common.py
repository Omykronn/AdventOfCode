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
