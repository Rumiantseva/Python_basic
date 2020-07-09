def div(*args):
    try:
        arg1 = int(input("Введите числитель "))
        arg2 = int(input("Введите знаменатель "))
        res = arg1 / arg2
    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return "Указан неправитльный знаменатель. На ноль делить нельзя!"
    return res
    '''
    if arg2 != 0:
        return arg1 / arg2
    else:
        print("Указан неправитльный знаменатель. На ноль делить нельзя!")
    '''
print(f'result  {div()}')