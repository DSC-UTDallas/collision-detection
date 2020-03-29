<h1 align="center">collision-detection</h1>

collision-detection is our idea to prevent fatalities due to automobile accidents by detecting collisions and rerouting nearby vehicles, thereby allowing emergency vehicles to approach the scene as fast as possible. 

Since red light cameras were recently banned in Texas, people may continue speeding to pass a red light signal, which is the cause of nearly 165,000 accidents; of which 50% of major collisions occur at intersections.

## Demo

View our [demo video](https://youtube.com)!

## Install
1. Clone the repository, `git clone https://github.com/DSC-UTDallas/collision-detection.git`.
2. You can compile the Flutter app from source, or download it [📲 here]().
```
cd collision-detection/flutter  #?
#?
```
3. A frozen model is found in `...`. Simply run `...` to see the inferencer in action. 
4. Now, the inferencer can be fed realtime data. Press ^C anytime to quit.
5. If a collision is detected, the server is contacted to update the Firebase database. The Flutter app will be dependent on the server to detect a change, and if the collision occurred nearby, an alternate route is provided. Different vehicles will be provided different routes, to minimize congestion.
6. At the same time, emergency vehicles are contacted with the fastest route to the collision site.

## Summary


### Problem that we want to solve
Since red light cameras were recently banned in Texas, people may continue speeding to pass a red light signal, which is the cause of nearly 165,000 accidents. Furthermore, 50% of major collisions occur at intersections.

### Solution to the problem
Our solution is to prevent fatalities by detecting collisions from analyzing traffic cameras at intersections through machine learning; then, immediately notify alternate routes to nearby vehicles with the app in order to reduce traffic congestion, so that emergency vehicles can get to the scene as quickly as possible. 

For testing, we plan to use pre-recorded footage of collisions and deploy our mobile application to get feedback from users, which might include improvements to usability, intuitiveness, and interface. We also plan to use live traffic camera feeds and monitor the performance of our neural network. Existing infrastructure makes this idea readily applicable for future growth.
<!-- tree command on dir -->

## Technologies used
Our solution uses an app to contact drivers approaching the accident, which uses Flutter along with the Maps API. The server backend uses Firebase, and collision detection while monitoring traffic cameras in real time uses Tensorflow.

* **Flutter**
* **Maps API**
* **Tensorflow**
* **Firebase**

## User testing

## Development overview
1. The first step was automobile detection. Using the SSD Inception v2 model as a fine-tuning checkpoint, supervised training was used through labeled images for detecting cars. 

2. A naive approach is a rule-based approach, by noticing intersection of car models through object detection in real time. However, we wanted to take it a step further by implementing a time-based model that uses a set of images to incorporate movement of cars.

3. 

## Future plans

We are planning on incorporating extra features, such as [-]

In terms of deployment, we hope to release a beta version by [-] 

## Thanks!
In the hectic time of the ongoing outbreak, we want to extend our thanks to Google and the UTD Developer Student Club in being proactive by providing helpful online workshops, meetings, and collaboration tools. Thank you!
