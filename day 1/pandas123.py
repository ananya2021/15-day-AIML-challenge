import pandas as pd

data = {
    "Name": ["A", "B", "C", "D", "E"],
    "Hours_Studied": [2, 4, 6, 8, 10],
    "Marks": [35, 50, 65, 80, 95]
}

df = pd.DataFrame(data)
print(df)
