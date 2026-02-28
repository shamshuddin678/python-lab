import random

empty=[]
total=0
for i in range(20):
    rmd=random.randint(1,100)
    empty.append(rmd)
    total=total+empty[i]
    
print(empty)
print("Average: ",total/20)
# empty.sort()
# print(empty)

# print("First: ",empty[0])
# print("Last: ",empty[len(empty)-1])

# print("second_smallest: ",empty[1])
# print("second_largest: ",empty[len(empty)-2])

n=len(empty)
for i in range(n-1):
    for j in range(n-i-1):
        if(empty[j]>empty[j+1]):
            empty[j],empty[j+1] = empty[j+1],empty[j]

new_empty=list(set(empty))
print(new_empty) 
print("First smallest: ",new_empty[0])
print("Second smallest: ",new_empty[len(empty)-1])

print("First largest: ",new_empty[1])
print("Second largest: ",new_empty[len(new_empty)-2])

count=0
for i in range(20):
   if(new_empty[i] % 2 ==0):
     count+=1
print("Even nums count: ",count)