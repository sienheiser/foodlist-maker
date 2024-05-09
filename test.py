import toml

with open("recepies.toml",'r') as f:
    recepies = toml.loads(f.read())
print(recepies.keys())

panner_ing = recepies["Panner tikka"]["ingredients"]
vegetable_ing = recepies["Vegetable stew"]["ingredients"]

def make_dic(ingredients:str) -> dict:
    dic = dict()
    for line in ingredients.splitlines():
        split_line = line.split(" - ")
        assert len(split_line) == 2,"There are more than two columns"
        dic[split_line[1]] = split_line[0]
    return dic

dic1 = make_dic(panner_ing)
dic2 = make_dic(vegetable_ing)
ingredient_list = dict()

def add_units(ing1:str,ing2:str)->str:
    if ("tbps" in ing1) and ("tbps" in ing2):
        num1 = ing1[:-5]
        num2 = ing2[:-5]
        return f"{float(num1)+float(num2)} tbps"
    elif ("tps" in ing1) and ("tps" in ing2):
        num1 = ing1[:-4]
        num2 = ing2[:-4]
        return f"{float(num1)+float(num2)} tps"
    elif ("can" in ing1) and ("can" in ing2):
        num1 = ing1[:-4]
        num2 = ing2[:-4]
        return f"{float(num1)+float(num2)} can"
    elif ("pack" in ing1) and ("pack" in ing2):
        num1 = ing1[:-5]
        num2 = ing2[:-5]
        return f"{float(num1)+float(num2)} pack"
    else:
        assert False,f"addition for case {ing1} and {ing2} not defined"

def add (key:str,ingredients1:dict,ingredients2:dict) -> dict:
    ing1 = ingredients1[key]
    ing2 = ingredients2[key]
    if ing1.isnumeric() and ing2.isnumeric():
        return f"{int(ing1)+int(ing2)}"
    else:
        return add_units(ing1,ing2)
for key in dic1.keys():
    if key in dic2.keys():
        ingredient_list[key] = add(key,dic1,dic2)
print(ingredient_list)




