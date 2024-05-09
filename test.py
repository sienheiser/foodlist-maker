import toml
from add_functions import add

def make_dic(ingredients:str) -> dict:
    dic = dict()
    for line in ingredients.splitlines():
        split_line = line.split("-")
        assert len(split_line) == 2,"There are more than two columns"
        dic[split_line[1]] = split_line[0]
    return dic

def function(selected_items:list) -> str:
    with open("recepies.toml",'r') as f:
        recepies = toml.loads(f.read())

    ingredients = []
    for item in selected_items:
        ingredients.append(recepies[item]["ingredients"])

    ingredients_dic = []
    for ing in ingredients:
        ingredients_dic.append(make_dic(ing))

    ingredient_list = dict()
    for i in range(0,len(ingredients_dic)):
        for key in ingredients_dic[i].keys():
            if key in ingredient_list.keys():
                ingredient_list[key] = add(key,ingredient_list,ingredients_dic[i])
            else:
                ingredient_list[key] = ingredients_dic[i][key]
    final_list = ""
    for key in ingredient_list.keys():
        final_list += f"{key} {ingredient_list[key]}\n"
    return final_list




