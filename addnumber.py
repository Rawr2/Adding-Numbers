while True:
    try:
        print("We be adding numbers!")
        Number_1 = int(input("Enter a number: "))
        Number_2 = int(input("Enter another number: "))
        print("Congratulations you got",Number_1 + Number_2)
        break
    except:
        print("Please enter a number!")
    
