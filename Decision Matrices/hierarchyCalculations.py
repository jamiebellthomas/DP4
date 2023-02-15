
import pandas as pd

# These functions run on a single row of scores from an imported data set.
# It needs to be iterated over all rows of data to calculate the scores for all drones.
def extract_model_name(data:pd.DataFrame,row:int):
    model_name = data['Company'][row] + ' ' + data['Model'][row]
    return model_name
def extract_scores(data:pd.DataFrame, sub_criteria_dictionary:dict,row:int):
    scores = {}
    for key in sub_criteria_dictionary:
        for sub_key in sub_criteria_dictionary[key]:
            scores[sub_key] = data[sub_key][row]
    return scores

def sub_criteria_weighted_scores(scores:dict, sub_criteria_dictionary:dict):
    weighted_sub_criteria_scores = {}
    for key in sub_criteria_dictionary:
        weighted_sub_criteria_scores[key] = []
        for sub_key in sub_criteria_dictionary[key]:
            weighted_sub_criteria_scores[key].append(scores[sub_key]*sub_criteria_dictionary[key][sub_key])
    return weighted_sub_criteria_scores

# Calculate weighted criteria scores
def criteria_weighted_scores(weighted_sub_criteria_scores:dict, criteria_dictionary:dict):
    weighted_criteria_scores = {}
    for key in criteria_dictionary:
        weighted_criteria_scores[key] = sum(weighted_sub_criteria_scores[key]) * criteria_dictionary[key]
    return weighted_criteria_scores

def alternative_score(weighted_criteria_scores:dict):
    #sum of weighted criteria scores
    score = sum(weighted_criteria_scores.values())
    return score



