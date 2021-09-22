import json
import math
f = open('all_vector.json', 'r', encoding='utf-8')
vector_dic = json.load(f)
f.close()

f = open('positive_vector.json', 'r', encoding='utf-8')
pos_vector_dic = json.load(f)
f.close()

f = open('dataset.json', 'r', encoding='utf-8')
dataset_dic = json.load(f)
f.close()

K = 10

def vector_dist(a, b):
    sum = 0
    for i in range(0, len(a)):
        sum += (a[i] - b[i]) * (a[i] - b[i])
    return math.sqrt(sum)

def lat_lang_dist(str1, str2):
    return math.sqrt((float(dataset_dic[str1]['latitude']) - float(dataset_dic[str2]['latitude']))**2 + (float(dataset_dic[str1]['longitude']) - float(dataset_dic[str2]['longitude']))**2)

format_dic = {}

ppp = 0
for a in vector_dic.keys():
    format_dic[a] = {}

    print(ppp)
    ppp += 1
    temp_dic = {}

    for k in pos_vector_dic.keys():
        temp_dic[k] = vector_dist(vector_dic[a], pos_vector_dic[k])

    now_arr = sorted(list(temp_dic.values()))
    
    format_dic[a] = 0
    if now_arr[0] == 0:
        if dataset_dic[a]['lab_status'] == 'Positive ID':
            format_dic[a] = 0
        else:
            for i in range(0, len(now_arr)):
                if now_arr[i] != 0:
                    format_dic[a] = now_arr[i]
                    break;
            
    else:
        format_dic[a] = now_arr[0]

f = open('vec_dist_min.json', 'w', encoding='utf-8')
json.dump(format_dic, f)
f.close()
