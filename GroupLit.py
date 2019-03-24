import serial
import requests

#use requests to send data to a url (want it to be a post)

connected = False
ser = serial.Serial(
    port = 'dev/tty96B0', #/dev/ttyUSB0 on Linux
    baudrate = 9600, #9600 on the DragonBoard
    timeout = 3
)
ser.open()
if ser.isOpen():
    print(ser.name + " is Open!")
    connected = True

#we want to send the request when the button is pushed but how do we know when the button is pushed
#we cant have the button press in arduino activate the request because its the wrong program

while connected == True:
    print('Test')
    if ser.inWaiting() > 0:
        reading = ser.readline().decode('ascii')
        print(reading, end='')
    data = {'key1' : 'value1', 'key2' : 'value2'}
    request = requests.post('https://litme.net/api/dinner', data=data)
    status = request.status_code
    print("status is: ", status)
