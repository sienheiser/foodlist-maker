
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
    elif ("ml" in ing1) and ("ml" in ing2):
        num1 = ing1[:-3]
        num2 = ing2[:-3]
        return f"{float(num1)+float(num2)} ml"
    elif ("g" in ing1) and ("g" in ing2):
        num1 = ing1[:-2]
        num2 = ing2[:-2]
        return f"{float(num1)+float(num2)} g"
    elif ("kg" in ing1) and ("kg" in ing2):
        num1 = ing1[:-3]
        num2 = ing2[:-3]
        return f"{float(num1)+float(num2)} kg"
    else:
        assert False,f"addition for case {ing1} and {ing2} not defined"

def add (key:str,ingredients1:dict,ingredients2:dict) -> dict:
    ing1 = ingredients1[key]
    ing2 = ingredients2[key]
    if ing1.isnumeric() and ing2.isnumeric():
        return f"{int(ing1)+int(ing2)}"
    else:
        return add_units(ing1,ing2)
