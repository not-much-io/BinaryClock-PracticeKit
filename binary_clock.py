__author__ = 'kr'

from PyQt5 import QtWidgets
from main_window import UIMainWindow


def main():
    """Runs the program"""
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UIMainWindow(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()