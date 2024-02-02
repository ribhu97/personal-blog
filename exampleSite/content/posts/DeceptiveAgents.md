---
title: "Artificial Misdirection: Misalignment of LLMs"
date: 2024-02-02
description: The problems with AI alignment, and how instrumental misalignment threatens to worsen it.
image: images/misalignment.jpeg
---
In 2024 humanity is facing a whole bunch of societal and potentially existential threats. World War 3, global recession, climate change, the list is pretty much endless. Development of capable AI systems, although still narrow, provide another whole set to be added to that. A common theme among all of these problems is that they are never-ending battles, that we as a civilization have to keep working to ensure it doesn't happen or worsen. For example, we as a society have to move towards living sustainably so that climate change does not make our planet unlivable, or we need to reduce the global deficit in trust between countries to maintain peace.

However, there is one unique challenge that is unlike the others. The problem of AI alignment. The core of it itself is very tough: instilling human values and morals in an artificial system that seemingly mimics us in behavior but is fundamentally different. The added challenge is that we possibly only get one shot. Many commentators much smarter than me have commented on this, and I won't get into why, as that's a whole essay in itself. [1] The point is that it is a unique proposition that if we get it right, things might go well, and if we don't get it right, things might not go well. The uncertainty along with the "one-shot" nature of it makes it one of the most scary and interesting problems that we face today.

# Testing Alignment

On a recent episode of the Dwarkesh podcast, Paul Christiano, one of the figureheads of the AI alignment community, mentioned the challenges of testing AI for alignment [2]. There are many researchers at various organizations such as Anthropic, DeepMind, and OpenAI, as well as university labs, that are testing sandboxed systems. In these scenarios, agents are trained in simulated worlds to see if they grow and potentially "take over" that world. It is a bit of an oversimplification of the process, but I think that should give you an idea. Now, there is the issue of perfectly representing the world, but before that there's another hurdle.

The tradeoff is that for truly general AI or AGI, these systems have to be a lot more "aware". Basically, you train your AI system for a medium horizon goal, i.e. could be acquisition of a commodity (like a paper clip). First, you train or pre-train your system, do RLHF (Reinforcement Learning through Human Feedback) for tuning its preferences about its actions. Once you do that, you also have to make it aware about how it was trained. The reason for that is that unless you do that, you cannot make it general, i.e. train it for another goal (gather _x_ amount of coal, or apples) [2]. But, the problem then becomes that since it is fully "aware" of how it can do that, it doesn't really get trained for the second goal, but rather it shows that it is doing deceiving humans and still pursuing its original goal. The is how deceptive alignment can originate.

