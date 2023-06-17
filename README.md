# Volume-Gesture-Control
This is a program created using a handtracking module I created from mediapipes solutions. The program finds your hand and draws all landmarks
then draws a line between your pointer finger and thumb. The length of said line is what determines the volume of the system. The system was created on 
MacOS so the way the volume changes us by running a script with the volume in the command line. 

## Usage
To use this program make sure you are on MacOS and you need to install the required packages then put some audio on so you can see how the volume changes.
When you are ready to run enter this command:
```sh
python3 VolControl.py
```
Then put your hand in view of the camera and watch the volume change based on your hand!
