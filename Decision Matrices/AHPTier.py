import numpy as np
import pandas as pd
class AHPTier():
    def __init__(self,importance_matrix:np.array,criteria:list,):
        self.importance_matrix = importance_matrix
        self.criteria = criteria
    def matrix_checker(self):
        # Check if the matrix is square
        self.check = False
        self.square = False
        if self.importance_matrix.shape[0] == self.importance_matrix.shape[1]:
            self.square = True
        # Check if lead diagonal is 1
        self.lead_diagonal = False
        if np.all(np.diag(self.importance_matrix) == 1):
            self.lead_diagonal = True
        if self.square and self.lead_diagonal:
            self.check = True
        return self.check
    def weighting_calculator(self):
        # Sum of columns
        self.sum_of_columns = np.sum(self.importance_matrix, axis=0)
        # Divide each column by the sum of the column
        self.normalized_importance_matrix = self.importance_matrix / self.sum_of_columns
        # Average of each row (criteria weightings)
        self.criteria_weightings = np.mean(self.normalized_importance_matrix, axis=1)
        return self.criteria_weightings
    def consistency_checker(self):
        # Multiply the first colum of the importance matrix by the criteira weighting for the first row
        # Repeat for each row
        self.weighted_matrix = self.importance_matrix * self.criteria_weightings
        # Sum of each row of the weighted matrix
        self.weighted_sum_values = np.sum(self.weighted_matrix, axis=1)
        # divide each value of the weighted sum value by the ctieria weightings
        self.ratio_weighted_sum_values = self.weighted_sum_values / self.criteria_weightings
        # Average of the ratio weighted sum values
        self.lambda_max = np.mean(self.ratio_weighted_sum_values)
        # Consistency index
        self.consistency_index = (self.lambda_max - self.importance_matrix.shape[0]) / (self.importance_matrix.shape[0] - 1)
        # Random index for any number of criteria between 1 and 12 in a dictionary 
        self.random_index = {1:0,2:0,3:0.58,4:0.9,5:1.12,6:1.24,7:1.32,8:1.41,9:1.45,10:1.49,11:1.51,12:1.48}
        #Pick out the random index for the number of criteria
        self.random_index = self.random_index[self.importance_matrix.shape[0]]
        # Consistency ratio
        self.consistency_ratio = 0
        if self.importance_matrix.shape[0] > 2:
            self.consistency_ratio = self.consistency_index / self.random_index
        # Consistency ratio is less than 0.1 so the matrix is consistent
        self.consistent = False
        if self.consistency_ratio < 0.1:
            self.consistent = True
        return self.consistent
    def weightings_dictionary(self):
        self.weightings = {}
        for i in range(len(self.criteria)):
            self.weightings[self.criteria[i]] = self.criteria_weightings[i]
        return self.weightings
    

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
    criteria_tier = AHPTier(hierarchy_criteria_table,hierarchy_criteria)
    # Check if matrix is square and lead diagonal is 1
    criteria_tier.matrix_checker()
    # Calculate criteria weightings
    criteria_tier.weighting_calculator()
    # Check if matrix is consistent
    if criteria_tier.consistency_checker() == False:
        print('Criteria tier matrix is not consistent')
        return None
    return criteria_tier.weightings_dictionary(),len(hierarchy_criteria)


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
        
