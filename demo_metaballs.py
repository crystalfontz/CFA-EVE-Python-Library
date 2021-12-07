#!/usr/bin/env python3
import sys
import time
from py_cfeve import cfeve
import random

#===========================================================================
#
# Crystalfontz Raspberry-Pi Python example library for FTDI / BridgeTek
# EVE graphic accelerators.
#
#---------------------------------------------------------------------------
#
# This example program simply bounces a ball around the display.
# If the display has a touch panel enabled, the balls respond to a touch.
#
#---------------------------------------------------------------------------
#
# This file is part of the port/adaptation of existing C based EVE libraries
# to Python for Crystalfontz EVE based displays.
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

#see the py_cfeye/modules directory for supported Crystalfontz modules/displays
CFA_MODULE = 'CFAF800480E1-050SC-A2'
#see the py_cfeye/interfaces directory for supported coms interfaces
CFA_MODULE_INTERFACE = 'rpispi'

############################################################################

class blob:
	def __init__(self, width, height):
		self.x = random.randrange(16 * width)
		self.y = random.randrange(16 * height)
		self.dx = random.randrange(50) - 32
		self.dy = random.randrange(50) - 32

class metaball_demo:
	def __init__(self, eve):
		self.eve = eve
		#init vars
		#8 bit vars
		self.w = 31
		self.h = 18
		self.num_blobs = 80
		self.fade_in = 255
		#32 bit vars
		self.vel = 0
		self.center_x = 16 * 16 * (self.w / 2)
		self.center_y = 16 * 16 * (self.h / 2)
		self.touching = 0
		self.recip_sz = int((self.w*self.w + self.h*self.h) / 4 + 1)
		self.tval1 = 0
		self.tval2 = 0
		self.sx = 0
		self.sy = 0
		self.vel = 0
		self.m = 0
		self.d = 0
		self.bx = 0
		self.by = 0
		self.dx = 0
		self.dy = 0
		self.xx = 0

		#setup blobs
		self.blobs = []
		for i in range(0, self.num_blobs):
			self.blobs.append(blob(self.eve.LCD_WIDTH, self.eve.LCD_HEIGHT))

		self.recip = []
		self.recip.append(200)
		for i in range(1, self.recip_sz):
			self.recip.append(min(200, (self.eve.LCD_WIDTH * 10) / (4 * i)))
		self.fade_in = 255

	def v(self):
		# from the old C code
		# if defined(DISPLAY_RESOLUTION_WVGA) || defined( DISPLAY_RESOLUTION_HVGA_PORTRAIT)
		# return random(50)-32;
		# else return random(50)-32;
		return random.randrange(50) - 32

	def prepare(self):
		#do pre display loop EVE memory writes
		if (self.eve.iface.r16(eve.defs.EVE_REG_TOUCH_RAW_XY) & 0x8000) == 0:
			#touch panel is being touched
			self.sx = self.eve.iface.r16(eve.defs.EVE_REG_TOUCH_SCREEN_XY + 2)
			self.sy = self.eve.iface.r16(eve.defs.EVE_REG_TOUCH_SCREEN_XY)
			self.center_x = 16 * self.sx
			self.center_y = 16 * self.sy
			self.vel = 8
		else:
			#no touch detected
			self.center_x = self.eve.LCD_WIDTH * 16 / 2
			self.center_y = self.eve.LCD_HEIGHT * 16 / 2
			self.vel = 2

		for i in range(0, self.num_blobs):
			if self.blobs[i].x < self.center_x:
				self.blobs[i].dx += self.vel
			else:
				self.blobs[i].dx -= self.vel

			if self.blobs[i].y < self.center_y:
				self.blobs[i].dy += self.vel
			else:
				self.blobs[i].dy -= self.vel
			self.blobs[i].x += self.blobs[i].dx << 3
			self.blobs[i].y += self.blobs[i].dy << 3

		self.blobs[random.randrange(self.num_blobs)].dx = self.v()
		self.blobs[random.randrange(self.num_blobs)].dy = self.v()

		temp = []
		out_buf = [0] * ((self.h << 6) + self.w)
		for ih in range(0, self.h):
			for iw in range(0, self.w):
				m = self.fade_in
				for i in range(0, 3):
					self.bx = self.blobs[i].x >> 8
					self.by = self.blobs[i].y >> 8
					self.dx = self.bx - iw
					self.dy = self.by - ih
					self.d = (self.dx*self.dx) + (self.dy*self.dy)
					self.m += self.recip[min(self.d >> 2, self.recip_sz - 1)]
				temp.append(min(round(self.m), 255))
			for a in range(0, self.w):
				addr = (ih << 6) + a
				out_buf[addr] = temp[a]
		eve.iface.w8(eve.defs.EVE_RAM_G, out_buf)
		return

	def add_to_display_list(self):
		eve.buffer_cocmd_add(eve.defs.EVE_ENC_COLOR_RGB(255, 255, 0))
		eve.cocmd.filled_rectangle(0, 0, eve.LCD_WIDTH-1, eve.LCD_HEIGHT-1)
		eve.buffer_cocmd_add(eve.defs.EVE_ENC_BITMAP_SOURCE(0))
		eve.buffer_cocmd_add(eve.defs.EVE_ENC_BITMAP_LAYOUT(eve.defs.EVE_FORMAT_L8, 64, 64))
		eve.buffer_cocmd_add(eve.defs.EVE_ENC_BITMAP_SIZE(eve.defs.EVE_FILTER_BILINEAR,
			eve.defs.EVE_WRAP_BORDER, eve.defs.EVE_WRAP_BORDER, self.eve.LCD_WIDTH, self.eve.LCD_HEIGHT))
		if self.eve.LCD_WIDTH >= 512 or self.eve.LCD_HEIGHT >= 512:
			eve.buffer_cocmd_add(eve.defs.EVE_ENC_BITMAP_SIZE_H(self.eve.LCD_WIDTH>>9, self.eve.LCD_HEIGHT>>9));
		eve.buffer_cocmd_add(eve.defs.EVE_ENC_SAVE_CONTEXT())
		eve.buffer_cocmd_add(eve.defs.EVE_ENC_BITMAP_TRANSFORM_A(0, int(0x100 / 64)))
		eve.buffer_cocmd_add(eve.defs.EVE_ENC_BITMAP_TRANSFORM_E(0, int(0x100 / 64)))
		eve.buffer_cocmd_add(eve.defs.EVE_ENC_BEGIN(eve.defs.EVE_BEGIN_BITMAPS))
		eve.buffer_cocmd_add(eve.defs.EVE_ENC_BLEND_FUNC(eve.defs.EVE_BLEND_SRC_ALPHA, 0))
		eve.buffer_cocmd_add(eve.defs.EVE_ENC_COLOR_RGB(255, 0, 0))
		eve.buffer_cocmd_add(eve.defs.EVE_ENC_VERTEX2II(0,0,0,0))
		eve.buffer_cocmd_add(eve.defs.EVE_ENC_BLEND_FUNC(eve.defs.EVE_BLEND_SRC_ALPHA, 1))
		eve.buffer_cocmd_add(eve.defs.EVE_ENC_COLOR_RGB(255, 255, 0))
		eve.buffer_cocmd_add(eve.defs.EVE_ENC_VERTEX2II(0,0,0,0))
		eve.buffer_cocmd_add(eve.defs.EVE_ENC_RESTORE_CONTEXT())
		eve.buffer_cocmd_add(eve.defs.EVE_ENC_COLOR_RGB(0, 0, 0))
		eve.buffer_cocmd_add(eve.defs.EVE_ENC_BEGIN(eve.defs.EVE_BEGIN_POINTS))
		for i in range(3, self.num_blobs):
			eve.buffer_cocmd_add(eve.defs.EVE_ENC_POINT_SIZE(3 * i))
			eve.buffer_cocmd_add(eve.defs.EVE_ENC_VERTEX2F(self.blobs[i].x, self.blobs[i].y))
		#return

	def update(self):
		#nothing to do here
		pass

