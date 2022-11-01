# Чтение из файла

text = open('Words.txt', mode='r', buffering=-1, encoding=None,
            errors=None, newline=None, closefd=True, opener=None)
    #
    # -> https://docs-python.ru/tutorial/vstroennye-funktsii-interpretatora-python/funktsija-open/
    # :param file: абсолютное или относительное значение пути к файлу или файловый дескриптор открываемого файла.
    #               Параметр file есть обязательным в функции open(). Все другие параметры являются необязательными
    # :param mode: необязательно, строка, которая указывает режим, в котором открывается файл. По умолчанию 'r',
    #              это означает что файл открывается в текстовом режиме для чтения.
    # :param buffering: необязательно, целое число, используемое для установки политики буферизации.
    #                   Понятие «буферизация» означает, что при чтении (записи) информации из файла (в файл) эта информация
    #                   предварительно записывается в специальный участок памяти – буфер (buffer).
    #                   Таким образом, информация дублируется в буфере заданного размера.
    #                   Правильно подобранное значение размера буфера позволяет ускорить выполнение программы,
    #                   которая интенсивно использует работу с файлами.
    # :param encoding: необязательно, кодировка, используемая для декодирования или кодирования файла
    # :param errors: необязательно, строка, которая указывает, как должны обрабатываться ошибки кодирования и декодирования.
    #                 Не используется в -бинарном режиме
    # :param newline: необязательно, режим перевода строк. Варианты: None, '\n', '\r' и '\r\n'.
    #                 Следует использовать только для текстовых файлов
    # :param closefd: необязательно, bool, флаг закрытия файлового дескриптора.
    # :param opener: необязательно, пользовательский объект, возвращающий открытый дескриптор файла.
    # :return: файловый объект (поток).
print(type(text)) # io.TextIOWrapper() - буферизованный текстовый поток
text.close() # Закрывает открытый файл, освобождая ресурсы системы
             # Важно! Все открытые файлы нужно обязательно закрывать, т. к. из за незакрытых файлов
             # может произойти превышение лимита открытых дескрипторов в системе, что может повлечь сбой системы.

text = open('Words.txt') # Открытие файла с параметрами по умолчанию (для чтения)
print(text)

print(text.read()) # Считывает все содержимое файла как одну строку
print('Текущая позиция курсора:', text.tell()) # Возвращает текущую позицию курсора (указателя) в файле в (байтах!)

text.seek(0) # Устанавливает курсор в начало файла
print('Текущая позиция курсора:', text.tell()) # Возвращает текущую позицию курсора (указателя) в файле в (байтах!)

print(text.readline()) # Считывает только одну строку из файла и возвращает ее
text.seek(0) # Устанавливает курсор на начало файла

print(text.readlines()) # Возвращает все строки в файле в виде списка
text.seek(0) # Устанавливает курсор на начало файла

word_list = text.read().splitlines() # возвращает список строк, текста str, разделенного по универсальным разрывам строк.
print(word_list)

word_list = [i.upper() for i in word_list] # Перевод всех слов из списка в верхний регистр
print(word_list)

text.close() # Закрываем файл

print(text.closed) # Проверяем закрыт ли файл

# Альтернативный способ открытия файла через контекстный менеджер

with open('Words.txt') as text: # по смыслу аналогично text = open('Words.txt')
    word_list = text.read().splitlines()
    word_list = [i.upper() for i in word_list]
# После выполнения кода в теле конструкции with - файл закрывается автоматически!

print(word_list)

# Запись в файл

new_text = open("new_text.txt", mode='w') # Режим доступа 'w' - Открывает файл только для записи.
                                          # Перезаписывает файл, если файл существует.
                                          # Если файл не существует, создает новый файл для записи.
new_text.write('New_line_1') # Записывает переданную строку в файл
new_text.write('New_line_2') # Записывает переданную строку в файл
new_text.write('New_line_3') # Записывает переданную строку в файл

new_text.writelines(word_list) # Записывает список строк в файл

new_text.close()

new_text = open("new_text.txt", mode='a') # Режим доступа 'a' - Открывает файл для ДОЗАПИСИ.
                                          # Указатель файла находится в конце файла, если файл существует.
                                          # То есть файл находится в режиме добавления.
                                          # Если файл не существует, он создает новый файл для записи.
new_text.write('New_line_MOD_"a"')

new_text.close()

# Смешанные режимы для чтения и записи файла одновременно

# Режим доступа 'r+'
new_text = open("new_text.txt", mode='r+') # 'r+' - Открывает файл для чтения и записи.
                                           # Указатель файла помещается в начало файла.
new_text.write('WRITE_MOD_"r+"')

new_text.close()

# Режим доступа 'w+'
new_text = open("new_text.txt", mode='w+') # 'w+' - Открывает файл для чтения и записи.
                                           # Перезаписывает существующий файл, если файл существует.
                                           # Если файл не существует, создается новый файл для чтения и записи.
                                           # -> Стирает всю информацию из файла в случае записи
new_text.write('WRITE_MOD_"w+"')
new_text.close()

# Режим доступа 'a+'
new_text = open("new_text.txt", mode='a+') # 'a+' - Открывает файл для добавления и чтения.
                                           # Указатель файла находится в конце файла, если файл существует.
                                           # Файл открывается в режиме добавления.
                                           # Если файл не существует, он создает новый файл для чтения и записи.
new_text.write('WRITE_MOD_"a+"')
new_text.close()
