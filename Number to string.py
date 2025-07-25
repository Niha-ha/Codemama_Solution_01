# Dictionary to map digits to word
digit_to_word = {
    "0" : "zero",
    "1" : "one",
    "2" : "two", 
    "3" : "three",
    "4" : "four",
    "5" : "five",
    "6" : "six",
    "7" : "seven",
    "8" : "eight",
    "9" : "nine",
      }

# Take Input
N = input()

# output in one line
print(" ".join(digit_to_word[digit] for digit in N))
