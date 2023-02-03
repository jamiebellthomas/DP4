import numpy as np
criteria_importance = np.array([[1,1,3,5,5],[1,1,3,5,5],[1/3,1/3,1,3,3],[1/5,1/5,1/3,1,1],[1/5,1/5,1/3,1,1]])
# Sum of columns
sum_of_columns = np.sum(criteria_importance, axis=0)
#print('Column sum (ctieria importance):', sum_of_columns)

# Divide each column by the sum of the column
normalized_matrix = criteria_importance / sum_of_columns
#print('Normalized matrix (criteria importance): ', normalized_matrix)

# Average of each row
criteria_weightings = np.mean(normalized_matrix, axis=1)
print('Criteria weightings: ', criteria_weightings)

# Multiply the first colum of the importance matrix by the average of the first row of the normalized matrix
# Repeat for each row
weighted_matrix = criteria_importance * criteria_weightings
#print('Weighted matrix: ', weighted_matrix)

# Sum of each row of the weighted matrix
weighted_sum_values = np.sum(weighted_matrix, axis=1)
#print('Weighted sum vales:', weighted_sum_values)

# divide each value of the weighted sum value by the ctieria weightings
ratio_weighted_sum_values = weighted_sum_values / criteria_weightings
#print('Weighted sum vales to criteria weightings ratios', ratio_weighted_sum_values)

# Average of the ratio weighted sum values
lambda_max = np.mean(ratio_weighted_sum_values)
#print('Lambda max:', lambda_max)

# Consistency index
consistency_index = (lambda_max - 5) / 4
#print('Consistency index:', consistency_index)

# Consistency ratio
consistency_ratio = consistency_index / 1.12
print('Consistency ratio:', consistency_ratio)

# Consistency ratio is less than 0.1 so the matrix is consistent
if consistency_ratio < 0.1:
    print('The matrix is consistent')
else:
    print('The matrix is not consistent')
