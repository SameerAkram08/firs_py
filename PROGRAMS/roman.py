def roman_to_decimal(roman):
    roman_to_decimal = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    prev_value = 0
    
    for letter in roman[::-1]:
        value = roman_to_decimal[letter]
        if value >= prev_value:
            total += value
        else:
            total -= value
        prev_value = value
    
    return total


roman_numeral = input("Enter the value in roman (Uppercase letter) ==> ")

print(roman_to_decimal(roman_numeral))  
