BEGIN unit_converter
#   DISPLAY “==== UNIT CONVERTER ====”
#	DISPLAY “This program converts values between units for:”
#	DISPLAY “1. Time (days, hours, minutes, seconds)”
#	DISPLAY “2. Distance (meters, kilometers, miles)”
#	DISPLAY “3. Temperature (celsius, fahrenheit)”
#	DISPLAY “Enter the number corresponding to the desired option:”
#	GET option_input
#	SET option = CONVERT option_input TO integer
#	DISPLAY “Enter the input unit:”
#	GET input_unit_type
#	DISPLAY “Enter the input unit value:”
#	GET input_unit_value_input
#	SET input_unit_value = CONVERT  input_unit_value_input TO float
#	DISPLAY “Enter the output unit type:”
#	GET output_unit_type
#	IF option == 1 THEN
#		IF input_unit_type == “days” THEN
#			IF output_unit_type == “hours” THEN
#				SET output_unit_value = input_unit_value * 24
#			ELIF output_unit_type == “minutes” THEN
#				SET output_unit_value =  input_unit_value * 24 * 60
#			ELIF output_unit_type == “seconds” THEN
#				SET output_unit_value =  input_unit_value * 24 * 60 * 60
#			ELSE
#				DISPLAY “Invalid output option:”
#				DISPLAY “It must be in the list AND be different from input”
#			END IF
#
#		ELIF  input_unit_type == “hours” THEN
#			IF output_unit_type == “days” THEN
#				SET output_unit_value = input_unit_value / 24
#			ELIF output_unit_type == “minutes” THEN
#				SET output_unit_value =  input_unit_value * 60
#			ELIF output_unit_type == “seconds” THEN
#				SET output_unit_value =  input_unit_value * 60 * 60
#			ELSE
#				DISPLAY “Invalid output option:”
#				DISPLAY “It must be in the list AND be different from input”
#			END IF
#
#		 ELIF  input_unit_type == “minutes” THEN
# 			IF output_unit_type == “days” THEN
#				SET output_unit_value = input_unit_value / (24 * 60)
#			ELIF output_unit_type == “hours” THEN
#				SET output_unit_value =  input_unit_value / 60
#			ELIF output_unit_type == “seconds” THEN
#				SET output_unit_value =  input_unit_value * 60
#			ELSE
#				DISPLAY “Invalid output option:”
#				DISPLAY “It must be in the list AND be different from input”
#			END IF
#
#		ELIF input_unit_type == “seconds” THEN
#			IF output_unit_type == “days” THEN
#				SET output_unit_value = input_unit_value / (24 * 60 * 60)
#			ELIF output_unit_type == “hours” THEN
#				SET output_unit_value =  input_unit_value / (60 * 60)
#			ELIF output_unit_type == “minutes” THEN
#				SET output_unit_value =  input_unit_value / 60
#			ELSE
#				DISPLAY “Invalid output option:”
#				DISPLAY “It must be in the list AND be different from input”
#			END IF
#		ELSE
#			DISPLAY “Invalid input option:”
#			DISPLAY “It must be in the list!”
#		END IF
#	ELIF option == 2 THEN
#		IF input_unit_type == “meters” THEN
#			IF output_unit_type == “kilometers” THEN
#				SET output_unit_value = input_unit_value / 1000
#			ELIF output_unit_type == “miles” THEN
#				SET output_unit_value = input_unit_value / (1000 * 1.609344)
#			ELSE
#				DISPLAY “Invalid output option:”
#				DISPLAY “It must be in the list AND be different from input”
#			END IF
#		ELIF input_unit_type == “kilometers” THEN
#			IF output_unit_type == “meters” THEN
#				SET output_unit_value = input_unit_value * 1000
#			ELIF output_unit_type == “miles” THEN
#				SET output_unit_value = input_unit_value / 1.609344
#			ELSE
#				DISPLAY “Invalid output option:”
#				DISPLAY “It must be in the list AND be different from input”
#			END IF
#		ELIF input_unit_type == “miles” THEN
#			IF output_unit_type == “meters” THEN
#				SET output_unit_value = input_unit_value * 1000 * 1.609344
#			ELIF output_unit_type == “kilometers” THEN
#				SET output_unit_type = input_unit_value *  1.609344
#			ELSE
#				DISPLAY “Invalid output option:”
#				DISPLAY “It must be in the list AND be different from input”
#			END IF
#		ELSE
#			DISPLAY “Invalid input option:”
#			DISPLAY “It must be in the list!”
#		END IF
#	ELIF option == 3 THEN
#		IF input_unit_type == “celsius” THEN
#			IF output_unit_type == “fahrenheit” THEN
#				SET output_unit_value = (input_unit_value * 9 / 5) + 32
#			ELSE
#				DISPLAY “Invalid output option:”
#				DISPLAY “It must be in the list AND be different from input”
#			END IF
#		ELIF input_unit_type == “fahrenheit” THEN
#			IF output_unit_type == “celsius” THEN
#				SET output_unit_value = (input_unit_value – 32) * 5 / 9
#			ELSE
#				DISPLAY “Invalid output option:”
#				DISPLAY “It must be in the list AND be different from input”
#			END IF
#		ELSE
#			DISPLAY “Invalid input option:”
#			DISPLAY “It must be in the list!”
#		END IF
#	ELSE
#		DISPLAY “Invalid conversion option! Please choose from the list”
#	END IF
#
#	DISPLAY “**** INPUT UNIT ****”
#	DISPLAY input_unit_type
#	DISPLAY “**** INPUT VALUE ****”
#	DISPLAY input_unit_value
#	DISPLAY “**** OUTPUT UNIT ****”
#	DISPLAY output_unit_type
#	DISPLAY “**** OUTPUT VALUE ****”
#	DISPLAY output_unit_value
#	DISPLAY “==== END OF PROGRAM ====”
#END

