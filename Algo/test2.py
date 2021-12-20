# [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"},{"VIII":"S007"}]

#Expected output: {'S005', 'S002', 'S007', 'S001', 'S009'}

target_dict={}

list_of_dict = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"},{"VIII":"S007"}]

for d in list_of_dict:
    tmp = list(d.values())
    print(*tmp)
    target_dict.setdefault(*tmp)

print(target_dict)

# {'S001': None, 'S002': None, 'S005': None, 'S009': None, 'S007': None}