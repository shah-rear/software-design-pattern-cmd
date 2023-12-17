# Yeni bir komut sınıfı ve alıcı sınıfı eklendi
class FanOnCommand(Command):
    def __init__(self, fan):
        self.fan = fan

    def execute(self):
        self.fan.turn_on()

class Fan:
    def turn_on(self):
        print("Fan is ON")

# Yeni komut ve alıcı eklenince...
fan = Fan()
fan_on = FanOnCommand(fan)

# İlk örnekteki gibi bir uzaktan kumandayı kullanarak fanı açabiliriz.
remote.set_command(fan_on)
remote.press_button()
