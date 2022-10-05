# Motion capture animation using google mediapipe pose estimation

Inverse project from screenspace to worldspace
Fix jittering with smooth sampling multiple frames

For 3d animation missing camera pose estimation model
(mediapipe tracks joints only in screenspace),
so for 3d animation to work camera has to be still and
pitch 90° from ground (or set manually)

to retarget skeleton: blender rokoko or some motion retargeting
