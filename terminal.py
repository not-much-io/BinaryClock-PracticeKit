__author__ = 'kr'

from PyQt5 import QtWidgets, QtCore
from key_matrix import KeyMatrix


class Terminal(QtWidgets.QPlainTextEdit):

    def __init__(self, parent_frame, ref_to_time_mechanism):
        super(Terminal, self).__init__(parent_frame)

        self.setStyleSheet("background: #232a32")
        self.resize(170, 111)
        self.appendPlainText("$")

        self.cmd = ""
        self.previous_command = ""
        self.key_matrix = KeyMatrix(ref_to_time_mechanism)

    def t_print(self, text):
        """Prints text to terminal window"""
        self.insertPlainText(text)

    def keyPressEvent(self, QKeyEvent):
        """Overwritten keyPressEvent function to limit the input a user can enter."""
        if QKeyEvent.key() == QtCore.Qt.Key_Enter:
            self.appendHtml('<span style="color:{0}">->{1}</span>'.format(*self.send_cmd(self.cmd)))
            self.appendPlainText("$")
        elif QKeyEvent.key() == QtCore.Qt.Key_0:
            pass
        elif QKeyEvent.key() == QtCore.Qt.Key_1:
            pass
        elif QKeyEvent.key() == QtCore.Qt.Key_Backspace:
            pass
            #Currently cannot delete, might be difficult to do
        elif QKeyEvent.key() == QtCore.Qt.Key_Up:
            #Bring back previous command
            pass
        else:
            pass

    def send_cmd(self, cmd):
        """Passes the currently entered command to the key matrix and get the result.

        :return A color string and a integer showing either success or failure(0 or 1).
        :rtype tuple
        """
        self.previous_command = self.cmd
        self.cmd = ""
        try:
            self.key_matrix.pass_message(cmd)
            return "green", 0
        except KeyError:
            return "red", 1

    def mousePressEvent(self, evt):
        """Overwritten to minimize user interaction in the terminal."""
        pass

    def mouseDoubleClickEvent(self, evt):
        """Overwritten to minimize user interaction in the terminal."""
        pass

    def contextMenuEvent(self, evt):
        """Overwritten to minimize user interaction in the terminal."""
        pass
