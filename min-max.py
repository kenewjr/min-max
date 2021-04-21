def maxs(x):
  max = x[0] 
  for check in x: 
    if check > max: 
      max = check 
  return max

def mins(x):
  min = x[0] 
  for check in x: 
    if check < min: 
      min = check 
  return min

my_list = str(1023)

print("Max : ", maxs(my_list))
print("Min : ", min(my_list))
