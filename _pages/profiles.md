---
layout: page
permalink: /people/
title: people
description: members of our lab
nav: true
nav_order: 7
display_categories: [Principal Investigator (PI), Administrative Assistant, Ph.D., Research Assistant, Visiting Student, Undergraduate, Alumni]
horizontal: false
---

<!-- pages/projects.md -->
<div class="projects">
{% if site.enable_people_categories and page.display_categories %}
  <!-- Display categorized projects -->
  {% for category in page.display_categories %}
  <a id="{{ category }}" href=".#{{ category }}">
    <h2 class="category">{{ category }}</h2>
  </a>
  {% assign categorized_projects = site.people | where: "category", category %}
  {% assign sorted_projects = categorized_projects | sort: "importance" %}
  
  {% if category == "Alumni" %}
  <!-- Special display for Alumni - list format instead of cards -->
  <div class="alumni-section mt-4">
    <p class="text-muted">
      We are proud of our alumni who have gone on to make significant contributions in academia and industry. 
      If you are an alumnus of our lab and would like to be featured here, please contact us.
    </p>
    
    <div class="row">
      <div class="col-md-6">
        <h5>Former Ph.D. Students</h5>
        <ul class="list-unstyled">
          {% for project in sorted_projects %}
            {% if project.subcategory == "Ph.D." %}
            <li class="mb-2">
              <i class="fas fa-graduation-cap text-primary me-2"></i>
              <strong>{{ project.title }}</strong>{% if project.description %} - <span class="text-muted">{{ project.description }}</span>{% endif %}
            </li>
            {% endif %}
          {% endfor %}
          {% unless sorted_projects %}
          <li class="mb-2">
            <i class="fas fa-graduation-cap text-primary me-2"></i>
            <span class="text-muted">Coming soon...</span>
          </li>
          {% endunless %}
        </ul>
      </div>
      
      <div class="col-md-6">
        <h5>Former Research Assistants</h5>
        <ul class="list-unstyled">
          {% for project in sorted_projects %}
            {% if project.subcategory == "Research Assistant" %}
            <li class="mb-2">
              <i class="fas fa-user-graduate text-primary me-2"></i>
              <strong>{{ project.title }}</strong>{% if project.description %} - <span class="text-muted">{{ project.description }}</span>{% endif %}
            </li>
            {% endif %}
          {% endfor %}
          {% unless sorted_projects %}
          <li class="mb-2">
            <i class="fas fa-user-graduate text-primary me-2"></i>
            <span class="text-muted">Coming soon...</span>
          </li>
          {% endunless %}
        </ul>
      </div>
    </div>
    
    <div class="row mt-4">
      <div class="col-12">
        <h5>Former Visiting Students & Interns</h5>
        <ul class="list-unstyled">
          {% for project in sorted_projects %}
            {% if project.subcategory == "Visiting Student" or project.subcategory == "Intern" %}
            <li class="mb-2">
              <i class="fas fa-users text-primary me-2"></i>
              <strong>{{ project.title }}</strong>{% if project.description %} - <span class="text-muted">{{ project.description }}</span>{% endif %}
            </li>
            {% endif %}
          {% endfor %}
          {% unless sorted_projects %}
          <li class="mb-2">
            <i class="fas fa-users text-primary me-2"></i>
            <span class="text-muted">Coming soon...</span>
          </li>
          {% endunless %}
        </ul>
      </div>
    </div>
  </div>
  {% else %}
  <!-- Generate cards for each project (non-Alumni categories) -->
  {% if page.horizontal %}
  <div class="container">
    <div class="row row-cols-1 row-cols-md-2">
    {% for project in sorted_projects %}
      {% include projects_horizontal.liquid %}
    {% endfor %}
    </div>
  </div>
  {% else %}
  <div class="row row-cols-1 row-cols-md-3">
    {% for project in sorted_projects %}
      {% include projects.liquid %}
    {% endfor %}
  </div>
  {% endif %}
  {% endif %}
  {% endfor %}

{% else %}

<!-- Display projects without categories -->

{% assign sorted_projects = site.projects | sort: "importance" %}

  <!-- Generate cards for each project -->

{% if page.horizontal %}

  <div class="container">
    <div class="row row-cols-1 row-cols-md-2">
    {% for project in sorted_projects %}
      {% include projects_horizontal.liquid %}
    {% endfor %}
    </div>
  </div>
  {% else %}
  <div class="row row-cols-1 row-cols-md-3">
    {% for project in sorted_projects %}
      {% include projects.liquid %}
    {% endfor %}
  </div>
  {% endif %}
{% endif %}
</div>
