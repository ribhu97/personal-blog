---
title: "The Benchmark Trap: Why LLM Metrics Mislead and Evals Enlighten"
date: 2024-05-12
description: The multitude of issues with LLM benchmarks, and the problem of documenting the complexities to accurately test LLMs, and using evals as alternatives
categories: ["research"]
tags: ["benchmarks", "evals", "llm"]
image: images/benchmark-trap.jpeg
---

"We have just launched our newest large language model trained with the best curated dataset with the state-of-the-art GPUs and we have improved on the MMLU by *n* number of points, surpassing the previous best." Does this sound familiar? Reads like a press release of an AI company releasing their shiny new LLM for the world. As the arms race heats up it was bound to happen. But there's one big problem with this line. No, I'm not talking about the obvious x-risk with larger, uninterpretable, and unaligned models. I'm not talking about the effects on climate change due to the the emissions of data centres. I want to illustrate one issue that's not talked about as much but is actually much easier to control and to take action on.

I'm talking about benchmarks and evals. And I want to start with the elephant, or rather the whale in the room. The **MMLU**. It is treated as the gold standard of LLM benchmarks. Whenever a company releases their newest offering they boast about how much they have improved on it. Its almost as if getting a 100 means we have achieved AGI. But that's far from the truth. Look at the following questions: ![MMLU question quality issues](https://substackcdn.com/image/fetch/w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F82dec54b-cb33-4bd0-9529-f1fc0d4767af_1198x1592.png)

Do they make sense? At all? These are questions directly from the business ethics section of MMLU. And this is only the tip of the iceberg. There was a recent paper that tested LLM performance on grade school math using the GSM8K dataset which is another common benchmark, and they found glaring errors in it.[^1] Even other benchmarks like Hellaswag and CommonsenseQA have these problems.

## Challenge of Picking an LLM

Picking the right language model for your project can be tricky, and benchmarks have an obvious problem of reliability. But they are often the first line of evaluation when organisations or individuals decide which LLM to use in their workflows and products. The downstream effects of this unreliability can be catastrophic. Just as an example, imagine you are a company deploying an assistant for grade-school students to practice math. You evaluate your LLM-based agent on GSM8K, and it works really well, reaching state-of-the-art performance. Hence, you gladly deploy it to hundreds of students. At the end of the semester your inbox is flooded with parents' emails saying their child has performed worse than before.

While there are general rules-of-thumb, like use the Cohere models for RAG, or integrate Snowflake's new LLM for enterprise tasks, these are all qualitative heuristics. Vibes can only take you so far. The world of choosing the LLM of choice is not as straight forward as going to the benchmark leaderboard. Firstly, the domains are vast, and benchmarks right now are much more general. Secondly, the complexity of workflows, and the language required to capture it — in most use-cases you don't just do question→answer pairs. There are often chains or multiple in-between steps (chain-of-thought, ReAct, etc.) that also need to be evaluated, which benchmarks don't really cover. Third, prompt-LLM fit is a real thing.[^3][^4] How you prompt an LLM can drastically change its performance on benchmarks. And finally, there's the whole can of worms of evaluating multimodal LLMs.

The short answer is to use a few reliable benchmarks such as the GSM1K that was created by the same researchers who found the errors in GSM8K.[^1] Novel, synthetically generated benchmarks, which are also human evaluated, such as these are available. Another reliable "benchmark" is the LMSys Chat Arena, where human evaluators do 1-v-1 comparisons between different LLMs. Unfortunately these human-based evaluations are not scalable especially for smaller organisations, which brings us to the long answer.

## The real world needs evals...

![Eval pipeline diagram from Hamel Hussain's blog](https://substackcdn.com/image/fetch/w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7afcfbbe-9b0b-4e91-85a2-d591a376b6aa_2081x1109.png)

Every few weeks, you hear about problematic AI systems deployed to the world. There was the recent fiasco with a chatbot released by WHO which could have ended up [harming more people than helping them](https://twitter.com/rachelmetz/status/1781013667989106932). Another case a few months back was with the UK-based logistics company DPD. They deployed a chatbot for customer support, which somehow ended up bad-mouthing the company itself.[^5]

To fix all these issues, we need model evaluation, also called in the LLM world as evals. Without having a robust evaluation system in place, your LLM-powered product will never see the light of production.[^2] It is a mix of tracing logs, unit-tests, and dataset curation. Evaluations have 3 levels: unit tests being the most basic checks, model and human eval which involves more subjectivity, and A/B testing for really mature systems.

All this is great. I can evaluate an LLM-based product more fully. But how is this helping me pick the LLM compared to benchmarks? Firstly, benchmarks are general. Eval systems like these are not only specific to your task, but your product as well. You can evaluate how well the LLM fits into your whole use-case. Secondly, prompt-LLM fit can only be discovered through such a system. And third, many of these can be low-tech solutions which brings involvement of a broader set of stakeholders. Many "business" people can directly contribute to your eval and dataset curation.

## ...but its not as easy

Evals are the best thing since sliced bread, but the challenge is that they are hard to do, which seems counter-intuitive. Allow me to explain. First things first, the infrastructure of evals is still in the beginning stages. The whole LLMOps field seems completely new to even the industry folks, because it is.

Speaking of infrastructure, one of the most important components of testing is model evals, where another LLM evaluates yours. A big problem that we recently found out as a community is that these models are biased towards their own outputs.[^6] It makes the whole auto-eval thing a bit more tricky.

People are needed to do the most important job of this whole process though, and that's curating the datasets. First, we have the problem of standardising the workflow and finding the right tool for the job. But, the second part is the larger problem, which is to create eval datasets for agentic workflows. And we have the synthetic data route but to be really effective in that game you need a really good starting dataset. That gives us a cold-start problem.

## What is left to do

For all the slander I have dished out to benchmarks, a lot of them are genuinely helpful to get a general feel for the performance of LLMs. There's a reason both academia and industry have been using them for the last few years. What I wanted to highlight is that they are not flawless as many make them out to be. Furthermore, they are not very useful to measure the ability on specific domains or tasks. For this part, evals are a better choice and generally a good practice when building complex LLM-based workflows for your product.

In an era where LLMs hold both immense promise and peril, the commitment to continual, context-aware evaluation will separate the leaders from the laggards, paving the way for AI systems that are not only powerful but trustworthy and aligned with human values.

[^1]: Zhang, H. et al. (2024). *A Careful Examination of Large Language Model Performance on Grade School Arithmetic*. [arXiv preprint](https://arxiv.org/pdf/2405.00332)
[^2]: Hamel Hussain (2024). *Your AI Product Needs Evals*. [Link](https://hamel.dev/blog/posts/evals/)
[^3]: SmartGPT. [Link](https://github.com/Cormanz/smartgpt)
[^4]: Moghaddam, Shima R. Honey, Christopher J. (2023). *Boosting Theory of Mind Performance in Large Language Models*. [Link](https://arxiv.org/ftp/arxiv/papers/2304/2304.11490.pdf)
[^5]: Jane Clinton (2024). *DPD AI chatbot swears, calls itself 'useless' and criticises delivery firm*. [Link](https://www.theguardian.com/technology/2024/jan/20/dpd-ai-chatbot-swears-calls-itself-useless-and-criticises-firm)
[^6]: Panickssery, A., et. al. (2024). *LLM Evaluators Recognize and Favor Their Own Generations*. [arXiv preprint](https://arxiv.org/pdf/2404.13076)
