from RPi import GPIO
from time import sleep

import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

clk = 17
dt = 18
RST = 24


GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)

disp.begin()
disp.clear()
disp.display()

width = disp.width
height = disp.height
image = Image.new('1', (width, height))

draw = ImageDraw.Draw(image)

draw.rectangle((0,0,width,height), outline=0, fill=0)

padding = 2
top = padding
bottom = height-padding

#font = ImageFont.load_default()
font = ImageFont.truetype('Minecraftia.ttf', 8)

counter = 0
clkLastState = GPIO.input(clk)

try:

        while True:
                clkState = GPIO.input(clk)
                dtState = GPIO.input(dt)
                if clkState != clkLastState:
                        if dtState != clkState:
                                counter += 1
                        else:
                                counter -= 1
			disp.clear()	
                        print counter
			draw.text((x, top),  str(counter),  font=font, fill=255)
                clkLastState = clkState
                sleep(0.01)
finally:
disp.image(image)
disp.display()	
GPIO.cleanup()
