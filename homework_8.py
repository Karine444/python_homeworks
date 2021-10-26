# Ex:1

dict1 = {1: 10, 2: 20}
dict2 = {3: 30, 4: 40}
dict3 = {5: 50, 6: 60}
dict4 = {6: 50, 7: 60}


list_dict = {}

def new_dictionaries(new_dict):
    for i in (dict1, dict2, dict3):
        new_dict.update(i)
    return new_dict

print(f'New dictionary: {new_dictionaries(list_dict)}.')



#Ex:2

n = int(input("Input a number:"))

new_dict = {}

def create_new_dict(n_dict):
    for i in range(1, n + 1):
        n_dict[i] = i * i
    return n_dict


print(f'The new dictionary: {create_new_dict(new_dict)}.')


#Ex:3

original_dictionary = {'c1': 'Red', 'c2': 'Green', 'c3': None}
print(f'Original dictionary: {original_dictionary}.')

original_dictionary = {key:value for (key, value) in original_dictionary.items() if value is not None}

print(f'New dictionary without "None" items: {original_dictionary}')


#Ex:4

string = input("Write a sentence:\n\t")

def word_count(str):
    counts = dict()
    words = str.split()

    for i in words:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1

    return counts

print(f'Created dictionary with sentence words will be: {word_count(string)}')