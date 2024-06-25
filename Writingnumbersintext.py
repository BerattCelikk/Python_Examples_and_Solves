def number_to_text(number):
    if number < 0 or number > 1000:
        return "Number out of range"

    units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    hundreds = ["", "one hundred", "two hundred", "three hundred", "four hundred", "five hundred", "six hundred", "seven hundred", "eight hundred", "nine hundred"]
    
    if number == 0:
        return "zero"
    if number == 1000:
        return "one thousand"

    thousand = number // 1000
    hundred = (number // 100) % 10
    ten = (number // 10) % 10
    unit = number % 10

    result = ""
    
    if thousand > 0:
        result += "one thousand"
    
    if hundred > 0:
        if result:
            result += " "
        result += hundreds[hundred]
    
    if ten > 1:
        if result:
            result += " "
        result += tens[ten]
        if unit > 0:
            result += "-" + units[unit]
    elif ten == 1 and unit > 0:
        if result:
            result += " "
        result += teens[unit]
    else:
        if unit > 0:
            if result:
                result += " "
            result += units[unit]
    
    return result

number = int(input("Enter a number: "))
print(number_to_text(number))
