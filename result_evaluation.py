import sys
from sklearn.metrics import accuracy_score, roc_auc_score

filename = sys.argv[1]
label_1_prob = []
pred_label = []
truth_label = []
with open(filename, 'r', encoding='utf-8') as file:
    result_arr = file.readlines()
    for line in result_arr:
        tmp = line.strip().split('\t')
        label_1_prob.append(float(tmp[-3]))
        pred_label.append(int(tmp[-2]))
        truth_label.append(int(tmp[-1]))

acc_score = accuracy_score(pred_label, truth_label)
print('Accuracy: %.4f' %acc_score)

auc_score = roc_auc_score(truth_label, label_1_prob)
print('AUC Score: %.4f' %auc_score)
