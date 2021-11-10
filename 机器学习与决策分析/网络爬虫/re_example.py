import re

text = 'hello'
ret = re.match('he', text)
print(ret.group())

text = 'abc'
ret = re.match('a.', text)
print(ret.group())

text = '\n'
ret = re.match('.', text)
print(ret)

text = 'a+cd'
ret = re.match('a\Dc', text)
print(ret.group())


text = 'a\tcd'
ret = re.match('a\s', text)
print(ret.group())

text = 'a_bd'
ret = re.match('a\wb', text)
print(ret.group())

text = 'a我们bd'
ret = re.match('a\w+b', text)
print(ret.group())

text = 'a$bc'
ret = re.match('a\W', text)
print(ret.group())

text = '1'
ret = re.match('[a1]', text)
print(ret.group())




text = '0731-88888888'
ret = re.match('[\d-]+', text)
print(ret.group())

text = '029-8888'
ret = re.match('\d*', text)
print(ret.group())  # 结果是0731

text = 'abcde+'
ret = re.match('\w+', text)
print(ret.group()) # 结果是abcde


text = '+abcde'
ret = re.match('\w?', text)
print(ret.group()) # 结果是啥都没有
text = 'abcde'
ret = re.match('\w?', text)
print(ret.group()) # a


text = '029-8888'
ret = re.match('[\d-]{6}', text)
print(ret.group()) # abc
text = '12345'
ret = re.match('\d{4}', text)
print(ret.group()) # 1234

text = 'abcde'
ret = re.match('\w{1,2}', text)
print(ret.group()) # ab
text = 'ab3de+'
ret = re.match('\w{2,7}', text)
print(ret.group()) # 1234



text = '18357710774'
ret = re.match('1[34578]\d{9}', text)
print(ret.group())
print('=' * 50)

text = 'wang.di@xjtu.edu.cn'
# text = '287922308@qq.com'
# text = '287922308qq.com' 这是匹配不到的
ret = re.match('[\w.]+@[a-z0-9]+\.[a-z.]+', text)
print(ret.group())
print('=' * 50)


text = 'http://www.baidu.com/'
ret = re.match('(https|http|ftp)://[^\s]+', text)
print(ret.group())
print('=' * 50)

text = '41133019880618151x'
ret = re.match('\d{17}[\dxX]', text)
print(ret.group())
print('=' * 50)

text = 'hello'
ret = re.search('^he', text)
print(ret.group())
print('=' * 50)

text = 'xxx@163.com'
ret = re.match('[\w.]+@163\.com$', text)
print(ret.group())
print('=' * 50)

text = 'https'
ret = re.match('(http|https|ftp)', text)
print(ret.group())
print('=' * 50)

text = 'https://www.xjtu.edu.cn'
ret = re.match('(http|https|ftp)://', text)
print(ret.group())
print('=' * 50)


text = '0112344'
ret = re.match('\d+', text)
print(ret.group())
print('=' * 50)

text = '0112344'
ret = re.match('\d+?', text)
print(ret.group())
print('=' * 50)

text = '<h1>标题</h1>'
ret = re.match('<.+>', text)
print(ret.group())
# 结果为<h1>标题</h1>
print('=' * 50)

text = '<h1>标题</h1>'
ret = re.match('<.+?>', text)
print(ret.group())
# 结果为<h1>
print('=' * 50)




# 考虑四种情况：0，1，99，100
# 不可以出现的，09， 101
# 必须以匹配到的结尾，所以要加上$
text = '0'
ret = re.match('[1-9]?\d$|100$', text)
print(ret.group())
print('=' * 50)



text = 'apple price is $299'
ret = re.search('\$(\d+)', text)
print(ret.group())
print('=' * 50)

text = '\n'
print(text)  # 换行
text = '\\n'
print(text)  # 表示普通字符\n
text = r'\n'  # 表示原生(raw)，不做任何处理
print(text) # 表示普通字符\n
print('=' * 50)

  # 其实就是普通字符串'\c'
# python: ’\\c‘ = '\c'
# \\\\c =》 \\c
# 正则表达式: ’\n‘ = 转行
# \\c =》 \c
text = '\c'
ret = re.match('\\\\c', text)
print(ret.group())
# 结果是普通字符串\c
print('=' * 50)

text = '\c'
ret = re.match(r'\\c', text)
print(ret.group())
# 结果是普通字符串\c
print('=' * 50)

text = 'abc\ndef'
ret = re.match('ab.*ef', text, re.DOTALL)
print(ret.group())
# 结果为 'abc\ndef'
print('=' * 50)

text = 'apple price is $99, and the orange price is $88'
ret = re.search('\$\d+', text)
print(ret.group())
# 结果为$99
print('=' * 50)

text = 'apple price is $99, the orange price is $88, and the cherry price is $199'
ret = re.search('.+\$(\d+).+\$(\d+).+\$(\d+)', text)
print(ret.groups())
# ('99', '88', '199')

print(ret.group())  # apple price is $99, the orange price is $88, and the cherry price is $199
print(ret.group(0)) # apple price is $99, the orange price is $88, and the cherry price is $199
print(ret.group(1)) # 99
print(ret.group(2)) # 88
print(ret.group(3)) # 199
print(ret.group(1,2)) # ('99', '88')
print(ret.groups()) # ('99', '88', '199')
print('=' * 50)

text = 'apple price is $99, the orange price is $88, and the cherry price is $199'
ret = re.findall('\$\d+', text)
print(ret)
# 结果为一个列表['$99', '$88', '$199']
print('=' * 50)

text = 'apple price is $99, the orange price is $88, and the cherry price is $199'
ret = re.sub('\$', '￥', text)
print(ret)
# 结果为apple price is ￥99, the orange price is ￥88, and the cherry price is ￥199
print('=' * 50)

text = '''
<div class="job-detail">
        【职位描述】
    <br>
    <br>1.根据业务需求，进行技术编码，调试，单元测试，能够解决核心技术问题；
    <br>
    <br>2.运用项目开发相关工作技能，及时发现设计工作中的问题，提出解决问题的途径；
    <br>
    <br>3.主动与业务部门保持沟通，根据业务需求分析系统要点及系统开发点；
    <br>
    <br>4.参与技术需求的调研，技术可行性分析，系统架构的设计、优化；
    <br>
    <br>5.完成模块详细设计与开发。
    <br>
</div>
'''

ret = re.sub('<.+?>', '', text)
print(ret)
ret2 = re.sub('\s', '', ret)
print(ret2)

text = 'Hello world. I love python'
ret = re.split(' ', text)
print(ret)
# 结果为['Hello', 'world.', 'I', 'love', 'python']
print('=' * 40)
ret = re.split('[^a-zA-Z]+', text)
print(ret)
# 在单词world后有两个非英文字符
# 结果为['Hello', 'world', 'I', 'love', 'python']

text = 'the number is 20.50, which is much larger than 0.01'
r = re.compile(r'''
                \d+  # 小数点前面数字
                \.?  # 小数点
                \d* # 小数点后面的数字
                ''', re.VERBOSE)
ret = re.findall(r, text)
print(ret)
# 结果为['20.50', '0.01']