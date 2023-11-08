# import os

# folder = os.getcwd() + '\data\\'
# walk = os.walk(folder)

# for line in walk:
#     print(line)    
# files = line[2] 

#1(сколько всего файлов)
# import os

# folder = os.getcwd() + '\data\\'
# walk = os.walk(folder)
# sum = 0

# for line in walk:
#     print(line)    
# files = line[2] 

# a = len(files)
# sum  += a
# print(sum)

#2(сколько файлов в имени имеют цифру)

# import os

# folder = os.getcwd() + '\data\\'
# walk = os.walk(folder)

# count = 0
# nums = ['0','1','2','3','4','5','6','7','8','9']

# for line in walk:
#     print(line)    
# files = line[2] 


# for i in files:
#     for num in nums:
#         if num in i:
#             count+=1
#             break
# print(count)

#3(сколько имеют 'g')

# import os

# folder = os.getcwd() + '\data\\'
# walk = os.walk(folder)

# count = 0
# nums = ['g']

# for line in walk:
#     print(line)    
# files = line[2] 


# for i in files:
#     for num in nums:
#         if num in i:
#             count+=1
#             break
# print(count)

#4(сколько имеют 'gg')

# import os

# folder = os.getcwd() + '\data\\'
# walk = os.walk(folder)

# count = 0
# nums = ['gg']

# for line in walk:
#     print(line)    
# files = line[2] 


# for i in files:
#     for num in nums:
#         if num in i:
#             count+=1
#             break
# print(count)

#5(сумма чисел больше 10)

# import os
# import re

# folder = os.getcwd() + '\data\\'
# walk = os.walk(folder)

# for line in walk:
#     print(line)    
# files = line[2] 

# sum_greater_than_10_count = 0
# for file in files:
#     numbers = re.findall(r'\d+', file)
#     if sum(map(int, numbers)) > 10:
#         sum_greater_than_10_count += 1
# print(f"Количество файлов, где сумма чисел больше 10: {sum_greater_than_10_count}")



























