import cv2
import matplotlib.pyplot as plt
import numpy as np
import minionsModule as mm
import seaborn as sns

cap=cv2.VideoCapture(0)

print 'width: {0}, height: {1}'.format(cap.get(3),cap.get(4))
cap.set(3,1024)
cap.set(4,600)

_x = 400
_y = 240


while(True):
    ret, frame = cap.read()
    
    
    cv2.line(frame, (0,0),(800,480), (0, 255, 0), 2)
    cv2.line(frame, (800,0),(0,480), (0, 255, 0), 2)
    #cv2.line(frame, (400,0),(400,480), (0, 255, 0), 2) #ver
    cv2.line(frame, (0,240),(800,240), (0, 255, 0), 2)
    cv2.circle(frame, (_x,_y), 3, (255, 0, 0), 3)
    #              coordinate   rad  color(b,g,r) thick
    
    if (ret):
        
        #FULL SCREEN
        cv2.namedWindow('frame', cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty('frame', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        
        cv2.imshow('frame', frame)
        
        maxChannel, soundData = mm.minionsMaxChannel()
        fArray = mm.minionsMakeArray(soundData)
        

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
cap.release()
cv2.destroyAllWindows()

