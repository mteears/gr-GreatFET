#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2019 MTeears.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import numpy as np
from gnuradio import gr
import time
import greatfet
from greatfet import GreatFET
from greatfet.protocol import vendor_requests

class gpio_sink_f(gr.sync_block):
    """
    docstring for block gpio_sink_f
Port chooses default GPIO pin on GreatFET device
State is 0 for low, 1 for high
Switch is selecting between GPIO  4,5,6,7,8 where 0=4, 1=5, etc.
    """
    def __init__(self, port=None, state=None, switch=None):
	gr.sync_block.__init__(self,
        name="GreatFET GPIO Sink",
        in_sig=[np.float32, np.float32, np.float32],
        out_sig=[])
        
	gf = GreatFET()
	self.gf = gf
        self.port = port
	self.state = state
	self.switch = switch

    def work(self, input_items, output_items):
        gf = GreatFET()
	in0 = input_items[0]
	in1 = input_items[1]
	gpio = str(int(in0[0]+4))
	pin_string = 'J1_P' + gpio
	pin = gf.gpio.get_pin(pin_string)
	pin.set_direction(gf.gpio.DIRECTION_OUT)
	if(in1[0] == float(1)):
		pin.write(True)
	if(in1[0] != float(1)):
		pin.write(False)
	# <+signal processing here+>

	
        return len(input_items[0])

