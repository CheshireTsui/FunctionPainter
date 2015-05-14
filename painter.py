# -*- coding: UTF-8 -*-
import Image, ImageDraw, ImageFont
from settings import *

#Set the edge distance
edge = 25
title_height = 30

def mypoint(x, y, color = (0,0,0)):
    for k in range(x-1,x+2):
        for j in range(y-1, y+2):
            draw.point((k,j), fill=color)

#Create the Image object
img = Image.new('RGB', (WIDTH+edge*2,HEIGHT+edge*3+int(title_height*1.3)), BACKGROUND_COLOR)
#Create the Font object
font_title = ImageFont.truetype(FONT_TYPE, 30)
font_label = ImageFont.truetype(FONT_TYPE, 12)
# Create the Draw object
draw = ImageDraw.Draw(img)
#Draw the basic layer
draw.rectangle([(edge, edge), (edge+WIDTH, edge+HEIGHT)], fill = (225,225,225))
ratio_x = (X_AXIS_RANGE[1] - X_AXIS_RANGE[0]) / float(WIDTH)
ratio_y = (Y_AXIS_RANGE[1] - Y_AXIS_RANGE[0]) / float(HEIGHT)
space_x = (WIDTH % edge) / 2
space_y = (HEIGHT % edge) / 2
#Draw the x-axis
draw.line([(edge,edge+HEIGHT),(edge+WIDTH+17,edge+HEIGHT)], fill=(0,0,0))
for i in range(0,WIDTH,edge):
    draw.line([(edge+i,edge+HEIGHT+1),(edge+i,edge+HEIGHT+5)], fill=(0,0,0))
    num = X_AXIS_RANGE[0] + i*ratio_x
    adjust = 0
    if num < 0: adjust += 3
    if abs(num) >= 10: adjust += 3
    draw.text((edge+i-adjust,edge+HEIGHT+7), str(num), font=font_label, fill=(0,0,0))
    if SUBLINE:
        for j in range(HEIGHT):
            if i > 0:
                if (j % edge) < edge * 0.8: draw.point((edge+i, edge+HEIGHT-j), fill=(200,200,200)) 
for i in range(1,16):
    draw.line([(WIDTH+edge+i+1,HEIGHT+edge-4+i/4), (WIDTH+edge+i+1,HEIGHT+edge-i/4+4)],fill=(0,0,0))
draw.text((edge+8,edge-12*1.4), X_AXIS_NAME+' '+X_AXIS_UNIT, font=font_label, fill=(0,0,0))
#Draw the y-axis
draw.line([(edge,edge+HEIGHT),(edge,edge-17)], fill=(0,0,0))
for i in range(0,HEIGHT,edge):
    draw.line([(edge,edge+HEIGHT-i),(edge-5,edge+HEIGHT-i)], fill=(0,0,0))
    num = Y_AXIS_RANGE[0] + i*ratio_y
    adjust = 0
    if num < 0: adjust += 3
    if abs(num) >= 10: adjust += 3
    draw.text((edge-adjust-20,edge+HEIGHT-10-i), '%.1f'%num, font=font_label, fill=(0,0,0))
    if SUBLINE:
        for j in range(WIDTH):
            if i > 0:
                if (j % edge) < edge * 0.8: draw.point((edge+j, edge+HEIGHT-i), fill=(200,200,200))
msg = Y_AXIS_NAME+' '+Y_AXIS_UNIT
draw.text((edge+WIDTH-len(msg)*6+18,edge+HEIGHT-12*1.4), msg, font=font_label, fill=(0,0,0))
for i in range(1,16):
    draw.line([(edge-4+i/4,edge-i-1), (edge+4-i/4,edge-i-1)],fill=(0,0,0))
#Draw all functions
for func, color in FUNCTION_LIST:
    for i in range(WIDTH):
        y = func(X_AXIS_RANGE[0]+ratio_x*i)
        if (y>=Y_AXIS_RANGE[0])and(y<=Y_AXIS_RANGE[1]):
            mypoint(edge+i, edge+HEIGHT-int((y-Y_AXIS_RANGE[0])/ratio_y), color = color)

#Draw the legend
legend_height = len(FUNCTION_LIST)*12*1.5
legend_width = 0
for func, color in FUNCTION_LIST:
    if len(func.func_doc)*6 > legend_width: 
        legend_width = len(func.func_doc)*6
legend_width += 9+edge
draw.rectangle([(edge+WIDTH,edge),(edge+WIDTH-legend_width,edge+legend_height)],fill=(150,150,150))
head =0.1
for func, color in FUNCTION_LIST:
    draw.line([(edge+WIDTH-legend_width+3,edge+6*1.5+head), (2*edge+WIDTH-legend_width+3,edge+6*1.5+head)],fill = color)
    draw.text((2*edge+WIDTH-legend_width+6,edge+head+2), func.func_doc, font = font_label, fill = (0,0,0))
    head +=12*1.5

#Draw the title
draw.text((edge,edge*2+HEIGHT), TITLE, font=font_title, fill=(0,0,0))

#Save the image
img.save(TITLE.strip()+'.'+IMG_TYPE, IMG_TYPE)
