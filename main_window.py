from PyQt5 import QtCore, QtWidgets
from clock_display import ClockDisplay
from terminal import Terminal


class UIMainWindow():

    def __init__(self, MainWindow):

        #Create main window
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 130)
        MainWindow.setWindowTitle("Programmable Binary Clock")
        MainWindow.setStyleSheet("background: #25262a")

        #Create central main frame
        self.central_frame = QtWidgets.QWidget(MainWindow)
        self.central_frame.setObjectName("centralwidget")

        #Create right frame for clock display
        self.right_frame = QtWidgets.QWidget(self.central_frame)
        self.right_frame.setGeometry(QtCore.QRect(10, 10, 171, 111))
        self.right_frame.setObjectName("right_frame")

        #Create clock display, placing it inside right_frame
        self.clock_display = ClockDisplay(self.right_frame)

        #Create left frame for terminal
        self.left_frame = QtWidgets.QWidget(self.central_frame)
        self.left_frame.setGeometry(QtCore.QRect(215, 10, 171, 111))
        self.left_frame.setObjectName("left_frame")

        #Create terminal, placing it inside left_frame and passing it a reference to the clock displays time mechanism
        self.terminal = Terminal(self.left_frame, self.clock_display.time_mechanism)

        MainWindow.setCentralWidget(self.central_frame)

        #Create separator line
        self.line = QtWidgets.QFrame(self.central_frame)
        self.line.setGeometry(QtCore.QRect(189, 10, 21, 111))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

