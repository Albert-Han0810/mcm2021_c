import pandas as pd
import numpy as np
import nltk
import wordcloud
import matplotlib.pyplot as plt

#nltk.download()
r = pd.read_excel("dataset.xlsx")
data = r.values
data = pd.DataFrame(data, columns = ["ID", "Date", "Note", "Status", "Comment", "Submission Date", "Latitude", "Longitude"])
dic = {}
ng_data = data[data["Status"] == "Negative ID"]

notes = ng_data.loc[:, ["Note", "Comment"]]
for id, rec in notes.iterrows():
    if rec["Note"] != "":
        text = str(rec["Note"])
        sens = nltk.sent_tokenize(text)
        for sent in sens:
            words = nltk.pos_tag(nltk.word_tokenize(sent))
            for word, tag in words:
                if tag == "NN" or tag == "JJ":
                    dic[word] = dic.get(word, 0) + 1
    '''
    if rec["Comment"] != "":
        text = str(rec["Comment"])
        sens = nltk.sent_tokenize(text)
        for sent in sens:
            words = nltk.pos_tag(nltk.word_tokenize(sent))
            for word, tag in words:
                if tag == 'NN' or tag == "JJ":
                    dic[word] = dic.get(word, 0) + 1
    '''

word_cnt = [(dic[word], word) for word in dic.keys()]
sorted(word_cnt)
ws = [word_cnt[i][1] for i in range(50)]
string = " ".join(x for x in ws)
print(string)
wc = wordcloud.WordCloud(background_color = "white").generate(string)
plt.axis("off")
plt.imshow(wc)
plt.show()