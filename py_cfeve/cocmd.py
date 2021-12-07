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

import time
import importlib

class cocmd:
	def __init__(self, eve):
		self.eve = eve

	#######################

	def point(self, x,y, size):
		command_list = [
			self.eve.defs.EVE_ENC_POINT_SIZE(size),						#select the size of the dot to draw
			self.eve.defs.EVE_ENC_BEGIN(self.eve.defs.EVE_BEGIN_POINTS),	#indicate to draw a point (dot)
			self.eve.defs.EVE_ENC_VERTEX2F(x,y),							#set the point center location
			self.eve.defs.EVE_ENC_END()									#end the point
		]
		self.eve.buffer_cocmd_add(command_list)

	def line(self, x0,y0, x1,y1, width):
		command_list = [
			self.eve.defs.EVE_ENC_LINE_WIDTH(width*16),					#set line width
			self.eve.defs.EVE_ENC_BEGIN(self.eve.defs.EVE_BEGIN_LINES),		#start a line
			self.eve.defs.EVE_ENC_VERTEX2F(x0*16,y0*16),					#set the first point
			self.eve.defs.EVE_ENC_VERTEX2F(x1*16,y1*16),					#set the second point
			self.eve.defs.EVE_ENC_END()									#end the line
		]
		self.eve.buffer_cocmd_add(command_list)

	def filled_rectangle(self, x0,y0, x1,y1):
		command_list = [
			self.eve.defs.EVE_ENC_LINE_WIDTH(16),							#set the line width (16/16 of a pixel--appears to be about as sharp as it gets)
			self.eve.defs.EVE_ENC_BEGIN(self.eve.defs.EVE_BEGIN_RECTS),		#start a rectangle
			self.eve.defs.EVE_ENC_VERTEX2F(x0*16,y0*16),					#set the first point
			self.eve.defs.EVE_ENC_VERTEX2F(x1*16,y1*16),					#set the second point
			self.eve.defs.EVE_ENC_END()									#end the rectangle
		]
		self.eve.buffer_cocmd_add(command_list)

	def slider(self, x, y, w, h, options, val, range):
		command_list = [
			self.eve.defs.EVE_ENC_CMD_SLIDER,
			(y << 16) | x,
			(h << 16) | w,
			(val << 16) | options,
			range
		]
		self.eve.buffer_cocmd_add(command_list)

	def spinner(self, x, y, style, scale):
		command_list = [
			self.eve.defs.EVE_ENC_CMD_SPINNER,
			(y << 16) | x,
			(scale << 16) | style
		]
		self.eve.buffer_cocmd_add(command_list)

	def gauge(self, x, y, r, options, major, minor, val, range):
		command_list = [
			self.eve.defs.EVE_ENC_CMD_GAUGE,
			(y << 16) | x,
			(options << 16) | r,
			(minor << 16) | major,
			(range << 16) | val
		]
		self.eve.buffer_cocmd_add(command_list)

	def dial(self, x, y, r, options, val):
		command_list = [
			self.eve.defs.EVE_ENC_CMD_DIAL,
			(y << 16) | x,
			(options << 16) | r,
			val
		]
		self.eve.buffer_cocmd_add(command_list)

	def track(self, x, y, w, h, tag):
		command_list = [
			self.eve.defs.EVE_ENC_CMD_TRACK,
			(y << 16) | (x & 0xffff),
			(h << 16) | (w & 0xffff),
			tag
		]
		self.eve.buffer_cocmd_add(command_list)

	def cmd_number(self, x, y, font, options, num):
		command_list = [
			self.eve.defs.EVE_ENC_CMD_NUMBER,
			(y << 16) | x,
			(options << 16) | font,
			num
		]
		self.eve.buffer_cocmd_add(command_list)

	def gradient(self, x0, y0, rgb0, x1, y1, rgb1):
		command_list = [
			self.eve.defs.EVE_ENC_CMD_GRADIENT,
			(y0 << 16) | x0,
			rgb0,
			(y1 << 16) | x1,
			rgb1
		]
		self.eve.buffer_cocmd_add(command_list)

	def text(self, x, y, font, options, str):
		if len(str) == 0:
			return
		command_list = [
			self.eve.defs.EVE_ENC_CMD_TEXT,
			(y << 16) | (x & 0xFFFF),
			(options << 16) | (font & 0xffff)
		]
		#append text (pack the string into 32bit words)
		strb = [ord(c) for c in str]
		d = 0
		for i in range(0, len(strb)):
			d |= strb[i] << ((i % 4) * 8)
			if (i % 4) == 3:
				command_list.extend([d])
				d = 0
		if d != 0:
			command_list.extend([d])
		#add it to the co display list
		self.eve.buffer_cocmd_add(command_list)

	def set_bitmap(self, addr, fmt, width, height):
		command_list = [
			self.eve.defs.EVE_ENC_CMD_SETBITMAP,
			addr & 0xFFFFFFFF,
			((width & 0xFFFF) << 16) | (fmt & 0xFFFF),
			(height & 0xFFFF)
		]
		self.eve.buffer_cocmd_add(command_list)

	"""
	#not confirmed to work
	def set_bitmap_h(self, handle, source, format, width, height, colstride, rowstride, filter, wrapx, wrapy):
		command_list = [
			self.eve.defs.EVE_ENC_BITMAP_HANDLE(handle),
			self.eve.defs.EVE_ENC_BITMAP_SOURCE(source),
			self.eve.defs.EVE_ENC_BITMAP_EXT_FORMAT(format),
			self.eve.defs.EVE_ENC_BITMAP_LAYOUT_H(colstride>>10, rowstride>>9),
			self.eve.defs.EVE_ENC_BITMAP_LAYOUT(self.eve.defs.EVE_GLFORMAT, colstride, rowstride),
			self.eve.defs.EVE_ENC_BITMAP_SIZE_H(width>>9, height>>9),
			self.eve.defs.EVE_ENC_BITMAP_SIZE(filter, wrapx, wrapy, width,height)
		]
		self.eve.buffer_cocmd_add(command_list)
	"""

	def mem_cpy(self, dest, src, num):
		command_list = [
			self.eve.defs.EVE_ENC_CMD_MEMCPY,
			dest,
			src,
			num
		]
		self.eve.buffer_cocmd_add(command_list)

	def mem_zero(self, dest, length):
		command_list = [
			self.eve.defs.EVE_ENC_CMD_MEMZERO,
			dest,
			length
		]
		self.eve.buffer_cocmd_add(command_list)

	def get_ptr(self):
		command_list = [self.eve.defs.EVE_ENC_CMD_GETPTR, 0]
		self.eve.buffer_cocmd_add(command_list)

	def gradient_color(self, c):
		command_list = [self.eve.defs.EVE_ENC_CMD_GRADCOLOR, c]
		self.eve.buffer_cocmd_add(command_list)

	def fg_color(self, c):
		command_list = [self.eve.defs.EVE_ENC_CMD_FGCOLOR, c]
		self.eve.buffer_cocmd_add(command_list)

	def bg_color(self, c):
		command_list = [self.eve.defs.EVE_ENC_CMD_BGCOLOR, c]
		self.eve.buffer_cocmd_add(command_list)

	def translate(self, tx, ty):
		command_list = [self.eve.defs.EVE_ENC_CMD_TRANSLATE, tx, ty]
		self.eve.buffer_cocmd_add(command_list)

	def rotate(self, a):
		command_list = [self.eve.defs.EVE_ENC_CMD_ROTATE, a]
		self.eve.buffer_cocmd_add(command_list)

	def set_rotate(self, rotation):
		command_list = [self.eve.defs.EVE_ENC_CMD_SETROTATE, rotation]
		self.eve.buffer_cocmd_add(command_list)

	def scale(self, sx, sy):
		command_list = [self.eve.defs.EVE_ENC_CMD_SCALE, sx, sy]
		self.eve.buffer_cocmd_add(command_list)

	def calibrate(self, result):
		command_list = [self.eve.defs.EVE_ENC_CMD_CALIBRATE, result]
		self.eve.buffer_cocmd_add(command_list)

	def manual_calibrate(self):
		self.eve.buffer_cocmd_add(self.eve.defs.EVE_ENC_CLEAR(1,1,1))
		self.eve.buffer_cocmd_add(self.eve.defs.EVE_ENC_COLOR_RGB(255,255,255))
		self.text(self.eve.LCD_WIDTH>>1, self.eve.LCD_HEIGHT>>1, 26, self.eve.defs.EVE_OPT_CENTERX | self.eve.defs.EVE_OPT_CENTERY, "Please tap on a dot")
		self.calibrate(0)
		#flush the cocmd buffer
		self.eve.buffer_cocmd_flush()
		#update the ring buffer pointer so the graphics processor starts executing
		self.eve.update_fifo()
		return

	def sketch(self, x, y, w, h, ptr, format, freq):
		if self.eve.EVE_DEVICE == 800 and self.eve.module.TOUCH_CAPACITIVE == True:
			#use csketch for FT801
			command_list = [
				self.eve.defs.EVE_ENC_CMD_CSKETCH,
				(y << 16) | (x & 0xFFFF),
				(h << 16) | (w & 0xffff),
				ptr,
				(freq << 16) | (format & 0xffff)
			]
		else:
			#use sketch (freq is ignored)
			command_list = [
				self.eve.defs.EVE_ENC_CMD_CSKETCH,
				(y << 16) | (x & 0xFFFF),
				(h << 16) | (w & 0xffff),
				ptr,
				(format & 0xffff)
			]
		self.eve.buffer_cocmd_add(command_list)
		return

	def button(self, x, y, w, h, font, options, s):
		command_list = [
			self.eve.defs.EVE_ENC_CMD_BUTTON,
			(y << 16) | (x & 0xFFFF),
			(h << 16) | (w & 0xffff),
			(options << 16) | (font & 0xffff),
			s
		]
		#Gpu_CoCmd_SendStr(phost, s);
		self.eve.buffer_cocmd_add(command_list)
		return
