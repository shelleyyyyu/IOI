import sys
import os

def clean_data(data):
    max_word_len = 0
    avg_word_len = 0
    new_data = []
    for d in data:
        split_d = d.strip().split('\t')
        if len(split_d) != 3:
            continue
        new_split_d = []
        for d in split_d:
            #print(len(' '.join([i for i in d.split(' ') if i != ''])))
            #print([i for i in d.split(' ') if i != ''])
            tmp_arr = [i for i in d.split(' ') if i != '']
            if max_word_len < len(tmp_arr):
                max_word_len = len(tmp_arr)
            avg_word_len += len(tmp_arr)
            new_split_d.append(' '.join(tmp_arr))
        new_data.append('\t'.join(new_split_d))
    return new_data, max_word_len, int(avg_word_len/len(data))


def process_data(train_fname, result_path):
    with open(train_fname, 'r', encoding='utf-8') as file:
        data = file.readlines()
        data, max_word_len, avg_word_len = clean_data(data)
        print(max_word_len, avg_word_len)

    data_len = len(data)
    train_data_len = int(data_len*0.9)
    train_data = data[:train_data_len]
    valid_data = data[train_data_len:]

    path = os.path.join(result_path, './train.txt')
    with open(path, 'w', encoding='utf-8') as file:
        for data in train_data:
            file.write(data+'\n')

    path = os.path.join(result_path, './valid.txt')
    with open(path, 'w', encoding='utf-8') as file:
        for data in valid_data:
            file.write(data+'\n')

if __name__ == "__main__":
    train_fname = sys.argv[1]
    result_path = sys.argv[2]
    process_data(train_fname, result_path)