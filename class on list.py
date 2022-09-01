# numbers_list = [10,12,23,74,55,76]
# result = []

# for item in numbers_list:
#     result.append(item+1)
# print(result)

# for i in range (len(numbers_list)):
#     numbers_list[i] += 
#         print(numbers_list)
# test_list = {7,5,2,6,9,1}
# for item in test_list:
#     if item % 2:
#         print(test_list)
# index = 0
# while index < len(numbers_list):
#     numbers_list[index] *=10
#     index += 1

# print(numbers_list)
# print(index, 'This is INDEX!')
# write a solution that will remove all occurrences of 23 in any list.
# from unittest import sult


numbers_list = [23,23,23,23,23,23,23]

for item in numbers_list:
    if(item == 23):
        numbers_list.remove(item)
 
print (numbers_list)
