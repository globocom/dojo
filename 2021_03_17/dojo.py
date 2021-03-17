def separate_names(names):
    list_no = list()
    list_yes = list()
    for i in names:
        if i[1] == "NO":
            list_no.append(i[0])
        else:
            list_yes.append(i[0])
    return (list_yes, list_no)

def get_bigger_name(names):
    bigger = ""
    for name in names:
        if len(name)>len(bigger):
            bigger = name
    return bigger

def ordenados(names):
    return sorted(set(names))

