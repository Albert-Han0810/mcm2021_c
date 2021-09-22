import json

f = open('wordsfreq.txt', 'r', encoding='utf-8')
words_arr = json.load(f)
f.close()

words_useless_set = set(['', 'a', 'the', 'I', 'it', 'and', 'was', 'in', 'to', 'my', 'on', 'of', 'It', 'but', 'this', 'have', 'is', 'not', 'at', 'our', 'seen', 'saw', 'with', 'one', 'like', 'an', '2', '1', 'about', 'get', 'that', 'We', 'very', 'around', 'me', 'for', 'were', 'we', 'as', 'had', 'be', 'what', 'if', 'from', 'out', 'back', 'Found', 'or', 'by', 'so', 'The', 'away', 'before', 'than', 'when', 'found', 'just', 'This', 'up', 'near', 'body', '5', 'into', 'are', 'could', 'off', 'then', 'Was', 'thought', 'see', 'never', 'did', 'WA', 'look', 'Not', 'over', 'My', 'two', 'am', 'take', 'them', 'time', '3', 'got', 'Saw', 'you', 'other', 'these', 'they', 'didn\'t', 'ever', 'any', 'think', 'there', 'while', 'no', 'i', 'more', 'close', 'able', 'its', 'because', 'I\'ve', 'it\'s', 'last', 'all', 'They', '2', 'can', 'A', 'About', "I'm", 'good', 'Seen', 'almost', "There", "4", 'where', 'still', 'next', 'down', 'came', 'Very', 'anything', 'too', 'been', 'went', 'after', '2"', 'A', 'About', 'No', "don't", "But", 'ago', '&', 'On', 'will', 'between', '2\u201d', 'wa', 'Wa' ])

words_selected = []

for i in range(0, len(words_arr)):
    if (words_arr[i][0] not in words_useless_set):
        words_selected.append(words_arr[i][0])
        if (len(words_selected) >= 494):
            break

words_selected += ['colony', 'hatched', 'Insects', 'suspect', 'Specimen','outdoor']
        
f = open('words_selected.json', 'w', encoding='utf-8')
json.dump(words_selected, f)
f.close()