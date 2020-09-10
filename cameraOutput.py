import cv2
# import minionsRecord as mr

# whereSoundIs = mr.minionsMaxChannel()
cap=cv2.VideoCapture(0)

print 'width: {0}, height: {1}'.format(cap.get(3),cap.get(4))
cap.set(3,1024)
cap.set(4,600)

_x = 400
_y = 240

img = cv2.imread('heatmap.png', cv2.IMREAD_COLOR)

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
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
cap.release()
cv2.destroyAllWindows()

