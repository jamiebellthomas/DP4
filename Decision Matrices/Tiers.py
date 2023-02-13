from AHPTier import AHPTier
import numpy as np
tier1 = AHPTier(np.array([[1,1,3,5,5],[1,1,3,5,5],[1/3,1/3,1,3,3],[1/5,1/5,1/3,1,1],[1/5,1/5,1/3,1,1]]),['Payload Capabilities','Flight Capabiities','Speed Capabilities','Dimensions','Drone Type'],None)
tier1.matrix_checker()
tier1.weighting_calculator()
tier1.consistency_checker()
print(tier1.weightings_dictionary())


tier2 =  AHPTier(np.array([[1,5],[0.2,1]]),['Payload Capabilities','Flight Capabiities'],None)
tier2.matrix_checker()
tier2.weighting_calculator()
print(tier2.consistency_checker())
print(tier2.weightings_dictionary())

