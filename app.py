import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QTabWidget, QWidget,
                               QVBoxLayout, QHBoxLayout, QLabel, QTextEdit,
                               QPushButton, QSpinBox, QLineEdit)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

# Импортируем классы заданий
from tasks.task1 import Task1
from tasks.task2 import Task2
from tasks.task3 import Task3

STEP = 0.01

class Task1Tab(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        title = QLabel("f(x) = 0.5x - 2")
        title_font = QFont()
        title_font.setPointSize(12)
        title_font.setBold(True)
        title.setFont(title_font)
        layout.addWidget(title)

        # Параметры
        params_layout = QVBoxLayout()
        label_font = QFont()
        label_font.setPointSize(10)

        # Начало
        start_layout = QHBoxLayout()
        start_label = QLabel("Начало:")
        start_label.setFont(label_font)
        start_layout.addWidget(start_label)
        self.start_TextBox = QLineEdit()
        self.start_TextBox.setText("0")
        start_layout.addWidget(self.start_TextBox)
        params_layout.addLayout(start_layout)

        # Конец
        end_layout = QHBoxLayout()
        end_label = QLabel("Конец:")
        end_label.setFont(label_font)
        end_layout.addWidget(end_label)
        self.end_TextBox = QLineEdit()
        self.end_TextBox.setText("100")
        end_layout.addWidget(self.end_TextBox)
        params_layout.addLayout(end_layout)

        # Количество
        count_layout = QHBoxLayout()
        count_label = QLabel("Количество:")
        count_label.setFont(label_font)
        count_layout.addWidget(count_label)
        self.n_TextBox = QLineEdit()
        self.n_TextBox.setText("50")
        count_layout.addWidget(self.n_TextBox)
        params_layout.addLayout(count_layout)

        layout.addLayout(params_layout)

        # Кнопка выполнения
        self.calculate_btn = QPushButton("Вычислить")
        self.calculate_btn.clicked.connect(self.calculate_values)
        layout.addWidget(self.calculate_btn)

        # Поле для вывода результатов
        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)
        layout.addWidget(self.result_text)

        self.setLayout(layout)

    def calculate_values(self):
        try:
            start = float(self.start_TextBox.text())
            end = float(self.end_TextBox.text())
            n = int(self.n_TextBox.text())

            task = Task1(start, end, n)
            values = task.get_values()

            result_str = ""
            x = start
            for i, val in enumerate(values):
                result_str += f"{i + 1}. x = {x:.2f}, f(x) = {val:.4f}\n"
                x += STEP

            self.result_text.setText(result_str)
        except Exception as e:
            self.result_text.setText(f"Ошибка: {str(e)}")

class Task2Tab(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Заголовок с увеличенным шрифтом
        title = QLabel("Проверка треугольников")
        title_font = QFont()
        title_font.setPointSize(12)
        title_font.setBold(True)
        title.setFont(title_font)
        layout.addWidget(title)
        label_font = QFont()
        label_font.setPointSize(10)

        # Параметры
        params_layout = QVBoxLayout()
        label_diap = QLabel("Диапазон длин сторон треугольников")
        params_layout.addWidget(label_diap)
        # начальное значение диапазона
        min_layout = QHBoxLayout()
        min_label = QLabel("Начало диапазона")
        min_label.setFont(label_font)
        min_layout.addWidget(min_label)
        self.start_spin = QLineEdit()
        self.start_spin.setText("2")
        min_layout.addWidget(self.start_spin)
        params_layout.addLayout(min_layout)

        # Конечное значение диапазона
        max_layout = QHBoxLayout()
        max_label = QLabel("Конец диапазона:")
        max_label.setFont(label_font)
        max_layout.addWidget(max_label)
        self.end_spin = QLineEdit()
        self.end_spin.setText("20")
        max_layout.addWidget(self.end_spin)
        params_layout.addLayout(max_layout)

        # Количество комбинаций
        count_layout = QHBoxLayout()
        count_label = QLabel("Количество:")
        count_label.setFont(label_font)
        count_layout.addWidget(count_label)
        self.n_spin = QLineEdit()
        self.n_spin.setText("20")
        count_layout.addWidget(self.n_spin)
        params_layout.addLayout(count_layout)

        layout.addLayout(params_layout)

        # Кнопка выполнения
        self.calculate_btn = QPushButton("Проверить")
        self.calculate_btn.clicked.connect(self.check_triangles)
        layout.addWidget(self.calculate_btn)

        # вывод результатов
        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)
        layout.addWidget(self.result_text)

        self.setLayout(layout)

    def check_triangles(self):
        try:
            start = int(self.start_spin.text())
            end = int(self.end_spin.text())
            n = int(self.n_spin.text())

            task2 = Task2(start, end + 1, n)
            results = task2.get_values()

            # вывод
            output = ""
            for i, (sides, is_triangle) in enumerate(results, 1):
                a, b, c = sides
                txt = "Да" if is_triangle else "Нет"
                output += f"{i}. Стороны: ({a}, {b}, {c}) Образуют треугольник: {txt}\n"

            self.result_text.setText(output)


        except Exception as e:
            self.result_text.setText(f"Ошибка: {str(e)}")


class Task3Tab(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Заголовок
        title = QLabel("Нахождение 4 наибольших чисел")
        title_font = QFont()
        title_font.setPointSize(12)
        title_font.setBold(True)
        title.setFont(title_font)
        layout.addWidget(title)
        label_font = QFont()
        label_font.setPointSize(10)

        # Ввод чисел
        input_layout = QVBoxLayout()
        input_label = QLabel("Введите числа через пробел:")
        input_label.setFont(label_font)
        input_layout.addWidget(input_label)
        self.numbers_input = QLineEdit()
        input_layout.addWidget(self.numbers_input)
        layout.addLayout(input_layout)
        label_cnt = QLabel("Введите искомое количество максимальных значений")
        label_cnt.setFont(label_font)
        input_layout.addWidget(label_cnt)
        self.cnt = QLineEdit()
        self.cnt.setText("4")
        input_layout.addWidget(self.cnt)
        # Кнопка выполнения
        self.calculate_btn = QPushButton("Найти")
        self.calculate_btn.clicked.connect(self.find_max_numbers)
        layout.addWidget(self.calculate_btn)

        # Поле для вывода результатов
        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)
        layout.addWidget(self.result_text)

        self.setLayout(layout)
    # нахождение наибольшиз чисел
    def find_max_numbers(self):
        try:
            input_text = self.numbers_input.text().strip()
            if not input_text:
                self.result_text.setText("Введите числа!")
                return
            n = int(self.cnt.text())
            task3 = Task3(input_text, n)
            result = task3.write_max()

            result_text = f"4 наибольших: {result}"
            self.result_text.setText(result_text)
        except Exception as e:
            self.result_text.setText(f"Ошибка: проверьте ввод")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(450, 150, 250, 400)

        tab_widget = QTabWidget()

        task1_tab = Task1Tab()
        task2_tab = Task2Tab()
        task3_tab = Task3Tab()

        tab_widget.addTab(task1_tab, "Задание 1")
        tab_widget.addTab(task2_tab, "Задание 2")
        tab_widget.addTab(task3_tab, "Задание 3")

        self.setCentralWidget(tab_widget)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()