def SystemToDecimal(number, system):
    number = str(number)
    system = int(system)
    decimal = 0
    power = 0
    for digit in number[::-1]:
        if (digit.isnumeric() == False):
            digit = ord(digit)-55
        decimal += int(digit)*(system**power)
        power += 1
    return decimal

def DecimalToSystem(decimal, system):
    decimal = int(decimal)
    system = int(system)
    number = ''
    while (decimal >= system):
        number = number + str(decimal % system)
        decimal = decimal // system
    number = number + str(decimal)
    invertedNumber = number[::-1]
    return int(invertedNumber)

def SystemToSystem(number, systemFrom, systemTo):
    decimal = SystemToDecimal(number, systemFrom)
    outputSystemNumber = DecimalToSystem(decimal, systemTo)
    return outputSystemNumber

print(SystemToSystem('15', 36, 2))