phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

plist.pop(8)
plist.remove('D')
plist.remove("'")
plist.remove('i')
plist.remove('c')
plist.remove('!')
plist.remove('t')
plist.insert(3, 't')
plist.remove('p')
plist.append('p')

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)