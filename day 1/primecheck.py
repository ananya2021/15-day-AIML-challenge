n = int(input("enter the no to check:")) # intput of no 
is_prime = True # always always consider something as true when checking 
if n <= 1:
    is_prime = False
else:
    for i in range (2,n):
      if n%i == 0 :
        is_prime = False 
        break
if is_prime :
   print("prime")
else:
   print("not prime")


     
