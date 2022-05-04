# Object Tracking in Adverse Weather Conditions

<center><img src="Figures/University-of-Wisconsin-Madison-Logo.png" class="centerImage" width="300" height="102"></center>

<center><img src="Figures/Madison_Day.gif" width="500" height="375"></center> <center><img src="Figures/Madison_Night_Rain.gif" width="500" height="375"></center>

Footage from different weather conditions in Madison, WI.

## Motivation
Object tracking is fundamental for autonomous vehicles (AVs) to perform path planning and object avoidance. Datasets commonly used to train object tracking algorithms for AVs contain mostly video from clear, open-air environments, causing the models to fail in adverse weather conditions. Even with data available, the performance of these algorithms severely degrades in adverse weather. The inability to perform object detection and tracking in various weather conditions is therefore a major roadblock for the use of AVs. In this project, we investigate object tracking in adverse weather conditions. 

We investigate a prominent model in the object detection literature: [IA-YOLO](https://arxiv.org/abs/2112.08088) ("Image Adaptive"), a modification of the original [YOLO](https://pjreddie.com/darknet/yolo/) ("You Only Look Once") architecture with modules to perform defogging and brightening of images. This model is trained on the [BDD100k dataset](https://www.bdd100k.com/). 

## Approach
We implement the IA-YOLO algorithm described in the paper above. The figure below illustrates the model: 



## Implementation

## Results

## Discussion

## Source Code
