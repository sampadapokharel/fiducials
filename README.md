# Follow Fiducial 

This program uses fiducial to make the robot go towards a specific destination. For this PA, my robot starts without either fiducial in sight. It turns in its current location to find the first fiducial, 101. Once it spots it, it goes towards it fixing its angle and once it reaches desired distance, which is 0.50 in this case, it stops and turns to look for the second fiducial, 105. It follows the same process and stops at the desired distance away from the fiducial.  

Something that I learned when doing this PA was that translation z was basically calcualting the distance from the fiducial and translation x represted the angle of the robot. Once I figured this out, it was pretty easy to get the robot moving. 

# Video of the program running on a real robot 
https://drive.google.com/drive/folders/1DAZb6ubbTOq60F3tM1f9jSlu3dVNNMYK?usp=sharing

The robot stops further than the desired distance the second time because the camera couldn't locate the fiducial as it was prinited bigger, because the wall block was bigger compared to the other blocks, and the fiducial got cut off. 
