
import json
import re

f = open("dataset.json", 'r', encoding='utf-8')
dataset_dic = json.load(f)
f.close()

words_dic = {}

for tag in dataset_dic.keys():
    note_str = dataset_dic[tag]['notes']
    words_arr = re.split(' |,|\(|\)|/|-|\.|,', note_str)
    for wod in words_arr:
        if (wod in words_dic.keys()):
            words_dic[wod] += 1
        else:
            words_dic[wod] = 1

f = open('out.txt', 'w', encoding='utf-8')
f.write(str(words_dic))
f.close()

words_arr = sorted(words_dic.items(), key=lambda d:d[1], reverse=True)
words_arr2 = []
for i in range(0, len(words_arr)):
    words_arr2.append(list(words_arr[i]))

f = open('wordsfreq.txt', 'w', encoding='utf-8')
json.dump(words_arr2, f)
f.close()

