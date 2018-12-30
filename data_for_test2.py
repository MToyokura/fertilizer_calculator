# class plant:
#     def __init__(self, name, N, P, K)
#         self.name = name
#         self.necessary_N_kg_per_a = N
#         self.necessary_P_kg_per_a = P
#         self.necessary_K_kg_per_a = K

plant_data = {
    ## 生育に必要な養分量(kg(成分)/a)
    'spinach' : {
        'N' : 2.7,
        'P' : 3.5,
        'K' : 2.2,
    }
}

fertilizer_data = {
    ## 肥料に含まれる成分(kg(成分)/kg(全体))
    '888' : {
        'N' : 0.08,
        'P' : 0.08,
        'K' : 0.08,
    }
}