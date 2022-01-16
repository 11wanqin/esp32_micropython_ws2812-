from machine import UART
from machine import Timer
import micropython
import neopixel
import time
from machine import Pin
import random
import machine

class Gradually_led():
    
    def __init__(self,ledtimer=0, pin=27,num=1):
        self.base_light=20 #最低亮度
        self.sum_1=200-self.base_light
        self.step_num=1
        self.loop_num=int(self.sum_1 / self.step_num)
        self.g_start=random.randint(1, self.loop_num-1)
        self.b_start=random.randint(1, self.loop_num-1)
        self.i=1
        self.flag=1
        self.flag_g=1
        self.flag_b=1
        self.delay_time=70
        self.pin=pin
        self.num=num
        self.state=0
        self.init_ws2812()
        timer=Timer(0)
        timer.init(period=self.delay_time,callback=self.cb)
 #       irq_state = machine.disable_irq(


        
    def init_ws2812(self):
        self.p = Pin(self.pin, Pin.OUT) 
        self.n = neopixel.NeoPixel(self.p, self.num)

    
    def cb(self,tim):
        self.i=self.i+self.flag
        self.g_start=self.g_start+self.flag_g
        self.b_start=self.b_start+self.flag_b
        self.state=1
        
    def display(self):
        if self.state == 1:
            
            self.n[0] = (self.i*self.step_num+self.base_light,self.g_start*self.step_num+self.base_light , self.b_start*self.step_num+self.base_light)
            self.n.write()
            irq_state = machine.disable_irq()
            if self.i >= self.loop_num or self.i <= 1:
                self.flag=-self.flag
            if self.g_start >= self.loop_num or self.g_start <= 1 :
                self.flag_g=-self.flag_g
                if self.g_start <= 1:
                    self.g_start=2
            if self.b_start >= self.loop_num or self.b_start <= 1:
                self.flag_b=-self.flag_b
                if self.b_start <= 1:
                    self.b_start=3
        #print(self.i,self.g_start,self.b_start)
            self.state=0
            machine.enable_irq(irq_state)
        
