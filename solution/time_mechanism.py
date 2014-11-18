__author__ = 'kr'

from PyQt5 import QtCore
from datetime import datetime, timedelta


class TimeMechanism():

    def __init__(self, display):
        self.display = display
        self.timer = QtCore.QTimer(display.clock_grid)
        self.timer.timeout.connect(self.tick)
        self.timer.start(1000)

        self.mode = "clock"
        self.time_adjustment = 0
        self.timer_on = False
        self.timer_time = 0
        self.stopper_on = False
        self.stopper_time = 0
        self.alarm_time = None
        self.alarm_twinkle = True

    def tick(self):
        """Is called every second to update the display accordingly."""
        self.display.update(self.get_time())

    def get_time(self):
        """Return the time to be currently displayed in the clock display, dependent on the current mode.

         :return A tuple representation of time
         :rtype tuple
        """
        #Keep these running independent of what is being displayed
        if self.timer_on:
            self.timer_time -= 1
            if self.timer_time <= 0:
                self.mode = "notification"
        if self.stopper_on:
            self.stopper_time += 1

        #Mode specifies what is displayed
        if self.mode == "clock":
            dt = datetime.now() + timedelta(0, self.time_adjustment)
            time = (dt.hour, dt.minute, dt.second)
            if self.alarm_time is not None and self.alarm_time <= (dt.hour*60*60 + dt.minute*60 + dt.second):
                    self.mode = "notification"
        elif self.mode == "timer":
            time = self.seconds_to_time_tuple(self.timer_time)
        elif self.mode == "stopper":
            time = self.seconds_to_time_tuple(self.stopper_time)
        elif self.mode == "standby":
            time = (0, 0, 0)
        elif self.mode == "notification":
            if self.alarm_twinkle:
                #Hacker emblem, can be anything
                time = (00, 1, 53)
            else:
                time = (0, 0, 0)
            self.alarm_twinkle = not self.alarm_twinkle
        else:
            raise RuntimeError("Invalid mode in time_mechanism")
        return time

    @staticmethod
    def seconds_to_time_tuple(seconds):
        hour = 0
        minute = 0
        while seconds >= 60:
            minute += 1
            seconds -= 60
        while minute >= 60:
            hour += 1
            minute -= 60
        return hour, minute, seconds

