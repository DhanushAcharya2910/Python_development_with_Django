
sample_dict = {'a': 2, 'b': 3, 'c': 4}

total_product = 1

for value in sample_dict.values():
    total_product *= value
print("Product of all items:",total_product)