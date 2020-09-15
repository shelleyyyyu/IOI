with open('set3.train.pos.seg', 'r', encoding='utf-8') as file:
    tmp_arr = file.readlines()
    data_len = int(len(tmp_arr)/2)
    data_1_array = tmp_arr[:data_len]
    data_2_array = tmp_arr[data_len:]

with open('set3.train.pos.seg.part.1', 'w', encoding='utf-8') as file:
    for data in data_1_array:
        file.write(data)

with open('set3.train.pos.seg.part.2', 'w', encoding='utf-8') as file:
    for data in data_2_array:
        file.write(data)