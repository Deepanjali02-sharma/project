bill_amount = float(input("Enter the total bill amount:rupees"))
num_friends = int(input("Enter the number of friends to split the bill:"))
tip_percent = float(input("Enter the tip percentage you want to give (10 to 60):"))
if tip_percent < 10 or tip_percent>50:
    print("Tip should be between 10% and 50%.")
else:
    tip_amount = (tip_percent /100)
    bill_amount
    total_with_tip = bill_amount+ tip_amount
    per_person_amount = total_with_tip/num_friends
    print("\n--- Bill Summary ---")
    print(f"Original Bill: rupees{bill_amount:.2f}")
    print(f"Total Amount with Tip: rupeesb{total_with_tip:.2f}") 
    print(f"Each Friend Should Pay:rupees {per_person_amount:.2f}")
    
    


