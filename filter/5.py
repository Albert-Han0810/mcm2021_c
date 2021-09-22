import json
import re
import math

f = open('words_selected.json', 'r', encoding='utf-8')
words_arr = json.load(f)
f.close()

words_map = {}

for i in range(0, len(words_arr)):
    words_map[words_arr[i]] = i


f = open('dataset.json', 'r', encoding='utf-8')
dataset_dic = json.load(f)
f.close()

split_dic = {}
for k in dataset_dic.keys():
    temp_str = dataset_dic[k]['notes']
    split_dic[k] = re.split(' |,|\(|\)|/|-|\.|,', temp_str)

vector_dic = {}

def idf_log(word, dic):
    temp_sum = 0
    for a in dic.keys():
        if word in dic[a]:
            temp_sum += 1
    return math.log(len(dic) / (temp_sum + 1))

for k in dataset_dic.keys():
    vector_dic[k] = list(range(0, len(words_arr)))
    for i in range(0, len(words_arr)):
        vector_dic[k][i] = 0
    split_arr = split_dic[k]
    for a in split_arr:
        if (a in words_arr):
            vector_dic[k][words_map[a]] += idf_log(a,  split_dic) / len(split_arr)

f = open('all_vector.json', 'w', encoding='utf-8')
json.dump(vector_dic, f)
f.close()

pos_vector_dic = {}

for k in dataset_dic.keys():
    if dataset_dic[k]['lab_status'] == "Positive ID":
        pos_vector_dic[k] = vector_dic[k]

f = open('positive_vector.json', 'w', encoding='utf-8')
json.dump(pos_vector_dic, f)
f.close()
