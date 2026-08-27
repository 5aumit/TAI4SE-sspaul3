#!/usr/bin/env python
# -*- coding:utf-8 -*-

from PIL import Image, ImageFont, ImageDraw, ImageFilter
import random

def rndChar():
	return chr(random.randint(65, 90))

def rndColor():
	return (random.randint(64,255), random.randint(64, 255), random.randint(64, 255))

def rndColor2():
	return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))

font = ImageFont.truetype('/usr/share/fonts/lyx/cmmi10.ttf', 36)

draw = ImageDraw.Draw(image)

for x in range(width):
	for y in range(height/2):
		
		draw.point((x, 2*y), fill = rndColor())

for t in range(4):
	draw.text((60 * t + 10, 10), rndChar(), font = font, fill = rndColor2())

image.save('./test/test3.jpg','jpeg')

image = image.filter(ImageFilter.BLUR)

image.save('./test/test4.jpg','jpeg')
