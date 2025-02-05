def count_input(string, vowel_count="aeiouAEIOU"):
    counter = 0 
    vowels = 0   
    consonants = 0  
    
    for i in string:
        if i == " " or i == '\n':  
            counter += 1
        elif i in vowel_count:
            vowels += 1
        elif i.isalpha():
            consonants += 1
    
    return len(string), counter, vowels, consonants

input_string = input("Enter a String: ")
char_count, space_count, vowel_count, consonant_count = count_input(input_string)

print("=============================")
print("Character Count:", char_count)
print("Spaces Count:", space_count)
print("Vowel Count:", vowel_count)
print("Consonant Count:", consonant_count)
print("=============================")