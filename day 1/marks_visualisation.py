import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Name": ["A", "B", "C", "D", "E"],
    "Hours_Studied": [2, 3, 6, 8, 10],
    "Marks": [35, 50, 65, 80, 95]
}

df = pd.DataFrame(data)


import matplotlib.pyplot as plt
plt.scatter(df["Hours_Studied"],df["Marks"])
plt.xlabel("Hours_Studied")
plt.ylabel("Marks")
plt.title("plot of hrs vs marks")
plt.show()