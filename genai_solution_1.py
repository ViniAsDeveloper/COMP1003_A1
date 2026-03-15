print("==== UNIT CONVERTER ====")
print("This program converts values between units for:")
print("1. Time (days, hours, minutes, seconds)")
print("2. Distance (meters, kilometers, miles)")
print("3. Temperature (celsius, fahrenheit, kelvin)")
option_input = input("Enter the number corresponding to the desired option: ")
option = int(option_input)

input_unit_type = input("Enter the input unit type: ").lower()
input_unit_value_input = input("Enter the input unit value: ")
input_unit_value = float(input_unit_value_input)

output_unit_type = input("Enter the output unit type: ").lower()

output_unit_value = 0.0
valid_conversion = True

if option == 1:
    if input_unit_type == 'days':
        if output_unit_type == 'hours':
            output_unit_value = input_unit_value * 24
        elif output_unit_type == 'minutes':
            output_unit_value = input_unit_value * 24 * 60
        elif output_unit_type == 'seconds':
            output_unit_value = input_unit_value * 24 * 60 * 60
        else:
            print("Invalid output option:")
            print("It must be in the list AND be different from input")
            valid_conversion = False
    elif input_unit_type == 'hours':
        if output_unit_type == 'days':
            output_unit_value = input_unit_value / 24
        elif output_unit_type == 'minutes':
            output_unit_value = input_unit_value * 60
        elif output_unit_type == 'seconds':
            output_unit_value = input_unit_value * 60 * 60
        else:
            print("Invalid output option:")
            print("It must be in the list AND be different from input")
            valid_conversion = False
    elif input_unit_type == 'minutes':
        if output_unit_type == 'days':
            output_unit_value = input_unit_value / (24 * 60)
        elif output_unit_type == 'hours':
            output_unit_value = input_unit_value / 60
        elif output_unit_type == 'seconds':
            output_unit_value = input_unit_value * 60
        else:
            print("Invalid output option:")
            print("It must be in the list AND be different from input")
            valid_conversion = False
    elif input_unit_type == 'seconds':
        if output_unit_type == 'days':
            output_unit_value = input_unit_value / (24 * 60 * 60)
        elif output_unit_type == 'hours':
            output_unit_value = input_unit_value / (60 * 60)
        elif output_unit_type == 'minutes':
            output_unit_value = input_unit_value / 60
        else:
            print("Invalid output option:")
            print("It must be in the list AND be different from input")
            valid_conversion = False
    else:
        print("Invalid input option:")
        valid_conversion = False

elif option == 2:
    if input_unit_type == 'meters':
        if output_unit_type == 'kilometers':
            output_unit_value = input_unit_value / 1000
        elif output_unit_type == 'miles':
            output_unit_value = input_unit_value / 1609.344
        else:
            print("Invalid output option:")
            print("It must be in the list AND be different from input")
            valid_conversion = False
    elif input_unit_type == 'kilometers':
        if output_unit_type == 'meters':
            output_unit_value = input_unit_value * 1000
        elif output_unit_type == 'miles':
            output_unit_value = input_unit_value * 0.621371
        else:
            print("Invalid output option:")
            print("It must be in the list AND be different from input")
            valid_conversion = False
    elif input_unit_type == 'miles':
        if output_unit_type == 'meters':
            output_unit_value = input_unit_value * 1609.344
        elif output_unit_type == 'kilometers':
            output_unit_value = input_unit_value * 1.609344
        else:
            print("Invalid output option:")
            print("It must be in the list AND be different from input")
            valid_conversion = False
    else:
        print("Invalid input option:")
        valid_conversion = False

elif option == 3:
    if input_unit_type == 'celsius':
        if output_unit_type == 'fahrenheit':
            output_unit_value = input_unit_value * 9 / 5 + 32
        elif output_unit_type == 'kelvin':
            output_unit_value = input_unit_value + 273.15
        else:
            print("Invalid output option:")
            print("It must be in the list AND be different from input")
            valid_conversion = False
    elif input_unit_type == 'fahrenheit':
        if output_unit_type == 'celsius':
            output_unit_value = (input_unit_value - 32) * 5 / 9
        elif output_unit_type == 'kelvin':
            output_unit_value = (input_unit_value - 32) * 5 / 9 + 273.15
        else:
            print("Invalid output option:")
            print("It must be in the list AND be different from input")
            valid_conversion = False
    elif input_unit_type == 'kelvin':
        if output_unit_type == 'celsius':
            output_unit_value = input_unit_value - 273.15
        elif output_unit_type == 'fahrenheit':
            output_unit_value = (input_unit_value - 273.15) * 9 / 5 + 32
        else:
            print("Invalid output option:")
            print("It must be in the list AND be different from input")
            valid_conversion = False
    else:
        print("Invalid input option:")
        valid_conversion = False

else:
    print("Invalid option:")
    valid_conversion = False

if valid_conversion:
    print(f"Input value: {input_unit_value} {input_unit_type}")
    print(f"Output value: {output_unit_value} {output_unit_type}")
else:
    print("Conversion failed.")
