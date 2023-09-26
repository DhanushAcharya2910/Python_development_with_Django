
sample_dict = {'a': 10, 'b': 20, 'c': 30}

key_to_check = 'b'

if key_to_check in sample_dict:
    print(f"'{key_to_check}' exists in the dictionary with a value of {sample_dict[key_to_check]}")
else:
    print(f"'{key_to_check}' does not exist in the dictionary")

value = sample_dict.get(key_to_check)
if value is not None:
    print(f"'{key_to_check}' exists in the dictionary with a value of {value}")
else:
    print(f"'{key_to_check}' does not exist in the dictionary")