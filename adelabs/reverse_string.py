def reverse_string(string):
  if len(string) <1 :
    return None
  elif string == string[::-1]:
    return True
  return string[::-1]
  