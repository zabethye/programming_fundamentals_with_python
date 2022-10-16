# first_string = input().split(", ")
# second_string = input().split(", ")
#
# new_list = []
# for first in first_string:
#     for second in second_string:
#         if first in second:
#             new_list.append(first)
#             break
#
# print(new_list)

first_string = input().split(", ")
second_string = input().split(", ")

result = [first for first in first_string if any(first in second for second in second_string)]
print(result)