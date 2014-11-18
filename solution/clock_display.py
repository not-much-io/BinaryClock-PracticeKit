__author__ = 'kr'

from PyQt5 import QtWidgets, QtCore
from time_mechanism import TimeMechanism


class ClockDisplay():

    def __init__(self, parent_frame):
        self.clock_grid = QtWidgets.QGridLayout(parent_frame)
        self.clock_grid.setContentsMargins(0, 0, 0, 0)
        self.clock_grid.setObjectName("clock_grid")

        self._blocks = {}

        '''A matrix of blocks is created and stored in a dictionary. Named block00 to block35, first digit is row and
         second the column'''

        for row_nr in range(4):
            for column_nr in range(6):
                block_name = "block" + str(row_nr) + str(column_nr)
                block_object = QtWidgets.QWidget(parent_frame)

                block_object.setMaximumSize(QtCore.QSize(25, 25))
                block_object.setObjectName(block_name)

                self.clock_grid.addWidget(block_object, row_nr, column_nr, 1, 1)

                self._blocks[block_name] = block_object

        self.time_mechanism = TimeMechanism(self)
        self.alarm_on = False

    def _block_on(self, block_id):
        """Will "activate" a block.

        :param block_id ex. block on row 3, 4-th position -> "block23"
        :type block_id str
        """
        self._blocks[block_id].setStyleSheet("background: white")

    def _block_off(self, block_id):
        """Will "deactivate" a block.

        :param block_id ex. block on row 3, 4-th position -> "block23" -> bit 4 of minute ones
        :type block_id str
        """
        self._blocks[block_id].setStyleSheet("background: black")

    def _set_block_state_in_grid(self, matrix):
        """Accepts a 4 by 6 matrix of zeros and ones and sets the appropriate blocks on or off in clock grid.

        :param matrix ex. 22:50:34 -> ['0010', '0010', '0101', '0000', '0011', '0100']
        :type matrix list
        """
        for column in range(len(matrix)):
            for row in range(len(matrix[column])):
                block_id = "block" + str(row) + str(column)
                if matrix[column][row] == "1":
                    self._block_on(block_id)
                else:
                    self._block_off(block_id)

    @staticmethod
    def _time_to_matrix(time):
        """Accepts a tuple representation of the current time and makes it into a matrix of ones and zeros.

        :param time A representation of the current time. ex. 22:50:30 -> (22, 50, 30)
        :type time tuple
        :return A matrix of zeros and ones
        """
        divided_time = [int(time[0] / 10), time[0] % 10,
                        int(time[1] / 10), time[1] % 10,
                        int(time[2] / 10), time[2] % 10]
        matrix = []

        for i in range(6):
            matrix.append(str(bin(divided_time[i]))[2:].rjust(4, "0"))

        return matrix

    def update(self, time):
        """Will display the passed time argument in the display grid, unless alarm is on.

        :param time A tuple representation of some time
        :type time tuple
        """
        if not self.alarm_on:
            self._set_block_state_in_grid(self._time_to_matrix(time))