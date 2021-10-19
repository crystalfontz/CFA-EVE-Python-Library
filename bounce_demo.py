#!/usr/bin/env python3
import sys
import time
from py_cfeve import cfeve

#===========================================================================
#
# Crystalfontz Raspberry-Pi Python example library for FTDI / BridgeTek
# EVE graphic accelerators.
#
#---------------------------------------------------------------------------
#
# This example program simply bounces a ball around the display.
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

#see the py_cfeye/modules directory for supported Crystalfontz modules/displays
CFA_MODULE = 'cfa10086'
#see the py_cfeye/interfaces directory for supported coms interfaces
CFA_MODULE_INTERFACE = 'rpispi'

############################################################################

#bounce demo
class bounce_demo:
	def __init__(self, eve):
		self.eve = eve
		#init vars
		self.r = 0xff
		self.g = 0x00
		self.b = 0x800
		#start ghostly, getting more solid
		self.transparency = 0
		self.transparency_direction = 1
		#define a default point x-location (1/16 anti-aliased)
		self.x_position = (self.eve.LCD_WIDTH >> 1) << 4
		self.x_velocity = 3 * 16
		#define a default point y-location (1/16 anti-aliased)
		self.y_position = (self.eve.LCD_HEIGHT >> 1) << 4
		self.y_velocity = -2 * 16
		#start small
		self.ball_size = 50 * 1
		self.ball_delta = 1 * 16

	def add_to_display_list(self):
		#set the variable color of the bouncing ball
		self.eve.send_command(self.eve.defs.EVE_ENC_COLOR_RGB(self.r,self.g,self.b))
		#make it transparent
		self.eve.send_command(self.eve.defs.EVE_ENC_COLOR_A(self.transparency))
		#draw the ball -- a point (filled circle)
		self.eve.point(self.x_position, self.y_position, self.ball_size)

		#draw the rubberband.
		#maximum stretched would be LCD_WIDTH/2 + LCD_WIDTH/2 (manhatten) make that
		#1 pixels wide, make the minimum 10 pixels wide
		rubberband_width = 0
		x_distance = 0
		y_distance = 0

		if (self.x_position >> 4) < (self.eve.LCD_WIDTH >> 1):
			x_distance = (self.eve.LCD_WIDTH >> 1) - (self.x_position >> 4)
		else:
			x_distance= (self.x_position >> 4) - (self.eve.LCD_WIDTH >> 1)

		if (self.y_position >> 4) < (self.eve.LCD_HEIGHT >> 1):
			y_distance = (self.eve.LCD_HEIGHT >> 1) - (self.y_position >> 4)
		else:
			y_distance = (self.y_position >> 4) - (self.eve.LCD_HEIGHT >> 1)

		#straight math does not make it skinny enough. This seems like it should
		#underlow often, but in real life never goes below 1. Need to dissect
		rubberband_width = int( 10 - ((9+1) * (x_distance+y_distance)) / ((self.eve.LCD_WIDTH >> 1) + (self.eve.LCD_HEIGHT >> 1)) )
		#check for underflow just in case
		if rubberband_width & 0x8000:
			rubberband_width = 1

		#now that we know the rubberband width, drawing it is simple
		self.eve.send_command(self.eve.defs.EVE_ENC_COLOR_RGB(200,0,0))
		#transparency set above still in effect
		self.eve.line(self.eve.LCD_WIDTH >> 1, self.eve.LCD_HEIGHT >> 1, self.x_position >> 4, self.y_position >> 4, rubberband_width)

	def update(self):
		#bounce the ball
		MIN_POINT_SIZE = 10 << 4
		MAX_POINT_SIZE = ((self.eve.LCD_HEIGHT >> 2) - 20) << 4
		#update the colors
		self.r += 1
		self.g -= 1
		self.b += 2
		#cycle the transparancy
		if self.transparency_direction:
			#getting more solid
			if self.transparency != 255:
				self.transparency += 1
			else:
				self.transparency_direction = 0
		else:
			#getting more clear
			if 128 < self.transparency:
				self.transparency -= 1
			else:
				self.transparency_direction = 1
		#change the point (ball) size.
		if self.ball_delta < 0:
			#Getting smaller. OK to decrease again?
			if MIN_POINT_SIZE < (self.ball_size+self.ball_delta):
				#it will be bigger than min after decrease
				self.ball_size += self.ball_delta
			else:
				#It would be too small, bounce.
				self.ball_size = MIN_POINT_SIZE+(MIN_POINT_SIZE-(self.ball_size+self.ball_delta))
				#Turn around.
				self.ball_delta = -self.ball_delta
		else:
			#Getting larger. OK to increase again?
			if (self.ball_size+self.ball_delta) < MAX_POINT_SIZE:
				#it will be smaller than max after increase
				self.ball_size += self.ball_delta
			else:
				#It would be too big, bounce.
				self.ball_size = MAX_POINT_SIZE-(MAX_POINT_SIZE-(self.ball_size+self.ball_delta))
				#Turn around.
				self.ball_delta=-self.ball_delta

		#Move X, bouncing
		if self.x_velocity < 0:
			#Going left. OK to move again?
			if 0 < (self.x_position-(self.ball_size)+self.x_velocity):
				#it will be onscreen after decrease
				self.x_position += self.x_velocity
			else:
				#It would be too small, bounce.
				self.x_position = self.ball_size+(self.ball_size-(self.x_position+self.x_velocity))
				#Turn around
				self.x_velocity =- self.x_velocity
		else:
			#Getting larger. OK to increase again?
			if (self.x_position+(self.ball_size)+self.x_velocity) < (self.eve.LCD_WIDTH << 4):
				#it will be on screen after increase
				self.x_position += self.x_velocity
			else:
				#It would be too big, bounce
				max_x_ctr = (self.eve.LCD_WIDTH << 4) - self.ball_size
				self.x_position = max_x_ctr-(max_x_ctr-(self.x_position+self.x_velocity))
				#Turn around
				self.x_velocity =- self.x_velocity

		#Move Y, bouncing
		if self.y_velocity < 0:
			#Going left. OK to move again?
			if 0 < (self.y_position-(self.ball_size)+self.y_velocity):
				#it will be onscreen after decrease
				self.y_position += self.y_velocity
			else:
				#It would be too small, bounce.
				self.y_position = self.ball_size+(self.ball_size-(self.y_position+self.y_velocity))
				#Turn around.
				self.y_velocity =- self.y_velocity
		else:
			#Getting larger. OK to increase again?
			if (self.y_position+(self.ball_size)+self.y_velocity) < (self.eve.LCD_HEIGHT << 4):
				#it will be on screen after increase
				self.y_position += self.y_velocity
			else:
				#It would be too big, bounce.
				max_y_ctr = (self.eve.LCD_WIDTH << 4) - self.ball_size
				self.y_position = max_y_ctr-(max_y_ctr-(self.y_position+self.y_velocity))
				#Turn around.
				self.y_velocity =- self.y_velocity


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
#init the demo
demo = bounce_demo(eve)

