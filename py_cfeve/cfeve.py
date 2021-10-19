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

import time
import importlib

class cfeve:
	def __init__(self, module_type, interface_type):
		#imports
		self.iface = importlib.import_module('.interface.'+interface_type, package='py_cfeve').iface()
		self.module = importlib.import_module('.module.'+module_type, package='py_cfeve')
		self.defs = importlib.import_module('.evedef.'+str(self.module.EVE_DEVICE), package='py_cfeve')

		#init vars
		self.LCD_WIDTH = self.module.LCD_WIDTH
		self.LCD_HEIGHT = self.module.LCD_HEIGHT
		self.EVE_DEVICE = self.module.EVE_DEVICE
		self.fifo_location = 0
		self.ramg_unused_start = 0

		#eve reset & wake up
		time.sleep(0.020)
		self.iface.eve_reset()
		self.host_command(0x00) #EVE_HCMD_ACTIVE
		time.sleep(0.040)
		#wait for REG_ID = 0x7C
		while self.iface.r8(self.defs.EVE_REG_ID) != 0x7C:
			print("waiting to read id = 0x7C")
			time.sleep(0.10)
		#wait for the self.defs.EVE_REG_CPURESET to indicate that all initializations are complete
		while self.iface.r8(self.defs.EVE_REG_CPURESET) != 0:
			print("waiting for reset to complete")
			time.sleep(0.10)
		#get and print chip id
		self.read_eve_id()
		#remind the chip of the speed it is running at
		self.iface.w32(self.defs.EVE_REG_FREQUENCY, self.module.EVE_CLOCK_SPEED)

		"""
		#gt911 touch setup
		if self.module.HAS_GOODIX == True:
			FT8xx_Init_Goodix_GT911()
		#configure touch & audio
		"""

		#get initial write pointer location
		self.fifo_location = self.iface.r16(self.defs.EVE_REG_CMD_WRITE)

		#turn off screen & backlight
		self.iface.w8(self.defs.EVE_REG_PCLK, 0)
		self.iface.w8(self.defs.EVE_REG_PWM_DUTY, 0)

		# load parameters of the physical screen
		self.iface.w16(self.defs.EVE_REG_HSIZE, self.module.LCD_WIDTH)
		self.iface.w16(self.defs.EVE_REG_HCYCLE, self.module.LCD_HCYCLE)
		self.iface.w16(self.defs.EVE_REG_HOFFSET, self.module.LCD_HOFFSET)
		self.iface.w16(self.defs.EVE_REG_HSYNC0, self.module.LCD_HSYNC0)
		self.iface.w16(self.defs.EVE_REG_HSYNC1, self.module.LCD_HSYNC1)

		self.iface.w16(self.defs.EVE_REG_VSIZE, self.module.LCD_HEIGHT)
		self.iface.w16(self.defs.EVE_REG_VCYCLE, self.module.LCD_VCYCLE)
		self.iface.w16(self.defs.EVE_REG_VOFFSET, self.module.LCD_VOFFSET)
		self.iface.w16(self.defs.EVE_REG_VSYNC0, self.module.LCD_VSYNC0)
		self.iface.w16(self.defs.EVE_REG_VSYNC1, self.module.LCD_VSYNC1)

		self.iface.w8(self.defs.EVE_REG_SWIZZLE, self.module.LCD_SWIZZLE)
		self.iface.w8(self.defs.EVE_REG_PCLK_POL, self.module.LCD_PCLKPOL)

		self.iface.w8(self.defs.EVE_REG_CSPREAD, self.module.LCD_PCLK_CSPREAD)
		self.iface.w8(self.defs.EVE_REG_DITHER, self.module.LCD_DITHER)

		#setup gpiox drive strength
		gpiox = self.iface.r16(self.defs.EVE_REG_GPIOX)
		if self.module.LCD_DRIVE_10MA == 1:
  			#Set 10mA drive for: PCLK, DISP , VSYNC, HSYNC, DE, RGB lines & BACKLIGHT
			gpiox = gpiox | 0x1000
		else:
			#Set 5mA drive for: PCLK, DISP , VSYNC, HSYNC, DE, RGB lines & BACKLIGHT
			gpiox = gpiox & ~0x1000
		self.iface.w16(self.defs.EVE_REG_GPIOX, gpiox)

		#touch inits
		#disable touch
		self.iface.w8(self.defs.EVE_REG_TOUCH_MODE, 0)
		#eliminate any false touches
		self.iface.w16(self.defs.EVE_REG_TOUCH_RZTHRESH, 0)

		#self.iface.w16(self.defs.EVE_REG_TOUCH_RZTHRESH, 1200)
		#self.iface.w8(self.defs.EVE_REG_TOUCH_MODE, 0x02)
		#self.iface.w8(self.defs.EVE_REG_TOUCH_ADC_MODE, 0x01)
		#self.iface.w8(self.defs.EVE_REG_TOUCH_OVERSAMPLE +self. RAM_REG, 15)

		#clear the lcd
		self.iface.w32(self.defs.EVE_RAM_DL + 0, self.defs.EVE_ENC_CLEAR_COLOR_RGB(0, 0, 0))
		self.iface.w32(self.defs.EVE_RAM_DL + 4, self.defs.EVE_ENC_CLEAR(1, 1, 1))
		self.iface.w32(self.defs.EVE_RAM_DL + 8, self.defs.EVE_ENC_DISPLAY())
		self.iface.w8(self.defs.EVE_REG_DLSWAP, self.defs.EVE_DLSWAP_FRAME)

		#enable the DISP line of the LCD
		gpiox = self.iface.r16(self.defs.EVE_REG_GPIOX)
		self.iface.w16(self.defs.EVE_REG_GPIOX, gpiox | 0x8000)

		#now start clocking data to the LCD panel, enabling the display
		self.iface.w8(self.defs.EVE_REG_PCLK, self.module.LCD_PCLK)

		#backlight frequency default is 250Hz
		self.iface.w16(self.defs.EVE_REG_PWM_HZ, 500)
		#Crystalfontz EVE displays have soft start. No need to ramp.
		self.iface.w8(self.defs.EVE_REG_PWM_DUTY, 128)

		#get initial write pointer location again
		self.fifo_location = self.iface.r16(self.defs.EVE_REG_CMD_WRITE)

		#TODO: do any touch calibration here

		#done

