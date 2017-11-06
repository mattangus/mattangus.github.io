---
layout: page
title: Research Interests
description: "Computer Vision for Autonomous Driving."
header-img: images/research.png
comments: false
modified: 2017-04-07
---

My main research interest is in computer vision, specifically semantic segmentation for scene understanding and end to end learning for steering angle regression.

## Semantic Segmentation
-----

Semantic segmentation is the task of taking an image and assigning a class to each pixel. An example is shown below.

**Original Image**
![Original Image][original]{:class="center-block"}

**Semantically Segmented Image**
![Segmented Image][segmented]{:class="center-block"}

State of the art algorithms rely on Convolutional Neural Networks (CNN).

*this section is under construction*

## Publications
-----

<div class='panel-pub'>
<ol>
{% for article in site.data.publications %}
    <li>
    <div class="title">
    <span class="title">{{ article.title }}</span>
    {% if article.fulltext %}
        <a title="fulltext" href="{{ site.url }}/downloads/journal/{{ article.fulltext }}"><i class="fa fa-file-pdf-o"></i></a>
    {% endif %}
    </div>
    <div class='author'>
    {% for author in article.author %}
        <span class='{{ author.role }}'>
        {{ author.family }}, {{ author.given }}{% if author.role contains 'corr' %}*{% endif %}; </span>
    {% endfor %}
    </div>
    <div class="pubinfo">
    <span class="source">{{ article.journal.abbreviation }} </span>
    <span class="year">{{ article.year }}, </span>
    <span class="volume">{{ article.volume }}, </span>
    <span class="page">{{ article.page }}.</span>
    </div>
    <div class="url">
        <a href="{{ article.URL }}">{{ article.URL }}</a>
    </div>
    </li>
{% endfor %}
</ol>
</div>

[original]: /images/research/input.jpg
[segmented]: /images/research/segmented.png