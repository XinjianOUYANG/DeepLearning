import json
# 将python对象转换为json字符串
persons = [
    {
        'username': '张三',
        'age': 20,
        'country': '中国'
    },
    {
        'username': 'Bill',
        'age': None,
        'country': 'America'
    }
]
json_str = json.dumps(persons)
print(type(json_str)) # <class 'str'>
print(json_str)  # 中文没有正确显示[{"username": "\u5f20\u4e09", "age": 20, "country": "China"},
                 # {"username": "\u674e\u56db", "age": 30, "country": "America"}]
json_str = json.dumps(persons, ensure_ascii=False)
print(json_str)



with open('person.json', 'w') as fp:
    json.dump(persons, fp, ensure_ascii=False)

json_str = '''
[{"username": "张三", "age": 20, "country": "China"}, 
{"username": "李四", "age": 30, "country": "America"}]
'''
persons = json.loads(json_str)
print(type(persons))
print(persons)

with open('person.json', 'r') as fp:
    persons = json.load(fp)
    print(type(persons))
    print(persons)