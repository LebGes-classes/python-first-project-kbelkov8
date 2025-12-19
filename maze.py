from random import *


class Maze:
    """Класс генерации лабиринта."""
    __matrix = []
    enter = 0
    out = 0

    def __init__(self, length, height) -> None:
        """Конструктор класса Maze.
        Args:
            length: длина строки лабиринта.
            height: высота лабиринта.
        """

        self.length = length
        self.height = height

    def generate(self) -> None:
        """Метод генерации исходной матрицы."""

        matrix = [[1 for i in range(self.length)] for j in range(self.height)]

        enter = randint(1, self.length - 2)
        matrix[0][enter] = 0

        self.enter = enter
        self.__matrix = matrix

    def custom(self) -> None:
        """Метод преобразования матрицы в лабиринт с проходами."""

        x = self.__matrix[0].index(0)

        stroka = 0

        while stroka < (self.height - 1):

            choise = choice([1, -1, 2, -2]) # 1 - up, -1 - down, 2 - left, -2 - right

            if choise == 1 and stroka > 2:
                stroka -= 1
                self.__matrix[stroka][x] = 0
            elif choise == -1 and stroka < (self.height - 1):
                stroka += 1
                self.__matrix[stroka][x] = 0
            elif choise == 2 and x > 0:
                x -= 1
                self.__matrix[stroka][x] = 0
            elif choise == -2 and x < (self.length - 1):
                x += 1
                self.__matrix[stroka][x] = 0
            else:
                continue
        
        self.out = self.__matrix[-1].index(0)
        self.__matrix[0][self.enter] = 2
        self.__matrix[-1][self.out] = 3

    def get_enter(self) -> int:
        """Метод получения координаты входа."""

        return self.enter

    def get_matrix(self) -> list:
        """Метод для возврата лабиринта."""

        return self.__matrix

