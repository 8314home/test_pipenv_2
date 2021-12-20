# convert a list of dates ['11/07/2001', '11-08-2001', '12.09.2001']
# to print as yyyy-mm-dd


from datetime import datetime
list_of_dates = ['11/07/2001', '11-08-2001', '12.09.2001']

l2 = []

# str.maketrans creates a translation table
# x.translate() uses this translation table to replace items

for x in list_of_dates:
    for sep in ['/', '.', '-']:
        if sep in x:
            l2.append(x.translate(str.maketrans({'/': '-', '.': '-'})))


print(l2)

for i in l2:
    print(datetime.strftime(datetime.strptime(i, "%d-%m-%Y"), "%Y-%m-%d"))



