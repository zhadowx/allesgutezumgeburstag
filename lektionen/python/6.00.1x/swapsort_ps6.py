def swapSort(L):
  """ L is a list on integers"""
  print("Original L: ", L)
  ci = 0
  cj = 0
  for i in range(len(L)):
    ci+=1
    # for j in range(i+1, len(L)):  # for increasing order
    for j in range(len(L)):
      cj+=1
      if L[j] < L[i]:
        # the next line is a short
        # form for swap L[i] and L[j]
        L[j], L[i] = L[i], L[j]
        print(L, "ci:", ci, "cj:", cj)
  print("Final L: ", L)

L = [1, 2, 3, 4, 5, 6, 7, 8, 9]

swapSort(L)