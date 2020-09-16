import sys
def process(fname, fname_2, new_train_fname, new_valid_fname):
    result_file = open(fname, 'r', encoding='utf-8')
    origin_file = open(fname_2, 'r', encoding='utf-8')
    new_train_file = open(new_train_fname, 'w', encoding='utf-8')
    new_valid_file = open(new_valid_fname, 'w', encoding='utf-8')
    result_arr = result_file.readlines()
    origin_arr = origin_file.readlines()
    total_data_cnt = len(result_arr)
    train_data_cnt = int(total_data_cnt*0.9)
    print(train_data_cnt)

    for i in range(len(result_arr)):

        result_tmp = result_arr[i].strip().split('\t')
        origin_tmp = origin_arr[i].strip().split('\t')
        #context_list, response_list, pred_scores, pred_labels, ture_labels
        context = origin_tmp[0]
        response = origin_tmp[1]
        new_label = result_tmp[-2]
        if i <= train_data_cnt:
            new_train_file.write(context+'\t'+response+'\t'+str(new_label)+'\n')
        else:
            new_valid_file.write(context+'\t'+response+'\t'+str(new_label)+'\n')

    result_file.close()
    origin_file.close()
    new_file.close()

if __name__ == "__main__":
    result_file = sys.argv[1]
    origin_file = sys.argv[2]
    new_train_file = sys.argv[3]
    new_valid_file = sys.argv[4]
    process(result_file, origin_file, new_train_file, new_valid_file)