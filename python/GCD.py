arr = ['zero','one','two','three','four','five','six','seven','eight','nine']
def convnumtoword(n):
    if(n==0):
        return ""
    else:
        small_ans = arr[n%10]
        ans = convnumtoword(int(n/10)) + small_ans
    return ans

def gcd(a, b):
    if(b == 0):
        return a
    else:
        return gcd(b, a % b)

def convwordtonum(inp):
    i=0
    number=0
    element=0
    for element in range(i,len(inp)-1):
        substr=inp[element]+inp[element+1]
        if(substr=="ze"):
            number=number*10
            element=element+3
        elif(substr=="on"):
            number=number*10+1
            element=element+2
        elif(substr=="tw"):
            number=number*10+2
            element=element+2
        elif(substr=="th"):
            number=number*10+3
            element=element+4
        elif(substr=="fo"):
            number=number*10+4
            element=element+3
        elif(substr=="fi"):
            number=number*10+5
            element=element+3
        elif(substr=="si"):
            number=number*10+6
            element=element+2
        elif(substr=="se"):
            number=number*10+7
            element=element+4
        elif(substr=="ei"):
            number=number*10+8
            element=element+4
        elif(substr=="ni"):
            number=number*10+9
            element=element+3
    return number

print("Enter Input1:",end="\n")
inp=input()
print("Enter Input2:",end="\n")
inp2=input()
number1=convwordtonum(inp)
number2=convwordtonum(inp2)

result=gcd(number1,number2)
print("Here Is Your Output: ",end="\n")
print(convnumtoword(result))