__version__ = 'V2.0'

import os, random, time
from argparse import ArgumentParser, RawTextHelpFormatter

argparser = ArgumentParser(description=f'''
Программа, переименовывающая фотки,
описания или любые другие файлы
однотипных товаров в пределах папки.

Автор: Платон Быкадоров (platon.work@gmail.com), 2020
Версия: {__version__}
Лицензия: GNU General Public License version 3
Поддержать проект: https://money.yandex.ru/to/41001832285976
Багрепорты/пожелания/общение: https://github.com/PlatonB/business-python-scripts/issues

Вернуть изначальные имена будет нельзя!

Условные обозначения в справке по CLI:
- краткая форма с большой буквы - обязательный аргумент;
- в квадратных скобках - значение по умолчанию;
- в фигурных скобках - перечисление возможных значений.
''',
                           formatter_class=RawTextHelpFormatter)
argparser.add_argument('-S', '--src-dir-path', metavar='str', dest='src_dir_path', type=str,
                       help='Путь к папке с исходными файлами')
argparser.add_argument('-t', '--trg-dir-path', metavar='[None]', dest='trg_dir_path', type=str,
                       help='Путь к папке для переименованных файлов (по умолчанию - путь к исходной папке)')
argparser.add_argument('-1', '--first-const-part', metavar='[None]', dest='first_const_part', type=str,
                       help='Одинаковая для всех файлов начальная часть имени (перед опциональной датой переименования)')
argparser.add_argument('-d', '--cur-date', dest='cur_date', action='store_true',
                       help='Вписывать в имена файлов дату переименования')
argparser.add_argument('-2', '--second-const-part', metavar='[None]', dest='second_const_part', type=str,
                       help='Одинаковая для всех файлов серединная часть имени (между опциональной датой переименования и артикулом)')
argparser.add_argument('-a', '--art-digits-quan', metavar='[8]', default=8, dest='art_digits_quan', type=int,
                       help='Количество цифр случайных артикулов')
argparser.add_argument('-3', '--third-const-part', metavar='[None]', dest='third_const_part', type=str,
                       help='Одинаковая для всех файлов завершающая часть имени (между артикулом и расширением)')
args = argparser.parse_args()

if args.trg_dir_path is None:
        trg_dir_path = os.path.normpath(args.src_dir_path)
else:
        trg_dir_path = os.path.normpath(args.trg_dir_path)
        
minimum = 10 ** (args.art_digits_quan - 1)
maximum = 10 ** args.art_digits_quan - 1

print(f'\nПереименование файлов папки {os.path.basename(args.src_dir_path)}\n')

for src_file_name in os.listdir(args.src_dir_path):
        trg_file_draft = [str(random.randint(minimum, maximum))]
        if args.cur_date:
                trg_file_draft.insert(0, '_'.join(map(str, time.localtime()[:3])))
        if args.first_const_part != None:
                trg_file_draft.insert(0, args.first_const_part)
        if args.second_const_part != None:
                trg_file_draft.insert(-1, args.second_const_part)
        if args.third_const_part != None:
                trg_file_draft.append(args.third_const_part)
        src_file_ext = src_file_name.split('.')[-1]
        src_file_path = os.path.join(args.src_dir_path, src_file_name)
        trg_file_name = '_'.join(trg_file_draft) + f'.{src_file_ext}'
        trg_file_path = os.path.join(trg_dir_path, trg_file_name)
        os.rename(src_file_path, trg_file_path)
