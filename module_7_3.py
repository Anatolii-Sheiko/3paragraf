import io
# объявление класса WordsFinder
class WordsFinder:
    # объявление метода __init__ принимающая множество названий текстовых файлов
    def __init__(self, *file_txt):
        # объявление атрибута класса file_names
        self.file_names = file_txt
    # объявление подготовительного метода get_all_word, который возвращает
    # словарь all_words
    def get_all_words(self):
        # объявление словаря all_words
        all_words = {}
        # цикл перебора строк файла с открытием оператором with для чтения в
        # кодировке utf-8
        for i in self.file_names:
            with open(i, 'r', encoding='utf-8') as file:
                # перевод в нижний регистр стоки переменной file
                file = file.read().lower()
                # цикл перебора и поиска в текста указанных в [] знаков
                for j in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    # подмена найденных знаков на пустое значене (избавляемся от знаков) в строке
                    file = file.replace(j, '')
                # разбиение строки на элементы списка методом split()
                words = file.split()
                # присвоение словарю all_words ключу (i) значения списка слов (words)
                all_words[i] = words
        # возврат словаря метода get_all_words()
        return all_words

    # объявление метода find(self, word), где word - искомое слово. Возврат: ключ - название
    # файла, значение - позиция первого такого слова в списке слов этого файла
    def find(self, word):
        # объявление пустого словаря result
        result = {}
        # цикл перебора в файле (i) слов (word_) из словаря all_words из метода get_all_words
        for i, word_ in self.get_all_words().items():
            # цикл перебора (поиска) номера (j) слова (wd) из списка word_ начиная c 1
            for j, wd in enumerate(word_, 1):
                # условие сравнения слова (wd) и приведенного к нижнему регистру принятого
                # (искомого) слова (word)
                if wd == word.lower():
                    # присвоение переменной result[i] найденного номера
                    result[i] = j
                    # выход из условия при нахождении первого тождества
                    break
        # возврат метода find()
        return result

    # объявление метода count(self, word). Возвращает словарь, где ключ - название файла,
    # значение - количество слова word в списке слов этого файла
    def count(self, word):
        # объявление пустого словаря result_
        result_={}
        # цикл перебора в файле (i) слов (word_) из словаря all_words из метода get_all_words
        for i, word_ in self.get_all_words().items():
            # присвоение словарю result_[i] количества совпадений word_ в приведенном к
            # нижнему регистру искомого (принятого) слова word
            result_[i] = word_.count(word.lower())
        # возврат метода count()
        return result_

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
