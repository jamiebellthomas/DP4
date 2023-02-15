#Import hierarchy xlsx

import pandas as pd
import numpy as np
from AHPTier import * 
import pickle


data = pd.read_excel('hierarchy.xlsx', sheet_name='Sheet1', header=0, index_col=0)
model_name = (data.iat[0,5])
print(model_name)
parent_criteria_class = (criteria_class(data))
parent_criteria_class.weighting_calculator()
parent_criteria_class.consistency_checker()
if parent_criteria_class.consistency_checker() == False:
    print('Parent criteria tier matrix is not consistent')
    quit()





# Initialise dictionary to store sub criteria information
sub_criteria_dictionary = {}
for i in range(1,len(parent_criteria_class.criteria)+1):
    sub_criteria_table,sub_criteria,parent = sub_criteria_tier_importance(data,i)
    sub_criteria_dictionary[parent] = [sub_criteria_table,sub_criteria]


#print(sub_criteria_dictionary)

# Create AHPTier object for each sub criteria tier and calculate weightings for each sub criteria add to dictionary
for key in sub_criteria_dictionary:
    sub_criteria_tier = AHPTier(sub_criteria_dictionary[key][0],sub_criteria_dictionary[key][1])
    sub_criteria_tier.weighting_calculator()
    sub_criteria_tier.consistency_checker()
    if sub_criteria_tier.consistency_checker() == False:
        print('Sub criteria tier matrix is not consistent')
        break
    sub_criteria_dictionary[key].append(sub_criteria_tier.weightings_dictionary())

if sub_criteria_tier.consistency_checker():
    for key in sub_criteria_dictionary:
        sub_criteria_dictionary[key] = sub_criteria_dictionary[key][2]


# Remove first and second elements of each sub criteria dictionary



print('Criteria Dictionary:', parent_criteria_class.weightings_dictionary())
print('---------------------')
print('Sub-Criteria Dictionary:', sub_criteria_dictionary)

#with open(f'Models/{model_name}', 'wb') as f:
#    pickle.dump((criteria_dictionary, sub_criteria_dictionary), f)