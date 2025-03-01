import csv

def convert_rate(filename):
    rates = {}
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            rates[row['code']] = float(row['rate'])
    return rates

def main():
    rates = convert_rate('currency.csv') 
    amount = float(input("How much dollar do you have? "))
    currency = input("What currency you want to have? ").upper()
    if currency in rates:
        converted_amount = amount * rates[currency]
        print(f"Dollar: {amount} USD")
        print(f"{currency}: {converted_amount}")
    else:
        print("Currency is missing, try again.")
if __name__ == "__main__":
    main()