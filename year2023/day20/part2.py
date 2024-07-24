from year2023.day20.common import Pulse, Module, FlipFlopModule, BroadcastModule, ConjunctionModule
from toolbox.arithmetic import lcd


def prepare(src: str) -> {str: Module}:
    """
    Import data from a file, and format them
    """

    modules_list = {}

    with open(src, 'r') as file:
        for line in file.readlines():
            name, destinations_list = line.replace('\n', '').split(" -> ")
            destinations_list = destinations_list.split(", ")

            match name[0]:
                case 'b':
                    modules_list[name] = BroadcastModule(name, destinations_list)
                
                case '%':
                    modules_list[name[1:]] = FlipFlopModule(name[1:], destinations_list)

                case '&':
                    modules_list[name[1:]] = ConjunctionModule(name[1:], destinations_list)

    return modules_list

def solve(modules_list: {str: Module}) -> int:
    """
    Determine the flag of data
    """

    # Initiating Conjunction Modules
    queue = []

    for name in modules_list:
        queue += modules_list[name].send(Pulse.LOW)  # Every module emits a low pulse

    for pulse in queue:
        if pulse.destination in modules_list and type(modules_list[pulse.destination]) == ConjunctionModule:
            # Each pulse for a Conjunction Module is treated : at the end each Conjunction Module knows its input modules
            modules_list[pulse.destination].receive(pulse)  

    # Parametring
    (merger,) = [name for name in modules_list if "rx" in modules_list[name].destinations_list]
    periods = {}

    # Simulating until the n periods are found
    k = 0

    while len(periods) < len(modules_list[merger].mem):
        k += 1
        queue = [Pulse("button", "broadcaster", Pulse.LOW)]

        while queue:
            pulse = queue.pop(0)

            if pulse.destination != "rx":
                queue += modules_list[pulse.destination].receive(pulse)
            
            if pulse.destination == merger and pulse.magnitude and pulse.origin not in periods:
                periods[pulse.origin] = k

    return lcd(list(periods.values()))
