#python -p t o
#print characters from a string that are present at an even index number

user_text = input("Enter a word:")

size = len(user_text)

for i in range(0,size-1,2):
    print(user_text[i])

