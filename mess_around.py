lis = [7,2,8,9,4,13,7,1,9,10]

def collapse(x: list) -> list:
  index = -1
  for number in x:
    index += 1
    try:
      number_1 = x[index]
    except IndexError:
      pass
    try:
      number_2 = x[index+1]
    except IndexError:
        pass
    if number_1 < number_2:
      new_number = number_1 + number_2
      try:
        x.pop(index)
      except IndexError:
        pass
      try:
        x[index] = new_number
      except IndexError:
        pass
    elif number_1 > number_2:
      index += 1
  return x

print(collapse(lis))