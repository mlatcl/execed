---
layout: home
title: Executive Education on AI, Data Science and Machine Learning
---

This is a site that is *UNDER CONSTRUCTION* containing my material for Exec ed on data science and machine learning.

## Lectures

{% assign lastone = site.lectures | last %}
{% for lecture in site.lectures %}
{% include listlecture.html %}
{% endfor %}