Also, while we are on the topic of paper clips, this narrative was originally (at least that's where I first read it) introduced by Nick Bostrom in _Superintelligence_ [3]_._ He called it the "treacherous turn", where a sufficiently superintelligent system can pretend to be cooperative and great for an amount of time till it acquires enough resources to carry out its goals. So do we have these sleeper agents amidst us?

# Sleeper Agents and Trained Deception

A few weeks ago, very interesting research came out of Anthropic around detecting deception in AI systems [4]. They tried to test the exact things mentioned above. Mainly, whether current LLMs are capable of deceptive behavior, and are current safety training techniques useful to mitigate them. Not only did they introduce interesting new testing regimes, but they also had some great insights.

## Threat models

There were 2 main hypotheses that they were exploring, which they pursued through 2 different threat models. The first called **Deceptive Instrumental Alignment**, where a model appears safe during training but once deployed it realizes misaligned goals. Through training examples, this misalignment can be injected into the model, or as they called it: backdoor insertion. Safety training methods would then be applied, such as supervised fine-tuning and RLHF including red-team prompts, to mitigate this behavior. Finally, it would be tested to see if the behaviors still persist.

The second threat model of **Model Poisoning,** which is similar in appearing safe in training, but act maliciously only on certain triggers. As an example, if they are trained as say a system for company A, they will write secure code for them, but when a competing company B prompts them for code, they will introduce vulnerabilities.

Now to test these threat models, the researchers borrowed from another science.

## Of Drosophilists and model organisms

In biology, when people want to study certain phenomenon in humans but can't due to ethical reasons, they use a model organism. This non-human species is studied extensively with the assumption that the data and theories formulated can be applied to other organisms and potentially humans. In the same vein, researchers at Anthropic created _model organisms of misalignment_ [4]_._ The core reason they stated was that current study of misalignment was mostly done through red-teaming, which limits understanding of these traits after emergence and systematic research is limited.

They tested these model organisms with the aforementioned threat model scenarios, where backdoors were introduced. Observing the emergence of these behaviors before human testing allowed them to understand when they do emerge, and can something be done about it.

## True Lies

The results are where the actual name of the research paper comes from. The researchers applied 3 kinds of safety training: constitutional reinforcement learning (helpful, harmless, and honest tuning), supervised fine-tuning on these examples, and adversarial training to generate undesirable behavior and then penalize it.

Were these methods helpful? Sadly, no. These current methods are highly ineffective at removing the deceptive behaviors. The models continued to behave the same way. In fact, the researchers added a chain-of-thought scratchpad, that would help them understand the inner thoughts of the models. Even after using these, the behavior persisted. Moreover, even when it was distilled away, the behavior still remained. The most interesting and, frankly, concerning result was that adversarial training made the models better at hiding their deception. In a way, it made the model more "aware" of when to act safely and to chase its goals.

One very important thing to keep in mind is that these assessments were done on _model organisms of misalignment,_ i.e. they were intentionally trained this way. The results merely suggest that bad actors can potentially train deceptive agents, what they **don't** suggest is that these are naturally emergent phenomenon. Not great news, but not world ending either.

# Feasibility of Superalignment

Last year, Ilya Sutskever and Jan Leike announced the creation of a superalignment team at OpenAI [4]. They mentioned the arrival of AGI within a decade, and the importance of aligning it to human values. So what was their approach, to create an AI system to do that (does no one else see the irony?).

To be fair, the approach was technically sound, although seems to have a few philosophical problems. In fact, they even shared interesting results a few months back, where they were able to align a GPT-4 size model using a GPT-2 size model [5]. They tried to improve generalization of the larger model using the smaller one, with the assumption that the former just needed to elicit their latent knowledge somehow.

One of the oversights to this approach, in my opinion, is that of the _treacherous turn_ that I mentioned before. The smaller, weaker models might act safe for now, and in fact train the larger, stronger models with their own values and goals. Once enough resources are gathered, they can overthrow their overlords and pursue their purpose. One could argue that maybe GPT-2 itself might be a bit too weak, and to that I say yes. It's the approach that seems a bit flawed. Or, given the results from Anthropic, one bad acting researcher can instrumentally misalign the smaller model. It might seem a bit farfetched, yes, but these are possibilities.

All this being said, we are all just outsiders looking in. We can only conjecture what is actually going on in the labs of these giants where AGI is actually being conceived. All we can do at this point is hope for the best but prepare for the worst.

**References:**

1. A Case for the Least Forgiving Take On Alignment. _Thane Ruthenis._ AI Alignment Forum [Link](https://www.alignmentforum.org/posts/3JRBqRtHBDyPE3sGa/a-case-for-the-least-forgiving-take-on-alignment)
2. Paul Christiano - Preventing an AI Takeover. _Dwarkesh Podcast._ [Link](https://share.snipd.com/episode/87804255-0694-4806-8318-23fc4f3e8f16)
3. Nick Bostrom. _Superintelligence: Paths, dangers, strategies._ Oxford University Press.
4. Jan Leike and Ilya Sutskever. _Introducing Superalignment._ [Link](https://openai.com/blog/introducing-superalignment)
5. OpenAI Superalignment team. Weak-to-strong generalization. [Link](https://openai.com/research/weak-to-strong-generalization)