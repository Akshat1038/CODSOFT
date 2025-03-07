def Calculator():
    print("\n ----- CALCULATOR -----")
    print("Choose an Operation")
    print("1.Addtion(+)")
    print("2.Subtration(-)")
    print("3.Multiplication(*)")
    print("4.Divison(/)")

    choice = (input("\nEnter choice(1/2/3/4): "))

    if choice not in ('1','2','3','4'):
        print("Invalid choice! Please select a valid operation")
        return
    try:
        num1=int(input("Enter First number:"))
        num2=int(input("Enter a second number:"))

        if choice =='1':
            result= num1 + num2
            operation="+"
        elif choice =='2':
             result= num1 - num2
             operation="-"
        elif choice =='3':
             result= num1  * num2
             operation="*"
        elif choice =='4':
            if num2==0:
                print("Error!Divison by Zero is not allowed." )
                return
            result=num1/num2
            operation="/"

        print(f"Result:{num1} {operation} {num2}={result}")

    except ValueError:
        print("Invalid input! Please enter numeric values.")

Calculator()                         