#########################################################################################

	def host_command(self, command):
		data = [command & 0xFF, 0x00, 0x00]
		return self.iface.wr(data)

	def send_command(self, data):
		# send a command & update fifo location
		# data can be of type int or a list
		# note: there is no checking to make sure a command list
		#  will fit in the eve's buffer
		ret = self.iface.w32(self.fifo_location + self.defs.EVE_RAM_CMD, data)
		length = 1
		if isinstance(data, list):
			length = len(data)
		self.fifo_location += (self.defs.EVE_CMD_SIZE) * length
		self.fifo_location %= self.defs.EVE_RAM_CMD_SIZE
		return ret

	def fifo_free_space(self):
		cmdbuffer_rd = self.iface.r16(self.defs.EVE_REG_CMD_READ)
		cmdbuffer_wr = self.iface.r16(self.defs.EVE_REG_CMD_WRITE)
		cmdbuffer_diff = (cmdbuffer_wr - cmdbuffer_rd) % self.defs.EVE_RAM_CMD_SIZE
		return (self.defs.EVE_RAM_CMD_SIZE - self.defs.EVE_CMD_SIZE) - cmdbuffer_diff

	def fifo_wait(self, room):
		getfreespace = room - 1
		while getfreespace < room:
			getfreespace = self.fifo_freespace()
			time.sleep(0.005)

	def fifo_is_empty(self):
		cmdbuffer_rd = self.iface.r16(self.defs.EVE_REG_CMD_READ)
		cmdbuffer_wr = self.iface.r16(self.defs.EVE_REG_CMD_WRITE)
		if cmdbuffer_rd == cmdbuffer_wr:
			return True
		return False

	def fifo_wait_until_empty(self):
		#make the assumption that WR doesn't change while we wait
		#wont work for anything multi-threaded!
		#fast checking (small sleep time) chews CPU time!
		cmdbuffer_wr = self.iface.r16(self.defs.EVE_REG_CMD_WRITE)
		while self.iface.r16(self.defs.EVE_REG_CMD_READ) != cmdbuffer_wr:
			time.sleep(0.005)

	def update_fifo(self):
		# write the fifo location
		# causes the FT81x to process the command list
		return self.iface.w16(self.defs.EVE_REG_CMD_WRITE, self.fifo_location)

	def read_eve_id(self):
		#read
		#should be 0x08
		id = self.iface.r8(self.defs.EVE_CHIP_ID_ADDRESS)
		if id != 0x08:
			print("chip-id 0C0000h != 0x08")
			return False
		#should be 0x01
		id = self.iface.r8(self.defs.EVE_CHIP_ID_ADDRESS+2)
		if id != 0x01:
			print("chip-id 0C0002h != 0x01")
			return False
		#should be 0x00
		id = self.iface.r8(self.defs.EVE_CHIP_ID_ADDRESS+3)
		if id != 0x00:
			print("chip-id 0C0003h != 0x00")
			return False
		#get type
		type = self.iface.r8(self.defs.EVE_CHIP_ID_ADDRESS+1)
		print("chip-id = {}".format(hex(type)))
		return type

	def set_backlight(self, brightness):
		self.iface.w8(self.defs.EVE_REG_PWM_DUTY, brightness)

