def main(arr1, arr2):
    dic1 = getcount(arr1)
    dic2 = getcount(arr2)
    return dictdiff(dic1, dic2)


def getcount(arr1):
    dic = dict()

    for a in arr1:
        if a in dic:
            dic[a] += 1
        else:
            dic[a] = 1
    return dic


def dictdiff(dict1, dict2):
    result = []
    for k, v in dict1.items():
        if k not in dict2 or v != dict2[k]:
            result.append(k)
        if k in dict2:
            dict2.pop(k)
        result += dict2.keys()
    return list(set(result))
