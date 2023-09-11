def is_valid_anagram(str1, str2):
    return sorted(str1) == sorted(str2)


str1 = "listen"
str2 = "silent"

if is_valid_anagram(str1, str2):
    print(f"'{str1}' and '{str2}' are valid anagrams.")
else:
    print(f"'{str1}' and '{str2}' are not valid anagrams.")
