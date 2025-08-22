#Currency Converter (USD to PKR) 
#Input amount in USD. Convert using a fixed exchange rate. 

usd = float(input("Enter currency in USD$ : "))

pkr = float(usd / 283.62)

print(f"PKR : {pkr:.2f}")