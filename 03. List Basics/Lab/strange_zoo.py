tail = input()
body = input()
head = input()
# correct_arrange = [head, body, tail]
# print(correct_arrange)
lst = [tail, body, head]
lst[0], lst[2] = lst[2], lst[0]
print(lst)
