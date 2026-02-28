def vw(word, vowels):
    for  ch in word:
        if ch in vowels:
            
            return ch
    return "No V"

word = input("Enter a word: ")
vowels = {'a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U'}

c=vw(word,vowels)
if(c in vowels):
    print("V",*c)
else:
    print("N")
# for i in c:
#     print(c,end=" ")