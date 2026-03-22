# Vinicius Salem Henrique

# Student ID = 24897817

# BEGIN unit_converter
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
#			DISPLAY “\n**** ERROR ****\nInvalid input option:”
#			DISPLAY “Check the list!”
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
#			DISPLAY “\n**** ERROR ****\nInvalid input option:”
#			DISPLAY “Check the list!”
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
#			DISPLAY “\n**** ERROR ****\nInvalid input option:”
#			DISPLAY “Check the list!”
#		END IF
#	ELSE
#		DISPLAY “\n**** ERROR ****\nInvalid conversion option! Please choose from the list”
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

# INPUT -> here we get user input using the input() function and pass
# a string containing instructions to the users as the first argument to
# this function

print("\n\n================== UNIT CONVERTER ===================")
print("This program converts values between units for:")
print("1. Time (days, hours, minutes, seconds)")
print("2. Distance (meters, kilometers, miles)")
print("3. Temperature (celsius, fahrenheit)")

option_input = input("Enter the corresponding number to the desired option:\n_> ").strip().lower()
input_unit_type = input("Enter the input unit:\n_> ").strip().lower()
input_unit_value_input = input("Enter the input unit value:\n_> ").strip().lower()
output_unit_type = input("Enter the output unit type:\n_> ").strip().lower()


# PROCESS -> here we convert user input and check this input using if, elif and else
# statements to get the right logic branch in the program, to perform the correct
# calculations for the conversion choosen by the user

# validate option input
if not option_input.isdigit():
    print("\n**** ERROR ****\nOption must be a number between 1 and 4")
    print("\n=================== END OF PROGRAM ===================")
    quit()
option = int(option_input)

# validate value input | this is a float pattern validation, which is far more complex
# than validating a menu option
is_valid = True # a variable which stores the result of the validation process
input = input_unit_value_input # alias to make it faster to type the code
if len(input) == 0:
    is_valid = False
if input.count("+") > 0 and (input[0] != "+" or input.count("-") > 0):
    is_valid = False
if input.count("-") > 0 and (input[0] != "-" or input.count("+") > 0):
    is_valid = False
if input.count("+") > 1:
    is_valid = False
if input.count("-") > 1:
    is_valid = False
if input.count(".") > 1:
    is_valid = False
if not input.replace(".","").replace("+","").replace("-","").isdigit():
    is_valid = False

if not is_valid:
    print("\n**** ERROR ****\nThe input value must be a float and can only contain digits, a leading sign (+ or -) and one dot\n\n")
    print("\n=================== END OF PROGRAM ===================")
    quit()


input_unit_value = float(input)

if option == 1:
# if the above expression evaluates to True, enters the time conversion branch

    if input_unit_type == "days":
    # here, if True, enters the "input type = days" nested branch

        if output_unit_type == "hours":
        # here, if True, perform calculations to get the output value in hours.
        # The same logic is replicated for all possible combination of variables.
            output_unit_value = input_unit_value * 24
        elif output_unit_type == "minutes":
            output_unit_value = input_unit_value * 24 * 60
        elif output_unit_type == "seconds":
            output_unit_value = input_unit_value * 24 * 60 * 60
        else:
        # if the output_unit_value didn't match any previous check, than the
        # user input is not valid
            is_valid = False
            print("\n**** ERROR ****\nInvalid option:")
            print("It must be in the list AND be different from input")

    elif input_unit_type == "hours":
        if output_unit_type == "days":
            output_unit_value = input_unit_value / 24
        elif output_unit_type == "minutes":
            output_unit_value = input_unit_value * 60
        elif output_unit_type == "seconds":
            output_unit_value = input_unit_value * 60 * 60
        else:
            is_valid = False
            print("\n**** ERROR ****\nInvalid option:")
            print("It must be in the list AND be different from input")

    elif input_unit_type == "minutes":
        if output_unit_type == "days":
            output_unit_value = input_unit_value / (24 * 60)
        elif output_unit_type == "hours":
            output_unit_value = input_unit_value / 60
        elif output_unit_type == "seconds":
            output_unit_value = input_unit_value * 60
        else:
            is_valid = False
            print("\n**** ERROR ****\nInvalid option:")
            print("It must be in the list AND be different from input")

    elif input_unit_type == "seconds":
        if output_unit_type == "days":
            output_unit_value = input_unit_value / (24 * 60 * 60)
        elif output_unit_type == "hours":
            output_unit_value = input_unit_value / (60 * 60)
        elif output_unit_type == "minutes":
            output_unit_value = input_unit_value / 60
        else:
            is_valid = False
            print("\n**** ERROR ****\nInvalid option:")
            print("It must be in the list AND be different from input")
    else: # if the variable didn't match any check, than the user input is not valid
        is_valid = False
        print("\n**** ERROR ****\nInvalid input option:")
        print("Check the list!")

elif option == 2: # and so on, for all menu options
    if input_unit_type == "meters":
        if output_unit_type == "kilometers":
            output_unit_value = input_unit_value / 1000
        elif output_unit_type == "miles":
            output_unit_value = input_unit_value / (1000 * 1.609344)
        else:
            is_valid = False
            print("\n**** ERROR ****\nInvalid option:")
            print("It must be in the list AND be different from input")

    elif input_unit_type == "kilometers":
        if output_unit_type == "meters":
            output_unit_value = input_unit_value * 1000
        elif output_unit_type == "miles":
            output_unit_value = input_unit_value / 1.609344
        else:
            is_valid = False
            print("\n**** ERROR ****\nInvalid option:")
            print("It must be in the list AND be different from input")

    elif input_unit_type == "miles":
        if output_unit_type == "meters":
            output_unit_value = input_unit_value * 1000 * 1.609344
        elif output_unit_type == "kilometers":
            output_unit_value = input_unit_value * 1.609344
        else:
            is_valid = False
            print("\n**** ERROR ****\nInvalid option:")
            print("It must be in the list AND be different from input")
    else:
        is_valid = False
        print("\n**** ERROR ****\nInvalid input option:")
        print("Check the list!")

elif option == 3:
    if input_unit_type == "celsius":
        if output_unit_type == "fahrenheit":
            output_unit_value = (input_unit_value * 9 / 5) + 32
        else:
            is_valid = False
            print("\n**** ERROR ****\nInvalid option:")
            print("It must be in the list AND be different from input")
    elif input_unit_type == "fahrenheit":
        if output_unit_type == "celsius":
            output_unit_value = (input_unit_value - 32) * 5 / 9
        else:
            is_valid = False
            print("\n**** ERROR ****\nInvalid option:")
            print("It must be in the list AND be different from input")
    else:
        is_valid = False
        print("\n**** ERROR ****\nInvalid input option:")
        print("Check the list!")
else:
    is_valid = False
    print("\n**** ERROR ****\nInvalid conversion option! Please choose from the list")

if not is_valid:
    print("\n=================== END OF PROGRAM ===================")
    quit()

# OUTPUT
print(f"\n********* RESULTS *********\n\nINPUT UNIT: {input_unit_type:>15}")
# print(input_unit_type)
print(f"INPUT VALUE: {input_unit_value:>14,.2f}")
# print(input_unit_value)
print(f"OUTPUT UNIT: {output_unit_type:>14}")
# print(output_unit_type)
print(f"OUTPUT VALUE: {output_unit_value:>13,.2f}")
# print(output_unit_value)
print("\n*Results are trucated to 2 decimal places\n\n=================== END OF PROGRAM ===================")
