with open('input.txt') as f:
    file = f.read()

# lst_num = file.split('\n\n')
# highest = 0
# for lst in lst_num:
#     # convert to num
#     num_lst = [int(x) for x in lst.split('\n')]
#     sum_lst = sum(num_lst)
#     if sum_lst > highest:
#         highest = sum_lst

# print(highest)


lst_num = file.split('\n\n')
lst_of_sums = []
for lst in lst_num:
    # convert to num
    num_lst = [int(x) for x in lst.split('\n')]
    sum_lst = sum(num_lst)
    lst_of_sums.append(sum_lst)

lst_of_sums = sorted(lst_of_sums)
print(lst_of_sums[-1])

print(sum(lst_of_sums[-3:]))
