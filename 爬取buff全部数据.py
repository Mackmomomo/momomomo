import requests
import urllib.parse
import time
import pandas as pd
#输入登录好的buff  cookie
cookie = ""


headers={
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'cookie':cookie,
        'Host': 'buff.163.com',
        'Referer': 'https://buff.163.com/market/csgo',
        'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
}
current_time = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())

dataframes = []
print("正在执行爬取任务，一共256页数")
for page in range(1,256):
    time.sleep(3)
    print("冷却3秒")
    print("尝试获取第",page,"页")
    #name = urllib.parse.quote(x)
    shuju_url = "https://buff.163.com/api/market/goods?game=csgo&page_num={}&use_suggestion=0&_=1679445292127&page_size=80".format(page)
    shuju = requests.get(shuju_url, headers=headers)
    datas = shuju.json()
    print("获取第",page,"页数据")
    #print(datas.get('data').get('items'))
    df = pd.DataFrame(datas['data']['items'])
    dataframes.append(df)

result = pd.concat(dataframes)

# 添加翻译字典
translation_dict = {
    "appid": "应用ID",
    "bookmarked": "已收藏",
    "buy_max_price": "最高求购价格",
    "buy_num": "求购数量",
    "can_bargain": "可议价",
    "can_search_by_tournament": "可通过比赛搜索",
    "description": "描述",
    "game": "游戏",
    "goods_info": "商品信息",
    "has_buff_price_history": "有价格历史",
    "id": "ID",
    "market_hash_name": "市场哈希名称",
    "market_min_price": "最低市场价格",
    "name": "名称",
    "quick_price": "快速价格",
    "sell_min_price": "最低售价",
    "sell_num": "在售数量",
    "sell_reference_price": "参考售价",
    "short_name": "简称",
    "steam_market_url": "Steam市场网址",
    "transacted_num": "成交数量"
}

# 对第一行标题进行翻译
translated_columns = [translation_dict.get(col, col) for col in result.columns]

# 在第二行插入翻译后的标题
result.loc[-1] = translated_columns
result.index = result.index + 1
result = result.sort_index()

# 将数据写入 Excel 文件
filename = f"{current_time}.xlsx"
result.to_excel(filename, index=False, header=None)

