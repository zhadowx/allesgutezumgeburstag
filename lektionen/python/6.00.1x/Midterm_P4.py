def flatten(aList:list) -> list:
  ''' 
  aList: a list 
  Returns a copy of aList, which is a flattened version of aList 
  '''
  flat_list = []
  for element in aList:
    if type(element) != list:
      flat_list.append(element)
    else:
      for ele in element:
        if type(ele) != list:
          flat_list.append(ele)
        else:
          for e in ele:
            if type(e) != list:
              flat_list.append(e)
            else:
              for x in e:
                if type(x) != list:
            
                  flat_list.append(x)
                else:
                  for i in x:
                    if type(i) != list:
                      flat_list.append(i)
                    else:
                      for j in i:
                        if type(j) != list:
                          flat_list.append(j)
  return flat_list


print(flatten([[1,'a',['cat'],2],[[[3]],'dog'],4,5]))
#[1,'a','cat',2,3,'dog',4,5]