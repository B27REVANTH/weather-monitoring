from machine import Pin,ADC
import time,utime
from dht import DHT11   
sensor = DHT11(Pin(9,Pin.OUT, Pin.PULL_DOWN))
buz = Pin(15, Pin.OUT)
ss = ADC(27)
ms = ADC(28)
ldr= ADC(26)
trigger = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)
pump1=Pin(18,Pin.OUT)
pump2=Pin(19,Pin.OUT)
rs = machine.Pin(10,machine.Pin.OUT)
e = machine.Pin(11,machine.Pin.OUT)
d4 = machine.Pin(12,machine.Pin.OUT)
d5 = machine.Pin(13,machine.Pin.OUT)
d6 = machine.Pin(14,machine.Pin.OUT)
d7 = machine.Pin(15,machine.Pin.OUT)
def get_distance():
   trigger.low()
   utime.sleep_us(2)
   trigger.high()
   utime.sleep_us(5)
   trigger.low()
   while echo.value() == 0:
       signaloff = utime.ticks_us()
   while echo.value() == 1:
       signalon = utime.ticks_us()
   timepassed = signalon - signaloff
   dist = (timepassed * 0.0343) / 2
   return dist
def pulseE():
    e.value(1)
    utime.sleep_us(40)
    e.value(0)
    utime.sleep_us(40)
def send2LCD4(BinNum):
    d4.value((BinNum & 0b00000001) >>0)
    d5.value((BinNum & 0b00000010) >>1)
    d6.value((BinNum & 0b00000100) >>2)
    d7.value((BinNum & 0b00001000) >>3)
    pulseE()
def send2LCD8(BinNum):
    d4.value((BinNum & 0b00010000) >>4)
    d5.value((BinNum & 0b00100000) >>5)
    d6.value((BinNum & 0b01000000) >>6)
    d7.value((BinNum & 0b10000000) >>7)
    pulseE()
    d4.value((BinNum & 0b00000001) >>0)
    d5.value((BinNum & 0b00000010) >>1)
    d6.value((BinNum & 0b00000100) >>2)
    d7.value((BinNum & 0b00001000) >>3)
    pulseE()
def setUpLCD():
    rs.value(0)
    send2LCD4(0b0011)#8 bit
    send2LCD4(0b0011)#8 bit
    send2LCD4(0b0011)#8 bit
    send2LCD4(0b0010)#4 bit
    send2LCD8(0b00101000)#4 bit,2 lines?,5*8 bots
    send2LCD8(0b00001100)#lcd on, blink off, cursor off.
    send2LCD8(0b00000110)#increment cursor, no display shift
    send2LCD8(0b00000001)#clear screen
    utime.sleep_ms(2)#clear screen needs a long delay

uart0 = machine.UART(0,baudrate=9600,tx=Pin(0),rx=Pin(1))
print(uart0)
second=0
while True:
    #temp = sensor.temperature
    #humidity = sensor.humidity
    time.sleep(1)
    sval = ss.read_u16()/100
    mval = ms.read_u16()/100
    lval = ldr.read_u16()/100
    temp= 33#int(sensor.temperature)
    humidity= 56#int(sensor.humidity)
    #fval=1-fs.value()
    distance=get_distance() #Getting distance in cm
    print(distance)
    print("Temperature: {}°C   Humidity: {:.0f}% ".format(temp, humidity))
    print("SMOKE:"+ str(sval) + "   GAS:" + str(sval1))
    print("s1:"+ str(sval) + " M:" + str(mval))
    print("L:"+ str(lval))
    
    line1="T:"+ str(temp) + " H:" + str(humidity) + " L:" + str(lval)
    line2="s1:"+ str(sval) + " s2:" + str(mval) + " L:" + str(distance)
    
    if(temp>40 or humidity>85 or sval>50 or  sval1>50 or lval<100):
        buz.value(1)
        time.sleep(1)
        buz.value(0)
        time.sleep(1)
    
    setUpLCD()
    rs.value(1)
    for x in line1:
        send2LCD8(ord(x))
        time.sleep(0.02)
    rs.value(0)
    time.sleep(0.02)
    send2LCD8(0b11000000)#clear screen
    time.sleep(0.02)
    
    rs.value(1)
    for x in line2:
        send2LCD8(ord(x))
        time.sleep(0.02)
    
    second=second+1
    
    if(second==16):
        uart0.write(str(temp)+","+str(humidity) + ","+str(sval)+ ","+str(sval1)+ ","+str(lval)+",0\n")
        second=0
        print("uploading")