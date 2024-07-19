num=int(input("enter the number"))
if num == 1:
    print(num, "is not prime number")
elif num > 1 :
    for i in range(2,num):
        if (num%i) ==0 :
            print(num,"not prime number")
            break
    else:
        print(num,"prime number")
else:
    print(num,"not prime number")





