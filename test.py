import toml

with open("recepies.toml",'r') as f:
    recepies = toml.loads(f.read())
print(recepies.keys())

