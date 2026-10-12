print("welcome to the power calculator")
base=int(input("enter the base number:"))
exponent=int(input("enter the exponent number:"))

result=1

for i in range(1,exponent+1):
    result=result*base
    print("step",i, ": result=",result)
    print("\nAnswer:",base,"to the power",exponent,"=",result)