# INPUT
print("==== UNIT CONVERTER ====")
print("This program converts values between units for:")
print("1. Time (days, hours, minutes, seconds)")
print("2. Distance (meters, kilometers, miles)")
print("3. Temperature (celsius, fahrenheit)")

option_input = input("Enter the corresponding number to the desired option:")
option = int(option_input)

input_unit_type = input("Enter the input unit:")

input_unit_value_input = input("Enter the input unit value:")
input_unit_value = float(input_unit_value_input)

output_unit_type = input("Enter the output unit type:")


# PROCESS

if option == 1:
    if input_unit_type == "days":
        if output_unit_type == "hours":
            output_unit_value = input_unit_value * 24
        elif output_unit_type == "minutes":
            output_unit_value = input_unit_value * 24 * 60
        elif output_unit_type == "seconds":
            output_unit_value = input_unit_value * 24 * 60 * 60
        else:
            print("Invalid option:")
            print("It must be in the list AND be different from input")

    elif input_unit_type == "hours":
        if output_unit_type == "days":
            output_unit_value = input_unit_value / 24
        elif output_unit_value == "minutes":
            output_unit_value = input_unit_value * 60
        elif output_unit_value == "seconds":
            output_unit_value = input_unit_value * 60 * 60
        else:
            print("Invalid option:")
            print("It must be in the list AND be different from input")

    elif input_unit_type == "minutes":
        if output_unit_type == "days":
            output_unit_value = input_unit_value / (24 * 60)
        elif output_unit_value == "hours":
            output_unit_value = input_unit_value / 60
        elif output_unit_value == "seconds":
            output_unit_value = input_unit_value * 60
        else:
            print("Invalid option:")
            print("It must be in the list AND be different from input")

    elif input_unit_type == "seconds":
        if output_unit_type == "days":
            output_unit_value = input_unit_value / (24 * 60 * 60)
        elif output_unit_value == "hours":
            output_unit_value = input_unit_value / (60 * 60)
        elif output_unit_value == "minutes":
            output_unit_value = input_unit_value / 60
        else:
            print("Invalid option:")
            print("It must be in the list AND be different from input")
    else:
        print("Invalid input option:")
        print("It must be in the list!")

elif option == 2:
    if input_unit_type == "meters":
        if output_unit_type == "kilometers":
            output_unit_value = input_unit_value / 1000
        elif output_unit_value == "miles":
            output_unit_value = input_unit_value / (1000 * 1.609344)
        else:
            print("Invalid option:")
            print("It must be in the list AND be different from input")

    elif input_unit_type == "kilometers":
        if output_unit_type == "meters":
            output_unit_value = input_unit_value * 1000
        elif output_unit_value == "miles":
            output_unit_value = input_unit_value / 1.609344
        else:
            print("Invalid option:")
            print("It must be in the list AND be different from input")

    elif input_unit_type == "miles":
        if output_unit_type == "meters":
            output_unit_value = input_unit_value * 1000 * 1.609344
        elif output_unit_value == "kilometers:
            output_unit_value = input_unit_value * 1.609344
        else:
            print("Invalid option:")
            print("It must be in the list AND be different from input")
    else:
        print("Invalid input option:")
        print("It must be in the list!")

elif option == 3:
    if input_unit_type == "celsius":
        if output_unit_type == "fahrenheit":
            output_unit_value = (input_unit_value * 9 / 5) + 32
        else:
            print("Invalid option:")
            print("It must be in the list AND be different from input")
    elif input_unit_type == "fahrenheit":
        if output_unit_type == "celsius":
            output_unit_value = (input_unit_value - 32) * 5 / 9
        else:
            print("Invalid option:")
            print("It must be in the list AND be different from input")
    else:
        print("Invalid input option:")
        print("It must be in the list!")
else:
    print("Invalid conversion option! Please choose from the list")

# OUTPUT
print("**** INPUT UNIT ****")
print(input_unit_type)
print("**** INPUT VALUE ****")
print(input_unit_value)
print("**** OUTPUT UNIT ****")
print(output_unit_type)
print("**** OUTPUT VALUE ****")
print(output_unit_value)
print("==== END OF PROGRAM ====")
