#!/usr/bin/env python

"""
Hosts EPICS channels for testing the node-libca module.
Requires the pcaspy package available at:
https://code.google.com/p/pcaspy/
"""

import pcaspy
import time
import sys
import numpy as np
from pcaspy import SimpleServer, Driver

prefix = 'PYTHON_WORKSHOP:'
pvdb = {
    'MOTOR_POSITION': {'type': 'float', 'value': 10.5, 'lolim': 0., 'hilim': 20},
    'COUNTER' : {'type': 'int', 'value': 0, 'scan': 1},
    'SLOW_COUNTER' : {'type': 'int', 'value': 0, 'scan': 5},
    'NOISEY': {'type': 'float', 'scan': 0.2},
    'CAMERA_DATA': {'type': 'float', 'value': [1, 2, 3], 'count': 3},
    'DETECTOR_STATUS': {
        'type': 'enum',
        'enums': ['Unknown', 'Ready', 'Moving', 'Collecting', 'Fault'],
        'value': 1,
    },
}

class TestDriver(Driver):

    def __init__(self):
        super(TestDriver, self).__init__()

    def read(self, reason):
        if reason in ('COUNTER', 'SLOW_COUNTER'):
            value = (self.getParam(reason) + 1) % 0xffffffffff
            self.setParam(reason, value)
        elif reason is 'NOISEY':
            value = np.sin(time.time()) + np.random.normal(scale=0.3)
            self.setParam(reason, value)
        else:
            value = self.getParam(reason)
        return value

    def write(self, reason, value):

        lolim = pvdb[reason].get('lolim')
        if lolim is not None and value < lolim:
            return False

        hilim = pvdb[reason].get('hilim')
        if hilim is not None and value > hilim:
            return False

        self.setParam(reason, value)

        return True

if __name__ == '__main__':

    import os
    os.environ['EPICS_CAS_INTF_ADDR_LIST'] = 'localhost'

    ioc_server = SimpleServer()
    ioc_server.createPV(prefix, pvdb)
    driver = TestDriver()

    print('Please note: you will need to set EPICS_CA_ADDR_LIST=localhost '
          'to access PVs served by this IOC.')

    while True:
        ioc_server.process(.1)
