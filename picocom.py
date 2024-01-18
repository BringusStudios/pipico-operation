#
# This is the library that sits between the Pi Pico and the computer and handles 
# all the serial communication. I wouldn't make changes to this unless you're
# fixing bugs.

import serial
import time

class PiPicoCommunicator:
    def __init__(self, port=None, baudrate=57600, timeout=0.05, debug=False):
        self.debug_flag = debug
        self.start_time = time.time()  # Record the start time
        if self.debug_flag:
            print("PICOCOM DEBUG MSG: Debugging enabled")

        if port is None:
            raise ValueError("PICOCOM: Please specify a COM port.")
        self.ser = serial.Serial(port, baudrate=baudrate, timeout=timeout)
        self.contact_state = False

    def get_uptime(self):
        return time.time() - self.start_time

    def debug(self, msg):
        if self.debug_flag:
            uptime = self.get_uptime()
            print(f"{uptime:.2f} PICOCOM DEBUG MSG: {msg}")

    def read_serial(self):
        try:
            line = self.ser.readline().decode().strip()
        except UnicodeDecodeError as e:
            self.debug(str(e))
            self.debug(" Ran into an error trying to read a line from serial, I'm sending a no_contact and then continuing.")
            return "no_contact"
        if line:
            return line

    def check_state(self):
        message = self.read_serial()

        if message == "contact":
            self.debug("contact message received")
            if not self.contact_state:
                self.contact_state = True
                return "contact"
        elif message == "no_contact":
            self.debug("no_contact message received")
            if self.contact_state:
                self.contact_state = False
                return "no_contact"
        elif message != None:
            self.debug("Unexpected message received: {}".format(message))

        return None

    def send_direct_message(self, message):
        msg = message + '\n'
        self.ser.write(msg.encode('utf-8'))
        self.debug("sent direct message " + message)
        self.ser.flush()

    def send_message(self, action, param1, param2):
        msg = "?{},{},{}!".format(action, param1, param2)
        self.ser.write(msg.encode('utf-8'))
        self.debug("sent direct message " + msg)
        self.ser.flush()

    def rumble(self, motor, power):
        msg = "?rumble," + str(motor) + "," + str(power) + '!'
        self.ser.write(msg.encode('utf-8'))
        self.debug("sent rumble message " + str(msg))
        self.ser.flush()

    def close_connection(self):
        self.ser.close()
