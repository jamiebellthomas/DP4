from AHPTier import *
tier1 = AHPTier(np.array([[1,1,3,5,5],[1,1,3,5,5],[1/3,1/3,1,3,3],[1/5,1/5,1/3,1,1],[1/5,1/5,1/3,1,1]]),['Payload Capabilities','Flight Capabiities','Speed Capabilities','Dimensions','Drone Type'])
tier1.matrix_checker()
tier1.weighting_calculator()
tier1.consistency_checker()
print(tier1.weightings_dictionary())