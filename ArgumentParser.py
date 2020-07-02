# Python, argparse, and command line arguments
# import the necessary packages
import argparse

if __name__ == '__main__':
    # initialize the parser
    parser = argparse.ArgumentParser(description="this is my script")

    # add the parameters positional/optional
    # positional arguments:
    parser.add_argument('num1', help="Number1", type=float)
    # optional arguments:
    parser.add_argument('-i', '--num2', help="Number2", type=float, default='3')    # 'i'' is a short name
    # optional arguments:
    parser.add_argument('-o','--operation', help="provide operator", default='+')   # 'o'' is a short name

    # CMD running:
    # C:\Users\Felhasználó>python "c:\Users\Felhasználó\PycharmProjects\Elso\ArgumentParser.py" 5 --num2 3
    # C:\Users\Felhasználó>python "c:\Users\Felhasználó\PycharmProjects\Elso\ArgumentParser.py" 5 -i 2

    # parse the arguments
    args = parser.parse_args()
    print(args)
    result = None
    if args.operation == "+":
        result = args.num1 + args.num2
    if args.operation == "-":
        result = args.num1 - args.num2
    print(result)