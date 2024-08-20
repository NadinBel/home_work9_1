def apply_all_func(int_list, *functions):
    result = {}
    for i in (int_list):
        if isinstance(i, int|float):
            for func in functions:
                result[func.__name__] = func(int_list)
            return result
        else:
            print('Не числовое значение в списке')


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))