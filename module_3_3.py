from mobule_2_4 import primts


def print_params (a = 1, b = "строка", c = True):
    print(a, b, c)
print_params ()
print_params (7, 'абзац', False)
print_params (544, "Рука")
print_params (b="Озеро")
print_params (b= 25)
print_params (c = [1, 2, 3])

values_list = [458 , 'вода', False]
values_dict = {"a": 500, 'b': 'стол', 'c': True}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)





