import numpy as np
import cv2
from calibration import *

ls=[]  
lst=[] 
# read image
img = cv2.imread('test10.jpg')
  
# show image
cv2.imshow('image', img)



def get_inverse():
    res=[]
    val_ = helo()
    res.append(val_[0]-val_[6])
    res.append(val_[6]-val_[7])

    val=np.array(res).reshape(-1,2)
    #         print(val)


    out = np.divide(val, 2.4)
    out_=np.linalg.inv(out)
    return out_


def polygon(lst):
        area = 0
        for v in range(len(lst)):
            if v + 1 == len(lst):
                i = 0
            else:
                i = v + 1
            area += (lst[v][0] * lst[i][1] - lst[v][1] * lst[i][0])
        return abs(area / 2)

   
#define the events for the
# mouse_click.
def mouse_click(event, x, y, 
                flags, param):
    
    
    val=get_inverse()
    # print(val)
    # to check if left mouse 
    # button was clicked
    if event == cv2.EVENT_LBUTTONDOWN:
          
        # font for left click event
        font = cv2.FONT_HERSHEY_TRIPLEX
        LB = 'Left Button'
        v=[x,y]
        ls.append(v)
        # display that left button 
        # was clicked.
        cv2.putText(img, str(x) + ',' + 
                    str(y), (x,y), font,
                    1, (255, 0, 0), 2)
        # cv2.putText(img, LB, (x, y), 
        #             font, 1, 
        #             (255, 255, 0), 
        #             2) 
        cv2.circle(img, (x,y), 3, (0,255,255), -1)
        cv2.imshow('image', img)
          
          
    # to check if right mouse 
    # button was clicked
    if event == cv2.EVENT_RBUTTONDOWN:
           
        # font for right click event
        font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
        RB = 'Right Button'
        v=[x,y]
        ls.append(v)
        print(ls)
        # display that right button 
        # was clicked.
        cv2.putText(img, str(x) + ',' + 
                    str(y), (x,y), font,
                    1, (255, 0, 0), 2)
        # cv2.putText(img, RB, (x, y),
        #             font, 1, 
        #             (0, 255, 255),
        #             2)
        cv2.circle(img, (x,y), 3, (0,255,255), -1)
        cv2.imshow('image', img)



    if cv2.waitKey(0) & 0xFF == ord('q'):
        # print(ls @ val)
        lst=(ls @ val)
        print(lst)
        print(polygon(lst))
        
        cv2.destroyAllWindows()
  
cv2.setMouseCallback('image', mouse_click)
   
cv2.waitKey(0)
  
# close all the opened windows.
