def disemvowel(string):
  vowels = "aeiou"
  for char in string:
    if char.lower() in vowels:
      string = string.replace(char, '')
  return string

print(disemvowel("This website is for losers LOL!"))