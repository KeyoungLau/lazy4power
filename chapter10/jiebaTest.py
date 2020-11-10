import jieba
ls = jieba.lcut("全国计算机等级考试")
print(ls)
# 全模式，将所有可能的分词都列出来，冗余性最大
ls = jieba.lcut("全国计算机等级考试", cut_all=True)
print(ls)