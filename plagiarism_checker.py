import cProfile
import re
import jieba
# 文本预处理

# 文本预处理：去除标点符号和空格，将文本分割成单词列表。
def before_calculate(text):

    # 利用正则表达式去除标点符号和特殊字符
    text = re.sub(r'[^\w\s]', '', text)
    # 分割成单词列表
    words = text.split()
    return words

# 相似度计算
def similarity_calculate(orig_words,plag_words):
    orig_set=set(orig_words)
    plag_set=set(plag_words)
    intersection=orig_set.intersection(plag_set)
    union=orig_set.union(plag_set)
    similarity=len(intersection)/len(union) if union else  0
    return  similarity


