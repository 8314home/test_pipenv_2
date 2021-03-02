# for every position at ith location, we will check against all it's predecessor elements
# and try to calculate common difference from it
# if common difference is already present, we will increment by 1


def longest_ap_sequence_length(input_list_ap_sequence):

    dp_list_of_dicts = list()
    len_of_input_list_ap_sequence = len(input_list_ap_sequence)

    for i in range(len_of_input_list_ap_sequence):
        dp_list_of_dicts.append(dict())

    for i in range(1, len_of_input_list_ap_sequence):
        for j in range(0, i):
            k = str(input_list_ap_sequence[i] - input_list_ap_sequence[j]) # common difference calculation
            if k in dp_list_of_dicts[j].keys():
                # print(f"dp_list_of_dicts[{j}][{k}] - {dp_list_of_dicts[j][k]}")
                if int(dp_list_of_dicts[j][k]) + 1 > int(dp_list_of_dicts[j][k]):
                    dp_list_of_dicts[i][k] = int(dp_list_of_dicts[j][k]) + 1
            else:
                dp_list_of_dicts[i][k] = 1
        print(f"dp_list_of_dicts[{i}] - {dp_list_of_dicts[i]}")

    final_dict = dict()
    for v_dict in dp_list_of_dicts:
        for key in v_dict.keys():
            if key in final_dict.keys():
                print(f"key - {key} final_dict[key] - {final_dict[key]} v_dict[key]- {v_dict[key] }")
                if final_dict[key] < v_dict[key]:
                    final_dict[key] = v_dict[key]
            else:
                final_dict[key] = v_dict[key]
    print(f"final_dict - {final_dict}")

    return sorted(final_dict.items(), key=lambda x: x[1], reverse=True)[0]


if __name__ == "__main__":
    print("longest_ap_sequence_length")

    list_ap_sequence = [1, 7, 10, 13, 14, 19]
    print(f"longest_ap_sequence_length-{longest_ap_sequence_length(list_ap_sequence)}")
