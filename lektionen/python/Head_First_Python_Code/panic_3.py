phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

temp_list=[1,2,5,4,7,6]
new_phrase =[]
for i in temp_list:
  new_phrase +=  plist[i]

new_phrase = ''.join(new_phrase)
print(plist)
print(new_phrase)