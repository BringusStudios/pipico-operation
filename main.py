#
# This is the code that the Pi Pico runs on. You must save this file to the
# Pi Pico as 'main.py' for it to auto-run when the Pico is powered on.

import machine
import sys
import utime
import ustruct
import math
from machine import Pin, PWM
from time import sleep

# create objects for the onboard led and the operation tweezers, which are essentially a button
led = machine.Pin(25, machine.Pin.OUT)
button = machine.Pin(6, machine.Pin.IN, machine.Pin.PULL_UP)
game_led = machine.Pin(14, machine.Pin.OUT)

# set up the usb to serial adapter connection
uart = machine.UART(1, baudrate=57600, tx=8, rx=9)
uart.write("Starting up...\r\n")

# this function is used to create motor objects
def create_motor(pin):
    motor = PWM(Pin(pin))
    motor.freq(1000)
    return motor

# make pins 2, 3, 4, and 5 pwm outputs that will control the 4 motors
m1 = create_motor(2)
m2 = create_motor(3)
m3 = create_motor(4)
m4 = create_motor(5)

# send initial comminucation with the serial adapter to signify the button state
print("PICO DEBUG MSG: no_contact")
uart.write("no_contact\n")
contact_sent_flag = False  # flag to track if "contact" has been sent

# this converts a number in the 0-100 range to a value that the motors understand
def user_to_pwm(value):
    value = math.floor(value)
    return value * 65025 / 100

# these functions are what tells the motor controller to spin the motors
def spin_motor(motor, speed):
    motor.duty_u16(int(user_to_pwm(speed)))

def all_motors(speed):
    spin_motor(m1, speed)
    spin_motor(m2, speed)
    spin_motor(m3, speed)
    spin_motor(m4, speed)
    
# calling rumble() is the correct way you should be interacting with the motors.
# don't drive the pins directly.
def rumble(motor_name, speed):
    motor_functions = {
        "motor1": spin_motor(m1),
        "motor2": spin_motor(m2),
        "motor3": spin_motor(m3),
        "motor4": spin_motor(m4),
        "all_motors": all_motors
    }

    # reference the above table to convert the motor name string into a function reference
    motor_function = motor_functions.get(motor_name)
    if motor_function == None:
        print("\nPICO DEBUG MSG: Motor \'" + motor_name[5:len(motor_name)+1] + "\' could not be found, ignoring...")
        return
    
    # check to make sure the user isn't going to run the motor so slow that it won't work,
    # also if under 16% power is requested it will need to be sent a jolt of 17% power for
    # 100ms to get it moving from a dead stop
    if speed <= 16 and speed > 0 :
        if speed <= 9:
            print("\nPICO DEBUG MSG: Power level too low to run the motor, rounding up to 10")
            speed = 10
        desired_speed = speed
        motor_function(17)
        utime.sleep_ms(100)
        speed = desired_speed
        motor_function(speed)
        print("\nPICO DEBUG MSG: Rumbling \'" + str(motor_name) + "\' at \'" + str(speed) + "\'")
    elif speed > 100:
        print("\nPICO DEBUG MSG: Power level exceeds 100, ignoring...")
    elif speed < 0:
        print("\nPICO DEBUG MSG: Power level is negative, ignoring...")
    else:
        motor_function(speed)
        print("\nPICO DEBUG MSG: Rumbling \'" + str(motor_name) + "\' at \'" + str(speed) + "\'")
        
def process_command(command):
    
    # a proper command sent via serial to the pi pico in plaintext will look like ?rumble,1,20!
    # '?' is the marker to start a command, 'rumble' is the action to perform, '1' is the
    # motor to perform the action on, '20' is the power level of the action, and '!' signifies
    # that the command has been fully sent and we can begin processing it
    
    if command.startswith('?') and command.endswith('!'):
        
        # Remove markers and split the command into action, motor, and power level
        command = command[1:-1]
        try:
            action, motor_name, power_level = command.split(',')
        except ValueError as error:
            print("\nPICO DEBUG MSG: A command was received but incorrectly formatted, ignoring...")
            return
        
        print("\nPICO DEBUG MSG: Got command \'" + action + "\' for motor \'" + motor_name + "\' at power level \'" + power_level + "\'")
        
        # this is where we read the action and run the appropriate code for it. new actions
        # can easily be added by making more elif statements
        
        if action == "rumble":
            if motor_name == "all":
                rumble("all_motors", float(power_level))
            else:
                rumble(("motor" + motor_name), float(power_level))
        elif action == "ping":
            uart.write("pong\r\n")
            print("PICO DEBUG MSG: pong")
        elif action == "crash":
            uart.write("\nTriggering a system crash...\r\n")
            print("\nPICO DEBUG MSG: Triggering a system crash...")
            utime.sleep_ms(100)
            crashing = 8 + "meme"
        else:
            print("\nPICO DEBUG MSG: Action \'" + action + "\' not found, ignoring...")
        
buffer = ''

# main loop
try:
    while True:
        
        # this checks for changes to the button state and reports back when a change happens
        if button.value() == 0:
            if not contact_sent_flag:
                led.value(0)
                print("PICO DEBUG MSG: contact")
                uart.write("contact\n")
                contact_sent_flag = True
                game_led.on()
        else:
            if contact_sent_flag == 1:
                led.value(1)
                print("PICO DEBUG MSG: no_contact")
                uart.write("no_contact\n")
                contact_sent_flag = False
                game_led.off()
        
        # this monitors the incoming serial transmissions for commands
        data = uart.read(1)
        if data:
            try:
                char = data.decode('utf-8')
            except UnicodeError:
                print("\nPICO DEBUG MSG: Couldn't decode data, wtf are you sending me?")

            # Accumulate characters until '?' is received
            if char == '?':
                buffer = char
            elif buffer:
                # Accumulate characters until '!' is received
                buffer += char
                if char == '!':
                    # Process the command
                    process_command(buffer)
                    buffer = ''
        
except KeyboardInterrupt:
    print("\nPICO DEBUG MSG: Program interrupted, exiting...")
except Exception as error:
    print(str(error) + "\nPICO DEBUG MSG: Catastrophic error, rebooting...")
    utime.sleep_ms(100)
    machine.reset()
