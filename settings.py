# -*- coding: UTF-8 -*-

TITLE = "        Simple harmonic oscillation"
IMG_TYPE = 'png'
FONT_TYPE = 'Arial.ttf'
BACKGROUND_COLOR = (180,180,225)
WIDTH = 500
HEIGHT = 400
SUBLINE = True

X_AXIS_NAME = 'Time'
X_AXIS_UNIT = 's'
X_AXIS_RANGE = (-15, 10)

Y_AXIS_NAME = 'Distance'
Y_AXIS_UNIT = 'm'
Y_AXIS_RANGE = (-6, 7)

def Func01(t):
    '''d = 2sin t'''
    from math import sin
    d = 2*sin(t)
    return d

def Func02(t):
    '''d = 3cos t'''
    from math import cos
    d = 3*cos(t)
    return d

def Func03(t):
    '''d = 0.3cos 0.2t'''
    from math import cos
    d = 0.3*cos(t*0.2)
    return d

FUNCTION_LIST = [
    #(function_name,RGB_color)
    (Func01,(225,0,0)),
    (Func02,(0,225,0)),
    (Func03,(0,0,225)),
    ]