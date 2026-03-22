import re

def validate_count(input):
    if input.count("+") > 0 and (input[0] != "+" or input.count("-") > 0):
        return False
    if input.count("+") > 1:
        return False
    if input.count("-") > 0 and (input[0] != "-" or input.count("+") > 0):
        return False
    if input.count("-") > 1:
        return False
    if input.count(".") > 1:
        return False
    if not input.replace(".", "").replace("+", "").replace("-", "").isdigit():
        return False
    return True

def validate_loop(input):
    plus = 0
    minus = 0
    dots = 0
    message = "input is valid"
    for i in range(len(input)):
        if input[i] == "+":
            plus += 1
            if i != 0:
                message = "input cannot contain non-leading signs"
                return (False, message)
            if plus > 1:
                message = "input cannot contain multiple signs"
                return (False, message)
            if minus > 0:
                message = "input cannot contain different signs"
                return (False, message)

        elif input[i] == "-":
            minus += 1
            if i != 0:
                message = "input cannot contain non-leading signs"
                return (False, message)
            if minus > 1:
                message = "input cannot contain multiple signs"
                return (False, message)
            if plus > 0:
                message = "input cannot contain different signs"
                return (False, message)

        elif input[i] == ".":
            dots += 1
            if dots > 1:
                message = "input cannot contain multiple dots"
                return (False, message)
        elif not input[i].isdigit():
            message = "input can only contain digits, one dot and '+' or '-' at the start"
            return (False, message)
    return (True, message)

def validate_replace(input):
    if not input.replace("+","",1).replace("-","",1).replace(".","",1).isdigit():
        return False
    if (not input.replace("+","").replace(".","").isdigit()) and (not input.replace("-","").replace(".","").isdigit()):
        return False
    if input.replace("+","").replace(".","").isdigit() and not input.replace(".","").isdigit() and input[0] != "+":
        return False
    if input.replace("-","").replace(".","").isdigit() and not input.replace(".","").isdigit() and input [0] != "-":
        return False
    return True

def validate_recursion(input):
    def next(input, index, plus, minus, dots):
        if input[index] == "+":
            plus += 1
            if index != 0:
                return False
            if plus > 1:
                return False
            if minus > 0:
                return False
        elif input[index] == "-":
            minus += 1
            if index != 0:
                return False
            if minus > 1:
                return False
            if plus > 0:
                return False
        elif input[index] == ".":
            dots += 1
            if dots > 1:
                return False
        elif not input[index].isdigit():
            return False
        if index == len(input) - 1:
            return True
        else:
            return next(input, index + 1, plus, minus, dots)
    return next(input, 0, 0, 0, 0)

def validate_regex(input):
    if re.match(r"^[-+]?[0-9]*\.?[0-9]+$", input) or re.match(r"^[-+]?[0-9]+\.?[0-9]*?$", input):
        return True
    return False

def validate_except(input):
    try:
        float(input)
    except:
        return False
    return True

def run():
    text = input("")
    if text == "quit":
        return
    print("Count:", validate_count(text))
    print("Loop:", validate_loop(text))
    print("Replace:", validate_replace(text))
    print("Recursion:", validate_recursion(text))
    print("Regex:", validate_regex(text))
    print("Except:", validate_except(text))
    return run()

run()
