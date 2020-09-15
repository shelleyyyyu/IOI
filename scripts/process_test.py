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


def process_data(train_a_fname, train_b_fname, test_a_fname, test_b_fname, result_path):

    with open(test_a_fname, 'r', encoding='utf-8') as file:
        test_a_data = file.readlines()
        test_a_data, max_word_len, avg_word_len = clean_data(test_a_data)
        print(max_word_len, avg_word_len)

    with open(test_b_fname, 'r', encoding='utf-8') as file:
        test_b_data = file.readlines()
        test_b_data, max_word_len, avg_word_len = clean_data(test_b_data)
        print(max_word_len, avg_word_len)

    with open(train_a_fname, 'r', encoding='utf-8') as file:
        annotate_a_data = file.readlines()
        annotate_a_data, max_word_len, avg_word_len = clean_data(annotate_a_data)
        print(max_word_len, avg_word_len)

    with open(train_b_fname, 'r', encoding='utf-8') as file:
        annotate_b_data = file.readlines()
        annotate_b_data, max_word_len, avg_word_len = clean_data(annotate_b_data)
        print(max_word_len, avg_word_len)


    path = os.path.join(result_path, './test_a.txt')
    with open(path, 'w', encoding='utf-8') as file:
        for data in test_a_data:
            file.write(data+'\n')

    path = os.path.join(result_path, './test_b.txt')
    with open(path, 'w', encoding='utf-8') as file:
        for data in test_b_data:
            file.write(data+'\n')

    path = os.path.join(result_path, './annotate_a.txt')
    with open(path, 'w', encoding='utf-8') as file:
        for data in annotate_a_data:
            file.write(data+'\n')

    path = os.path.join(result_path, './annotate_b.txt')
    with open(path, 'w', encoding='utf-8') as file:
        for data in annotate_b_data:
            file.write(data+'\n')

if __name__ == "__main__":
    train_a_fname = sys.argv[1]
    train_b_fname = sys.argv[2]
    test_a_fname = sys.argv[3]
    test_b_fname = sys.argv[4]
    result_path = sys.argv[5]
    process_data(train_a_fname, train_b_fname, test_a_fname, test_b_fname, result_path)