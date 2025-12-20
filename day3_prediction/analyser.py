import numpy as np
import matplotlib.pyplot as plt 

marks = []

print ("enter marks of 5 subjects out of 100")
for i in range(5):
 mark = int(input(f"sub{i+1}:"))
 marks.append(mark)

marks = np.array(marks)
print(marks)

average = np.mean(marks)
print(average)

highest = np.max(marks[marks>90])
print("toppers",highest)

lowest = np.min(marks[marks<33])
print("failure",lowest)

subjects = ['Sub1', 'Sub2', 'Sub3', 'Sub4', 'Sub5']

plt.figure()
plt.bar(subjects, marks)
plt.axhline(y=average, linestyle='--', label='Average')
plt.title("My Performance Analyzer")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.legend()



normalized = (marks - np.min(marks)) / (np.max(marks) - np.min(marks))

plt.figure()
plt.plot(subjects, normalized, marker='o')
plt.title("Normalized Performance (ML Style)")
plt.ylabel("Normalized Value")


plt.show()
