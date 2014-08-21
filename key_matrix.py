__author__ = 'kr'


class KeyMatrix():

    def __init__(self, ref_to_clock_mechanism):
        self._ref_to_clock_mechanism = ref_to_clock_mechanism

        """
        Find a way to describe the function blocks that are talked about in "Key_Matrix_Description"
        """
        #ToDo Describe Function Blocks

    def _clock_mode_on(self):
        """Activates clock mode"""
        #ToDo Implement _clock_mode_on
        raise NotImplementedError

    def _set_time_modification(self, sec):
        """Set a modification for the normal time displayed in clock mode.

        :param sec Number of second to move the clock forward.
        :type sec int
        """
        #ToDo Implement _set_time_modification
        raise NotImplementedError

    def _unset_time_modification(self):
        """Resets time modification to 0."""
        #ToDo Implement _unset_time_modification
        raise NotImplementedError

    def _set_alarm(self, time):
        """Sets an alarm at the specified time of the day. The passed argument is the number of seconds since 00:00:00
        when the alarm should be triggered. Example: 3601 would signify that the alarm goes off at 01:00:01 any day.

        :param time How many seconds after midnight when the alarm should trigger.
        :type time int
        """
        #ToDo Implement _set_alarm
        raise NotImplementedError

    def _cancel_alarm(self):
        """Alarm is disabled."""
        #ToDo Implement _cancel_alarm
        raise NotImplementedError

    def _alarm_notification_off(self):
        """Turns off notification raised due to alarm. Goes to standby mode."""
        #ToDo Implement _alarm_notification_off
        raise NotImplementedError

    def _timer_mode_on(self):
        """Activates timer mode."""
        #ToDo Implement _timer_mode_on
        raise NotImplementedError

    def _start_timer(self, sec):
        """Starts timer by setting clock mechanism state to timer. After sec seconds have passed, a notification will
         trigger.

         :param sec Nr of seconds to count down from
         :type sec int"""
        #ToDo Implement _start_timer
        raise NotImplementedError

    def _stop_timer(self):
        """Stops timer by setting clock mechanism mode to standby and reverts timer countdown to 0."""
        #ToDo Implement _stop_timer
        raise NotImplementedError

    def _notification_off_timer(self):
        """Deactivates notification mode."""
        #ToDo Implement _notification_off_timer
        raise NotImplementedError

    def _stopper_mode_on(self):
        """Activates stopper mode."""
        #ToDo Implement _stopper_mode_on
        raise NotImplementedError

    def _start_stopper(self):
        """Starts stopper, by activating stopper mode in clock mechanism."""
        #ToDo Implement _start_stopper
        raise NotImplementedError

    def _stop_stopper(self):
        """Stops stopper, by activating standby mode in clock mechanism. Stopper time reset to 0."""
        #ToDo Implement _stop_stopper
        raise NotImplementedError

    def pass_message(self, message):
        """Unpacks the passed message and activates the specified function, if the message is viable.

        :param message Some message, as string of 0s and 1s
        :type message str
        :raise KeyError
        """
        #ToDo Implement pass_message
        raise NotImplementedError

if __name__ == "__main__":
    #Test Something out
    pass