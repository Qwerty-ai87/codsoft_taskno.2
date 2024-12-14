A=int(input("enter first number : "))
B=int(input("enter second number : "))
print("Please select operation -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n")
choice=int(input("Enter the operation you want to use :"))
if choice == 1:
    sum= A+B;
    print(A ,"+", B, "=", +sum)
                   

elif choice == 2:
    sub=A-B;
    print(A, "-",B, "=",+sub)

elif choice == 3:
    mul=A*B;
    print(A, "*", B, "=",+mul)


elif choice == 4:
    div=A/B;
    print(A, "/", B, "=",+div)
                    
else:
    print("Invalid input")