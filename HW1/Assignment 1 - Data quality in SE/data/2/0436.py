import re

with open('input.txt') as f:
    input_file = f.readlines()
input_file = [x.strip() for x in input_file]

def check_passport(text):
    arr = text.split()
    dct = {}
    for elem in arr:
        key = elem.split(":")[0]
        val = elem.split(":")[1]
        dct[key] = val
    
    try:
        if len(dct['byr']) != 4 or int(dct['byr']) < 1920 or int(dct['byr']) > 2002:
            print("byr invalid")
            return False
        if len(dct['iyr']) !=4 or int(dct['iyr']) < 2010 or int(dct['iyr']) > 2030:
            print("iyr invalid")
            return False
        if len(dct['eyr']) != 4 or int(dct['eyr']) < 2020 or int(dct['eyr']) > 2030:
            print("eyr invalid")
            return False
        if dct['hgt'][-2:] == 'in':
            if int(dct['hgt'][:-2]) < 59 or int(dct['hgt'][:-2]) > 76:
                print("hgt invalid")
                return False
        elif dct['hgt'][-2:] == 'cm':
            if int(dct['hgt'][:-2]) < 150 or int(dct['hgt'][:-2]) > 193:
                print("hgt invalid")
                return False
        else:
            print("hgt invalid")
            return False

        if dct['hcl'][0] != "#" or not re.compile("[0-9a-f]{6}").fullmatch(dct['hcl'][1:]):
            print("hcl invalid")
            return False

        ecl_options = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        if not any(dct['ecl'] == option for option in ecl_options):
            print("ecl invalid")
            return False
        if not re.compile("[0-9]{9}").fullmatch(dct['pid']):
            print("pid invalid")
            return False
        
        return True

    except KeyError as e:
        print("Key error: " + str(e))
        return False
        
    
    # if ("byr:" in text and "iyr:" in text and "eyr:" in text and "hgt:" in text and "hcl:" in text and "ecl:" in text and "pid:" in text):
    #     return True
    # else:
    #     return False


grouped_input = []
curr = ""
for i in input_file:
    if i != "":
        curr += " " + i
    else:
        grouped_input.append(curr[1:])
        curr = ""

count = 0
for i in range(0, len(grouped_input)):
    print(str(check_passport(grouped_input[i])) + " " + grouped_input[i])
    if check_passport(grouped_input[i]):
        count += 1

print(count)