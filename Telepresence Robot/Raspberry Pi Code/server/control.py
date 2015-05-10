import RPi.GPIO as GPIO
import sys
import socket
import serial
from time import sleep
TCP_IP =your wifi module ip address
TCP_PORT =yout wifi module port address
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)#4
GPIO.setup(11, GPIO.OUT)#17
GPIO.setup(15, GPIO.OUT)#22
GPIO.setup(16, GPIO.OUT)#23
ser=serial.Serial("/dev/ttyAMA0",baudrate=9600, timeout=3)
tcpsocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsocket.connect((TCP_IP, TCP_PORT))
k=int(sys.argv[1])

if k==0:
	GPIO.output(11, GPIO.HIGH)
	GPIO.output(7, GPIO.LOW)
	GPIO.output(15, GPIO.HIGH)
	GPIO.output(16, GPIO.LOW)
elif k==1:
	GPIO.output(11, GPIO.LOW)
	GPIO.output(7, GPIO.HIGH)
	GPIO.output(15, GPIO.LOW)
	GPIO.output(16, GPIO.HIGH)
elif k==2:
	GPIO.output(11, GPIO.HIGH)
	GPIO.output(7, GPIO.LOW)
	GPIO.output(15, GPIO.LOW)
	GPIO.output(16, GPIO.HIGH)
elif k==3:
	GPIO.output(11, GPIO.LOW)
	GPIO.output(7, GPIO.HIGH)
	GPIO.output(15, GPIO.HIGH)
	GPIO.output(16, GPIO.LOW)
elif k==4:
	GPIO.output(11, GPIO.LOW)
	GPIO.output(7, GPIO.LOW)
	GPIO.output(15, GPIO.LOW)
	GPIO.output(16, GPIO.LOW)
elif k==5:
	tcpsocket.send(bytes("On1", 'UTF-8'))
	tcpsocket.close()

elif k==6:
	tcpsocket.send(bytes("Off1", 'UTF-8'))
	tcpsocket.close()

sleep(50); 
GPIO.output(11, GPIO.LOW)
GPIO.output(7, GPIO.LOW)
GPIO.output(15, GPIO.LOW)
GPIO.output(16, GPIO.LOW)

