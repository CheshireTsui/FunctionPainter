# -*- coding: UTF-8 -*-

TITLE = "        Simple harmonic oscillation"
IMG_TYPE = 'png'
FONT_TYPE = 'Arial.ttf'
BACKGROUND_COLOR = (180,180,225)
WIDTH = 700
HEIGHT = 700
SUBLINE = True

X_AXIS_NAME = 'Time'
X_AXIS_UNIT = 's'
X_AXIS_RANGE = (-15, 15)

Y_AXIS_NAME = 'Distance'
Y_AXIS_UNIT = 'm'
Y_AXIS_RANGE = (-3, 7)

def Func01(t):
    '''d = sin t'''
    from math import sin
    d = sin(t)
    return d

def Func02(t):
    '''d = e^t'''
    from math import exp
    d = exp(t)
    return d

def Func03(t):
    '''d = ln t'''
    from math import log
    try:
        d = log(t)
    except Exception, e:
        d = None
    return d

def Func04(t):
    '''d =  5t'''
    return 5*t

FUNCTION_LIST = [
    #(function_name,RGB_color)
    (Func01,(225,0,0), False),
    (Func02,(0,225,0), False),
    (Func03,(0,0,225), False),
    (Func04,(150,0,150), True),
    ]