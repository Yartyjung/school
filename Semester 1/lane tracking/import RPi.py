import RPi.GPIO as GPIO
from time import sleep

# Pins for Motor Driver Inputs 
Motor1A = 12 
Motor1B = 13
Motor1E = 6

Motor2A = 21
Motor2B = 20
Motor2E = 26

def setup():
    GPIO.setmode(GPIO.BCM)# GPIO Numbering
    GPIO.setup(Motor1A,GPIO.OUT)  # All pins as Outputs
    GPIO.setup(Motor1B,GPIO.OUT)
    GPIO.setup(Motor1E,GPIO.OUT)
    GPIO.setup(Motor2A,GPIO.OUT)  # All pins as Outputs
    GPIO.setup(Motor2B,GPIO.OUT)
    GPIO.setup(Motor2E,GPIO.OUT)
    Motor1_pwm = GPIO.PWM(Motor1E,50)
    Motor2_pwm = GPIO.PWM(Motor2E,50)
    Motor1_pwm.start(0)
    Motor2_pwm.start(0)

def loop():
    # Going forwards
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.LOW)
    GPIO.output(Motor1E,GPIO.HIGH)
    
    GPIO.output(Motor2A,GPIO.HIGH)
    GPIO.output(Motor2B,GPIO.LOW)
    GPIO.output(Motor2E,GPIO.HIGH)

    sleep(5)
    # Going backwards
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.HIGH)
    GPIO.output(Motor1E,GPIO.HIGH)
    
    GPIO.output(Motor2A,GPIO.LOW)
    GPIO.output(Motor2B,GPIO.HIGH)
    GPIO.output(Motor2E,GPIO.HIGH)

    sleep(5)
    # Stop
    GPIO.output(Motor1E,GPIO.LOW)
    GPIO.output(Motor2E,GPIO.LOW)
    
def forward(pwm):
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.LOW)
    Motor1_pwm.ChangeDutyCycle(pwm)
    
    GPIO.output(Motor2A,GPIO.HIGH)
    GPIO.output(Motor2B,GPIO.LOW)
    Motor2_pwm.ChangeDutyCycle(pwm)
    
def backward(pwm):
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.HIGH)
    Motor1_pwm.ChangeDutyCycle(pwm)
    
    GPIO.output(Motor2A,GPIO.LOW)
    GPIO.output(Motor2B,GPIO.HIGH)
    Motor2_pwm.ChangeDutyCycle(pwm)
    
def forward_curve(pwm1,pwm2):
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.LOW)
    Motor1_pwm.ChangeDutyCycle(pwm1)
    
    GPIO.output(Motor2A,GPIO.HIGH)
    GPIO.output(Motor2B,GPIO.LOW)
    Motor2_pwm.ChangeDutyCycle(pwm2)
    
def backward_curve(pwm1,pwm2):
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.HIGH)
    Motor1_pwm.ChangeDutyCycle(pwm1)
    
    GPIO.output(Motor2A,GPIO.LOW)
    GPIO.output(Motor2B,GPIO.HIGH)
    Motor2_pwm.ChangeDutyCycle(pwm2)
    
def turn_left(pwm):
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.HIGH)
    Motor1_pwm.ChangeDutyCycle(100)
    
    GPIO.output(Motor2A,GPIO.HIGH)
    GPIO.output(Motor2B,GPIO.LOW)
    Motor2_pwm.ChangeDutyCycle(pwm)
    
def full_turn_left(pwm):
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.HIGH)
    Motor1_pwm.ChangeDutyCycle(pwm)
    
    GPIO.output(Motor2A,GPIO.HIGH)
    GPIO.output(Motor2B,GPIO.LOW)
    Motor2_pwm.ChangeDutyCycle(pwm)
    
def turn_right(pwm):
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.LOW)
    Motor1_pwm.ChangeDutyCycle(pwm)
    
    GPIO.output(Motor2A,GPIO.HIGH)
    GPIO.output(Motor2B,GPIO.HIGH)
    Motor2_pwm.ChangeDutyCycle(100)

def full_turn_right(pwm):
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.LOW)
    Motor1_pwm.ChangeDutyCycle(pwm)
    
    GPIO.output(Motor2A,GPIO.LOW)
    GPIO.output(Motor2B,GPIO.HIGH)
    Motor2_pwm.ChangeDutyCycle(pwm)
    
def stop():
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.LOW)
    Motor1_pwm.ChangeDutyCycle(0)
    
    GPIO.output(Motor2A,GPIO.LOW)
    GPIO.output(Motor2B,GPIO.LOW)
    Motor2_pwm.ChangeDutyCycle(0)
    
def stop_lock():
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.HIGH)
    Motor1_pwm.ChangeDutyCycle(100)
    
    GPIO.output(Motor2A,GPIO.HIGH)
    GPIO.output(Motor2B,GPIO.HIGH)
    Motor2_pwm.ChangeDutyCycle(100)



def destroy():
    GPIO.cleanup()

if __name__ == '__main__':     # Program start from here
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()