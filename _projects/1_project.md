---
layout: page
title: "World Modelling in Embodied AI"
description: "Developing structured world models to enable more robust, adaptive, and data-efficient embodied intelligence, with autonomous driving as a core testbed"
img: assets/img/ChatGPT Image 2025年8月22日 11_00_43
importance: 1
related_publications: true
---

<style>
.project-content {
    text-align: justify;
    text-justify: inter-word;
}

.project-content p {
    text-align: justify;
    text-justify: inter-word;
}

.project-content ul {
    text-align: justify;
    text-justify: inter-word;
}

.project-content ol {
    text-align: justify;
    text-justify: inter-word;
}

.project-content li {
    text-align: justify;
    text-justify: inter-word;
}

/* 保持图片描述居中 */
.project-content p[style*="font-size:14px; color:gray"] {
    text-align: center !important;
}

/* 更精确的选择器，针对图片描述 */
.project-content p[style*="font-size:14px"] {
    text-align: center !important;
}

/* 针对所有图片描述段落的通用居中样式 */
.project-content .figure-caption {
    text-align: center !important;
}
</style>

<div class="project-content">

<p>We develop structured world models to enable more robust, adaptive, and data-efficient embodied intelligence, with autonomous driving as a core testbed. Our research spans four directions: (i) enhancing rule understanding via generative world models, (ii) unifying multimodal understanding and generation, (iii) bridging simulation and reality for embodied robots, and (iv) learning high-level concepts for data-efficient driving intelligence. Together, these efforts aim to build agents that are safer, more adaptive, and capable of robust generalization in complex real-world environments.</p>


<br>

<h3><strong>Part 1: Enhancing Rule Understanding in Autonomous Driving Systems Using Generative World Models</strong></h3>

<br>




<h4>Our Objective:</h4>
<p>The core of an autonomous driving system lies in its deep understanding of the surrounding environment and traffic rules. However, current autonomous driving technology still faces challenges when dealing with complex or rare high-level rules. For instance, "How should the system decide when a police officer's hand gesture conflicts with traffic signal indications?" Such situations highlight the current system's shortcomings. Therefore, integrating these complex rules effectively into autonomous driving models becomes a critical issue for improving system reliability. The cause of this problem is the "long tail effect" of real-world data: rare but crucial hazardous scenarios are extremely sparse in datasets. Relying on manual data collection for such scenarios is not only costly but also entails significant safety risks. To address this challenge, our research utilizes Generative AI to construct a data feedback loop framework. This framework uses a Generative World Model to create large-scale simulation scenes that include complex high-level rules and complete 3D ground truth. These high-quality synthetic data are then used to train the main driving model, compensating for its shortcomings in rule understanding, and ultimately improving its decision-making ability in real-world environments.</p>

<!-- image -->
<div style="text-align:center; margin:20px 0;">
    <img src="/assets/img/proj1part1_abstract.png" alt="Enhancing Rule Understanding" width="80%">
    <p class="figure-caption" style="font-size:14px; color:gray;">Figure 1: Enhancing Rule Understanding Using Generative World Models.</p>
</div>


<br>

<h4>Our Achievements So Far:</h4>

<ul>
1. <strong>Static World Construction</strong>: Achieved fine-grained control in generating static 3D driving scenes. {% cite yang2023bevcontrol %}
    
    <br>
    
2. <strong>Dynamic World Synthesis</strong>: Expanded the model to include temporal sequences, resulting in the continuous generation of 4D video, demonstrating the model's performance in dynamic environments. {% cite ma2024unleashing %}
    
    <br>
    
3. <strong>Model Self-Correction</strong>: Built the data feedback loop framework, enabling the system to learn from the generated data and perform self-correction and optimization. {% cite ma2024unleashing %}
    
    <br>
    
4. <strong>Multimodal Joint Generation</strong>: By unifying multimodal features through a shared Bird's Eye View (BEV) space, we achieve consistent joint generation of multimodal sensor data, enhancing the multimodal perception capability of autonomous driving systems. {% cite tang2025omnigen %}
    
    <br>
    
5. <strong>Trajectory Risk Prediction Enhancement</strong>: By using synthetic trajectory data, we enhanced the Visual Language Model (VLM) in predicting the risks associated with planned trajectories, thereby improving the safety of the planned trajectories. This advancement helps foresee potential risks in real driving scenarios, optimizing the safety of autonomous driving decisions. {% cite hou2025drivemrp %}
</ul>

<br>

<h4>Future Outlook</h4>

<p>We will continue to optimize the self-correcting feedback loop framework, enhance the realism of the simulator, and improve high-level closed-loop capabilities. Our goal is to reduce data collection and training costs, further enhancing the robustness and generalization of autonomous driving models, ultimately driving autonomous driving technology toward a smarter and safer future.</p>

<br><br>

<h3><strong>Part 2: Unifying Muti-modal Understanding and Generation</strong></h3>

<br>

<h4>Our Objective:</h4>
<p>We believe that understanding and generation are two sides of the same coin in perceiving the world: deeper understanding enables more precise generation, while the ability to generate in turn reinforces the model’s grasp of the underlying patterns of the world. Toward this vision, we focus on (i) constructing more effective unified MLLM architectures, (ii) developing unified discrete/continuous multimodal representations, (iii) designing more effective visual tokenization methods, and (iv) exploring how generative capabilities can be leveraged to genuinely enhance understanding.</p>


