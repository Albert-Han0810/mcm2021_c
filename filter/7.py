import json
import re
import math

f = open('dataset.json', 'r', encoding='utf-8')
dataset_dic = json.load(f)
f.close()

f = open('vec_dist_min.json', 'r', encoding='utf-8')
vec_dist_dic = json.load(f)
f.close()

max_dist = max(list(vec_dist_dic.values()))
min_dist = min(list(vec_dist_dic.values()))

for k in vec_dist_dic.keys():
    vec_dist_dic[k] = (vec_dist_dic[k] - min_dist) / (max_dist - min_dist)

un_vec_dic = {}

for k in vec_dist_dic.keys():
    if dataset_dic[k]['lab_status'] == 'Unverified':
        un_vec_dic[k] = vec_dist_dic[k]

dist_arr = sorted(list(un_vec_dic.values()))

for i in range(0, len(dist_arr)):
    print(dist_arr[i])
    if (dist_arr[i] > 0.035):
        print(i)
        break

out_dic = {}

for k in un_vec_dic.keys():
    un_vec_dic[k] = math.exp(-6.376 * un_vec_dic[k])

f = open('final_vals_un.json', 'w', encoding='utf-8')
json.dump(un_vec_dic, f)
f.close()

for k in vec_dist_dic.keys():
    vec_dist_dic[k] = math.exp(-6.376 * vec_dist_dic[k])

f = open('final_vals_all.json', 'w', encoding='utf-8')
json.dump(vec_dist_dic, f)
f.close()
