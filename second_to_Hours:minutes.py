# Funtion that converts seconds to hour by performing integer division.
def sec_to_hour(sec):
  return sec // 3600
  
# Funtion that converts seconds(quotient) to minutes.
def sec_to_min(sec):
  return (sec % 3600) // 60

# Take input seconds that is to convert
sec = int(input())

# Calling the functions with proper arguments.
hours = sec_to_hour(sec)
minutes = sec_to_min(sec)

# Printing the result
print(f"{hours:02d}:{minutes:02d}"
