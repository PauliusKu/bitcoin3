import sys

from feeCalculator import FeeCalculator
from hashValidator import HashValidator

inputLength = len(sys.argv)

if inputLength == 1:
    print("1. Calculating transaction fee.")
    calculator = FeeCalculator()
    print(calculator.calculate("0627052b6f28912f2703066a912ea577f2ce4da4caa5a5fbd8a57286c345c2f2"))

elif inputLength == 3:
    if sys.argv[1] == 'A':
        print("A. Calculating transaction fee for specific transaction.")
        calculator = FeeCalculator()
        print(calculator.calculate(sys.argv[2]))
    elif sys.argv[1] == 'B':
        print("B. Validating Hashes.")
        validator = HashValidator()
        if validator.validate(sys.argv[2]):
            print("Hashes is valid.")
        else:
            print("Hashes is not valid.")
else:
    print("Incorect input parameters")
