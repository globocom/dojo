def get_solution(bag_size, time_pizzas):
    # bag_size = 10
    # time_pizzas = [
    #    (15, 5), 
    #    (23, 4), 
    #    (21, 2),
    #    (16, 4),
    #    (19, 5),
    #    (18, 2),
    # ]
    # solution = 62
    pass

def get_ratio(t):
    return t[0]/t[1]
    
def get_ratio_list(list):

    new_list = []

    for elemento in list:
        new_list.append((get_ratio(elemento),)+elemento)

    return new_list

# def func(element):
#     return (element[0], -element[2])


def order_desc_by_ratio(list_with_ratio):

    # return sorted(list_with_ratio, reverse=True, key=func)
    return sorted(list_with_ratio, reverse=True, key=lambda y: (y[0],-y[2]))
    # if list_with_ratio[0][0] == 5:
    #     return [(5,4,4), (2,5,5)]
    # if list_with_ratio[0][0] == 1:
    #     return [(1,4,4), (1,5,5)]
    # return [(6,24,4), (3,15,5)]

def main():
    return True
