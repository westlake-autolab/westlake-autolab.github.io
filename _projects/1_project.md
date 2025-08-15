---
layout: page
title: World Modelling in Embodoed AI
description: with background image
img: assets/img/12.jpg
importance: 1
category: work
related_publications: true
---

TODO: Summary

### Part 1: Enhancing Rule Understanding in Autonomous Driving Systems Using Generative World Models

#### Our Objective: 
The core of an autonomous driving system lies in its deep understanding of the surrounding environment and traffic rules. However, current autonomous driving technology still faces challenges when dealing with complex or rare high-level rules. For instance, "How should the system decide when a police officer’s hand gesture conflicts with traffic signal indications?" Such situations highlight the current system's shortcomings. Therefore, integrating these complex rules effectively into autonomous driving models becomes a critical issue for improving system reliability. The cause of this problem is the "long tail effect" of real-world data: rare but crucial hazardous scenarios are extremely sparse in datasets. Relying on manual data collection for such scenarios is not only costly but also entails significant safety risks. To address this challenge, our research utilizes Generative AI to construct a data feedback loop framework. This framework uses a Generative World Model to create large-scale simulation scenes that include complex high-level rules and complete 3D ground truth. These high-quality synthetic data are then used to train the main driving model, compensating for its shortcomings in rule understanding, and ultimately improving its decision-making ability in real-world environments.

#### Our Achievements So Far:

1. **Static World Construction**: Achieved fine-grained control in generating static 3D driving scenes. {% cite yang2023bevcontrol %}

2. **Dynamic World Synthesis**: Expanded the model to include temporal sequences, resulting in the continuous generation of 4D video, demonstrating the model's performance in dynamic environments. {% cite ma2024unleashing %}

3. **Model Self-Correction**: Built the data feedback loop framework, enabling the system to learn from the generated data and perform self-correction and optimization. {% cite ma2024unleashing %}

4. **Trajectory Risk Prediction Enhancement**: By using synthetic trajectory data, we enhanced the Visual Language Model (VLM) in predicting the risks associated with planned trajectories, thereby improving the safety of the planned trajectories. This advancement helps foresee potential risks in real driving scenarios, optimizing the safety of autonomous driving decisions. {% cite hou2025drivemrp %}

#### Future Outlook

We will continue to optimize the self-correcting feedback loop framework, enhance the realism of the simulator, and improve high-level closed-loop capabilities. Our goal is to reduce data collection and training costs, further enhancing the robustness and generalization of autonomous driving models, ultimately driving autonomous driving technology toward a smarter and safer future.


<!-- Every project has a beautiful feature showcase page.
It's easy to include images in a flexible 3-column grid format.
Make your photos 1/3, 2/3, or full width.

To give your project a background in the portfolio page, just add the img tag to the front matter like so:

    ---
    layout: page
    title: project
    description: a project with a background image
    img: /assets/img/12.jpg
    ---

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/1.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/3.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/5.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Caption photos easily. On the left, a road goes through a tunnel. Middle, leaves artistically fall in a hipster photoshoot. Right, in another hipster photoshoot, a lumberjack grasps a handful of pine needles.
</div>
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/5.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    This image can also have a caption. It's like magic.
</div>

You can also put regular text between your rows of images, even citations {% cite einstein1950meaning %}.
Say you wanted to write a bit about your project before you posted the rest of the images.
You describe how you toiled, sweated, _bled_ for your project, and then... you reveal its glory in the next row of images.

<div class="row justify-content-sm-center">
    <div class="col-sm-8 mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/6.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm-4 mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/11.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    You can also have artistically styled 2/3 + 1/3 images, like these.
</div>

The code is simple.
Just wrap your images with `<div class="col-sm">` and place them inside `<div class="row">` (read more about the <a href="https://getbootstrap.com/docs/4.4/layout/grid/">Bootstrap Grid</a> system).
To make images responsive, add `img-fluid` class to each; for rounded corners and shadows use `rounded` and `z-depth-1` classes.
Here's the code for the last row of images above:

{% raw %}

```html
<div class="row justify-content-sm-center">
  <div class="col-sm-8 mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/6.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm-4 mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/11.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
  </div>
</div>
``` -->

{% endraw %}
