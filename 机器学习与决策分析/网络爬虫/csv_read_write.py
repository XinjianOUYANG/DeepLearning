import csv

# reader & DictReader
with open('douban_music.csv', 'r') as fp:
    reader = csv.reader(fp)  # reader是一个迭代器
    next(reader)  # 执行next，遍历对象往下挪一位，即不读第一行标题行
    for x in reader: # x是列表形式
        name = x[1]
        score = x[-1]
        info = {
            'name': name,
            'score': score
        }
        print(info)


with open('douban_music.csv', 'r') as fp:
    # 使用DictReader创建的reader对象不会包含标题那行的数据
    reader = csv.DictReader(fp)  # reader是一个迭代器
    # reader是一个迭代器，遍历这个迭代器，返回来的是一个有序字典
    for x in reader: # x是有序字典
        name = x['name']
        score = x['score']
        info = {
            'name': name,
            'score': score
        }
        print(info)


# writer & DictWriter
headers = ['username', 'age', 'height']
values = (['张三', 18, 180],
    ['李四', 20, 170],
    ['王五', 30, 165])

with open('classroom.csv', 'w', newline='') as fp:
    writer = csv.writer(fp)
    writer.writerow(headers) # 写入头部标题
    writer.writerows(values) # 写入内容


headers = ['username', 'age', 'height']
values = [
            {'username': '张三', 'age': 18, 'height': 180},
            {'username': '李四', 'age': 20, 'height': 170},
            {'username': '王五', 'age': 30, 'height': 165},
         ]
with open('classroom1.csv', 'w', newline='') as fp:
    writer = csv.DictWriter(fp, headers)
    writer.writeheader()
    writer.writerows(values)
# 只有调用writeheader()才能写入表头信息