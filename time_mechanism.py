__author__ = 'kr'

from PyQt5 import QtCore
from datetime import datetime, timedelta


class TimeMechanism():

    def __init__(self, display):
        self.display = display
        self.timer = QtCore.QTimer(display.clock_grid)
        self.timer.timeout.connect(self._tick)
        self.timer.start(1000)

        #Decides what is being shown on the display
        self.mode = "clock"

        self.time_adjustment = 0
        self.timer_on = False
        self.timer_time = 0
        self.stopper_on = False
        self.stopper_time = 0
        self.alarm_time = None
        self.alarm_twinkle = True

    def _tick(self):
        """Is called every second to update the display accordingly."""
        #Main Logic
        self.display.update(self._get_time())

    def _get_time(self):
        """Return the time to be currently displayed in the clock display, dependent on the current mode.

         :return A tuple representation of time
         :rtype tuple
        """
        #ToDo Implement get_time
        #Keep these running if they are on independent of what mode is on (what is being displayed)
        if self.timer_on:
            pass
        if self.stopper_on:
            pass

        #Mode specifies what is displayed
        if self.mode == "clock":
            pass
        elif self.mode == "timer":
            pass
        elif self.mode == "stopper":
            pass
        elif self.mode == "standby":
            pass
        elif self.mode == "notification":
            pass
        else:
            raise RuntimeError("Invalid mode in time_mechanism")

        #return time

    @staticmethod
    def _seconds_to_time_tuple(seconds):
        #ToDo Implement seconds_to_time_tuple
        raise NotImplementedError

