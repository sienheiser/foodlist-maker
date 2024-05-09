import toml
from add_functions import add

with open("recepies.toml",'r') as f:
    recepies = toml.loads(f.read())

panner_ing = recepies["Panner tikka"]["ingredients"]
vegetable_ing = recepies["Vegetable stew"]["ingredients"]
random_ing = recepies["Random"]["ingredients"]

def make_dic(ingredients:str) -> dict:
    dic = dict()
    for line in ingredients.splitlines():
        split_line = line.split("-")
        assert len(split_line) == 2,"There are more than two columns"
        dic[split_line[1]] = split_line[0]
    return dic

dic1 = make_dic(panner_ing)
dic2 = make_dic(vegetable_ing)
dic3 = make_dic(random_ing)

dics = [dic1,dic2,dic3]

ingredient_list = dict()

l2 = list(dic2.keys())

for i in range(0,len(dics)):
    for key in dics[i].keys():
        if key in ingredient_list.keys():
            ingredient_list[key] = add(key,ingredient_list,dics[i])
        else:
            ingredient_list[key] = dics[i][key]

print(ingredient_list)




