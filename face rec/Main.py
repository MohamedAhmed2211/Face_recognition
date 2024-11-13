#!/usr/bin/env python
# coding: utf-8

# In[6]:


#import import-ipynb

import urllib.request
import cv2
import os
import numpy as np

from SimpleFacerec import SimpleFacerec

os.chdird("G:\face rec")
# Encode faces from a folder
sfr= SimpleFacerec()
sfr.load_encoding_images("players/")


url="http://192.168.1.8:8080/shot.jpg"

while true:
    img_arr= np.array(bytearray(urllib.request.urlopen(url).red()),dtype= np.uint8)
    img= cv2.imdecode(img_arr,-1)
  
    face_locations , face_names =sfr.detect_known_faces(frame)
    for face_loc ,f_name in zip(face_locations,face_names):
        y1,x2,y2,x1 =face_loc[0],face_loc[1],face_loc[2], face_loc[3]
    
        cv2.putText(frame, name,(x1,y1-10),cv2.FONT_HERSHEY_PLAIN,1, (0,0,255),2)
        cv2.rectangle(frame, (x1,y1),(X2,y2),(0,255,0),4)     
      
    cv2.imshow("frame",img)
    if cv2.waitKey(1)==ord('q'):
        break;     
        
        
        
cap.release()
cv2.destroyAllWindows()        


# In[16]:








face_locations , face_names =sfr.detect_known_faces(frame)
for face_loc ,f_name in zip(face_locations,face_names):
    y1,x2,y2,x1 =face_loc[0],face_loc[1],face_loc[2], face_loc[3]
    
    cv2.putText(frame, name,(x1,y1=10),cv2.FONT_HERSHEY_PLAIN,1, (0,0,255),2)
    cv2.rectangle(frame, (x1,y1),(X2,y2),(0,255,0),4)
    
    
    
   



# In[ ]:




