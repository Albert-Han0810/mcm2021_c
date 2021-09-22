【0】总体统计
Positive 个数14 
空 notes 个数3
negative 个数 2055
空 notes 个数 301
unverified 个数 2286
空 notes 个数 231
unprocessed 个数 13
空 notes 个数 0

【1】按照时间顺序对发现事件进行排序，删除时间栏为空、时间格式与大部分项不一致、时间分布不够密集的行
【2】2019年之前的数据过于稀少，故删除。经过上面两部操作后，还剩下4368项，时间区间为2019-2020年
【3】使用 python 统计 notes 中的词频，选择其中最多的100个（，并删除无用的词汇，并添加 Positive 的词汇 6 个，见于 4.py 中）使用它们来构成词语向量
【4】使用 tf-idf 来构成句子向量，筛选出其中的 Postive 向量
【5】计算所有向量到最近的 Positive 向量的距离。考虑到 Positive 向量中存在 0 向量，而 Unverified 中也存在不少的 0 向量，当处理的 notes 为空且为 Unverified 时，不考虑空的 Positive 向量，而是取该点对非空 Positive 向量的最小距离
【6】对距离进行归一化处理
考虑到
14/2055 = 0.68% 这是 pos/neg 的比率
0.68% * 2286 = 15.5 这是根据上面比率估计的 unverified 中的 positive 个数
发现当归一化距离阈值取 0.035 时，有 20个满足条件
e^(-k * 0.035) = 80%，可得 k = 6.376
故取函数为 e^-6.376

文件：
【1】1.py, 2.py  将 xlsx 转化为 json
【2】3.py，统计词频，得到 wordsfreq.txt 文件
【3】4.py，获取词语向量，放在 words_selected.json 中
【4】5.py，使用 tf-idf 获得每个 notes 的向量，将向量保存在 all_vector.json 和 positive_vector.json 中
【5】6.py，计算向量之间的距离，并把到 positive 的最小值保存到 vec_dist_min.json 中
【6】对距离归一化，并估计函数，得到的函数估计值放在 final_vals_un.json（其中是 unverified 的函数值）和 final_vals_all.json （其中是所有项的函数值）
它们分别保存到了 vals_un 和 vals_all 的 excel 中

