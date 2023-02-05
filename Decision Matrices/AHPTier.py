import numpy as np
class AHPTier():
    def __init__(self,importance_matrix:np.array,criteria:list):
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
        # Random index for any number of criteria
        self.random_index = {1:0, 2:0, 3:0.58, 4:0.9, 5:1.12, 6:1.24, 7:1.32, 8:1.41, 9:1.45, 10:1.49}
        #Pick out the random index for the number of criteria
        self.random_index = self.random_index[self.importance_matrix.shape[0]]
        # Consistency ratio
        self.consistency_ratio = self.consistency_index / 1.12
        # Consistency ratio is less than 0.1 so the matrix is consistent
        self.consistent = False
        if self.consistency_ratio < 0.1:
            self.consistent = True
        return self.consistent
    def weightings_dictionary(self):
        self.weightings = {}
        for i in range(len(self.criteria)):
            self.weightings[self.criteria[i]] = self.criteria_weightings[i].round(4)
        return self.weightings
    

        
        
        