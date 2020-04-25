# UMass Robotics Dream Team
A Pulse-Width Modulated Motor Design for Accurate Rotation and Precise Movement

Robot Dream Team (Or RDT) is a 4 motored autonomous vehicle that is guided by the readings of an ultrasonic sensor. Since the design of the robot was fixed, our repo was tasked with taking advantage of the robot’s hardware in such a way that we could determine the perimeter of the surroundings, the area of the enclosure, and all the while record the speed at which the robot was moving. Several of these feats were accomplished in different components of the project, so they will explained in greater detail.

## Controlling the Robots Speed

One of the first and most time-consuming tasks was controlling the speed (and accuracy) of the robot. One of the main reasons that we wanted to do this was because the different terrain of the surroundings can impact the RDT’s responsiveness. For example, in the 4-walled robot enclosure we built, in one corner of the box the cardboard sits a little higher than the others. As a result, the robot requires a little more current to the motors so that it can tackle the obstacle. But in general, the speed it requires to get out of this terrain is too fast for the other areas of the enclosure.

To tackle this we employed Pulse Width Modulation. Pulse Width Modulation is a useful tactic for delivering a steady frequency of the voltage to the motors in such a way that we can control the current intake directly through code while maintaining a steady 9V into the Motor Driver. This is both useful and practical, and it results in no hardware changes which is perfect since we do not have access to the hardware of the robot.

https://www.youtube.com/watch?v=7p2fTAiEle8&feature=youtu.be

## Rotation and Movement

What PWM is really useful for, however, is rotating. Rotating is one of the most difficult thing we have found to do with the robot. While rotating 90 degrees sounds simple, in actuality it is very difficult. In addition, only having one ultrasonic sensor to detect our movement makes it really difficult to verify that any of the turns we make are accurate to the degree we wanted to turn. Unfortunately this is a problem that is near impossible to solve with one sensor, so our next idea was how can me make our rotating as accurate as possible. PWM gives us the ability to do this. While complete accuracy cannot be guaranteed, with control of the speed we can get the car to roughly turn where it needs to.

 ## Movement Impedance and Interference

Through empirical testing, one of the most obvious problems that we ran into was getting stuck. RDT got stuck all the time, and the reality is this is always going to happen. To solve this problem, we created code to manage when the robot gets stuck to drive the motor speed up and try and ‘unhinge’ it from its current location. The only main problem this causes is the robots inability to know where it is located after it has been unhinged. This is something we worked really hard to resolve but we found it ultimately difficult to consistently work.
