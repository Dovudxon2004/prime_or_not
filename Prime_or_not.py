i=0
x=2
a=int(input('number, please'))
while x in range(2,a-1):
    x = x+1
    if x not in range(2,int(a/2)):
        break
    elif a%x != 0:
        i=i
    elif a%x == 0:
        i=i+1
        break
if i==0:
    print('this is a prime number')
else:
    print("this is not a prime number")
