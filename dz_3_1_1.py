import json
from pprint import pprint
from collections import Counter

def News_format(dict_json):
    news_str = ''
    for news in dict_json['rss']['channel']['items']:
        news_str += news['description']

    news_strs = news_str.split()
    news_strs.sort(key = len, reverse = True)
    output_list = []
    for word in news_strs:
        if len(word) >= 6:
            output_list.append(word)
    return output_list

def main():
    with open('newsafr.json', encoding ='utf-8') as json_file:
        news = json.load(json_file)
    output = Counter(News_format(news))
    pprint(output.most_common(10))

main()
