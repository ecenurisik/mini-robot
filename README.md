# mini-robot
Project Description
This project is a smart mini robot using Raspberry Pi and Arduino, capable of obstacle detection, distance measurement and manual control via Bluetooth. The robot detects obstacles around it through ultrasonic sensors and moves safely by changing direction. It also offers manual control via a smartphone thanks to its Bluetooth module. This robot has been made suitable for different usage scenarios with its ability to work both autonomously and user-controlled.

Hardware Used
Raspberry Pi: Used for motor control and Bluetooth connectivity.
Arduino Mega: Used to process sensor data and provide additional features.
HC-SR04 Ultrasonic Sensor: Used for obstacle detection and distance measurement.
L298N Motor Driver Module: Provides control of DC motors.
DC Motors: Provides the movement of the robot.
HC-05 Bluetooth Module: Connects with smartphone and provides manual control.
12V Battery: Used as a power source.
Servo Motor: Used in guidance and obstacle avoidance mechanisms.


Key Features
Obstacle Detection: Detects obstacles in the environment with ultrasonic sensors and measures the distance. When an obstacle is detected, the robot moves in the appropriate direction.
Intelligent Direction Change: When an obstacle is detected, the robot changes direction in the most appropriate way and avoids the obstacle.
Manual and Autonomous Mode: The robot can be controlled manually by the user or operate completely autonomously.
Bluetooth Controlled Movement: The robot's movements can be controlled via smartphone, allowing for more flexible use.
Guidance with Servo Motor: Precise guidance can be made according to obstacle situations.
Raspberry Pi Integration: Motors and sensor data are processed via Raspberry Pi and the motors are controlled.


Installation and Operation
Connect the Hardware: Connect all components used in the project as mentioned above (Arduino, Raspberry Pi, sensors, motors, etc.).
Load the Arduino Code: Load the sketch_dec25a.ino file into the Arduino Mega. This file will perform data reading from sensors, distance calculation and servo motor control.
Run the Raspberry Pi Python Code: Run the motor-control.py file to control the motors connected to the Raspberry Pi.
Establish Bluetooth Connection: Test the manual control functionality by establishing a Bluetooth connection with your smartphone.
Test the Servo Motor: Test the steering mechanism by checking if the servo motor is working correctly.


Code Descriptions
sketch_dec25a.ino: The main software used on the Arduino Mega to read data from sensors, calculate distances and direct the servo motor.
motor-control.py: Python program running on the Raspberry Pi that controls the movement of the motors and processes Bluetooth commands. It also ensures the safe movement of the robot by receiving sensor data.

 This project uses the following packages:
[![Python](https://img.shields.io/badge/python-3.12-000?style=for-the-badge&logo=python&logoColor=white&color=3776AB)](https://www.java.com/en/)
[![Arduino UNO](https://img.shields.io/badge/Arduino%20UNO-C70D2C?style=for-the-badge&logo=arduino&color=00878F)](https://www.arduino.cc/)
[![Raspberry Pi 4B](https://img.shields.io/badge/Raspberry%20Pi%204B-C70D2C?style=for-the-badge&logo=raspberrypi&color=A22846)](https://www.raspberrypi.com/)



Comparison
While this project has some similarities with the “Arduino Obstacle Avoidance Robot Project”, it offers the following advantages:

Bluetooth Control: The user can manually control the robot via Bluetooth with a smartphone.
Smart Direction Changing: When an obstacle is detected, the robot avoids the obstacle by choosing the most appropriate direction.
Raspberry Pi Integration: Data processing and motor control is done by Raspberry Pi, which provides more powerful and faster processing capacity.
Servo Motor Utilization: A servo motor is used to steer the robot, providing more precise and safe movement.


Contribution
Those who wish to contribute to the project can do so by submitting a pull request or by opening an issue related to the project.

License
This project is offered under the MIT License. See the LICENSE file for details.
