from data_for_test2 import plant_data, fertilizer_data


def comparison():
    # 各必要なkg肥料/aの大小比較
    if necessary_kg_per_a['N'] >= necessary_kg_per_a['P']:
        if necessary_kg_per_a['P'] >= necessary_kg_per_a['K']:
            return 'K'
        else:
            return 'P'
    elif necessary_kg_per_a['N'] <= necessary_kg_per_a['P']:
        if necessary_kg_per_a['N'] >= necessary_kg_per_a['K']:
            return 'K'
        else:
            return 'N'


# plant = input()
# fertilizer = input()
plant = 'spinach'
fertilizer = '888'

# 必要な肥料kg(全体)/a
necessary_kg_per_a = {
    'N' : plant_data[plant]['N'] / fertilizer_data[fertilizer]['N'],
    'P' : plant_data[plant]['P'] / fertilizer_data[fertilizer]['P'],
    'K' : plant_data[plant]['K'] / fertilizer_data[fertilizer]['K'],
}

a = comparison()
print('必要な肥料kg(全体)/a', necessary_kg_per_a)
print(a + 'を基準に施肥を行いましょう。')

# 一番少ないものを基準に肥料をまいた場合施肥される肥料kg(成分)/a
applied_fertilizer = {
    'N' : necessary_kg_per_a[a] * fertilizer_data[fertilizer]['N'],
    'P' : necessary_kg_per_a[a] * fertilizer_data[fertilizer]['P'],
    'K' : necessary_kg_per_a[a] * fertilizer_data[fertilizer]['K'],
}

# 一番少ないものを基準に肥料をまいた場合施肥した場合の不足するkg肥料/a
remaining = {
    'N' : plant_data[plant]['N'] - applied_fertilizer['N'],
    'P' : plant_data[plant]['P'] - applied_fertilizer['P'],
    'K' : plant_data[plant]['K'] - applied_fertilizer['K'],
}

print('施肥される成分量(kg(成分))/a', applied_fertilizer)
print('不足する成分量(kg(成分))/a', remaining)