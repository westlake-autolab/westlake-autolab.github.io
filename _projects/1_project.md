---
layout: page
title: "Project 1: World Modelling in Embodied AI"
description: with background image
img: assets/img/12.jpg
importance: 1
category: work
related_publications: true
---

<p>TODO: Summary</p>

<h3>Part 1: Enhancing Rule Understanding in Autonomous Driving Systems Using Generative World Models</h3>

<h4>Our Objective:</h4>
<p>The core of an autonomous driving system lies in its deep understanding of the surrounding environment and traffic rules. However, current autonomous driving technology still faces challenges when dealing with complex or rare high-level rules. For instance, "How should the system decide when a police officer's hand gesture conflicts with traffic signal indications?" Such situations highlight the current system's shortcomings. Therefore, integrating these complex rules effectively into autonomous driving models becomes a critical issue for improving system reliability. The cause of this problem is the "long tail effect" of real-world data: rare but crucial hazardous scenarios are extremely sparse in datasets. Relying on manual data collection for such scenarios is not only costly but also entails significant safety risks. To address this challenge, our research utilizes Generative AI to construct a data feedback loop framework. This framework uses a Generative World Model to create large-scale simulation scenes that include complex high-level rules and complete 3D ground truth. These high-quality synthetic data are then used to train the main driving model, compensating for its shortcomings in rule understanding, and ultimately improving its decision-making ability in real-world environments.</p>

<h4>Our Achievements So Far:</h4>

<ol>
    <li><strong>Static World Construction</strong>: Achieved fine-grained control in generating static 3D driving scenes. {% cite yang2023bevcontrol %}</li>
    
    <li><strong>Dynamic World Synthesis</strong>: Expanded the model to include temporal sequences, resulting in the continuous generation of 4D video, demonstrating the model's performance in dynamic environments. {% cite ma2024unleashing %}</li>
    
    <li><strong>Model Self-Correction</strong>: Built the data feedback loop framework, enabling the system to learn from the generated data and perform self-correction and optimization. {% cite ma2024unleashing %}</li>
    
    <li><strong>Multimodal Joint Generation</strong>: By unifying multimodal features through a shared Bird's Eye View (BEV) space, we achieve consistent joint generation of multimodal sensor data, enhancing the multimodal perception capability of autonomous driving systems. {% cite tang2025omnigen %}</li>
    
    <li><strong>Trajectory Risk Prediction Enhancement</strong>: By using synthetic trajectory data, we enhanced the Visual Language Model (VLM) in predicting the risks associated with planned trajectories, thereby improving the safety of the planned trajectories. This advancement helps foresee potential risks in real driving scenarios, optimizing the safety of autonomous driving decisions. {% cite hou2025drivemrp %}</li>
</ol>

<h4>Future Outlook</h4>

<p>We will continue to optimize the self-correcting feedback loop framework, enhance the realism of the simulator, and improve high-level closed-loop capabilities. Our goal is to reduce data collection and training costs, further enhancing the robustness and generalization of autonomous driving models, ultimately driving autonomous driving technology toward a smarter and safer future.</p>





<h3>Part 3: From Simulation to Reality: Toward Autonomous Embodied Robot</h3>

<h4>Our Objective:</h4>
<p>Human can quickly adapt to new environments and tasks by leveraging prior knowledge, physical intuition, and high-level reasoning. In contrast, robot often rely on massive-scale data collection and environment-specific training, yet still struggle to generalize across diverse scenarios and perform reliably in the real world.
Our research focuses on bridging this gap by developing agents capable of transferring skills from simulation to the real world (Sim2Real), while building structured world models that enable generalizable reasoning, robust planning, and adaptive decision-making. We aim to move beyond brute-force imitation learning and toward data-efficient, autonomous intelligence.</p>

<h4>Our Achievements So Far:</h4>

<p>We propose a generative simulation module capable of diverse training scenes. This enables continuous policy generation and refinement within a closed-loop pipeline, where simulated experiences directly guide policy learning, and improved policies, in turn, trigger automatic generation of more challenging environments.</p>

<p>To handle complex multi-agent environments, we introduce a socially-enhanced navigation policy that incorporates social attributes and interaction modeling into policy learning. By embedding social compliance, comfort metrics, and group dynamics into the reward structure, our agents achieve significantly better performance in crowded, dynamic, and socially-constrained navigation tasks.</p>


<h4>Future Outlook</h4>

<p>We plan to extend our framework to more diverse tasks and heterogeneous robotic platforms, enabling agents to autonomously collect data, learn concepts, and adapt policies online with minimal human supervision.
Our long-term goal is to establish a unified paradigm for autonomous embodied intelligence, where agents not only learn efficiently from limited data but also generalize robustly to unseen environments, novel tasks, and real-world uncertainties.
</p>





<h3>Part 4: From Data to Concepts: Toward Efficient Driving Intelligence</h3>

<h4>Our Objective:</h4>
<p>Human drivers typically require only limited formal training—covering traffic rules, basic operations, simulated road practice, and driving norms—before gradually adapting to increasingly complex and unfamiliar situations with experience. In contrast, autonomous driving systems have consumed millions or even billions of data samples, yet achieving fully reliable performance still remains a challenge.
Our research explores whether autonomous agents can move beyond brute-force data accumulation by developing higher-level conceptual understanding from their training, somewhat akin to the human ability to generalize through intuition. We believe such an approach could lead to more data-efficient learning and enable agents to handle rare and long-tail scenarios more effectively. {% cite jia2024bench2drive %}</p>

<h4>Our Achievements So Far:</h4>

<p>We are developing a concept-learning module that complements existing end-to-end driving architectures.{% cite renz2025simlingo %} This module aims to build a structured understanding of driving scenarios in parallel with traditional perception and control pipelines.</p>

<h4>Future Outlook</h4>

<p>We plan to extend this framework using more diverse datasets to improve the generalization of the concept model, with the ultimate goal of enhancing performance in unseen and complex situations while advancing the broader pursuit of data-efficient learning in autonomous driving.
</p>

