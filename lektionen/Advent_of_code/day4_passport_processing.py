passports = [""]
index = 0

with open("passport_batches.txt", "r", encoding = "utf8") as f:
  for line in f:
    if line == "\n":
      passports.append("")
      index+=1
    passports[index]+=" "+line.strip("\n")
print("total passports:", len(passports))
# Part 1
valid = 0
for ele in passports:
  if "byr" in ele and "iyr" in ele and "eyr" in ele and "hgt" in ele \
  and "hcl" in ele and "ecl" in ele and "pid" in ele:
    valid+=1
print("simple validation:", valid)
# Part 2
# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.
l_passports = []
for e in passports:
  l_passports.append(e.split(" "))

arr_passports = []
for ele in l_passports:
  d = {}
  for e in ele:
    if e != "":
      k, v = e.split(":")
      d[k] = v
  arr_passports.append(d)

numbers = "0123456789"
letters = "abcdef"
colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
super_valid = 0

for element in arr_passports:
  if "byr" in element and "iyr" in element and "eyr" in element and "hgt" in element \
   and "hcl" in element and "ecl" in element and "pid" in element:
    try:
      if (int(element["byr"]) >= 1920 and int(element["byr"]) <= 2002) and (int(element["iyr"]) >= 2010 \
      and int(element["iyr"]) <= 2020) and (int(element["eyr"]) >= 2020 and int(element["eyr"]) <= 2030) \
      and element["ecl"] in colors and element["hcl"][0] == "#" and len(element["byr"]) == 4 and \
      len(element["iyr"]) == 4 and len(element["eyr"]) == 4:
        leggit = 0
        if "in" in element["hgt"]:
          temp = element["hgt"].split("in")
          if int(temp[0]) >= 59 and int(temp[0]) <= 76:
            for i in range(1, len(element["hcl"])):
              if element["hcl"][i] in numbers or element["hcl"][i] in letters:
                leggit+=1
        if "cm" in element["hgt"]:
          temp = element["hgt"].split("cm")
          if int(temp[0]) >= 150 and int(temp[0]) <= 193:
            for i in range(1, len(element["hcl"])):
              if element["hcl"][i] in numbers or element["hcl"][i] in letters:
                leggit+=1
        leggit2 = 0
        for e in element["pid"]:
          if e in numbers:
            leggit2+=1
        if leggit == 6 and leggit2 == 9:
          super_valid+=1
    except:
      continue
print("super leggit:", super_valid)