from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer


# import sklearn

#
# sklearn.feature_extraction.DictVectorizer


def dictvec():
    """
    字典数据抽取

    """
    # 1,实例化
    dict = DictVectorizer()
    dict = DictVectorizer(sparse=False)
    # 2，调用 fit_transfor
    datainfo = []
    beijininfo = {'city': 'beijin', 'temperature': 100}
    shanghaiinfo = {'city': 'shanghai', 'temperature': 70}
    shenzhenifo =  {'city': 'shenzheng', 'temperature': 30}
    datainfo.append(beijininfo)
    datainfo.append(shanghaiinfo)
    datainfo.append(shenzhenifo)
    # print(datainfo)
    data = dict.fit_transform(datainfo)
    print(data)
    return None

def countvec():
    """
    对文本进行特征抽取 
    1,统计所有文章中的所有词，重复的只看做一次 词的列表 
    2，对每篇文章，在词的列表里面进行统计每个词出现的次数
    3，对单个字母不统计 ,没有分类的依据
    :return:None
    """
    cv = CountVectorizer()
    data = cv.fit_transform(["life life is short ,i like python"," life is too long , i dislike python"])
    print(data.toarray())
    print(cv.get_feature_names())

if __name__ == "__main__":
    # dictvec()
    countvec()
