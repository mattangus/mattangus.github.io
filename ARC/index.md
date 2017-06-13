---
layout: page
title: Autonomous Robotics Club
description: "University of Calgary"
header-img: images/IGVC.jpg
comments: false
modified: 2017-04-07
---

# About the club
---

The Autonomous Robotics Club (ARC) was founded with the goal of competing in the Intelligent Ground Vehicle Competition (IGVC). The robot - TAURUS - was entered in

# Hardware
---

## Sensors
- GPS
- Two cameras
- LIDAR
- Encoders
- Compass

## Actuators
- Motors/Motor Controller

## Computer & Microcontrollers
- Laptop
- Arduino

# Software
---

## Overview
The whole system was implemented in C++. Consisting of around 2700 lines of code. The system was running at about 0.6 seconds per iteration of the main loop. Each iteration consisted of collecting data from each sensor, processing the data and outputting a command to the actuators.

## Fuzzy Logic
Fuzzy Logic was used as the motion planner. 