<div style="text-align:center; margin:20px 0;">
    <img src="/assets/img/proj1_2.png" alt="Unifying Understanding and Generation" width="80%">
    <p class="figure-caption" style="font-size:14px; color:gray;">Figure 2: Understanding and generation are two sides of the same coin.</p>
</div>


<br>

<h4>Our Achievements So Far:</h4>

<ul>
1. <strong>Unified Visual Tokenizer</strong>: We proposed DualToken, a unified visual tokenizer for both understanding and generation. To disentangle the conflict between understanding and generation, we introduced separate codebooks for semantic and pixel-level objectives in visual tokenzier. DualToken achieves state-of-the-art performance in both reconstruction and semantic tasks while demonstrating remarkable effectiveness in downstream MLLM understanding and generation tasks. {% cite song2025dualtoken %}
    
    <br>
    
2. <strong>Can visual generation supervision enhance VLMs' understanding?</strong> We found that autoregressively reconstructing visual semantics can leads to stronger visual-language comprehension. {% cite wang2025autoregressive %}
</ul>

<br>

<h4>Future Outlook</h4>

<p>First, we aim to design more efficient and scalable tokenization mechanisms that can flexibly adapt to diverse modalities beyond vision and language, such as audio and video. Second, we intend to investigate how generative objectives can be more tightly integrated with understanding tasks, enabling mutual reinforcement between generation and understanding. Third, we envision applying our framework to real-world applications, such as embodied AI, to validate its broader impact.</p>

<br><br>

<h3><strong>Part 3: From Simulation to Reality: Toward Autonomous Embodied Robot</strong></h3>

<br>

<h4>Our Objective:</h4>
<p>Human can quickly adapt to new environments and tasks by leveraging prior knowledge, physical intuition, and high-level reasoning. In contrast, robot often rely on massive-scale data collection and environment-specific training, yet still struggle to generalize across diverse scenarios and perform reliably in the real world.
Our research focuses on bridging this gap by developing agents capable of transferring skills from simulation to the real world (Sim2Real), while building structured world models that enable generalizable reasoning, robust planning, and adaptive decision-making. We aim to move beyond brute-force imitation learning and toward data-efficient, autonomous intelligence.</p>


<div style="text-align:center; margin:20px 0;">
    <img src="/assets/img/proj1part3_abstract.png" alt="Towards Data-Driven Autonomous Embodied Robot" width="80%">
    <p class="figure-caption" style="font-size:14px; color:gray;">Figure 3: Towards Data-Driven Autonomous Embodied Robot. </p>
</div>


<br>

<h4>Our Achievements So Far:</h4>

<ul>
1. <strong>Generative Simulation Module</strong>: We propose a generative simulation module capable of diverse training scenes. This enables continuous policy generation and refinement within a closed-loop pipeline, where simulated experiences directly guide policy learning, and improved policies, in turn, trigger automatic generation of more challenging environments.
    
    <br>
    
2. <strong>Socially-Enhanced Navigation Policy</strong>: To handle complex multi-agent environments, we introduce a socially-enhanced navigation policy that incorporates social attributes and interaction modeling into policy learning. By embedding social compliance, comfort metrics, and group dynamics into the reward structure, our agents achieve significantly better performance in crowded, dynamic, and socially-constrained navigation tasks.
</ul>

<br>

<h4>Future Outlook</h4>

<p>We plan to extend our framework to more diverse tasks and heterogeneous robotic platforms, enabling agents to autonomously collect data, learn concepts, and adapt policies online with minimal human supervision.
Our long-term goal is to establish a unified paradigm for autonomous embodied intelligence, where agents not only learn efficiently from limited data but also generalize robustly to unseen environments, novel tasks, and real-world uncertainties.
</p>

<br><br>

<h3><strong>Part 4: From Data to Concepts: Toward Efficient Driving Intelligence</strong></h3>

<br>

<h4>Our Objective:</h4>
<p>Human drivers typically require only limited formal training—covering traffic rules, basic operations, simulated road practice, and driving norms—before gradually adapting to increasingly complex and unfamiliar situations with experience. In contrast, autonomous driving systems have consumed millions or even billions of data samples, yet achieving fully reliable performance still remains a challenge.
Our research explores whether autonomous agents can move beyond brute-force data accumulation by developing higher-level conceptual understanding from their training, somewhat akin to the human ability to generalize through intuition. We believe such an approach could lead to more data-efficient learning and enable agents to handle rare and long-tail scenarios more effectively. {% cite jia2024bench2drive %}</p>


<div style="text-align:center; margin:20px 0;">
    <img src="/assets/img/Project1_part4_by_zijian/concept_learning.png" alt="Data-driven vs Concept Illustration" width="80%">
    <p class="figure-caption" style="font-size:14px; color:gray;">Figure 4: Comparison between data-driven and concept-guided approaches.</p>
</div>


<br>

<h4>Our Achievements So Far:</h4>

<ul>
1. <strong>Concept-Learning Module</strong>: We are developing a concept-learning module that complements existing end-to-end driving architectures.{% cite renz2025simlingo %} This module aims to build a structured understanding of driving scenarios in parallel with traditional perception and control pipelines.
</ul>

<br>

<h4>Future Outlook</h4>

<p>We plan to extend this framework using more diverse datasets to improve the generalization of the concept model, with the ultimate goal of enhancing performance in unseen and complex situations while advancing the broader pursuit of data-efficient learning in autonomous driving.
</p>

<br>

</div>
