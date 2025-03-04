def calc(str):
    if '+' in str:
        a = int(str.split('+')[0])
        b = int(str.split('+')[1])
        return a+b
    if '-' in str:
        a = int(str.split('-')[0])
        b = int(str.split('-')[1])
        return a-b
    if '*' in str:
        a = int(str.split('*')[0])
        b = int(str.split('*')[1])
        return a*b
    if '/' in str:
        a = int(str.split('/')[0])
        b = int(str.split('/')[1])
        if b == 0:
            return 'Вы не можете делить на ноль'
        return a/b
    return 'Вы ввели неправильные данные'