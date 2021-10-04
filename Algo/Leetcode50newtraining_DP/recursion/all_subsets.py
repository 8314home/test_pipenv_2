final_list=[{}]
for i in [1,2]:
    for j in [1,2]:
        if {i, j} not in final_list:
            final_list.append({i, j})
print(final_list)