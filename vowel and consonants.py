#Vowel and consonants
string = input("Enter a string: ")
vowel="aeiou"
vowel_count = 0
consonant_count = 0
for i in string:
    if i in vowel:
        vowel_count+=1
    else:
        consonant_count+=1
print("Number of vowels:", vowel_count)
print("Number of consonants:", consonant_count)
        
        






