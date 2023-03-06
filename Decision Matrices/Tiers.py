from AHPTier import AHPTier
import numpy as np
"""
tier1 = AHPTier(np.array([[1,1,3,5,5],[1,1,3,5,5],[1/3,1/3,1,3,3],[1/5,1/5,1/3,1,1],[1/5,1/5,1/3,1,1]]),['Payload Capabilities','Flight Capabiities','Speed Capabilities','Dimensions','Drone Type'])
tier1.matrix_checker()
tier1.weighting_calculator()
tier1.consistency_checker()
print(tier1.weightings_dictionary())


tier2 =  AHPTier(np.array([[1,5],[0.2,1]]),['Payload Capabilities','Flight Capabiities'])
tier2.matrix_checker()
tier2.weighting_calculator()
print(tier2.consistency_checker())
print(tier2.weightings_dictionary())
"""
print(-np.inf<-10000)
test_array = np.array([[1,1,3,5,5],[1,1,3,5,5],[1/3,1/3,1,3,3],[1/5,1/5,1/3,1,1],[1/5,1/5,1/3,1,1]])
# Find all real eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(test_array)
# Find the index of the largest eigenvalue
max_index = np.argmax(eigenvalues)
# Find the largest eigenvalue
max_eigenvalue = eigenvalues[max_index]
# Find the corresponding eigenvector
max_eigenvector = eigenvectors[:,max_index]
# Normalize the eigenvector
max_eigenvector = max_eigenvector / np.sum(max_eigenvector)
# Calculate the consistency index
CI = (max_eigenvalue - len(test_array)) / (len(test_array) - 1)
# Calculate the consistency ratio
CR = CI / 0.9
print(CR)



