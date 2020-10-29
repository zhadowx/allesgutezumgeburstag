import string

def is_pangram(s):
  for l in string.ascii_lowercase:
    if l not in s.lower():
      return False
  return True

print(is_pangram("The quick, brown fox jumps over the lazy dog!"))