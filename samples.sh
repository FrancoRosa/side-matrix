# Run a sample scrolling text
sudo /home/pi/rpi-rgb-led-matrix/examples-api-use/scrolling-text-example --led-cols=64 --led-rows=32 --led-chain=2 --led-multiplexing=0 --led-slowdown-gpio=5 --led-brightness=100 --led-show-refresh --led-pwm-dither-bits=2 -f /home/pi/rpi-rgb-led-matrix/examples-api-use/10x20.bdf Aeropuerto - Molino - Terminal

# Create a pair of connected serial ports for debugging
sudo socat -d -d pty,raw,echo=0 pty,raw,echo=0 &

# Connect to a debugging serial port to send commands
sudo picocom /dev/pts/3 --omap crcrlf