calls=0
def count_calls():
    global calls #
    calls += 1 #
def string_info(string):
        count_calls() #
        length = len(string) #
        upper_case = string.upper() #
        lower_case = string.lower() #
        return (length, upper_case, lower_case) #
def is_contains(string, list_to_search):
        count_calls() #
        string_lower = string.lower()
        return string_lower in (item.lower() for item in list_to_search) #

result1 = string_info ("Россия")
print(result1)
result2 = is_contains ("Мир", ["Труд", "Май", "Дружба"])
print(result2)
print("Результат функции string_info:", result1)
print("Результат функции is_contains:", result2)
print("Количество вызовов функций:", calls)
