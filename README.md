# WEATHER MONITORING
This is an Raspberry Pi Based project which gives us information about climatic changes that are going to take
place by which man can be aware of present and for future climatic changes.  Most of the weather reporting applications extracts the data from accurate weather system. Here we are building our own weather reporting system which would give us information about present temperature, humidity etc. We can setup this in our home and get time 
to time changes in climate which would help us in planning our daily work easily. Like It would 
be helpful for a farmer in this agricultural activity by which he can protect his crops climatic 
changes. It would help in transportation giving information of weather conditions etc.

## Components Required:
---
• Raspberry Pi Pico W   
• 16×2 I2C LCD Display    
• Connecting Wires    
• Breadboard    
• Micro-USB Cable    
• Gas Sensors    
• Smoke Sensor   
• DHT11(Temperature & Humidity sensors)   
• LDR   

## Required Software Applications: 
---
• Thonny IDE    
• Thing view app  

##How does it work?
---
On the system side Raspberry Pi board operates as a data acquisition mode and as a web server 
mode. It collects data from Temperature and Humidity sensor, Pressure and Altitude sensor, Light 
intensity sensor and rain water Level sensor. This data is then sent to the client side using HTTP 
protocol. On client side real-time data can be seen from anywhere in the world on gecko.com. 
Internet connection to the board is given by using LAN through Ethernet port or by using USB 
dongle through USB port. On this website one channel is created and all six fields are placed in 
this channel.

## Procedure:
---
• Place the breadboard on a flat surface.   

• Connect the DHT11 temperature sensor to the breadboard using jumper wires. Connect the VCC 
  pin to a 3.3V pin on the Raspberry Pi, the GND pin to a GND pin on the Raspberry Pi, and the data 
  pin to GPIO pin 17.   
  
• Connect the DHT11 humidity sensor to the breadboard using jumper wires. Connect the VCC 
  pin to a 3.3V pin on the Raspberry Pi, the GND pin to a GND pin on the Raspberry Pi, and the data 
  pin to GPIO pin 27.   
  
• Connect the first MQ-2 gas sensor to the breadboard using jumper wires. Connect the VCC pin 
  to a 5V pin on the Raspberry Pi, the GND pin to a GND pin on the Raspberry Pi, and the data pin 
  to GPIO pin 18.   
  
• Connect the second MQ-2 gas sensor to the breadboard using jumper wires. Connect the VCC 
  pin to a 5V pin on the Raspberry Pi, the GND pin to a GND pin on the Raspberry Pi, and the data 
  pin to GPIO pin 22.   
  
• If you are using an Ethernet cable, plug one end into the Ethernet port on the Raspberry Pi and 
  the other end into your router or modem.   
  
• If you are using a Wi-Fi dongle, insert it into one of the USB ports on the Raspberry Pi.   

• Plug the power supply into a power outlet and the other end into the Raspberry Pi.    

• Wait for the Raspberry Pi to boot up.   

• First you need to create account on ThingSpeak website and create a ‘New channel’ in it. In
  new channel you have to define some fields for the data you want to monitor, like in this project 
  we will create three fields for Humidity, Temperature and Pressure data.   
  
• Now click on ‘API keys’ tab and save the Write and Read API keys, here we are only using 
  Write key. You need to Copy this key in ‘key’ variable in the Code.   
  
• After it, click on ‘Data Import/Export’ and copy the Update Channel Feed GET Request URL.    

• Now we need this ‘Feed Get Request URL’ in our Python code to open “api.thingspeak.com” 
  and then send data using this Feed Request as query string. And Before sending data user needs to 
  enter the temperature, humidity and pressure data in this query String using variables in program.   
  
• after creating channel successfully we will get a channel id. we can share this channel id and use 
  this id to search in Think View app to monitor the weather.   

## Block Diagram
---
![image](https://github.com/B27REVANTH/weather-monitoring/assets/112959086/900ef373-d412-49a3-a987-1c3af7b53109)

## Circuit Design
---
![image](https://github.com/B27REVANTH/weather-monitoring/assets/112959086/42a812d8-2441-4e92-b118-6df187c20091)

## Result in Lcd Display
---
![image](https://github.com/B27REVANTH/weather-monitoring/assets/112959086/60799c66-df9b-4632-a112-6e3134dcec0f)

## Result in Thing View app
---
![image](https://github.com/B27REVANTH/weather-monitoring/assets/112959086/bf103254-e7b5-44d8-b99f-6bfc4c817adc)
![image](https://github.com/B27REVANTH/weather-monitoring/assets/112959086/37abb5b4-8b6b-401f-abeb-b3b20d19f90e)
![image](https://github.com/B27REVANTH/weather-monitoring/assets/112959086/72218666-2c4c-4469-abe7-2cf407842335)






  


