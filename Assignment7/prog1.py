
sample_dict = {'apple': 3, 'banana': 1, 'cherry': 2, 'date': 4}

ascending_sorted = dict(sorted(sample_dict.items(), key=lambda item: item[1]))

descending_sorted = dict(sorted(sample_dict.items(), key=lambda item: item[1], reverse=True))

print("Ascending Order:", ascending_sorted)
print("Descending Order:", descending_sorted)