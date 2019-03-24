import serial
import requests

#use requests to send data to a url (want it to be a post)

connected = False
ser = serial.Serial(
    port = '/dev/tty96B0', #/dev/ttyUSB0 on Linux
    baudrate = 9600, #9600 on the DragonBoard
    timeout = 3
)
if not ser.isOpen():
    ser.open()
if ser.isOpen():
    print(ser.name + " is Open!")
    connected = True

#we want to send the request when the button is pushed but how do we know when the button is pushed
#we cant have the button press in arduino activate the request because its the wrong program

while connected == True:
    if ser.inWaiting() > 0:
        reading = ser.readline().decode('ascii')
        print(reading, end='')
        if reading == 'Cool':
            request = requests.post('https://litme.net/api/dinner')
