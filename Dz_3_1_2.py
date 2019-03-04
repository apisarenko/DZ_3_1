import xml.etree.ElementTree as ET
from pprint import pprint
from collections import Counter

def News_format(list):
    news_str = ''
    for news in list:
        news_str += news 

    news_strs = news_str.split()
    news_strs.sort(key = len, reverse = True) 
    output_list = []
    for word in news_strs:
        if len(word) >= 6:
            output_list.append(word)
    return output_list

def main():
    news = []
    tree = ET.parse('newsafr.xml')
    root = tree.getroot()
    descriptions = root.findall('channel/item/description')
    for text in descriptions:
        news.append(text.text)
    output = Counter(News_format(news))
    pprint(output.most_common(10))

main()
