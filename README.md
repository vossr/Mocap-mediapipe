### Motion capture animation using google mediapipe  

<img src="mocap.gif" width="300" height="auto"/>  

`pose.py` tracks and serializes binary file  

Inverse project from screenspace to worldspace  
Fix jittering with smooth sampling multiple frames  

<img src="ingame.gif" width="300" height="auto"/>  

For 3D animation, missing camera pose estimation model  
(mediapipe tracks joints in screenspace),  
so for 3D animation to work camera must be still and  
pitch 90° from ground (or set manually)  

To retarget skeleton: blender rokoko or some motion retargeting  

#### Hand Tracking with valve index cameras   
<img src="handtracking.png" width="400" height="auto"/> 
