import numpy as np 
from sklearn.linear_model import LogisticRegression 

data = np.array([
    [2,10,45],
    [4,8,99],
    [6,2,80],
    [1,11,20],
    [6,8,100],
    [2,2,87],
    [9,0,90],
    [2,6,75],
    [4,10,60],
    [5,9,99],
    [1,2,10],
    [3,1,20],
    [9,6,100],
    [3,4,57],
    [2,5,40],
    [2,4,33],  ]
)

y = np.array([0,1,1,0,1,1,1,1,1,1,0,0,1,1,0,0])

model = LogisticRegression()
model.fit(data,y)

z = []

print("enter no of hrs studies , no of hrs slept , previous marks")
for i in range(3):
    z.append(int(input()))

z = np.array([z]) 
'''
prediction = model.predict(z)
print(prediction)

if prediction[0] == 1:
  print("passs")
else:
  print("fail")
'''
print(model.coef_)
prob_pass = model.predict_proba(z)[0][1]
if prob_pass > 0.5:
    print(f"Student likely to PASS with {prob_pass*100:.1f}% confidence")
else:
    print(f"Student likely to FAIL with {(1-prob_pass)*100:.1f}% confidence")
