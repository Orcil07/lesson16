def print_params(a = 2, b = 'строка', c = True):
    print(a, b, c)


print_params(5, 'строка')
print_params( 7,None, False)
print_params(14)
print_params()


print_params(b=25)
print('print_params(b=25)')
print_params(c = [1,2,3])
print('print_params(c = [1,2,3])')


values_list = [745, None, 'Рожон']
values_dict = {'a':1256.2547, 'b':"Ляпсус", 'c':False}

print_params(*values_list)
print_params(**values_dict)


values_list_2 = ['Харчевня', 3]

print_params(*values_list_2, 42)
print('print_params(*values_list_2, 42)')

