import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Name": ["Ananya", "Rahul", "Priya", "Aman", "Neha"],
    "Hours_Studied": [2, 5, 3, 8, 6],
    "Marks": [35, 78, 55, 88, 72]
}

df = pd.DataFrame(data)


# -------- Scatter Plot --------
plt.figure()
plt.scatter(df["Hours_Studied"], df["Marks"])
plt.xlabel("Hours Studied")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")

# -------- Bar Plot --------
plt.figure()
plt.bar(df["Name"], df["Marks"])
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.title("Marks of Students")

plt.show()