s1=input("Enter s1: ")
s2=input("Enter s2: ")

if(len(s1) == len(s2)):
    print("YES")
    result=""
    for i in range(len(s1)):
       result= result+s1[i]+s2[i]
    print(result)
else:
    print("EXIT")
