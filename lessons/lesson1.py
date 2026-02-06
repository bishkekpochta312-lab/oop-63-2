class Hero:

    # Конструктор класса
    def __init__(self, nick, hp, lvl):
        # Атрибуты класса
        self.nick = nick
        self.hero = hp
        self.lvl = lvl

    # методы класса
    def action(self):
        return f"{self.nick} base action activate!!"

# Объект/Экземпляр класса
kirito = Hero("Kirito", 1000, 100)
asuna = Hero("Asuna", 1100, 101)
my_int = 123
# my_int.
my_str = "123"
# my_str.
print(type(my_int))
print(type(kirito))

# print(kirito.action())
# print(asuna.action())

# def some():
#     pass