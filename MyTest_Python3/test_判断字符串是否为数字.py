# -*- coding: UTF-8 -*-

#判断是否为数字
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False

#bool->string
def boolToStr(m_bool):
    if m_bool:
        return '是'
    else:
        return '不是'

# 测试字符串和数字
print('foo' + boolToStr(is_number('foo')) + '数字')
print('1' + boolToStr(is_number('1')) + '数字')
print('1.3' + boolToStr(is_number('1.3')) + '数字')
print('-1.37' + boolToStr(is_number('-1.37')) + '数字')
print('1e3' + boolToStr(is_number('1e3')) + '数字')

# 测试 Unicode
# 阿拉伯语 5
print('٥' + boolToStr(is_number('٥')) + '数字')
# 泰语 2
print('๒' + boolToStr(is_number('๒')) + '数字')
# 汉语
print('四' + boolToStr(is_number('四')) + '数字')
# 版本号 ©
print('©' + boolToStr(is_number('©')) + '数字')


