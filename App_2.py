# В большой текстовой строке подсчитать количество встречаемых слов и вернуть
# 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.

def get_popular_words(text, top_n=10):
    """Function finds popular words"""
    cleaned_text = ''.join(char.lower()
                           if char.isalpha() or char.isspace()
                           else ' ' for char in text)

    words = cleaned_text.split()

    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    popular_words = sorted(word_counts.items(),
                           key=lambda x: x[1],
                           reverse=True)[:top_n]

    return popular_words


def print_words(most_common_words):
    """Function prints words"""
    print("Вывод:")
    for word, count in most_common_words:
        print(f'Слово "{word}", {count} раз')


text = "Буэ́нос-А́йрес (исп. Buenos Aires, букв. «хороший воздух» или \
    «добрые ветра»; ['bwenos 'ai̯ɾes]) — город, столица Аргентины, \
    административный, культурный и экономический центр страны \
    и один из крупнейших городов Южной Америки. \
    Буэнос-Айрес расположен в центрально-восточной части страны, \
    на западном берегу крупнейшего залива-эстуария Рио-де-ла-Плата, \
    являющегося продолжением устья второй по длине реки Южной Америки — \
    Параны́. Своё современное укороченное название — «Буэнос-Айрес» город \
    носит с XVII века. До этого город официально именовался следующим полным \
    именем: исп. Ciudad de la Santísima Trinidad y Puerto de Nuestra Señora \
    de Santa María de los Buenos Aires, букв. \
    «Город Пресвятой Троицы и Порт Богородицы Святой Марии Добрых Ветров»."
top_10_words = get_popular_words(text, top_n=10)
print_words(top_10_words)
