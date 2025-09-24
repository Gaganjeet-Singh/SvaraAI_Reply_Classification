1. If you only had 200 labeled replies, how would you improve the model without collecting thousands more?
I would use data augmentation like paraphrasing or back-translation to create more examples. I could also fine-tune a pre-trained model and use cross-validation to make the most of the small dataset.

2. Suppose you want to generate personalized cold email openers using an LLM. What prompt design strategies would you use to keep outputs relevant and non-generic?
I would give the LLM specific context about the recipient, like industry, role, or past interactions, and tell it to focus on personalization and keep professional tone. Using examples and constraints in the prompt helps make sure output is relevant, interesting, and not generic.

3. How would you ensure your reply classifier doesn’t produce biased or unsafe outputs in production?
I check training data for bad words and make sure model not give wrong answers.