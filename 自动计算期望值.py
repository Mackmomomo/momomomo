import datetime
current_time = datetime.datetime.now()
datime = "当前日期为:{}\n".format(current_time.strftime("%Y-%m-%d %H:%M:%S"))

x=int(input("模式选择1为计算成本，2为计算期望值:"))
def expected_value(prices, probabilities):
    """计算期望值"""
    if len(prices) != len(probabilities):
        return None  # 价格列表和概率列表长度必须相等

    # 计算期望值
    expected = sum([prices[i] * probabilities[i] for i in range(len(prices))])

    return expected

def cb(datime):
    # 读取十个数并求和，记录输入过程
    total = 0
    process = ""
    for i in range(10):
        num = float(input("请输入第{}个成本: ".format(i + 1)))
        total += num
        if i < 9:
            process += "第{}个成本为：{}\n".format(i + 1, num)
        else:
            process += "第{}个成本为：{}".format(i + 1, num)
    # 将结果和输入过程写入文本文件
    with open("cb.txt", "a") as file:
        file.write("{}\n总成本的和为：{}\n{}\n".format(process, total,datime))
        input("回车退出")

def qwz(current_time):
    # 自定义数量的价格和概率
    cost = float(input("请输入成本："))
    with open("qwz.txt", "a") as file:
        file.write("成本为{}\n".format(cost))
    n = int(input("请输入模拟结果总数量为多少个："))
    prices = []
    probabilities = []
    for i in range(n):
        price = float(input("请输入模拟结果第{}个价格：".format(i+1)))
        with open("qwz.txt", "a") as file:
            file.write("请输入模拟结果第{}个价格：{}\n".format(i+1,price))
        probability = float(input("请输入模拟结果第{}个概率：".format(i+1)))
        with open("qwz.txt", "a") as file:
            file.write("请输入模拟结果第{}个概率：{}\n".format(i+1,probability))
        prices.append(price)
        probabilities.append(probability)


    # 计算期望值
    expected = expected_value(prices, probabilities)
    print("期望值为：{}".format(expected))

    # 计算期望率并输出

    expectancy_rate = ((expected - cost)/cost)*100

    print("期望率为：{:.2f}%".format(expectancy_rate))

    # 输出成本减去期望值
    profit = expected - cost
    if profit > 0:
        print("在理论上说炼金是盈利的，利润为：{}".format(profit))
        with open("qwz.txt", "a") as file:
            file.write("期望值为：{}\n期望率为：{}\n在理论上说炼金是盈利的，利润为：{}\n{}\n".format(expected, expectancy_rate,profit,datime))
    elif profit < 0:
        print("在理论上说炼金是亏损的，亏损为：{}".format(-profit))
        with open("qwz.txt", "a") as file:
            file.write("期望值为：{}\n期望率为：{}\n在理论上说炼金是亏损的，利润为：{}\n{}\n".format(expected, expectancy_rate,profit,datime))
    else:
        print("在理论上说炼金是不赚不亏的")
        with open("qwz.txt", "a") as file:
            file.write("期望值为：{}\n期望率为：{}\n在理论上说炼金是不亏不赚的，利润为：{}\n{}\n".format(expected, expectancy_rate,profit,datime))
    input("回车退出")


if x==1 :
    cb(datime)
if x==2 :
    qwz(datime)
