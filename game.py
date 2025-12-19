import os
from maze import (
Maze
)
from out import (
Exit
)


class Menu:
    """Класс взаимодействия пользователя с лабиринтом."""

    __maze = []
    choice = ""
    matrix = Maze(5, 5)
    y = 0
    x = 0

    def generate_matrix(self) -> None:
        """Метод запуска генерации лабиринта."""

        self.matrix.generate()
        self.matrix.custom()
        self.__maze = self.matrix.get_matrix()

    def localised(self) -> None:
        """Метод определения координат входа."""

        matrix = self.__maze

        for y in range(len(matrix)):
            if 2 in matrix[y]:
                x = matrix[y].index(2)
                self.x = x
                self.y = y


    def set_choice_menu(self) -> None:
        """Метод вывода пользовательского меню и выбора действия."""

        while self.choice != "EXIT":

            if  3 not in self.__maze[-1]:
                os.system('cls')
                
                print("Победа!!!!!")
                outer = Exit(self.__maze)
                outer.printer()
                break

            print("\nU - вверх\n"
                  "D - вниз\n"
                  "L - влево\n"
                  "R - вправо\n"
                  "EXIT - выход из игры\n"
                  )

            self.choice = input("Выбор: ")
            

            if self.choice == "U" and self.y > 0 and self.__maze[self.y - 1][self.x] != 1:
                self.__maze[self.y][self.x] = 0
                self.y -= 1
                self.__maze[self.y][self.x] = 2
                os.system('cls')

            elif self.choice == "D" and self.y < (len(self.__maze) - 1) and self.__maze[self.y + 1][self.x] != 1:
                self.__maze[self.y][self.x] = 0
                self.y += 1
                self.__maze[self.y][self.x] = 2
                os.system('cls')

            elif self.choice == "L" and self.x > 0 and self.__maze[self.y][self.x - 1] != 1:
                self.__maze[self.y][self.x] = 0
                self.x -= 1
                self.__maze[self.y][self.x] = 2
                os.system('cls')

            elif self.choice == "R" and self.x < (len(self.__maze) - 1) and (self.__maze[self.y][self.x + 1] != 1):
                self.__maze[self.y][self.x] = 0
                self.x += 1
                self.__maze[self.y][self.x] = 2
                os.system('cls')

            elif self.choice == "EXIT":
                outer = Exit(self.__maze)
                outer.printer()
                print("а был не так далеко)")

            outer = Exit(self.__maze)
            outer.now_printer()

    def choice_level(self) -> None:
        """Метод выбора уровня сложности."""

        print("Выберите уровень от 1 до 5\n")

        level = int(input("Уровень: "))

        size = 5

        match level:
            case 1:
                size = 7
            case 2:
                size = 9
            case 3:
                size = 11
            case 4:
                size = 13
            case 5:
                size = 15


        self.matrix = Maze(size, size)


a = Menu()
a.choice_level()
a.generate_matrix()
a.localised()
a.set_choice_menu()
