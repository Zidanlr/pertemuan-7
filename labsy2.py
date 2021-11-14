print("mencari bilangan terbesar dari 3 bilangan")

a=int(input("masukan bilangan 1:"))
b=int(input("masukan bilangan 2:"))
c=int(input("masukan bilangan 3:"))

if a > b > c:
    print("bilangan terbesar :",a)
elif b > c:
     print("bilangan terbesar :",b)   
else:
    print("bilangan terbesar :",c)
