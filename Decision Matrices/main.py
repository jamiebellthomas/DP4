# This script aims to combine a few other scriptys
# First the data will be imported
# The data will then be checked for errors in the user's inputs
# The data will then be checked for consisteicy in the user's decision making
# The output will be a pkl model that can be called in other scripts
import numpy as np
import pickle
import pandas as pd
from inputChecker import *



data = pd.read_excel('hierarchy.xlsx', sheet_name='Sheet1', header=0, index_col=0)


parents,number = criteria_info(data)
print("---------------------")
print("Checking for a valid model name...")
model_name_check,model_name = model_name_check(data)
if model_name_check == True:
    print(model_name_check)
if model_name_check == False:
    print("---------------------")
    quit()

print("---------------------")
print("Checking the uniqueness of parent criteria...")
parent_criteria_unique = criteria_unique(parents)
if parent_criteria_unique == True:
    print(parent_criteria_unique)
if parent_criteria_unique == False:
    print("---------------------")
    quit()

print("---------------------")
print("Checking that the parent criteria defined at the top of the input spreadsheet match the parent criteria defined in the subsequent tiers...")
parents_matching = parent_match(data,parents ,number)
if parents_matching == True:
    print(parents_matching)
if parents_matching == False:
    print("---------------------")
    quit()

print("---------------------")
print("Checking the uniqueness of sub-criteria...")
sub_criteria_uniqueness = sub_criteria_unique(data,number)
if sub_criteria_uniqueness == True:
    print(sub_criteria_uniqueness)
if sub_criteria_uniqueness == False:
    print("---------------------")
    quit()

print("---------------------")
print("Checking parent criteria have been added in a sequential manner (no gaps)...")
sequential_criteria = criteria_sequentially(data)
if sequential_criteria == True:
    print(sequential_criteria) 
if sequential_criteria == False:
    print("---------------------")
    quit()

print("---------------------")
print("Checking sub-criteria have been added in a sequential manner (no gaps)...")
sequential_sub_criteria = sub_criteria_sequentially(data,number)
if sequential_sub_criteria == True:
    print(sequential_sub_criteria)
if sequential_sub_criteria == False:
    print("---------------------")
    quit()

print("---------------------")
print("Checking that the pairwise comparison table for parent criteria is complete...")
parent_table_check = criteria_importance_table_checker(data,number)
if parent_table_check == True:
    print(parent_table_check)
if parent_table_check == False:
    print("---------------------")
    quit()

print("---------------------")
print("Checking that the pairwise comparison tables for sub-criteria are complete...")
sub_criteria_table_check = sub_criteria_importance_table_checker(data,number)
if sub_criteria_table_check == True:
    print(sub_criteria_table_check)
if sub_criteria_table_check == False:
    print("---------------------")
    quit()

print("---------------------")
print("USER INPUT CHECKS COMPLETE")
print("---------------------")

# The next step is to check the consistency of the user's decision making


