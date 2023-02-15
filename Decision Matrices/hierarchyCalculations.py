import pickle
import pandas as pd
import numpy as np


with open('Models/default', 'rb') as f:
    criteria_dictionary, sub_criteria_dictionary = pickle.load(f)

print('Criteria Dictionary:', criteria_dictionary)
print('---------------------')
print('Sub-Criteria Dictionary:', sub_criteria_dictionary)
for key in sub_criteria_dictionary:
    print(sub_criteria_dictionary[key])

# Import dummy drone data

data = pd.read_excel('dummy_drone_data.xlsx', sheet_name='Sheet1', header=0, index_col=0)

scores = data.iloc[2]
print(scores)
# Extract scores for each criteria
criteria_scores = {}
for key in criteria_dictionary:
    for sub_key in sub_criteria_dictionary[key]:
        criteria_scores[sub_key] = scores[sub_key]
    
#print(criteria_scores)
weighted__sub_criteria_scores = {}
for key in sub_criteria_dictionary:
    weighted__sub_criteria_scores[key] = []
    for sub_key in sub_criteria_dictionary[key]:
        weighted__sub_criteria_scores[key].append(criteria_scores[sub_key]*sub_criteria_dictionary[key][sub_key])
print(weighted__sub_criteria_scores)

# Calculate weighted criteria scores
weighted_criteria_scores = {}
for key in criteria_dictionary:
    weighted_criteria_scores[key] = sum(weighted__sub_criteria_scores[key]) * criteria_dictionary[key]

alternative_score = sum(weighted_criteria_scores.values())
print(alternative_score)

