import random

# Створюємо клас гри
class TreasureHunt:
    def __init__(self, width, height, username):
        self.width = width
        self.height = height
        self.username = username
        self.treasure_x = random.randint(0, width-1)
        self.treasure_y = random.randint(0, height-1)

    def play(self):
        print(f"Вітаю, {self.username}! Вирушаємо на пошуки скарбів! Координати нашого скарбу - ({self.treasure_x}, {self.treasure_y})")
        attempts = 0
        while True:
            guess_x = int(input("Введіть координату x: "))
            guess_y = int(input("Введіть координату y: "))
            attempts += 1
            if guess_x == self.treasure_x and guess_y == self.treasure_y:
                print(f"Вітаю, ви знайшли скарб за {attempts} спроб!")
                break
            else:
                print("Ви не знайшли скарб, спробуйте знову")

# Створюємо меню вибору складності та нікнейму користувача
print("Вітаю в грі Пошук скарбів!")
username = input("Введіть ваш нікнейм: ")
difficulty = input("Оберіть складність (легкий, середній, складний): ")
if difficulty == "легкий":
    game = TreasureHunt(5, 5, username)
elif difficulty == "середній":
    game = TreasureHunt(10, 10, username)
elif difficulty == "складний":
    game = TreasureHunt(20, 20, username)
else:
    print("Невірна складність, гра завершена")
    exit()

game.play()