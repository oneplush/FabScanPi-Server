__author__ = "Mario Lukas"
__copyright__ = "Copyright 2017"
__license__ = "GPL v2"
__maintainer__ = "Mario Lukas"
__email__ = "info@mariolukas.de"

class Laser:
    def __init__(self, serial_object):
        self.serial_connection = serial_object
        self.laser_is_on = False

    def on(self, laser=0):
        if (laser != None) and (self.serial_connection != None) and not self.laser_is_on:
            if laser == 0:
                command = "M21;"
            else:
                command = "M19;"

            self.serial_connection.send_and_receive(command)
            self.laser_is_on = True

    def off(self, laser=0):
        if (laser != None) and (self.serial_connection != None) and self.laser_is_on:
            if laser == 0:
                command = "M22;"
            else:
                command = "M20;"

            self.serial_connection.send_and_receive(command)
            self.laser_is_on = False