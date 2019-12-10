#!/usr/bin/env python

import cgi
import cgitb    #display CGI error on browser
import time
import RPi.GPIO as GPIO


def setservo(angle):
    
    one_degree = 0.010444444444444444
    hz = (float(angle) + 90.0) * one_degree
    duty = (hz + 0.5) / 20.0 * 100

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(2, GPIO.OUT)
    servo = GPIO.PWM(2, 50)
    servo.start(0.0)

    servo.ChangeDutyCycle(duty)
    time.sleep(1.0)

print('Content-type: text/html; charset=UTF-8\r\n')
print('Web ServoMotor')

print('<form action="" method="post">')
print('<input type="text" name="deg" value="" maxlength="4">')
print('<input type="submit" value="ok">')
print('</form>')


form = cgi.FieldStorage()
value = form.getvalue("deg")

setservo(int(value))
