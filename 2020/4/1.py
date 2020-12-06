with open('input') as f:
    passports = "".join(f.readlines()).split("\n\n")

required_fields = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid"   
]

eye_colors = "amb blu brn gry grn hzl oth".split(" ")

def check_if_hex_valid(colorHex):
    valid_chars = "abcdef0123456789"
    for i in colorHex:
        if (not i in valid_chars):
            return False
    return True

"""
    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
    If cm, the number must be at least 150 and at most 193.
    If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.
""" 
def check_valid(details):
    for field in required_fields:
        if not field in details:
            return False
    
    if(not(int(details["byr"]) >= 1920 and int(details["byr"]) <= 2002)):
        return False
    
    if(not(int(details["iyr"]) >= 2010 and int(details["iyr"]) <= 2020)):
        return False
    
    if(not(int(details["eyr"]) >= 2020 and int(details["eyr"]) <= 2030)):
        return False
    
    if(not(details["hgt"][-2:] == "cm" or details["hgt"][-2:] == "in")):
        return False

    if(details["hgt"][-2:] == "cm"):
        if(not(int(details["hgt"][:-2]) >= 150 and int(details["hgt"][:-2]) <= 193)):
            return False

    if(details["hgt"][-2:] == "in"):
        if(not(int(details["hgt"][:-2]) >= 59 and int(details["hgt"][:-2]) <= 76)):
            return False

    if(not (details["hcl"][0] == "#" and check_if_hex_valid(details["hcl"][1]))):
        return False

    if(not(details["ecl"] in eye_colors)):
        return False

    if(not (len(details["pid"]) == 9 and details["pid"].isdecimal())):
        return False

    return True

valid_count= 0

for i in range(0, len(passports)):
    passports[i] = passports[i].replace("\n", " ").split(" ")

    parsed_passport = {}
    for detail in passports[i]:
        parsed_passport[detail.split(":")[0]] = detail.split(":")[1]

    valid_count += check_valid(parsed_passport)

print(valid_count)
