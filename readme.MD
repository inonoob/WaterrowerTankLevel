# Waterrower Tank Level Reader

Just a simple python script which connects with the Waterrower via USB cable. And checks
how many liters has been set on the S4 monitor. 

## Installation

    git clone https://github.com/inonoob/WaterrowerTankLevel.git

## Usage

Start the script on your computer:

    python3 WaterLevelCheck.py 
    Tankinhalt ist: 17.0 l
    Tankinhalt ist: 17.0 l
    Tankinhalt ist: 17.0 l

Go to your S4 Waterrower monitor: 
- click 8 times the button **"advanced"** in order to get to the set water tank level
- use arrow key to increase or decrease the amount of water in the tank
- check python script output to check what level currently is set 
- If correct amount is set. Press **"ok"** button on the S4 monitor to store
- Double check the script output if set correctly. 
- Profit :) 

## Requirements

project has been done with python 3.8 

needed modules: 
- pyserial 

## Motivation 

I bought for cheap a S4 Waterrower monitor with a cracked screen. As I only use the app Coxswain 
and also read the data via USB cable. I didn't mind the broken screen. But in order to have 
the correct caluclation for power, the amount of water in the tank has to be correct. Therefore 
I wrote a little script in order to read the level out of the memory of the S4 and interact with 
the monitor to set it to the right amount of water. I haven't found a way yet to set it from 
the pc. 


## License
MIT License

Copyright (c) 2020 inonoob

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.