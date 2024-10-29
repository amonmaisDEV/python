print("Choose 1 for Celsius --> Fahrenheit ")
print("Choose 2 for Fahrenheit --> Celsius")
print("Choose 3 for Kelvin --> Celsius")
print("Chooose 4 for Celsius --> Kelvin")

def celsius_to_fahrenheit(celtofahr=9/5):
    conv_input = float(input("Temperature in °C: "))
    conversion = (conv_input * celtofahr)+32
    print(conversion)



def fahrenheit_to_celsius(fahrtocel=5/9):
    conv_input = float(input("Temperature in °F: "))
    conversion  = (conv_input-32)*fahrtocel
    print(conversion)


def kelvin_to_celsius():
    conv_input = float(input("Temperature in Kelvin: "))
    conversion = conv_input - 273.15
    print(conversion)


def celsius_to_kelvin():
    conv_input = float(input("Temperature in °C: "))
    conversion = conv_input + 273.15
    print(conversion)


while True:
    try:
        choose = int(input("What do you choose"))
        if choose == 1:
            celsius_to_fahrenheit()
            
        elif choose == 2:
            fahrenheit_to_celsius()
            
        elif choose == 3:
            kelvin_to_celsius()
            
        elif choose == 4:
            celsius_to_kelvin
            
        else:
            print("invalid choice")
            print(choose)
    except:
        print("Enter Valid")
        print(choose)
        