#########################################################################################

	def point(self, x,y, size):
		command_list = [
			self.defs.EVE_ENC_POINT_SIZE(size),						#select the size of the dot to draw
			self.defs.EVE_ENC_BEGIN(self.defs.EVE_BEGIN_POINTS),	#indicate to draw a point (dot)
			self.defs.EVE_ENC_VERTEX2F(x,y),							#set the point center location
			self.defs.EVE_ENC_END()									#end the point
		]
		self.send_command(command_list)

	def line(self, x0,y0, x1,y1, width):
		command_list = [
			self.defs.EVE_ENC_LINE_WIDTH(width*16),					#set line width
			self.defs.EVE_ENC_BEGIN(self.defs.EVE_BEGIN_LINES),		#start a line
			self.defs.EVE_ENC_VERTEX2F(x0*16,y0*16),					#set the first point
			self.defs.EVE_ENC_VERTEX2F(x1*16,y1*16),					#set the second point
			self.defs.EVE_ENC_END()									#end the line
		]
		self.send_command(command_list)

	def filled_rectangle(self, x0,y0, x1,y1):
		command_list = [
			self.defs.EVE_ENC_LINE_WIDTH(16),							#set the line width (16/16 of a pixel--appears to be about as sharp as it gets)
			self.defs.EVE_ENC_BEGIN(self.defs.EVE_BEGIN_RECTS),		#start a rectangle
			self.defs.EVE_ENC_VERTEX2F(x0*16,y0*16),					#set the first point
			self.defs.EVE_ENC_VERTEX2F(x1*16,y1*16),					#set the second point
			self.defs.EVE_ENC_END()									#end the rectangle
		]
		self.send_command(command_list)

	def slider(self, x, y, w, h, options, val, range):
		command_list = [
			self.defs.EVE_ENC_CMD_SLIDER,
			(y << 16) | x,
			(h << 16) | w,
			(val << 16) | options,
			range
		]
		self.send_command(command_list)

	def spinner(self, x, y, style, scale):
		command_list = [
			self.defs.EVE_ENC_CMD_SPINNER,
			(y << 16) | x,
			(scale << 16) | style
		]
		self.send_command(command_list)

	def gauge(self, x, y, r, options, major, minor, val, range):
		command_list = [
			self.defs.EVE_ENC_CMD_GAUGE,
			(y << 16) | x,
			(options << 16) | r,
			(minor << 16) | major,
			(range << 16) | val
		]
		self.send_command(command_list)

	def dial(self, x, y, r, options, val):
		command_list = [
			self.defs.EVE_ENC_CMD_DIAL,
			(y << 16) | x,
			(options << 16) | r,
			val
		]
		self.send_command(command_list)

	def track(self, x, y, w, h, tag):
		command_list = [
			self.defs.EVE_ENC_CMD_TRACK,
			(y << 16) | x,
			(h << 16) | w,
			tag
		]
		self.send_command(command_list)

	def cmd_number(self, x, y, font, options, num):
		command_list = [
			self.defs.EVE_ENC_CMD_NUMBER,
			(y << 16) | x,
			(options << 16) | font,
			num
		]
		self.send_command(command_list)

	def gradient(self, x0, y0, rgb0, x1, y1, rgb1):
		command_list = [
			self.defs.EVE_ENC_CMD_GRADIENT,
			(y0 << 16) | x0,
			rgb0,
			(y1 << 16) | x1,
			rgb1
		]
		self.send_command(command_list)

	"""
	TODO text
	def text(self, x, y, font, options, str):
		length = len(str)
		if length == 0:
			return
		uint32_t* data = (uint32_t*)calloc((length / 4) + 1, sizeof(uint32_t))
		sptr = 0
		for (ptr = 0 ptr < (length / 4) ++ptr, sptr = sptr + 4)
			data[ptr] = (uint32_t) str[sptr + 3] << 24
				| (uint32_t) str[sptr + 2] << 16 | (uint32_t) str[sptr + 1] << 8
				| (uint32_t) str[sptr]
		for (i = 0 i < (length % 4) ++i, ++sptr)
			data[ptr] |= (uint32_t) str[sptr] << (i * 8)
		self.send_command(self.defs.EVE_ENC_CMD_TEXT)
		self.send_command(((uint32_t) y << 16) | x)
		self.send_command(((uint32_t) options << 16) | font)
		for (i = 0 i <= length / 4 i++)
			self.send_command(data[i])
		free(data)
	"""

	def set_bitmap(self, addr, fmt, width, height):
		command_list = [
			self.defs.EVE_ENC_CMD_SETBITMAP,
			addr & 0xFFFFFFFF,
			((width & 0xFFFF) << 16) | (fmt & 0xFFFF),
			(height & 0xFFFF)
		]
		self.send_command(command_list)

	"""
	#not confirmed to work
	def set_bitmap_h(self, handle, source, format, width, height, colstride, rowstride, filter, wrapx, wrapy):
		command_list = [
			self.defs.EVE_ENC_BITMAP_HANDLE(handle),
			self.defs.EVE_ENC_BITMAP_SOURCE(source),
			self.defs.EVE_ENC_BITMAP_EXT_FORMAT(format),
			self.defs.EVE_ENC_BITMAP_LAYOUT_H(colstride>>10, rowstride>>9),
			self.defs.EVE_ENC_BITMAP_LAYOUT(self.defs.EVE_GLFORMAT, colstride, rowstride),
			self.defs.EVE_ENC_BITMAP_SIZE_H(width>>9, height>>9),
			self.defs.EVE_ENC_BITMAP_SIZE(filter, wrapx, wrapy, width,height)
		]
		self.send_command(command_list)
	"""

	def memcpy(self, dest, src, num):
		command_list = [
			self.defs.EVE_ENC_CMD_MEMCPY,
			dest,
			src,
			num
		]
		self.send_command(command_list)

	def get_ptr(self):
		command_list = [self.defs.EVE_ENC_CMD_GETPTR, 0]
		self.send_command(command_list)

	def gradient_color(self, c):
		command_list = [self.defs.EVE_ENC_CMD_GRADCOLOR, c]
		self.send_command(command_list)

	def fg_color(self, c):
		command_list = [self.defs.EVE_ENC_CMD_FGCOLOR, c]
		self.send_command(command_list)

	def bg_color(self, c):
		command_list = [self.defs.EVE_ENC_CMD_BGCOLOR, c]
		self.send_command(command_list)

	def translate(self, tx, ty):
		command_list = [self.defs.EVE_ENC_CMD_TRANSLATE, tx, ty]
		self.send_command(command_list)

	def rotate(self, a):
		command_list = [self.defs.EVE_ENC_CMD_ROTATE, a]
		self.send_command(command_list)

	def set_rotate(self, rotation):
		command_list = [self.defs.EVE_ENC_CMD_SETROTATE, rotation]
		self.send_command(command_list)

	def scale(self, sx, sy):
		command_list = [self.defs.EVE_ENC_CMD_SCALE, sx, sy]
		self.send_command(command_list)

	def calibrate(self, result):
		command_list = [self.defs.EVE_ENC_CMD_CALIBRATE, result]
		self.send_command(command_list)

	"""
	TODO manual calibrate
	"""

