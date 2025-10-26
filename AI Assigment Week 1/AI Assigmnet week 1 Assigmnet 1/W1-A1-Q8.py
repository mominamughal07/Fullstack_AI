# Calculate Profit or Loss 
# Input cost price and selling price. Display either: 
# Profit and amount, or 
# Loss and amount, or 
# No Profit No Loss 

CostPrice = float(input("Enter cost price : "))
SellingPrice = float(input("Enter Selling price :"))

amount = SellingPrice - CostPrice

if SellingPrice == CostPrice:
    print("NO PROFIT AND NO LOSS")
elif SellingPrice > CostPrice:
    print("Profit with amount : " , amount)
elif SellingPrice < CostPrice :
    print("Loss with amount : " , abs(amount))