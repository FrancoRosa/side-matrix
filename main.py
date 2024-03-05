from time import sleep

import serial
import json
import subprocess

port = "/dev/pts/2"
baud = 9600
id = 1
uppercase = True
chain = 2


dir = "/home/pi/rpi-rgb-led-matrix/examples-api-use/"


def stop_display():
    print("... stop display")
    command = 'sudo pkill -f scrolling-text-example'

    subprocess.run(command, shell=True, stdout=subprocess.PIPE,
                   stderr=subprocess.PIPE, text=True)
    print(command)


def start_display(text, speed, brightness):
    stop_display()
    print("... start display")

    command = 'sudo %s' % (dir) + \
        'scrolling-text-example ' + \
        '--led-cols=64 --led-rows=32 --led-chain=%d ' % chain + \
        '--led-multiplexing=0 --led-slowdown-gpio=5 ' + \
        '--led-brightness=%d ' % brightness + \
        '--led-pwm-dither-bits=2 ' + \
        '-f %sShareTechMono-Regular-30.bdf -y 5 -s %s %s' % (
            dir, speed, text.upper() if uppercase else text)

    subprocess.Popen(command, shell=True)
    print(command)


def get_text(index, speed, brightness):
    with open('texts.json', 'r') as file:
        texts = json.load(file)
        try:
            text = " - ".join(texts[index])
            start_display(text, speed, brightness)
            return text
        except Exception as e:
            print(e)
            return ""


def process_line(line):
    try:
        if int(line[0]) == id:
            index = line[19:22]
            speed = line[22]
            brightness = line[23]
            print(index, speed, brightness)
            brightness = 10*(int(line[23]) + 1)

            print(get_text(index, speed, brightness))
    except Exception as e:
        print(e)
        pass


while True:
    # Configure the serial port
    # Adjust 'COM1' to your serial port and 9600 to the baud rate
    try:
        ser = serial.Serial(port, baud)
        print("Serial port connected.")

        try:
            while True:
                # Read a line of text from the serial port
                line = ser.readline().decode('utf-8').strip()
                process_line(line)
                # Print the received text
                print("Received:", line)

        except KeyboardInterrupt:
            # Close the serial port when the program is interrupted
            ser.close()
            print("Serial port closed.")
            break
    except Exception as e:

        # Print the exception message
        print(f"An error occurred: {e}")
        print("... trying again in 10 secs")

        sleep(10)

# Receive commands on the serial line and get the
# number after the id


# if the id is included on the "text.json"
# display that text on the LED display
