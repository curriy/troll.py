import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import webbrowser


def button1_press():
    webbrowser.open_new('https://store.steampowered.com/app/570/Dota_2/')

def application():
    app = QApplication(sys.argv)
    window = QMainWindow()

    window.setWindowTitle('init')
    window.setGeometry(300, 250, 250, 120)

    text = QtWidgets.QLabel(window)
    text.setText('Мать жива?')
    text.setStyleSheet("""
            QLabel {color: gray}
        """)
    text.move(100, 10)
    text.adjustSize()

    button1 = QtWidgets.QPushButton(window)
    button1.move(80, 30)
    button1.setText('Нет')
    button1.adjustSize()
    button1.clicked.connect(button1_press)
    button1.setStyleSheet("""
            QPushButton:hover { background-color: gray }
            QPushButton:!hover { background-color: white }
            QPushButton:pressed { background-color: black }
            QPushButton:pressed { color: white }
        """)

    button2 = QtWidgets.QPushButton(window)
    button2.move(80, 70)
    button2.setText('Да')
    button2.adjustSize()
    button2.setStyleSheet("""
        QPushButton:hover { background-color: gray }
        QPushButton:!hover { background-color: white }
        QPushButton:pressed { background-color: black }
        QPushButton:pressed { color: white }
    """)

    window.show()
    sys.exit(app.exec_())

    
if __name__ == '__main__':
    application()
