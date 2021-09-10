"""
Написать функцию revert_rows, которая принимает путь к файлу и делает новый
файл. Создать новый файл, каждая строка которого получается из соответствующей
строки исходного файла перестановкой слов в обратном порядке.
"""


def revert_rows(path):
    f = open(path, 'r')
    nf = open('new_text.txt', 'a')
    for line in f:
        line_list = line.split()
        x = line_list[::-1]
        nf.write(' '.join(x) + '\n')
    f.close()
    nf.close()


if __name__ == '__main__':
    revert_rows('text.txt')
