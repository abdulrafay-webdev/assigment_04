def main():
    print("Fahrenheit to Celsius converter")
    fahrenheit = input("Enter temperature in Fahrenheit: ")
    fahrenheit:int = int(fahrenheit)
    degrees_celsius = (fahrenheit - 32) * 5.0/9.0
    print(f"{fahrenheit} Fahrenheit is equal to {degrees_celsius} Celsius.")

if __name__ == '__main__':
    main()