#Ex:1
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def without_duplicate(arg:int) -> int:
   x=set(arg)
   dup=[]
   for c in x:
      if(arg.count(c)<=1):
         dup.append(c)

   return dup

print(f"The original list {a} -> List without duplicates {without_duplicate(a)}")
print(f"The original list {b} -> List without duplicates {without_duplicate(b)}")

#Ex:2


c = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print(f"The original list {c}")

def divisors_of_five(new_value):
    new_list =[]
    for i in new_value:
        if 5 % i == 0:
            new_list.append(i)
    return new_list

print(f"The new list with divisors of five: {divisors_of_five(c)}")


#Ex:3

my_text= input("Write the sentence you want to flip.\n\t")

def reverse(text:str) -> str:
  reverse_text = text.split()
  reverse_text.reverse()
  return " ".join(reverse_text)

print(f"The reversed text will be -> {reverse(my_text)}")



#Ex:4

my_tup = (1, "text", 1, True)

def Reverse(tuples):
    new_tup = ()
    for k in reversed(tuples):
        new_tup = new_tup + (k,)
    return new_tup

print(f"The reversed tuple will be{Reverse(my_tup)}")


#Ex:5

data_list = [-23, 5, 0, 23, -6, 23, 67,-2]

def sorting(sort_list):
   new_list = []
   while sort_list:
       minimum = sort_list[0]  
       for x in sort_list: 
           if x < minimum:
               minimum = x
       new_list.append(minimum)
       sort_list.remove(minimum)    
   return new_list


print(sorting(data_list))


#Ex:6

my_list = [-23, 5, 0, 23, -6, 23, 67,-2]

def second_max_el(second):
   new_list = []
   while second:
       maximum = second[0]  
       for x in second: 
           if x > maximum:
               maximum = x
       new_list.append(maximum)
       second.remove(maximum)    
   return new_list[1]


print(f"The second largest element of the list:{second_max_el(my_list)}")




