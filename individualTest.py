import RPi.GPIO as GPIO          
from time import sleep

#Back Motor Motion
in1 = 23
in2 = 24
ena = 25

#Front Motor Motion
in3 = 12#8
in4 = 16#7
enb = 20#1

#Direction
in5 = 26
in6 = 21
enc = 19

temp1=1

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(in5,GPIO.OUT)
GPIO.setup(in6,GPIO.OUT)

GPIO.setup(ena,GPIO.OUT)
GPIO.setup(enb,GPIO.OUT)
GPIO.setup(enc,GPIO.OUT)

GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
GPIO.output(in5,GPIO.LOW)
GPIO.output(in6,GPIO.LOW)


p1=GPIO.PWM(ena,1000) #back motor
p2=GPIO.PWM(enb,1000) #front motor
p3=GPIO.PWM(enc,1000) #direction

p1.start(25)
p2.start(25)
p3.start(45)
#p.start controls how fast car goes and how much it turns

print("\n")
print("\n")     

while(1):

    x=input()
    
    if x=='r':
        print("run")
        if(temp1==1):
         GPIO.output(in1,GPIO.HIGH)
         GPIO.output(in2,GPIO.LOW)
         GPIO.output(in3,GPIO.HIGH)
         GPIO.output(in4,GPIO.LOW)
         print("forward")
         x='z'
         
    elif x=='s':
        print("stop")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
        GPIO.output(in5,GPIO.LOW)
        GPIO.output(in6,GPIO.LOW)
        x='z'    

    elif x=='bf':
        print("backForward")
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        temp1=1
        x='z'

    elif x=='bb':
        print("backBackward")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        temp1=0
        x='z'
        
    elif x=='ff':
        print("frontForward")
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
        temp1=1
        x='z'

    elif x=='fb':
        print("frontBackward")
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)
        temp1=0
        x='z'    
        
                
    elif x=='dr':
        print("directionRight")
        GPIO.output(in5,GPIO.HIGH)
        GPIO.output(in6,GPIO.LOW)
        temp1=1
        x='z'

    elif x=='dl':
        print("directionLeft")
        GPIO.output(in5,GPIO.LOW)
        GPIO.output(in6,GPIO.HIGH)
        temp1=0
        x='z'   

    elif x=='l':
        print("low")
        p1.ChangeDutyCycle(25)
        x='z'

    elif x=='m':
        print("medium")
        p1.ChangeDutyCycle(50)
        x='z'

    elif x=='h':
        print("high")
        p1.ChangeDutyCycle(75)
        x='z'
        
    elif x=='e':
        GPIO.cleanup()
        break
    
    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")
    
  
