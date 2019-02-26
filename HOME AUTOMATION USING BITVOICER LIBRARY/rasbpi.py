import os
import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)

state = 1;
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)


os.system('flite -t "HOME AUTOMATION ,INITIALISED"'); 

while(state):

    
    device1 = open('relay1.txt','r');
    device2 = open('relay2.txt','r');
    device3 = open('relay3.txt','r');
    device4 = open('relay4.txt','r');
    
    dev1 = device1.read();
    dev2 = device2.read();
    dev3 = device3.read();
    dev4 = device4.read();

    if (dev1=='ON'):
        GPIO.output(5,False)
    if (dev1=='OFF'):
        GPIO.output(5,True)

    if(dev2=='ON'):
        GPIO.output(7,False);
    if(dev2=='OFF'):
         GPIO.output(7,True);
  
    if(dev3=='ON'):
        GPIO.output(11,False);
    if(dev3=='OFF'):
         GPIO.output(11,True);

    if(dev4=='ON'):
        GPIO.output(13,False);
    if(dev4=='OFF'):
         GPIO.output(13,True);
         
    time.sleep(2);          




