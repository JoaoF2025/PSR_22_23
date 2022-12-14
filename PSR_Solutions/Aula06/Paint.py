#!/usr/bin/env python3
#Exercise 1c


import cv2
from functools import partial
import numpy as np
from colorama import Fore,init
from math import sqrt


background=np.ones([400,600,3],dtype=np.uint8)
background.fill(255)

def click_event(event, x, y, flags, params, options):
    
    if event == cv2.EVENT_LBUTTONDOWN:
        options['shape'] = True 
        options['ix'], options['iy'] = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if options['shape'] == True:
            copy = background.copy()
            options['radius'] = int(sqrt(((options['ix']-x)**2)+((options['iy']-y)**2)))
            cv2.circle(copy, (options['ix'],options['iy']), options['radius'], options['color'], 2)
            cv2.imshow('Paint.py', copy)
        else:           
            cv2.circle(background, (x,y), 4, options['color'], -1)                
    elif event == cv2.EVENT_LBUTTONUP:
        options['shape'] = False
        cv2.circle(background, (options['ix'],options['iy']), options['radius'], options['color'], 2)
        

def main(): 

    
    options={'draw':False,'color':(0,0,255),'shape':False,'ix':-1,'iy':-1,'x1':-1,'y1':-1,'radius':0}

    cv2.namedWindow('Paint.py')
    cv2.setMouseCallback('Paint.py', partial(click_event, options=options))
    print('You are now drawing in red')

    while True:

        cv2.imshow('Paint.py',background)

        k=cv2.waitKey(0) & 0xFF

        if k == ord('r'):
            options['color']=(0,0,255)
            print('You are now drawing in red')
        elif k == ord('g'):
            options['color']=(0,255,0)
            print('You are now drawing in green')
        elif k == ord('b'):
            options['color']=(255,0,0)
            print('You are now drawing in blue')
        elif k == ord('c'):
            options['color']=(255,0,0)
            background.fill(255)
            print('Canvas cleared')     
        elif k==ord('q'):
            print('Quitting program')
            cv2.destroyAllWindows()
            break

if __name__ == '__main__':
    main()
