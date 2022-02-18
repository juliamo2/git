"""
     1.根据需求，定义函数
     2.将变化点单独定义为函数
     3.讲通用的代码定义为函数（使用参数隔离变化点）
     4.在IterableHelper类中添加新功能
     5.在当前模块中进行测试

"""

def sum01():
    sum_value = 0
    for item in list01:
        sum_value += item.age
    return sum_value

def sum01():
    sum_value = 0
    for item in list01:
        sum_value += item.height
    return sum_value

def sum(func):
    sum_value = 0
    for item in list01:
        sum_value += func(item)
    return sum_value



list01 = []


def find(func):
    for item in list01:
        if func(item):
            yield item


def condition02(item):
    return item.hight < 170


def condition03(item):
    return len(item.name) > 2


def condition04(item):
    return item.age < 25


def get_count(func):
    count = 0
    for item in list01:
        if func(item):
            count += 1
    return count


def handle01(item):
    return item.name


def handle02(item):
    return (item.name, item.score)


def select(func):
    for item in list01:
        yield func(item)


def condition01(item):
    return item.face.score > 90


for item in find(lambda item: item.face.score > 90):
    print(item)

