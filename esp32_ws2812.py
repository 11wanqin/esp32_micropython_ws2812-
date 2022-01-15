# -*- coding: utf-8 -*-
from machine import UART
import neopixel
import time
from machine import Pin
import random


# 32 LED strip connected to X8.
p = Pin(27, Pin.OUT) 
n = neopixel.NeoPixel(p, 1)
#uart1 = UART(1, baudrate=115200, tx=1, rx=3)

# Draw a red gradient.
base_light=20
sum_1=200-base_light
step_num=1
loop_num=int(sum_1 / step_num)
g_start=random.randint(1, loop_num-1)
b_start=random.randint(1, loop_num-1)
i=1

flag=1
flag_g=1
flag_b=1

delay_time=70



while True:
    i=i+flag
    g_start=g_start+flag_g
    b_start=b_start+flag_b
    time.sleep_ms(delay_time)
    
    n[0] = (i*step_num+base_light,g_start*step_num+base_light , b_start*step_num+base_light)
#    print(i ,",",g_start,",",b_start)

    n.write()
    if i == loop_num or i == 1:
        flag=-flag
    if g_start == loop_num or g_start == 1 :
        flag_g=-flag_g
        if g_start == 1:
            g_start=2
    if b_start == loop_num or b_start == 1:
        flag_b=-flag_b
        if b_start == 1:
            b_start=3
    
# Update the strip.
