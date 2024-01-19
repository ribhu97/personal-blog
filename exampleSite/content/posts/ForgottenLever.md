---
title: The Forgotten Lever of Neural Scaling Laws
date: 2024-01-19
description: "How Data Quality can be leveraged in the era of LLMs, and how people often overlook it when talking about scaling laws"
image: images/scaling_mountain.jpeg
---
While driving a few weeks back, I was listening to a podcast (Cognitive Revolution) episode where the Perplexity CEO, Aravind Srinivas was talking about moats in the AI space [1]. One of the things he mentioned really stuck out to me.

> Everybody's building their index because I think in the world where large language models are commodity and the training recipe for them or the weights are just right on their open source, the edge goes to the data markets (...) You don't even want 100 billion pages in your index. It's not about the quantity here again, right? You want the best web pages on your that's probably a billion or 10 billion.

"Wait a second! I was told quantity of data is always good " is what you might be thinking to yourself. Its the narrative that has ruled the AI world since the days of GPT-3, where the more data you have you can just train a big model that can make things better. Right?

## Applying Scaling Laws

Given the current situation with Large Language Models (LLMs henceforth), and how the pace has picked up in their development, not just from the big players but even the open source world. The basis of most of the development in the domain has been the result of the seminal works of neural scaling laws [2,3,4]. The major focus of such research has been on three knobs: data, compute, and parameter-size. To those of you unfamiliar about what I'm talking about, neural scaling laws show that as you increase one or more of these knobs, the performance of models scale exponentially according to a power law.

Following this assumption, companies such as OpenAI and Anthropic began exploring LLMs. Causal language models scaled up to have billions of parameters, trained on trillions of available texts on the internet, and tuned by human feedback (a la reinforcement learning), and these models held up the assumption. This is where the mainstream narrative was taken over by the "more data, more compute, bigger models = $$$"

## The Forgotten Lever

In a talk at the Simons Institute, Deepmind's Yasaman Bahri mentioned explicitly at the beggining of her talk that she would not focus on data quality in the discussion [10]. Now, its perfectly fine to do so, especially given that the talk was about the Taxonomy and Origins of Scaling Laws. But, I have noticed this trend that people tend to focus a lot more on the obvious 3 levers, and leave a 4th one out.

Moreover, another question was asked about the quality of data used in the training of LLMs. Models such as Phi [5, 6], which show that significantly smaller models when trained on small quantity but high quality of data can reach close to the performance of larger models trained on larger amount of data with mixed quality.

Data quality has become more talked about recently even though discussions on scaling laws have been going on for a few years now. It wasn't until the Beyond Scaling Laws paper, in which it was directly addressed [11]. As has been shown in the research done before, the diminishing returns of increasing data, parameters, and compute, can be helped by pruning for data quality. In fact it is so effective that it changes the Power Law from linear (or realistically sub-linear) to exponential. Not only did they simply discover and discuss it, but gave practical methods to go about it in an unsupervised manner.

Much more recently one of the co-authors of the Mamba architecture, Tri Dao talked about how data quality is the only thing that changes the slope of neural scaling [12], and different architectures are not that different. Coming from someone who has led a challenge to the transformer as the status quo for the first time in almost half a decade, that's a huge claim.

## The End (?)

The problem of quality becomes much more evident when we start realising how a lot of text currently produced on the internet is by LLMs. Hence, future LLMs will be trained on synthetic data, i.e. non human-generated data. While the dead internet theory might ring in your head, its more about the paths LLM development can take. On the one hand, there is the optimistic take of models like Orca [7], trained on the traces of GPT-4, which performs quite well on certain benchmarks. But as many people in the field believe, it might just plateau out at some point in the future. So on the other hand, there is the curse of recursion [8] that signal decay in models trained on too much synthetically generated data.

Further, the issue is not limited to openly available data. Certain knowledge workers on platforms such as Amazon's Mechanical Turk are incentivized to use LLMs to increase their productivity. So much so that it is estimated around 33-46% of them use LLMs for data annotation [9]. In case you thought you could get around the terrible quality of freely scrapable data on the internet, then you need to think again.

## Remembering the Forgotten

All hope is not lost. Data quality is hard to judge, and yes we do not exactly know how important it is for which sorts of data, for what architectures, and in which tasks. But, as I mentioned before, there are ways to prune out data and figure out a general idea of which data points can help scale your model's performance exponentially.

Yes, its not perfect, but there are nascent methods out there. It is harder to have general solutions since quality itself is hard to generally define, i.e. it is heavily context dependent. Sure using synthetic datasets, one can control for quality to some extent, but it comes with its own set of caveats. There could be benchmarks in the future that check for general quality of text through parameters like truthfulness, completeness, and so on.

With smaller models being easier to use, and fine-tuning them becoming even easier (due to new methods like DPO), training models on your own smaller, high quality data becomes more feasible. And hence, the forgotten lever can be utilised for "scaling" the slopes of error graphs (pun intended)

#### References:

1. Gunning for Google with Perplexity CEO Aravind Srinivas. Cognitive Revolution. [Link](https://share.snipd.com/snip/73a24ca0-bb74-4918-853c-a3c0b907491f)

2. Explaining Neural Scaling Laws. Bahri et. al. (2021). [Link](https://arxiv.org/pdf/2102.06701.pdf)

3. Scaling Laws for Neural Language Models. Kaplan & McCandlish et. al. (2020). [Link](https://arxiv.org/abs/2001.08361)

4. Scaling Laws for Autoregressive Generative Modeling. Henighan et. al. (2020). [Link](https://arxiv.org/abs/2010.14701)

5. Textbooks are all you need. Gunasekar et. al. (2023) [Link](https://arxiv.org/abs/2306.11644)

6. Textbooks Are All You Need II: phi-1.5 technical report. Li et. al. (2023). [Link](https://arxiv.org/abs/2309.05463)

7. Orca : Progressive Learning from Complex Explanation Traces of GPT-4. Mukherjee et. al. (2023). [Link](https://arxiv.org/abs/2306.02707)

8. The Curse of Recursion: Training on Generated Data Makes Models Forget. Shumailov et. al. (2023). [Link](https://arxiv.org/abs/2305.17493v2)

9. Artificial Artificial Artificial Intelligence: Crowd Workers Widely Use Large Language Models for Text Production Tasks. Veselovsky et. al. (2023). [Link](https://arxiv.org/abs/2306.07899)

10. Understanding the origins and taxonomy of neural scaling laws. Yasaman Bahri (2023). [Link](https://www.youtube.com/watch?v=MUvFuZpxLU8)

11. Beyond neural scaling laws: beating power law scaling via data pruning. Sorscher et. al. (2022). [Link](https://arxiv.org/abs/2206.14486)

12. Interviewing Tri Dao and Michael Poli of Together ai on the Future of LLM Architectures. Interconnects AI. [Link](https://www.youtube.com/watch?v=OFFHiJzPpCQ&t=1902s)