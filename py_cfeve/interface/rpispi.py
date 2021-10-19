#===========================================================================
#
# Crystalfontz Raspberry-Pi Python example library for FTDI / BridgeTek
# EVE graphic accelerators.
#
#---------------------------------------------------------------------------
#
# This file is part of the port/adaptation of existing C based EVE libraries
# to Python for Crystalfontz EVE based displays.
#
# THIS LIBRARY IS A WORK IN PROGRESS!
#
# 2021-10-20 Mark Williams / Crystalfontz America Inc.
# https:#www.crystalfontz.com/products/eve-accelerated-tft-displays.php
#---------------------------------------------------------------------------
#
# This is free and unencumbered software released into the public domain.
# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.
# In jurisdictions that recognize copyright laws, the author or authors
# of this software dedicate any and all copyright interest in the
# software to the public domain. We make this dedication for the benefit
# of the public at large and to the detriment of our heirs and
# successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to this
# software under copyright law.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
# For more information, please refer to <http:#unlicense.org/>
#
#============================================================================

import spidev
import RPi.GPIO as gpio
import time

# RPI GPIO10  (pin 19) = EVE MOSI
# RPI GPIO9   (pin 21) = EVE MISO
# RPI GPIO11  (pin 23) = EVE SCK
# RPI GPIO8   (pin 24) = EVE CS
# RPI GPIO10  (pin 19) = EVE MOSI
# RPI GPIO5   (pin 29) = EVE INT
# RPI GPIO6   (pin 31) = EVE PD

class iface:
	#config
	SPI_BUS = 0
	SPI_DEV = 0
	SPI_MODE = 0b00
	SPI_MAX_SPEED = 32000000
	GPIO_EVE_INT = 29
	GPIO_EVE_PD = 31

	def __init__(self):
		#gpio init
		gpio.setmode(gpio.BOARD)
		gpio.setwarnings(False)
		gpio.setup(self.GPIO_EVE_INT, gpio.IN)
		gpio.setup(self.GPIO_EVE_PD, gpio.OUT)
		#spi init
		self.spi = spidev.SpiDev()
		self.spi.open(self.SPI_BUS, self.SPI_DEV)
		self.spi.max_speed_hz = self.SPI_MAX_SPEED
		self.spi.mode = self.SPI_MODE
		self.spi.lsbfirst = False

	def eve_reset(self):
		#reset eve (power down/up)
		gpio.output(self.GPIO_EVE_PD, 0)
		time.sleep(0.020)
		gpio.output(self.GPIO_EVE_PD, 1)
		time.sleep(0.050)
		return True

	def wr(self, data):
		return self.spi.xfer(data)

	def r(self, count):
		data = [0 for i in range(count+1)]
		return self.spi.xfer(data)

	def w8(self, addr, data):
		#data can be single int, or list
		sdata = [(((addr >> 16) & 0xFF) | 0x80), ((addr >> 8) & 0xFF), (addr & 0xFF)] #address first
		if isinstance(data, int):
			sdata.extend([data & 0xFF])
		elif isinstance(data, list) or isinstance(data, bytes):
			sdata.extend(data)
		else:
			return False
		return self.spi.xfer3(sdata)

	def w16(self, addr, data):
		sdata = [(((addr >> 16) & 0xFF) | 0x80), ((addr >> 8) & 0xFF), (addr & 0xFF)] #address first
		if isinstance(data, int):
			sdata.extend([(data & 0xFF), ((data >> 8) & 0xFF)])
		elif isinstance(data, list) or isinstance(data, bytes):
			for d in data:
				sdata.extend([(d & 0xFF), ((d >> 8) & 0xFF)])
		else:
			return False
		return self.spi.xfer(sdata)

	def w32(self, addr, data):
		#data can be single int, or list
		sdata = [(((addr >> 16) & 0xFF) | 0x80), ((addr >> 8) & 0xFF), (addr & 0xFF)] #address first
		if isinstance(data, int):
			sdata.extend([(data & 0xFF), ((data >> 8) & 0xFF), ((data >> 16) & 0xFF), ((data >> 24) & 0xFF)])
		elif isinstance(data, list) or isinstance(data, bytes):
			for d in data:
				sdata.extend([(d & 0xFF), ((d >> 8) & 0xFF), ((d >> 16) & 0xFF), ((d >> 24) & 0xFF)])
		else:
			return False
		return self.spi.xfer3(sdata)

	def r8(self, addr):
		#addr, dummy, one to read
		data = [((addr >> 16) & 0xFF), ((addr >> 8) & 0xFF), (addr & 0xFF), 0x00, 0x00]
		ret = self.spi.xfer(data)
		return ret[4]

	def r16(self, addr):
		#addr, dummy, two to read
		data = [((addr >> 16) & 0xFF), ((addr >> 8) & 0xFF), (addr & 0xFF), 0x00, 0x00, 0x00]
		ret = self.spi.xfer(data)
		return (ret[5] << 8) | ret[4]

	def r32(self, addr):
		#addr, dummy, four to read
		data = [((addr >> 16) & 0xFF), ((addr >> 8) & 0xFF), (addr & 0xFF), 0x00, 0x00, 0x00, 0x00, 0x00]
		ret = self.spi.xfer(data)
		return (ret[7] << 24) | (ret[6] << 16) | (ret[5] << 8) | ret[4]
