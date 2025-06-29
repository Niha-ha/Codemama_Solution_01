def remove_special_characters(s):
    special_chars =".!@#$%^&  *()/" 

    result = ""  
    for char in s:
        if char not in special_chars:
            result += char
    return result

s = input()
print(remove_special_characters(s))