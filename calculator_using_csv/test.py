import pandas as pd

plant_df = pd.read_csv('plant_data.csv')
# CSVの項目: 作物名,作型,基肥N,基肥P,基肥K,追肥N,追肥P,追肥K,合計N,合計P,合計K,施肥の留意点
# データは埼玉県の施肥基準(https://www.pref.saitama.lg.jp/a0903/sehikijun.html)
# 単位はkg/10a

fertilizer_df = pd.read_csv('fertilizer_data.csv')
# 肥料名,N,P,K,Mg,Ca,S
# 単位は%

作物名 = input('キュウリ or ナス を入力\n')
# 作型 = input()
作型 = '半促成'

# ['作物名'] == 作物名である行を抜き出し、さらにその中の['作型'] == 作型]の行を抜き出す。
a = plant_df.loc[plant_df['作物名'] == 作物名].loc[plant_df['作型'] == 作型]

# 先程抜き出した行をPythonの辞書に変換する。
# このとき、 a.to_dict() だと縦横が逆になるので a.T で縦横を逆にしてから to_dict() する。
plant_dict = a.T.to_dict()
# この時点では、 plant_dict 内のほしい情報がキーが一つだけの辞書に格納されてしまうため、
# 一度 list(plant_dict.values()) というリストを作り、次にその0番目を抜き取る。
# (もっとスマートな方法がある気がするので提案あったら教えて！！！)
temp_list = list(plant_dict.values())
plant_dict = temp_list[0]
print(plant_dict)

# 肥料名 = input()
肥料名 = 'やさいの元肥'

b = fertilizer_df.loc[fertilizer_df['肥料名'] == 肥料名]
fertilizer_dict = b.T.to_dict()[0]
# 後の計算が面倒くさくなるのでここで全ての値に0.01をかける。
# これによりfertilizer_dictの中身は肥料1kgあたりの成分含有重量の数値となる。
for key in fertilizer_dict:
    if type(fertilizer_dict[key]) == int or type(fertilizer_dict[key]) == float:
        fertilizer_dict[key] = fertilizer_dict[key] * 0.01
print(fertilizer_dict)



def comparison():
    # 各必要なkg肥料/aの大小比較
    if necessary_motohi_kg_per_10a['N'] > necessary_motohi_kg_per_10a['P']:
        if necessary_motohi_kg_per_10a['P'] > necessary_motohi_kg_per_10a['K']:
            return 'K'
        else:
            return 'P'
    elif necessary_motohi_kg_per_10a['N'] <= necessary_motohi_kg_per_10a['P']:
        if necessary_motohi_kg_per_10a['N'] > necessary_motohi_kg_per_10a['K']:
            return 'K'
        else:
            return 'N'


# 必要な肥料kg(基肥)/10a
necessary_motohi_kg_per_10a = {
    'N' : plant_dict['基肥N'] / fertilizer_dict['N'],
    'P' : plant_dict['基肥P'] / fertilizer_dict['P'],
    'K' : plant_dict['基肥K'] / fertilizer_dict['K'],
}
print('\n10aあたり必要な', 肥料名, 'は、N, P, Kでそれぞれに合わせた場合、\n',necessary_motohi_kg_per_10a)

c = comparison()
print('\n', c, 'を基準に、',肥料名, 'を10aあたり',necessary_motohi_kg_per_10a[c], 'kg施肥しましょう。')

# 一番少ないものを基準に肥料をまいた場合施肥される肥料kg(成分)/10a
applied_fertilizer = {
    'N' : necessary_motohi_kg_per_10a[c] * fertilizer_dict['N'],
    'P' : necessary_motohi_kg_per_10a[c] * fertilizer_dict['P'],
    'K' : necessary_motohi_kg_per_10a[c] * fertilizer_dict['K'],
}

# 一番少ないものを基準に肥料をまいた場合施肥した場合の不足するkg肥料/a
remaining = {
    'N' : plant_dict['基肥N'] - applied_fertilizer['N'],
    'P' : plant_dict['基肥P'] - applied_fertilizer['P'],
    'K' : plant_dict['基肥K'] - applied_fertilizer['K'],
}

print('\n施肥される成分量(kg(成分))/10a', applied_fertilizer)
print('\n不足する成分量(kg(成分))/10a', remaining)
print('\n\n')