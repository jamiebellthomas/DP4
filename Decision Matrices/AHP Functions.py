import numpy as np
criteria_importance = np.array([[1,1,3,5,5],[1,1,3,5,5],[1/3,1/3,1,3,3],[1/5,1/5,1/3,1,1],[1/5,1/5,1/3,1,1]])
def matrix_checker(criteria_importance):
    # Check if the matrix is square
    check = False
    square = False
    if criteria_importance.shape[0] == criteria_importance.shape[1]:
        square = True
    # Check if lead diagonal is 1
    lead_diagonal = False
    if np.all(np.diag(criteria_importance) == 1):
        lead_diagonal = True
    if square and lead_diagonal:
        check = True
    return check
    
def weighting_calculator(criteria_importance):
    # Sum of columns
    sum_of_columns = np.sum(criteria_importance, axis=0)
    # Divide each column by the sum of the column
    normalized_importance_matrix = criteria_importance / sum_of_columns
    # Average of each row (criteria weightings)
    criteria_weightings = np.mean(normalized_importance_matrix, axis=1)
    return criteria_weightings

def consistency_checker(criteria_importance, criteria_weightings):
    # Multiply the first colum of the importance matrix by the criteira weighting for the first row
    # Repeat for each row
    weighted_matrix = criteria_importance * criteria_weightings
    # Sum of each row of the weighted matrix
    weighted_sum_values = np.sum(weighted_matrix, axis=1)
    # divide each value of the weighted sum value by the ctieria weightings
    ratio_weighted_sum_values = weighted_sum_values / criteria_weightings
    # Average of the ratio weighted sum values
    lambda_max = np.mean(ratio_weighted_sum_values)
    # Consistency index
    consistency_index = (lambda_max - criteria_importance.shape[0]) / (criteria_importance.shape[0] - 1)
    # Random index for any number of criteria
    random_index = {1:0, 2:0, 3:0.58, 4:0.9, 5:1.12, 6:1.24, 7:1.32, 8:1.41, 9:1.45, 10:1.49}
    #Pick out the random index for the number of criteria
    consistency_ratio = 0
    if criteria_importance.shape[0] > 2:
        random_index = random_index[criteria_importance.shape[0]]
        # Consistency ratio
        consistency_ratio = consistency_index / random_index


    # Consistency ratio is less than 0.1 so the matrix is consistent
    consistent = False
    if consistency_ratio < 0.1:
        consistent = True
    return consistent


#print('Square matrix & Lead diagonal = 1:', matrix_checker(criteria_importance))
#print('Criteria weightings:', weighting_calculator(criteria_importance))
#print('Consistent:', consistency_checker(criteria_importance, weighting_calculator(criteria_importance)))






