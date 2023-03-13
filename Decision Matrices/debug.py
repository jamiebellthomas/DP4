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
    parent_criteria_class = (criteria_class(data))
    print(parent_criteria_class.importance_matrix)
    print(parent_criteria_class.weighting_calculator())
    # THIS IS THE PROBLEM ^^^ 
    # It was fixed by specifying dtype = float 

if __name__ == "__main__":
    main()

