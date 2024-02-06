### Facade

class CPU:
    def start(self):
        pass


class Memory:
    def load(self):
        pass


class HardDrive:
    def read(self):
        pass

    def write(self):
        pass


class PowerSupply:
    def turn_on(self):
        pass

    def turn_off(self):
        pass


class Computer:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hard_drive = HardDrive()
        self.power_supply = PowerSupply()

    def start(self):
        self.cpu.start()
        self.memory.load()
        self.hard_drive.read()
        self.power_supply.turn_on()

    def shutdown(self):
        self.hard_drive.write()
        self.power_supply.turn_off()


computer = Computer()
computer.start()
