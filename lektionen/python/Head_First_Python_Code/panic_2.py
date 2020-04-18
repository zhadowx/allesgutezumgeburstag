phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

new_phrase = [plist[1]] + [plist[2]] + [plist[5]] + [plist[4]] + [plist[7]] + [plist[6]]

new_phrase = ''.join(new_phrase)
print(plist)
print(new_phrase)