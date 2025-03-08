import cProfile
import re
import jieba
# 文本预处理
def before_calculate(text):
    # 去除标点符号和特殊字符
    text = re.sub(r'[^\w\s]', '', text)
    # 使用jieba进行中文分词
    words = jieba.lcut(text)
    # 去除空格和空白字符
    words = [word for word in words if word.strip()]
    return words

# 相似度计算
def similarity_calculate(orig_words,plag_words):
    orig_set=set(orig_words)
    plag_set=set(plag_words)
    intersection=orig_set.intersection(plag_set)
    union=orig_set.union(plag_set)
    similarity=len(intersection)/len(union) if union else  0
    return  similarity


