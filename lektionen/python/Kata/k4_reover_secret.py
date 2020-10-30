def recoverSecret(triplets):
  secret = ""
  letters = ""

  for arr in triplets:
    for l in arr:
      if l not in letters:
        letters+=l
  
  times = str(len(letters))

  for i in range(int(times)):
    dict_index = dict()
    for letter in letters:
      dict_index[letter] = 0
      for arr in triplets:
        if letter in arr:
          dict_index[letter] += arr.index(letter)

    for l in dict_index.keys():
      if dict_index[l] == 0:
        secret+=l
        letters = letters.replace(l, "")
        for arr in triplets:
          if l in arr:
            arr.remove(l)

  return secret

print(recoverSecret([
  ['t','u','p'],
  ['w','h','i'],
  ['t','s','u'],
  ['a','t','s'],
  ['h','a','p'],
  ['t','i','s'],
  ['w','h','s']
]))

