string=input("Enter string: ")

str_split=string.split() #split() use to convert list

str_join = "".join(string) #.join(): it joins the words in the  given string

dict={
    "string":string,
    "str_split":str_split,
    "str_join":str_join
}

print(dict)