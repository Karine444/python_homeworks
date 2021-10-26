#Ex:2

sample_list = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
print(f"Sample list: {sample_list}")

def duplicates(remove_duplicates):
    remove_duplicates.sort()
    dup_new= []
    for i in remove_duplicates:
        if i not in dup_new:
            dup_new.append(i)
    return dup_new


print(f"List After removing duplicates: {duplicates(sample_list)} ")


#Ex:3


original_list = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
print(f"The original list: {sample_list}")

def flatten_list(new_value):
    new_list = []
    for i in new_value:
        if type(i) is list:
            for j in i:
                new_list.append(j)
        else:
            new_list.append(i)
    return new_list

print(f"List After: {flatten_list(original_list)} ")


#Ex:4 


original_list_1 = [1, 1, 2, 3, 4, 4, 5, 1]
print(f"The original list: {original_list}")


length = int(input("Input the length of the first part of the list (example 3):\n\t")) 

def split(split_list, len):
    return split_list[:len], split_list[len:]


print(f"Splitted the said list into two parts: {split(original_list_1, length)}")