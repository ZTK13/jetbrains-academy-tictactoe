string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'

vowel_count = 0

for letter in string:
    if letter in vowels:
        vowel_count += 1

print(vowel_count)
