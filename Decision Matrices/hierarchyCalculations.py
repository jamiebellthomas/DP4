import pickle

with open('Models/default', 'rb') as f:
    criteria_dictionary, sub_criteria_dictionary = pickle.load(f)

print('Criteria Dictionary:', criteria_dictionary)
print('---------------------')
print('Sub-Criteria Dictionary:', sub_criteria_dictionary)