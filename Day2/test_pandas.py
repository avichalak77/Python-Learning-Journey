import pandas as pd

print(pd.__version__)

data = {
    "Name": ["Avii", "Rahul", "Priya"],
    "Age": [21, 22, 20]
}

df = pd.DataFrame(data)
print(df)