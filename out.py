class Exit:
    """Класс для визуального изображения лабиринта."""

    def __init__(self, matrix: list) -> None:
        """Конструктор класса Exit.
        Arg:
            matrix: лабиринт в виде матрицы.
        """

        self.matrix = matrix

    def printer(self) -> None:
        """Метод для вывода структуры лабиринта."""

        full_picture = []

        for i in self.matrix:
            picture = ""

            for j in i:

                if j == 0:
                    picture += "🟩"
                elif j == 2:
                    picture += "🚶"
                elif j == 3:
                    picture += "🚩"
                else:
                    picture += "🟦"

            full_picture.append(picture)


        for i in full_picture:
            print(i)

    def now_printer(self) -> None:
        """Метод для вывода текущего состояния лабиринта."""

        full_picture = []

        for i in self.matrix:
            picture = ""

            for j in i:

                if j == 10:
                    picture += "🟩"
                elif j == 2:
                    picture += "🚶"
                elif j == 3:
                    picture += "🚩"
                else:
                    picture += "⬜"

            full_picture.append(picture)

        for i in full_picture:
            print(i)

