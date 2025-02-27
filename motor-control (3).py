import RPi.GPIO as GPIO
import time
import serial
import threading


IN1 = 17
IN2 = 27
IN3 = 23
IN4 = 24
TRIGGER_PIN = 5
ECHO_PIN = 6


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)
GPIO.setup(TRIGGER_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)


def get_distance():
    GPIO.output(TRIGGER_PIN, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIGGER_PIN, GPIO.LOW)

    pulse_start = time.time()
    while GPIO.input(ECHO_PIN) == 0:
        pulse_start = time.time()

    pulse_end = time.time()
    while GPIO.input(ECHO_PIN) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    return round(distance, 2)

def move_forward():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)

def move_backward():
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)

def turn_left():
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)

def turn_right():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)

def stop_motors():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)

def process_command(command):
    if command == 'F0':
        move_forward()
    elif command == 'B0':
        move_backward()
    elif command == 'L0':
        turn_left()
    elif command == 'R0':
        turn_right()
    else:
        stop_motors()

bluetooth = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
bluetooth.flush()

def distance_monitor():
    while True:
        distance = get_distance()
        if distance < 20:   
            print(f"Engel  Mesafe: {distance} cm. Motorlar durduruluyor.")
            stop_motors()
        time.sleep(0.1)
def bluetooth_control():
    while True:
        if bluetooth.in_waiting > 0:
            command = bluetooth.readline().decode('utf-8', errors='ignore').strip()
            print(f"Gelen Veri: {command}")
            process_command(command)

try:
    distance_thread = threading.Thread(target=distance_monitor)
    bluetooth_thread = threading.Thread(target=bluetooth_control)

    distance_thread.daemon = True
    bluetooth_thread.daemon = True

    distance_thread.start()
    bluetooth_thread.start()

    while True:
        time.sleep(1)

except KeyboardInterrupt:
    stop_motors()
finally:
    GPIO.cleanup()