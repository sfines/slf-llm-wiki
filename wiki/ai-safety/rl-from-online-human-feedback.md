# Reinforcement Learning from Online Human Feedback

In the context of interactive oversight, Reinforcement Learning (RL) can be used to train an interaction agent using only online feedback signals from weak human supervisors.

For instance, an agent can be rewarded for minimizing the frequency of "I don't care" or "I don't know" responses from users during a decomposition-interaction loop. This online User Reward encourages the model to ask more effective, engaging, and relevant questions that better capture user intent. This demonstrates a weak-to-strong optimization effect, where non-expert feedback at interaction time is sufficient to optimize the question-asking and alignment strategies of strong models without relying heavily on post-hoc expert rating.

---
**Source:** [Steering LLMs via Scalable Interactive Oversight](../../raw/interactive-oversight-paper.md)