#Import hierarchy xlsx

import pandas as pd
import numpy as np
from AHPTier import AHPTier


data = pd.read_excel('hierarchy.xlsx', sheet_name='Sheet1', header=0, index_col=0)
def criteria_tier_weightings(data:pd.DataFrame):
    #Read in hierarchy
    hierarchy = data
    criteria_row = list(hierarchy.iloc[1])
    hierarchy_criteria = [x for x in criteria_row if str(x) != 'nan']
    # Index of hierarchy criteria
    hierarchy_criteria_index = [i for i, x in enumerate(criteria_row) if str(x) != 'nan']
    # Table of hierarchy criteria
    hierarchy_criteria_table = hierarchy.iloc[2:2+len(hierarchy_criteria),hierarchy_criteria_index]
    # Convert dataframe to numpy array
    hierarchy_criteria_table = hierarchy_criteria_table.to_numpy()
    # Create AHPTier object
    criteria_tier = AHPTier(hierarchy_criteria_table,hierarchy_criteria,None)
    # Check if matrix is square and lead diagonal is 1
    criteria_tier.matrix_checker()
    # Calculate criteria weightings
    criteria_tier.weighting_calculator()
    # Check if matrix is consistent
    if criteria_tier.consistency_checker() == False:
        print('Criteria tier matrix is not consistent')
        return None
    return criteria_tier.weightings_dictionary()

print(criteria_tier_weightings(data))

def sub_criteria_tier_importance(data:pd.DataFrame,sub_criteria_number:int):
    #Read in hierarchy
    hierarchy = data
    sub_criteria_row = list(hierarchy.iloc[13+(21*(sub_criteria_number-1))])
    sub_criteria = [x for x in sub_criteria_row if str(x) != 'nan']
    # Index of sub criteria
    sub_criteria_index = [i for i, x in enumerate(sub_criteria_row) if str(x) != 'nan']
    # Table of sub criteria
    sub_criteria_table = hierarchy.iloc[14+(21*(sub_criteria_number-1)):14+(21*(sub_criteria_number-1))+len(sub_criteria),sub_criteria_index]
    # Convert dataframe to numpy array
    sub_criteria_table = sub_criteria_table.to_numpy()
    # Define parent
    parent_row = list(hierarchy.iloc[12+(21*(sub_criteria_number-1))])
    parent = [x for x in parent_row if str(x) != 'nan']
    parent = parent[-1]

    return sub_criteria_table,sub_criteria,parent


print(criteria_tier_weightings(data))


criteria_row = list(data.iloc[1])
hierarchy_criteria = [x for x in criteria_row if str(x) != 'nan']
for i in range(1,len(hierarchy_criteria)+1):
    sub_criteria_table,sub_criteria,parent = sub_criteria_tier_importance(data,i)
    # Create AHPTier object for each sub criteria tier