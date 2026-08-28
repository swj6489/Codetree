lst1 = []
lst2 = []
for i in range(10):
    n = int(input())

    if n % 3 == 0: 
        lst1.append(n)
        if n % 5 == 0:
            lst2.append(n)
    
    elif n % 5 == 0:
        lst2.append(n)
    

print(len(lst1), len(lst2))