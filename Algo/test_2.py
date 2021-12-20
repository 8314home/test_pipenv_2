"""
Problem
We want to extract and transform results from a list of dicts as follows:

For each dict record, extract the numbers from columns field excluding the first two values and the last one.
For any float values, it should be rounded to two decimal places.
"""





result = [
    {'row': {'columns': [1547140535233, None, 0, -1.3598071336738, -0.0727811733098497, 2.53634673796914,
                         1.37815522427443, -0.338320769942518, 0.462387777762292, 0.239598554061257,
                         0.128539358273528, -0.189114843888824, 0.133558376740387, -0.0210530534538215, 149.62,
                         u'0']}},
    {'row': {'columns': [1547140535233, None, 0, -0.0727811733098497, 2.53634673796914, 1.37815522427443,
                         -0.338320769942518, 0.462387777762292, 0.239598554061257, 0.0986979012610507,
                         0.363786969611213, 0.0907941719789316, -0.551599533260813, -0.617800855762348,
                         -0.991389847235408, -0.311169353699879, 1.46817697209427, -0.470400525259478,
                         0.207971241929242, '0']}},
    {'row': None}]


def transform(result):
    """ Transform the result by returning only the numbers in "columns" field without the first two and the last element. Round remaining values to two decimals.

        Hint: Use round(value, 2) to round a value to two decimals.

    """
    res = []
    for d in result:
        print(type(d))
        tmp_v = d.get('row')  # save value part, also a dict
        print(tmp_v)
        if tmp_v:
            tmp_v2 = tmp_v['columns']  # list of values
            print(tmp_v2)
            if tmp_v2:
                l_v = tmp_v2[2:len(tmp_v2)-1]  # eliminate first 2 and last number
                print(l_v)
                l_v2 = list(map(lambda x: round(x,2), l_v)) # round upto 2
                print(l_v2)
                res.append(l_v2)
        print('-----')

    return res  # Add implementation and return real result

records = transform(result)

for record in records:
    print(record)

# It should print out:
# [0, -1.36, -0.07, 2.54, 1.38, -0.34, 0.46, 0.24, 0.13, -0.19, 0.13, -0.02, 149.62]
# [0, -0.07, 2.54, 1.38, -0.34, 0.46, 0.24, 0.1, 0.36, 0.09, -0.55, -0.62, -0.99, -0.31, 1.47, -0.47, 0.21]
