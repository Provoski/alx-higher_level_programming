#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    import calculator_1


    args_no = len(argv)
    operators = ["+", "-", "*", "/"]
    if args_no != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if argv[2] not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    
    a = int(argv[1])
    b = int(argv[3])
    """handling addition"""
    if argv[2] == "+":
        result = calculator_1.add(a, b)
        print("{:d} + {:d} = {:d}".format(a, b, result))

    """handling subtraction"""
    if argv[2] == "-":
        result = calculator_1.sub(a, b)
        print("{:d} - {:d} = {:d}".format(a, b, result))

    """handling division"""
    if argv[2] == "/":
        result = calculator_1.sub(a, b)
        print("{:d} / {:d} = {:d}".format(a, b, result))

    """handling multiplication"""
    if argv[2] == "*":
        result = calculator_1.sub(a, b)
        print("{:d} * {:d} = {:d}".format(a, b, result))
