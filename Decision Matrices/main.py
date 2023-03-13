# This script aims to combine a few other scriptys
# First the data will be imported
# The data will then be checked for errors in the user's inputs
# The data will then be checked for consisteicy in the user's decision making
# The output will be a pkl model that can be called in other scripts
import numpy as np
import pickle
import pandas as pd
from inputChecker import *
from AHPTier import *
import sys
import os
import shutil

data = pd.read_excel('hierarchy.xlsx', sheet_name='Sheet1', header=0, index_col=0)
    
def main():
    sys.stdout = open("output.log", "w")
    parents,number = criteria_info(data)
    print("---------------------")
    print("Checking for a valid model name...")
    model_name_bool,model_name = model_name_check(data)
    if model_name_bool == True:
        print(model_name_bool)
    if model_name_bool == False:
        print("---------------------")
        return False, model_name

    print("---------------------")
    print("Checking the uniqueness of parent criteria...")
    parent_criteria_unique = criteria_unique(parents)
    if parent_criteria_unique == True:
        print(parent_criteria_unique)
    if parent_criteria_unique == False:
        print("---------------------")
        return False, model_name

    print("---------------------")
    print("Checking that the parent criteria defined at the top of the input spreadsheet match the parent criteria defined in the subsequent tiers...")
    parents_matching = parent_match(data,parents ,number)
    if parents_matching == True:
        print(parents_matching)
    if parents_matching == False:
        print("---------------------")
        return False, model_name

    print("---------------------")
    print("Checking the uniqueness of sub-criteria...")
    sub_criteria_uniqueness = sub_criteria_unique(data,number)
    if sub_criteria_uniqueness == True:
        print(sub_criteria_uniqueness)
    if sub_criteria_uniqueness == False:
        print("---------------------")
        return False, model_name

    print("---------------------")
    print("Checking parent criteria have been added in a sequential manner (no gaps)...")
    sequential_criteria = criteria_sequentially(data)
    if sequential_criteria == True:
        print(sequential_criteria) 
    if sequential_criteria == False:
        print("---------------------")
        return False, model_name

    print("---------------------")
    print("Checking sub-criteria have been added in a sequential manner (no gaps)...")
    sequential_sub_criteria = sub_criteria_sequentially(data,number)
    if sequential_sub_criteria == True:
        print(sequential_sub_criteria)
    if sequential_sub_criteria == False:
        print("---------------------")
        return False, model_name

    print("---------------------")
    print("Checking that the pairwise comparison table for parent criteria is complete...")
    parent_table_check = criteria_importance_table_checker(data,number)
    if parent_table_check == True:
        print(parent_table_check)
    if parent_table_check == False:
        print("---------------------")
        return False, model_name

    print("---------------------")
    print("Checking that the pairwise comparison tables for sub-criteria are complete...")
    sub_criteria_table_check = sub_criteria_importance_table_checker(data,number)
    if sub_criteria_table_check == True:
        print(sub_criteria_table_check)
    if sub_criteria_table_check == False:
        print("---------------------")
        return False, model_name

    print("---------------------")
    print("USER INPUT CHECKS COMPLETE")
    print("---------------------")

    # The next step is to check the consistency of the user's decision making

    # Now the each pairwise comparison table will be passed into an AHP object, the weightings will be calculated and the consistency will be checked
    # The weightings will then be added to a dictionary
    # The dictionary will then be added to a dictionary of dictionaries
    # Finally, the dictionary of dictionaries will then be saved as a pkl file

    # First let's create call AHPTier to create an AHP object for the parent criteria
    # The procedure for this was mocked up in hierarchyReader.py script
    print("---------------------")
    print("Now the consistency of the user's decision making will be checked")
    print("---------------------")
    

    parent_criteria_class = (criteria_class(data))
    print(parent_criteria_class.importance_matrix)
    parent_criteria_class.weighting_calculator()
    if parent_criteria_class.consistency_checker() == True:
        print("Parent Criteria Consistency Check: Passed")
        parent_criteria_weightings_dictionary = parent_criteria_class.weightings_dictionary()
    if parent_criteria_class.consistency_checker() == False:
        print("Parent Criteria Consistency Check: Failed")
        print("Check the pairwise comparison table for parent criteria and ensure your decision making is consistent")
        print("---------------------")
        return False, model_name
    print("Parent criteria weightings:", parent_criteria_weightings_dictionary)
    print("---------------------")

    # Now let's create call AHPTier to create an AHP object for the sub-criteria
    # First let's extract the sub-criteria pair wise tables from the input spreadsheet and save them in a dictionary where the key is the parent criteria
    # This will help us keep track of the hierarchy structure
    sub_criteria_dictionary = {}
    for i in range(1,len(parent_criteria_class.criteria)+1):
        sub_criteria_table,sub_criteria,parent = sub_criteria_tier_importance(data,i)
        sub_criteria_dictionary[parent] = [sub_criteria_table,sub_criteria]

    sub_criteria_weightings_dictionary_db = {}
    tier = 0
    print("Sub-criteria weightings:")
    print("---------------------")

    for key in sub_criteria_dictionary:
        tier+=1
        sub_criteria_class = AHPTier(sub_criteria_dictionary[key][0],sub_criteria_dictionary[key][1])
        sub_criteria_class.weighting_calculator()
        if sub_criteria_class.consistency_checker() == True:
            print(f"{key} sub-criteria (Tier 2.{tier}) consistency check: Passed")
            sub_criteria_weightings_dictionary = sub_criteria_class.weightings_dictionary()
            print(f"({sub_criteria_weightings_dictionary})")
            print("---------------------")

            sub_criteria_weightings_dictionary_db[key] = sub_criteria_weightings_dictionary
            
        if sub_criteria_class.consistency_checker() == False:
            print(f"{key} sub-criteria (Tier 2.{tier}) consistency check: Failed")
            print(f"Check the pairwise comparison table for (Tier 2.{tier}) and ensure your decision making is consistent")
            print("---------------------")
            return False, model_name
    print("USER DECISION MAKING CONSISTENCY CHECKS COMPLETE")
    print("---------------------")

    # Now let's save the parent criteria weightings dictionary and the sub-criteria weightings dictionary of dictionaries as a pkl file
    # The pkl file will be saved in the Models folder and will be named after the model name the user has specified

    print(f"Exporting model as a pkl file to {os.getcwd()}\Models\{model_name}")
    path = f'Models/{model_name}'
    if not os.path.exists(path):
        os.makedirs(path)
        
    with open(f'Models/{model_name}/{model_name}', 'wb') as f:
        pickle.dump((parent_criteria_weightings_dictionary, sub_criteria_weightings_dictionary_db), f)
    print("...")
    print("Export completed")
    print("---------------------")
    # close thte output log file
    sys.stdout.close()
    # Move the output log file to the Models folder
    shutil.move('output.log', f'Models\{model_name}\output.log')
    sys.stdout = sys.__stdout__
    return True, model_name
    
    
    
if __name__ == "__main__":
    result, model_name = main()

if result == False:
    # close thte output log file
    sys.stdout.close()
    # Move the output log file to the Models folder
    path = f'Models/{model_name}'
    if not os.path.exists(path):
        os.makedirs(path)
    shutil.move('output.log', f'Models/{model_name}/output.log')
    sys.stdout = sys.__stdout__
    print("---------------------")
    print("Model creation failed")
    print("Check the output log file for more information")
    print(f"Path: {os.getcwd()}\Models\{model_name}\output.log")
    print("---------------------")

if result == True:
    print("---------------------")
    print("Model creation successful")
    print(f"Path: {os.getcwd()}\Models\{model_name}")
    print("---------------------")
    
    

    