##########################################################################################

	def get_ramg_end_addr(self):
		#get the end memory address of data inflated by CMD_INFLATE
		#make sure that the chip is caught up
		self.fifo_wait_until_empty()
		#tell the chip to get the first free location in RAM_G
		self.get_ptr()
		#update the ring buffer pointer so the graphics processor starts executing
		self.update_fifo()
		#wait for the chip to catch up
		self.fifo_wait_until_empty()
		#we know that the answer is 4 addresses lower than
		#read the value and pass it back to the caller know what we found
		ramg_end_addr = self.iface.r32(self.RAM_CMD + (self.fifo_location - 4) & 0x0FFF)
		return ramg_end_addr

	def infate_to_ramg(self, data, ramg_address):
		#inflate ZLIB deflated data into ramg at ramg_address
		#extend list to ensure 4-byte alignment
		data_length = (len(data) + 0x03) & 0xFFFFFFFC
		data.extend([0] * (data_length - len(data)))
		#load and inflate data from flash to RAM_G
		#write the self.defs.EVE_ENC_CMD_INFLATE and parameters
		self.send_command([self.defs.EVE_ENC_CMD_INFLATE, ramg_address])
		#pipe out data_length of data from data_address
		#use chunks so we can handle images larger than 4K
		data_position = 0
		while data_length != 0:
			#what is the maximum we can transfer in this block?
			#see how much room is available in the self.defs.EVE_RAM_CMD
			bytes_free = self.fifo_free_space()
			if data_length <= bytes_free:
				#everything will fit in the available space
				bytes_this_block = data_length
			else:
				#it won't all fit, transfer the maximum amount
				bytes_this_block = bytes_free - 4
			#set the address in self.defs.EVE_RAM_CMD for this block
			command_list = [self.defs.EVE_ENC_CMD_MEMWRITE]
			#add the data
			command_list += data[data_position:data_position+bytes_this_block]
			#send it
			self.send_command(command_list)
			#process the data
			self.update_fifo()
			#now wait for it to catch up
			self.fifo_wait_until_empty()

		#get the first free address in RAM_G from after the inflated data, and
		#push it into the caller's variable
		ramg_address = self.get_ramg_end_addr()
		#to be safe, force RAM_G_Address to be 8-byte aligned (maybe not needed, certainly does not hurt)
		ramg_address = (ramg_address + 0x07) & 0xFFFFFFF8
		#return the new ramg_address
		return ramg_address

	def write_blob_to_flash_sect0(self, first_unused_ramg_address, flash_sector):
		#wait until EVE is caught up
		self.fifo_wait_until_empty()
		#expand the flash_blob, keep track of how big it expands to
		end_ramg_address = self.infate_to_ramg(self.defs.EVE_FLASH_BLOB, first_unused_ramg_address)
		#now ask the EVE to program the 1st sector of flash with the expanded flash_blob sitting in RAMG at
		command_list = [self.defs.EVE_ENC_CMD_FLASHUPDATE,
			#destination in flash (must be 4096 byte aligned)
			flash_sector * 4096,
			#source in RAM_G (must be 4-byte aligned)
			first_unused_ramg_address,
			#size (must be multiple of 4096)
			end_ramg_address - first_unused_ramg_address
		]
		self.send_command(command_list)
		#update the ring buffer pointer so the coprocessor starts executing
		self.update_fifo()
		#remember that the flash sector 0 is used
		#*Flash_Sector = 1; !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
		#now wait for the coprocessor to catch up
		self.fifo_wait_until_empty()

##########################################################################################

