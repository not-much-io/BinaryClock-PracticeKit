__author__ = 'kr'

from PyQt5 import QtWidgets, QtCore
from time_mechanism import TimeMechanism


class ClockDisplay():

    def __init__(self, parent_frame):
        self.clock_grid = QtWidgets.QGridLayout(parent_frame)
        self.clock_grid.setContentsMargins(0, 0, 0, 0)
        self.clock_grid.setObjectName("clock_grid")

        self._blocks = {}

        '''
        ----------------------------------------------------------------------------------------------------------------
        Fill out the clock_grid with widgets "named" block00 to block35, first digit is row and
        second column.
        ----------------------------------------------------------------------------------------------------------------
        Note: It is bad practice to program variable variable names (not a typo) with exec().
        ----------------------------------------------------------------------------------------------------------------
        Code to make a single block_object:

        block_object = QtWidgets.QWidget(parent_frame)
        block_object.setMaximumSize(QtCore.QSize(25, 25))
        block_object.setObjectName(block_name)
        ----------------------------------------------------------------------------------------------------------------
        Code to add widget to clock_grid:

        self.clock_grid.addWidget(block_object, row_nr, column_nr, 1, 1)
        '''
        #ToDo Fill clock grid with 24 correctly labeled blocks

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
        #ToDo Implement _set_block_state_in_grid
        raise NotImplementedError

    @staticmethod
    def _time_to_matrix(time):
        """Accepts a tuple representation of the current time and makes it into a matrix of ones and zeros that
        represent the values of the times DIGITS (so hour 22 is 0010(2) 0010(2)) in binary.

        :param time A representation of the current time. ex. 22:50:34 -> (22, 50, 34)
        :type time tuple
        :return A matrix of zeros and ones ex. ['0010', '0010', '0101', '0000', '0011', '0100']
        """
        #ToDo Implement _time_to_matrix
        raise NotImplementedError

    def update(self, time):
        """Will display the passed time argument in the display grid, unless alarm is on.

        :param time A tuple representation of some time
        :type time tuple
        """
        if not self.alarm_on:
            #The main logic behind the display.
            self._set_block_state_in_grid(self._time_to_matrix(time))