__author__ = 'kr'


class KeyMatrix():

    def __init__(self, ref_to_clock_mechanism):
        self._ref_to_clock_mechanism = ref_to_clock_mechanism
        self._function_blocks = {
            "00": {
                "00": self._clock_mode_on,
                "01": self._set_time_modification,
                "10": self._unset_time_modification
            },
            "01": {
                "00": self._set_alarm,
                "01": self._cancel_alarm,
                "10": self._notification_off_alarm
            },
            "10": {
                "00": self._timer_mode_on,
                "01": self._start_timer,
                "10": self._stop_timer,
                "11": self._notification_off_timer
            },
            "11": {
                "00": self._stopper_mode_on,
                "01": self._start_stopper,
                "10": self._stop_stopper
            }
        }

    def _clock_mode_on(self):
        """Activates clock mode"""
        self._ref_to_clock_mechanism.mode = "clock"

    def _set_time_modification(self, sec):
        """Set a modification for the normal time displayed in clock mode.

        :param sec Number of second to move the clock forward.
        :type sec int
        """
        self._ref_to_clock_mechanism.time_adjustment = sec

    def _unset_time_modification(self):
        """Resets time modification to 0."""
        self._ref_to_clock_mechanism.time_adjustment = 0

    def _set_alarm(self, time):
        """Sets an alarm at the specified time of the day. The passed argument is the number of seconds since 00:00:00
        when the alarm should be triggered. Example: 3601 would signify that the alarm goes off at 01:00:01 any day.

        :param time How many seconds after midnight when the alarm should trigger.
        :type time int
        """
        self._ref_to_clock_mechanism.alarm_time = time

    def _cancel_alarm(self):
        """Alarm is disabled."""
        self._ref_to_clock_mechanism.alarm_time = None

    def _notification_off_alarm(self):
        """Turns off notification raised due to alarm. Goes to standby mode."""
        self._ref_to_clock_mechanism.alarm_time = None
        self._ref_to_clock_mechanism.mode = "standby"

    def _timer_mode_on(self):
        """Activates timer mode."""
        self._ref_to_clock_mechanism.mode = "timer"

    def _start_timer(self, sec):
        """Starts timer by setting clock mechanism state to timer. After sec seconds have passed, a notification will
         trigger.

         :param sec Nr of seconds to count down from
         :type sec int"""
        self._ref_to_clock_mechanism.timer_on = True
        self._ref_to_clock_mechanism.timer_time = sec

    def _stop_timer(self):
        """Stops timer by setting clock mechanism mode to standby and reverts timer countdown to 0."""
        self._ref_to_clock_mechanism.timer_on = False
        self._ref_to_clock_mechanism.timer_time = 0

    def _notification_off_timer(self):
        """Deactivates notification mode."""
        self._stop_timer()
        self._ref_to_clock_mechanism.mode = "standby"

    def _stopper_mode_on(self):
        """Activates stopper mode."""
        self._ref_to_clock_mechanism.mode = "stopper"

    def _start_stopper(self):
        """Starts stopper, by activating stopper mode in clock mechanism."""
        self._ref_to_clock_mechanism.stopper_on = True

    def _stop_stopper(self):
        """Stops stopper, by activating standby mode in clock mechanism. Stopper time reset to 0."""
        self._ref_to_clock_mechanism.stopper_on = False
        self._ref_to_clock_mechanism.stopper_time = 0

    def pass_message(self, message):
        """Unpacks the passed message and activates the specified function, if the message is viable.

        :param message Some message, as string of 0s and 1s
        :type message str
        :raise KeyError
        """
        if len(message) < 4 or len(message) > 21:
            raise KeyError
        fn_block = message[0:2]
        function = message[2:4]
        if len(message) > 4:
            parameter = int(message[3:-1], base=2)
            try:
                self._function_blocks[fn_block][function](parameter)
            except TypeError:
                raise KeyError
        else:
            try:
                self._function_blocks[fn_block][function]()
            except TypeError:
                raise KeyError

if __name__ == "__main__":
    pass