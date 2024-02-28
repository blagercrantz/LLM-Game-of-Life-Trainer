# LLM-Game-of-Life-Trainer
How we can train LLMs to think more logically

This is a simple logic puzzle based on Conway's Game of Life. The goal is to predict how a grid of any given size will look after one iteration. What if we generate incrementally harder logic puzzles such as these and let GPT-4 or a model of its size solve them? If the model gets the answer right, we create more versions of that model, with slightly tweaked weights in the last layer of the neural network. This could lead to more and more logical versions of the LLM evolving.

One notable aspect that separates this kind of puzzle from physics or math problems is that the internet has way less material on how to solve this kind of puzzle. This means that any potential correct answers will be because of original logical reasoning instead of the LLM copying already existing solutions from similar problems on the internet.
