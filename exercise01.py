# #
# # price = float(input("请输入商品定金"))
# # total = float(input("请输入商品总价"))
# # remaining = price - total*2
# # print("尾款应付"+str(remaining))
# #
# # dollar = input("请输入美元")
# # rmb = float(dollar) * 6.6813
# # print("转换为人民币为"+str(rmb))
#
# # a=1
# # b=2
# # print(123)
# # print(1,2,3)
# # print(a,"a",+int(a),str(b),float(b),"%f"%a)
# # print("打印", a, "结束")
# #
# # a = 1+2j
# # print(int(a))
#
#
# #  ex5
# # day = input("请输入天")
# # hour = input("请输入时")
# # mini = input("请输入分")
# # s =input("请输入秒")
# # print(day+"天"+hour+"时"+mini+"分"+s+"秒")
# # mino = (((int(day)*24+int(hour))*60)*60+int(mini))*60+int(s)
# # print("总秒数为"+str(mino))
#
# # change
# # a = input("请输入数字a")
# # b = input("请输入数字b")
# # c = a
# # a = b
# # b = c
# # print("交换后a="+a, "b=" + b)
#
# # miao
# total = int(input("请输入秒数"))
# day = total // (24 * 3600 * 60)
# hour = (total - (day * 3600 * 24)) // 3600
# mini = (total - ((day * 3600 * 24) - hour * 3600)) // 60
# s = total % 60
# print(str(day) + "天" + str(hour) + "时" + str(mini) + "分" + str(s) + "秒")
# # print(day, "天", hour, "时", mini, "分", s, "秒", sep="")
# print(day, hour, mini, s)

# list01 = [90, "ww", 1]
# list02 = list("北大附中")
# list02.append("时")
# list02.insert(4,"有")
# print(list02)

# list01 = ["水星", "金星", "地球", "木星", "土星", "天王星"]
# list01.append("海王星")
# list01.insert(3,"火星")
# print(list01[-1])
# print(list01[0:2])
# # list01.remove("金星")
# # del list01 [2:(len(list01)+1)]
# for i in range(len(list01)-1,-1,-1):
#     print(list01[i])
#
# print(list01)

# list01 = list()
# while True:
#     a = input("请输入成绩")
#     if a == ' ':
#         break
#     else:
#         list01.append(int(a))
# print(list01)
#
# # for i in range(len(list01)):
# #     print(list01[i])
#
# for item in list01:
#     print(item)
#
# print(max(list01))
# print(min(list01))
# print(sum(list01))


# list01 = [10,20]
# list02 = list01
# list01 = 100
# print(list02[0])
import copy

# list01 = [10, 20, 30]
# list02 = copy.deepcopy(list01)
# print(list02)
#
# list_temp = []
# while True:
#     str_input = input("请输入")
#     if str_input == "":
#         break
#     list_temp.append(str_input)
# str_result = "".join(list_temp)
# print(str_result)
#
# str_start = "How are you"
# list01 = str_start.split(" ")
# list02 = list01[-1:-4:-1]
# print(list01)
# print(list02)
# str_end = " ".join(list02)
# print(str_end)


# dict_commodity = {}
# while True:
#     name = input("")
#     if name == "":
#         break
#     price = int(input(""))
#     dict_commodity[name] = price
#
# for k,v in dict_commodity.items():
#     print(k)
#     print(v)
# if "" in dict_commodity:
#     print()

# str_target = "abcbdeacb"
# dict_result = {}
# for item in str_target:
#     if item not in dict_result:
#         dict_result[item] = 1
#     else:
#         dict_result[item] += 1
# for k,v in dict_result.items():
#     print("字符%s,%d次"%(k,v))
# print(item)


# a = [10]
# b = [10]
# fun03(a,b)
# print(a)
# print(b)

def fun01(a,b,c)
    print(a)
    print(b)
    print(c)

fun01(1,2)