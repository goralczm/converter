def SystemToDecimal(number, system):
    if (system > 36 or system < 2):
        return "System not supported! Available system are from base-2 to base-36"
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
    if (system > 36 or system < 2):
        return "System not supported! Available system are from base-2 to base-36"
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
    if (systemFrom > 36 or systemFrom < 2 or systemTo > 36 or systemTo < 2):
        return "System not supported! Available system are from base-2 to base-36"
    decimal = SystemToDecimal(number, systemFrom)
    outputSystemNumber = DecimalToSystem(decimal, systemTo)
    return outputSystemNumber