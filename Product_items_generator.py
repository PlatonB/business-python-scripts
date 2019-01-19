print('''
Python3-скрипт, генерирующий случайные артикулы товаров.
Автор: Платон Быкадоров (platon.work@gmail.com), 2019.
Версия: V1.0.
Лицензия: GNU General Public License version 3.
Поддержать проект: https://money.yandex.ru/to/41001832285976

Простое руководство по установке среды разработки и запуску скриптов:
github.com/PlatonB/bioinformatic-python-scripts#Установка-среды-разработки

Пример полученных результатов:
арт50131175
арт46620375
арт55406092
арт42913551
арт74214404
''')

def item_settings():
        str_before = input('''\nНабор символов перед числовой частью артикулов
(игнорирование ввода ==> в артикулах будет только числовая часть)
[<enter>|арт|код товара: |ID|...]:''')
        
        quan_of_digits = int(input('\nСколько цифр должно быть в числовой части артикулов? '))
        minimum = int('1' + '0' * (quan_of_digits - 1))
        maximum = int('9' * quan_of_digits)
        
        quan_of_items = int(input('\nКоличество генерируемых артикулов: '))
        
        return str_before, minimum, maximum, quan_of_items

####################################################################################################

import sys, os, random

trg_dir_path = input('\nПуть к папке для конечных файлов: ')

quan_of_catalogs = input('''\nДля скольких каталогов товаров генерировать артикулы?
(игнорирование ввода ==> для одного)
[1(|<enter>)|2|3|...]: ''')
if quan_of_catalogs == '':
        quan_of_catalogs = 1
else:
        quan_of_catalogs = int(quan_of_catalogs)
if quan_of_catalogs < 1:
        print(f'{quan_of_catalogs} - недопустимая опция')
        sys.exit()
        
elif quan_of_catalogs > 1:
        diff_settings = input('''\nРазные каталоги - разные параметры артикула?
(игнорирование ввода ==> одинаковые параметры для всех каталогов)
[yes(|y)|no(|n|<enter>):''')
        if diff_settings != 'yes' and diff_settings != 'y' and diff_settings != 'no' \
           and diff_settings != 'n' and diff_settings != '':
                print(f'{diff_settings} - недопустимая опция')
                sys.exit()
                
#Цикл, количество итераций которого
#зависит от того, для скольких каталогов
#пользователь решил создавать артикулы.
for catalog_num in range(quan_of_catalogs):
        
        ##Запрос(-ы) параметров артикула для нескольких каталогов.
        try:
                
                #Если пользователь хочет задать обособленные настройки для
                #артикулов каждого каталога товаров, то соответствующий диалог будет
                #появляться столько же раз, сколько предполагается быть каталогов.
                if diff_settings == 'yes' or diff_settings == 'y':
                        print(f'\n\nНастройки артикулов каталога {catalog_num + 1}')
                        str_before, minimum, maximum, quan_of_items = item_settings()
                        
                #Если пользователь предпочёл применить одни и те же настройки
                #артикулов для всех каталогов, то диалог, в котором
                #будут запрошены эти настройки, появится только единожды.
                else:
                        if 'str_before' not in locals():
                                str_before, minimum, maximum, quan_of_items = item_settings()
                                
        ##Запрос параметров артикула для единственного каталога.
        except NameError:
                str_before, minimum, maximum, quan_of_items = item_settings()
                
        ##Работа с конечным файлом и, собственно, генерация артикулов.
        trg_file_name = f'Catalog_{catalog_num + 1}_product_items.tsv'
        with open(os.path.join(trg_dir_path, trg_file_name), 'w') as trg_file_opened:
                
                #Генерация того количества артикулов, что задал пользователь.
                #Прописывание результатов в конечный файл.
                for item_num in range(quan_of_items):
                        trg_file_opened.write(str_before + str(random.randint(minimum, maximum)) + '\n')
