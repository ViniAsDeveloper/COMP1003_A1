# Vinicius Salem Henrique

# Student ID = 24897817

#  BEGIN
#    DISPLAY “===== BILL SPLITER =====\n”
#    DISPLAY “Enter the total bill amount (without tip):”
#    GET bill_amount_input
#    SET bill_amount = CONVERT bill_amount_input TO float
#    DISPLAY “Enter the tip percentage (0-100):”
#    GET tip_percentage_input
#    SET tip_percentage = CONVERT tip_percentage_input TO float
#    DISPLAY “Enter the number of people who will split the bill:”
#    GET number_of_people_input
#    SET number_of_people = CONVERT number_of_people_input TO integer
#    SET amount_per_person = bill_amount / number_of_people
#    SET suggested_tip_per_person = tip_percentage / 100 * amount_per_person
#    SET final_value_per_person = amount_per_person +  suggested_tip_per_person
#    DISPLAY “**** AMOUNT PER PERSON (withou tip) ****”
#    DISPLAY amount_per_person
#    DISPLAY “**** SUGESTED TIP PER PERSON ****”
#    DISPLAY  suggested_tip_per_person
#    DISPLAY “**** FINAL VALUE PER PERSON ****”
#    DISPLAY  final_value_per_person
#    DISPLAY “==== END OF PROGRAM ====”
#  END


# INPUT -> here we get user input using the input() function, which gets
# a string containing instructions to the user as the first argument.

print("===== BILL SPLITER =====\n")
bill_amount_input = input("Enter the total bill amount (without tip):")
tip_percentage_input = input("Enter the tip percentage (0-100):");
number_of_people_input = input("Enter the number of people who will split the bill:")

# PROCESS -> here we convert inputs to its intended types and perform
# the necessary calculations to obtain the output value

bill_amount = float(bill_amount_input)
tip_percentage = float(tip_percentage_input)
number_of_people = int(number_of_people_input)

amount_per_person = bill_amount / number_of_people
suggested_tip_per_person = tip_percentage / 100 * amount_per_person
final_value_per_person = amount_per_person + suggested_tip_per_person

# OUTPUT -> here we print the output values in a readable way to the user

print("**** AMOUNT PER PERSON (withou tip) ****")
print(amount_per_person)
print("**** SUGESTED TIP PER PERSON ****")
print(suggested_tip_per_person)
print("**** FINAL VALUE PER PERSON ****")
print(final_value_per_person)
print("==== END OF PROGRAM ====")
