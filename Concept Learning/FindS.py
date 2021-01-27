"""
The Find-S algorithm is a basic concept learning algorithm. It finds the most specific hypothesis that fits all
the positive examples. The algorithm moves from the most specific hypothesis to the most general hypothesis.
Notation :=
    1. '?' : Any value is possible
    2. 'A' : The value A is possible
    3. '-' : No value is possible
    4. Most general hypothesis : ['?', '?' .... , '?']
    5. Most specific hypothesis : ['-', '-', ...., '-']

Steps : 1. Start with the most specific hypothesis
        2. Take the next example. If it is negative, there is no change
        3. If the example is positive and our current hypothesis is too specific update our current hypothesis
           to a more general
        4. Repeat above for all examples and we're done
"""
import pandas as pd
import sample_data

data = sample_data.get_sport_data()
num = len(data.columns)
h = ['-'] * (num-1)
print('Initial :', h)
for i in range(data.shape[0]):
    example = data.iloc[[i]]
    if example['EnjoySport'].item() == 'Yes':
        for j, col in enumerate(example.drop('EnjoySport', axis=1)):
            if h[j] == '-':
                h[j] = example[col].item()
            elif example[col].item() != h[j]:
                h[j] = '?'
            else:
                pass
    print(example['EnjoySport'].item(), ':', h)
