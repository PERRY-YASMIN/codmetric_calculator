# unit_converter.py

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles / 0.621371

def kg_to_pounds(kg):
    return kg * 2.20462

def pounds_to_kg(pounds):
    return pounds / 2.20462

# Dictionary mapping choice to function and labels
conversions = {
    1: ("Celsius to Fahrenheit", celsius_to_fahrenheit, "°C", "°F"),
    2: ("Fahrenheit to Celsius", fahrenheit_to_celsius, "°F", "°C"),
    3: ("Kilometers to Miles", km_to_miles, "km", "miles"),
    4: ("Miles to Kilometers", miles_to_km, "miles", "km"),
    5: ("Kilograms to Pounds", kg_to_pounds, "kg", "lbs"),
    6: ("Pounds to Kilograms", pounds_to_kg, "lbs", "kg")
}

print("Welcome to Codmetric Unit Converter!\n")

while True:
    print("Select a conversion:")
    for key, value in conversions.items():
        print(f"{key}. {value[0]}")
    print("0. Exit")

    try:
        choice = int(input("\nEnter your choice: "))
        
        if choice == 0:
            print("Thank you for using Codmetric Unit Converter!")
            break
        
        if choice in conversions:
            value = float(input(f"Enter value in {conversions[choice][2]}: "))
            result = conversions[choice][1](value)
            print(f"{value:.2f} {conversions[choice][2]} = {result:.2f} {conversions[choice][3]}\n")
        else:
            print("❌ Invalid choice! Please select a valid option.\n")

    except ValueError:
        print("❌ Invalid input! Please enter a number.\n")
