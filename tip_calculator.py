def calculator(bill):
    print("What percentage tip would you like to give ?")
    print("10%, 12%, and 15%")
    
    #initalizing tip
    tip = int(input("Enter tip % : "))
    
    # initalizing tolal_bill 
    total_bill = bill+bill*(tip/100)

    print("How many people to split the bill ?")
    # initalizing how_many_people
    how_many_people = int(input())

    total_bill = int(total_bill/how_many_people)

    
    output = f"Each person should pay : {total_bill}" 


    return output

print("Welcome to Tip Calculator")
# initializing bill
bill = int(input("Enter the Total bill \n"))
result = calculator(bill)
print(result)