print("welcome to the word reverser")

string=input("enter any word or sentence:")

string2=""

for i in string:
    string2=i+string2

print("the original string is",string)
print("the reversed string is",string2)
