vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

def check_vowel(S):
     mid = len(S) // 2
     first_half = S[:mid]
     sec_half = S[mid:]
     vowels_in_first_half = sum(1 for char in first_half if char in vowels)
     vowels_in_second_half = sum(1 for char in sec_half if char in vowels)
     return vowels_in_first_half == vowels_in_second_half
      

S = input()
print(str(check_vowel(S)).lower())
