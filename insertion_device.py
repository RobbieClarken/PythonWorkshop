from epics import PV

__version__ = '0.1.0'

class InsertionDevice(object):
    def __init__(self, beamline):
        self.gap_setpoint = PV(beamline + ':GAP_SP')
        self.gap_monitor = PV(beamline + ':GAP_MONITOR')
        self.moving_monitor = PV(beamline + ':MOVING_STATUS')

    @property
    def gap(self):
        return self.gap_monitor()

    @gap.setter
    def gap(self, value):
        return self.gap_setpoint.put(value)

    @property
    def moving(self):
        return self.moving_monitor.get(as_string=True) == 'Moving'
