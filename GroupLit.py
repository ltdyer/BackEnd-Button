import serial
import requests

#use requests to send data to a url (want it to be a post)

connected = False
ser = serial.Serial(
    port = '/dev/tty96B0', #/dev/ttyUSB0 on Linux
    baudrate = 9600, #9600 on the DragonBoard
    timeout = 3
)
ser.open()
if ser.isOpen():
    print(ser.name + " is Open!")
    connected = True


while connected == True:
    print('Test')
    if ser.inWaiting() >= 0:
        reading = ser.read(ser.inWaiting()).decode('ascii')
        print(reading, end='')
    #other code