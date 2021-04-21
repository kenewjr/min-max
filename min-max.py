def max_check(x):
  max_val = x[0] 
  for check in x: 
    if check > max_val: 
      max_val = check 
  return max_val

def min_check(x):
  min_val = x[0] 
  for check in x: 
    if check < min_val: 
      min_val = check 
  return min_val

my_list = str(10235768)

print("Max : ", max_check(my_list))
print("Min : ", min_check(my_list))