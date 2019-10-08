from abc import ABCMeta, abstractmethod


class Light(object):

    def __init__(self, room=''):
        self.room = room

    def on(self):
        print('{} light is on.'.format(self.room))

    def off(self):
        print('{} light is off.'.format(self.room))


class GarageDoor(object):

    def __init__(self, room=''):
        self.room = room

    def up(self):
        print('{} garage door is up.'.format(self.room))

    def down(self):
        print('{} garage door is down.'.format(self.room))


class Stereo(object):

    def __init__(self, room=''):
        self.room = room

    def on(self):
        print('{} stereo is on.'.format(self.room))

    def off(self):
        print('{} stereo is off.'.format(self.room))

    def set_cd(self):
        print('{} stereo is set for CD input.'.format(self.room))

    def set_volume(self, volume):
        print('{} stereo volume set to {}.'.format(self.room, volume))


class Command(metaclass=ABCMeta):

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class NoCommand(Command):

    def execute(self):
        pass

    def undo(self):
        pass


class LightOnCommand(Command):

    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.on()

    def undo(self):
        self.light.off()


class LightOffCommand(Command):

    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.off()

    def undo(self):
        self.light.on()


class GarageDoorUpCommand(Command):

    def __init__(self, garage_door):
        self.garage_door = garage_door

    def execute(self):
        self.garage_door.up()

    def undo(self):
        self.garage_door.down()


class GarageDoorDownCommand(Command):

    def __init__(self, garage_door):
        self.garage_door = garage_door

    def execute(self):
        self.garage_door.down()

    def undo(self):
        self.garage_door.up()


class StereoOnWithCDCommend(Command):

    def __init__(self, stereo):
        self.stereo = stereo

    def execute(self):
        self.stereo.on()
        self.stereo.set_cd()
        self.stereo.set_volume(11)

    def undo(self):
        self.stereo.off()


class StereoOffCommend(Command):

    def __init__(self, stereo):
        self.stereo = stereo

    def execute(self):
        self.stereo.off()

    def undo(self):
        self.stereo.on()
        self.stereo.set_cd()
        self.stereo.set_volume(11)


class MacroCommand(Command):

    def __init__(self, commands):
        self.commands = commands

    def execute(self):
        for command in self.commands:
            command.execute()

    def undo(self):
        for command in self.commands:
            command.undo()


class RemoteControlWithUndo(object):

    def __init__(self):
        self.on_commands = []
        self.off_commands = []
        self.undo_commend = None

        no_command = NoCommand()
        for i in range(8):
            self.on_commands.append(no_command)
            self.off_commands.append(no_command)
        self.undo_commend = no_command

    def __str__(self):
        res = '\n'
        res += '------ Remote Control ------\n'
        for i in range(len(self.on_commands)):
            res += '[slot{}] {}\t{}\n'.format(i,
            self.on_commands[i].__class__.__name__,
            self.off_commands[i].__class__.__name__)
        res += '[undo] {}\n'.format(self.undo_commend.__class__.__name__)
        return res

    def set_command(self, slot, on_command, off_command):
        self.on_commands[slot] = on_command
        self.off_commands[slot] = off_command

    def on_button_was_pushed(self, slot):
        self.on_commands[slot].execute()
        self.undo_commend = self.on_commands[slot]

    def off_button_was_pushed(self, slot):
        self.off_commands[slot].execute()
        self.undo_commend = self.off_commands[slot]

    def undo_button_was_pushed(self):
        self.undo_commend.undo()


if __name__ == '__main__':
    remote_control = RemoteControlWithUndo()

    living_room_light = Light('Living Room')
    kitchen_light = Light('Kitchen')
    garage_door = GarageDoor('')
    stereo = Stereo('Living Room')

    living_room_light_on = LightOnCommand(living_room_light)
    living_room_light_off = LightOffCommand(living_room_light)
    kitchen_light_on = LightOnCommand(kitchen_light)
    kitchen_light_off = LightOffCommand(kitchen_light)

    garage_door_up = GarageDoorUpCommand(garage_door)
    garage_door_down = GarageDoorDownCommand(garage_door)

    stereo_on_with_cd = StereoOnWithCDCommend(stereo)
    stereo_off = StereoOffCommend(stereo)

    party_on = [living_room_light_on, stereo_on_with_cd]
    party_off = [living_room_light_off, stereo_off]
    party_on_macro = MacroCommand(party_on)
    party_off_macro = MacroCommand(party_off)

    remote_control.set_command(0, living_room_light_on, living_room_light_off)
    remote_control.set_command(1, kitchen_light_on, kitchen_light_off)
    remote_control.set_command(2, stereo_on_with_cd, stereo_off)
    remote_control.set_command(3, party_on_macro, party_off_macro)

    print(remote_control)
    remote_control.on_button_was_pushed(0)
    remote_control.off_button_was_pushed(0)
    print(remote_control)
    remote_control.undo_button_was_pushed()
    remote_control.off_button_was_pushed(0)
    remote_control.on_button_was_pushed(0)
    print(remote_control)
    remote_control.undo_button_was_pushed()

    remote_control.on_button_was_pushed(1)
    remote_control.off_button_was_pushed(1)
    remote_control.on_button_was_pushed(2)
    remote_control.off_button_was_pushed(2)

    print('--- Pushing Macro On ---')
    remote_control.on_button_was_pushed(3)
    print('--- Pushing Macro Off ---')
    remote_control.off_button_was_pushed(3)
