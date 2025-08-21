---
layout: page
title: projects
permalink: /projects/
description: a growing collection of our cool projects.
nav: true
nav_order: 3
horizontal: true
---

<!-- pages/projects.md -->
<div class="projects">
{% assign sorted_projects = site.projects | sort: "importance" %}

<!-- Display projects in horizontal layout -->
<div class="container">
  <div class="row row-cols-1">
  {% for project in sorted_projects %}
    {% include projects_horizontal.liquid %}
  {% endfor %}
  </div>
</div>
</div>