############################################################################

#MAIN PROGRAM

#read brightness value if specified on command line args
brightness = 50
if len(sys.argv) == 2:
    #brightness
    brightness = int(sys.argv[1])
    if brightness > 100: brightness = 100
    if brightness < 0: brightness = 0
print("brightness: {} pct".format(brightness))
brightness = int((brightness / 100.0) * 128.0)

#init the EVE module and set backlight brightness
eve = cfeve(CFA_MODULE, CFA_MODULE_INTERFACE)
eve.set_backlight(brightness)

#calibrate if needed
if eve.module.TOUCH_RESISTIVE == True:
	eve.cocmd.manual_calibrate()

#init the demo
demo = metaball_demo(eve)

loop_count = 0
fps_time = time.perf_counter()
while True:
	#setup display
	prep_time_start = time.perf_counter()
	demo.prepare()
	prep_time_elapsed = time.perf_counter() - prep_time_start
	#start the display list
	setup_time_start = time.perf_counter()
	eve.buffer_cocmd_add(eve.defs.EVE_ENC_CMD_DLSTART)
	#set the default clear color to black
	eve.buffer_cocmd_add(eve.defs.EVE_ENC_CLEAR_COLOR_RGB(0,0,0))
	#clear the screen - this and the previous prevent artifacts between lists
	eve.buffer_cocmd_add(eve.defs.EVE_ENC_CLEAR(1,1,1))
	#add display list from demo
	demo.add_to_display_list()
	#instruct the graphics processor to show the list
	eve.buffer_cocmd_add(eve.defs.EVE_ENC_DISPLAY())
	#make this list active
	eve.buffer_cocmd_add(eve.defs.EVE_ENC_CMD_SWAP)
	#flush the cocmd buffer
	#print("cocmd-buf-len: {} cmds".format(eve.buffer_cocmd_length()))
	eve.buffer_cocmd_flush()
	#update the ring buffer pointer so the graphics processor starts executing
	eve.update_fifo()
	#setup done
	setup_time_elapsed = time.perf_counter() - setup_time_start

	#update calculations
	wait_time_start = time.perf_counter()
	demo.update()
	#wait until display list is empty before continuing
	eve.fifo_wait_until_empty()
	wait_time_elapsed = time.perf_counter() - wait_time_start

	#print timing every 100 loops
	loop_count += 1
	if loop_count % 100 == 0:
		#fps
		fps = 1.0 / ((time.perf_counter() - fps_time) / 100)
		fps_time = time.perf_counter()
		#
		print("")
		print("loop-count: {}".format(loop_count))
		print("prep-time:  {:.3f}mS".format(prep_time_elapsed * 1000.0))
		print("setup-time: {:.3f}mS".format(setup_time_elapsed * 1000.0))
		print(" wait-time: {:.3f}mS".format(wait_time_elapsed * 1000.0))
		print("       fps: {:.3f}".format(fps))
	#loop back to start

############################################################################