loop_count = 0
fps_time = time.perf_counter()
while True:
	#setup display
	setup_time_start = time.perf_counter()
	#start the display list
	eve.send_command(eve.defs.EVE_ENC_CMD_DLSTART)
	#set the default clear color to black
	eve.send_command(eve.defs.EVE_ENC_CLEAR_COLOR_RGB(0,0,0))
	#clear the screen - this and the previous prevent artifacts between lists
	eve.send_command(eve.defs.EVE_ENC_CLEAR(1,1,1))
	#fill background with white
	eve.filled_rectangle(0, 0, eve.LCD_WIDTH-1, eve.LCD_HEIGHT-1)
	#bounce
	demo.add_to_display_list()
	#instruct the graphics processor to show the list
	eve.send_command(eve.defs.EVE_ENC_DISPLAY())
	#make this list active
	eve.send_command(eve.defs.EVE_ENC_CMD_SWAP)
	#update the ring buffer pointer so the graphics processor starts executing
	eve.update_fifo()
	#setup done
	setup_time_elapsed = time.perf_counter() - setup_time_start

	wait_time_start = time.perf_counter()
	#update bounce
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
		print("setup-time: {:.3f}mS".format(setup_time_elapsed * 1000.0))
		print(" wait-time: {:.3f}mS".format(wait_time_elapsed * 1000.0))
		print("       fps: {:.3f}".format(fps))
	#loop back to start

############################################################################

