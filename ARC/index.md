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

The Autonomous Robotics Club (ARC) was founded with the goal of competing in the Intelligent Ground Vehicle Competition (IGVC). The robot - Taurus - was first entered into IGVC in 2016, where we won the Rooky of the year award. Taurus uses sensors such as GPS, LiDAR and Compass to determine its position in the environment. A list of components is below. Taurus runs on a small laptop that is mounted on the rear, and coded in C++.

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
Fuzzy logic is a system of non binary logic. Instead of truth values (true/1 and false/0), statements are assigned a value between 0 and 1 inclusive. This value is called the membership value. It represents the membership of a set or concept. We will call these Fuzzy Sets. Fuzzy Logic was used as the motion planner. The controller consisted of three fuzzy sets: Near-Far, Target, and Free-Space.

