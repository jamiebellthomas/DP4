import numpy as np
import pickle
import pandas as pd
from hierarchyCalculations import *
with open('Models/default2', 'rb') as f:
    criteria_dictionary, sub_criteria_dictionary = pickle.load(f)

print('Criteria Dictionary:', criteria_dictionary)
print('---------------------')
print('Sub-Criteria Dictionary:', sub_criteria_dictionary)
#for key in sub_criteria_dictionary:
#    print(sub_criteria_dictionary[key])

# Import dummy drone data with index and column names
data = pd.read_excel('dummy_drone_data.xlsx', sheet_name='Sheet1', header=0)

# Iterate over all rows of data

for row in range(0,len(data)):
    model_name = extract_model_name(data,row)
    scores = extract_scores(data, sub_criteria_dictionary,row)
    print("---------------------")
    print(f'{model_name} scores:')
    print(scores)

    weighted_sub_criteria_scores = sub_criteria_weighted_scores(scores, sub_criteria_dictionary)
    print("---------------------")
    print(f'{model_name} weighted sub-criteria scores:')
    print(weighted_sub_criteria_scores)
    weighted_criteria_scores = criteria_weighted_scores(weighted_sub_criteria_scores, criteria_dictionary)
    print("---------------------")
    print(f'{model_name} weighted criteria scores:')
    print(weighted_criteria_scores)
    final_score = alternative_score(weighted_criteria_scores)
    print(f'{model_name} has an alternative score of {final_score}')
    print("---------------------")

