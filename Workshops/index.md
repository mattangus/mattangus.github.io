---
layout: page
title: Workshops
description: "Workshops/Tutorials I've Hosted"
header-img: images/abstract-6.jpg
comments: false
modified: 2017-04-07
---

# Creating Custom Operations in Tensorflow

This workshop was hosted at the University of Waterloo. I hosted it as part of the course "Autonomous Driving Perception".

The workshop was split into 5 parts. Each of those stages can be found on a different branch of the [github page](https://github.com/mattangus/TF-Custom-Op-Workshop). The slides for this workshop can be dowloaded [here]({{ site.url }}/downloads/CustomOperations.pdf).

Unfortunitely the session was not recorded and the slides were designed to be an aid, not to stand alone.

### Skeleton

The [skeleton](https://github.com/mattangus/TF-Custom-Op-Workshop/tree/skeleton) branch is a bare bones template for creating Tensorflow custom operations. It only contains enough code so that it will compile. It does not register the operation within the TF framework.

### Shape Inference

The [shape_inf](https://github.com/mattangus/TF-Custom-Op-Workshop/tree/shape_inf) branch registers the operation with the TF framework and performs error checks on the shape of the input Tensors as well as setting the output shape.

### CPU

The [CPU](https://github.com/mattangus/TF-Custom-Op-Workshop/tree/cpu) branch contains code to run the add operation on the CPU.

### GPU

The [GPU](https://github.com/mattangus/TF-Custom-Op-Workshop/tree/gpu) branch is where things get interesting. It contains a GPU implementation of the add operation.

# Robotics Community Engagement

While in the [Autonomous Robotics Club]({{ site.url }}/ARC) The club executives, myself and Sam, presented at a Jr. high school in Calgary. The target audience was grad 7-9. The purpose of the talk was to increase interest in robotics. The slides for this talk can be found [here]({{ site.url }}/downloads/Jr_High_Presentation.pptx).