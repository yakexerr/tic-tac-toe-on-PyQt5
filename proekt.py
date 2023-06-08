import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication


class MyWidget(QMainWindow):
    """ главное окно"""

    def __init__(self):
        super().__init__()
        uic.loadUi('mainWin.ui', self)

        # нужные переменные
        self.buttons = [self.btn_1, self.btn_2, self.btn_3, self.btn_4, self.btn_5, self.btn_6, self.btn_7, self.btn_8,
                        self.btn_9]
        self.x_turn = False
        self.current_motion = 0
        self.field = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.count_btn = 0

        # начало игры при нажатии старта
        self.start_btn.clicked.connect(self.start_game)

        # todo оптимизировать активацию кнопок поля

        self.btn_1.clicked.connect(lambda: self.btn_realize(self.btn_1, 0))
        self.btn_2.clicked.connect(lambda: self.btn_realize(self.btn_2, 1))
        self.btn_3.clicked.connect(lambda: self.btn_realize(self.btn_3, 2))
        self.btn_4.clicked.connect(lambda: self.btn_realize(self.btn_4, 3))
        self.btn_5.clicked.connect(lambda: self.btn_realize(self.btn_5, 4))
        self.btn_6.clicked.connect(lambda: self.btn_realize(self.btn_6, 5))
        self.btn_7.clicked.connect(lambda: self.btn_realize(self.btn_7, 6))
        self.btn_8.clicked.connect(lambda: self.btn_realize(self.btn_8, 7))
        self.btn_9.clicked.connect(lambda: self.btn_realize(self.btn_9, 8))

    def win_check(self, field, sign):
        """ чек победу"""

        # перебор всевозможных вариантов победы
        if field[0] == field[1] == field[2] == sign or field[3] == field[4] == field[5] == sign or field[6] == field[
            7] == \
                field[8] == sign or field[0] == field[3] == field[6] == sign or field[1] == field[4] == field[
            7] == sign or \
                field[2] == field[5] == field[8] == sign or field[0] == field[4] == field[8] == sign or field[2] == \
                field[
                    4] == field[6] == sign:
            return True
        else:
            return False

    def btn_realize(self, btn, cur_mot):
        """нажатие на кнопку"""
        if self.count_btn != 8:
            self.count_btn += 1
            self.x_turn = not self.x_turn
            if self.x_turn:
                btn.setText('X')
            else:
                btn.setText('O')

            # связь с хранением промежуточной таблицы
            self.current_motion = cur_mot
            if self.x_turn:
                self.field[self.current_motion] = 'X'
            else:
                self.field[self.current_motion] = 'O'
            if self.win_check(self.field, 'X'):
                self.res_txt.setText('Победил Х')
            elif self.win_check(self.field, 'O'):
                self.res_txt.setText('Победил O')
        else:
            if self.x_turn:
                btn.setText('O')
            else:
                btn.setText('X')
            self.res_txt.setText('ничья')

    def start_game(self):
        """функция начала игры"""

        self.res_txt.setText(' ')
        self.count_btn = 0

        # очистка поля внутри окна
        self.x_turn = False
        for btn in self.buttons:
            btn.setText('')

        # сброс памяти поля
        self.field = [" ", " ", " ", " ", " ", " ", " ", " ", " "]


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())