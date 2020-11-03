def rot13(message):
  lowers = "abcdefghijklmnopqrstuvwxyz"
  uppers = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  ciph_decry = ""
  for l in message:
    if l in lowers:
      if lowers.find(l) < 13:
        ciph_decry+=lowers[lowers.find(l) + 13]
      else:
        ciph_decry+=lowers[lowers.find(l) - 13]
    elif l in uppers:
      if uppers.find(l) < 13:
        ciph_decry+=uppers[uppers.find(l) + 13]
      else:
        ciph_decry+=uppers[uppers.find(l) - 13]
    else:
      ciph_decry+=l
  return ciph_decry

print(rot13(" Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf."))