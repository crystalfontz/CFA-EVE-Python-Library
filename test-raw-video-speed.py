#!/usr/bin/env python3

#===========================================================================
#
# Crystalfontz Raspberry-Pi Python example library for FTDI / BridgeTek
# EVE graphic accelerators.
#
#---------------------------------------------------------------------------
#
# This example program tests full screen update speed by converting a RGB888
# framebuffer image to RGB565, placing it in the EVE's RAM_G memory and
# displaying it as quickly as possible.
# The update rate is currently limited by SPI speed.
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

import sys
import time
from py_cfeve import cfeve
import random
from PIL import Image, ImageDraw
import numpy

#see the py_cfeye/modules directory for supported Crystalfontz modules/displays
CFA_MODULE = 'cfa10086'
#see the py_cfeye/interfaces directory for supported coms interfaces
CFA_MODULE_INTERFACE = 'rpispi'

############################################################################

def image_to_rgb565_bytes(image):
	#some cleverness to convert RGB888 image to RGB565
	rgb888 = numpy.asarray(image)
	# check that image have 3 color components, each of 8 bits
	assert rgb888.shape[-1] == 3 and rgb888.dtype == numpy.uint8
	r5 = (rgb888[..., 0] >> 3 & 0x1f).astype(numpy.uint16)
	g6 = (rgb888[..., 1] >> 2 & 0x3f).astype(numpy.uint16)
	b5 = (rgb888[..., 2] >> 3 & 0x1f).astype(numpy.uint16)
	rgb565 = r5 << 11 | g6 << 5 | b5
	return rgb565.tobytes()

def send_data8(data):
	#write data in SEND_SEG_SIZE max byte blocks to RAM_G
	SEND_SEG_SIZE = 4096 - 3 #3 bytes needed for addr
	startseg = 0
	data_size = len(data)
	while True:
		ramg_loc = eve.defs.EVE_RAM_G + startseg
		if (startseg + SEND_SEG_SIZE) > data_size:
			#send smaller/last seg
			endseg = startseg + (data_size - startseg)
			ret = eve.iface.w8(ramg_loc, data[startseg:endseg])
			#done
			break
		else:
			#send full seg
			endseg = startseg + SEND_SEG_SIZE
			ret = eve.iface.w8(ramg_loc, data[startseg:endseg])
			startseg += SEND_SEG_SIZE
		if ret == False:
			print("FAIL")
			break

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

#create image / framebuffer
IMAGE_SIZE = (320, 240)
img = Image.new('RGB', IMAGE_SIZE, color=(0,0,0))
img_draw = ImageDraw.Draw(img)

#main loop
loop_count = 0
fps_time = time.perf_counter()
while True:
	#setup display
	#setup while the EVE is processing previous display list
	setup_time_start = time.perf_counter()
	#new random pixel point
	x = int(random.randrange(0,IMAGE_SIZE[0]))
	y = int(random.randrange(0,IMAGE_SIZE[1]))
	r = int(random.randrange(0,255))
	g = int(random.randrange(0,255))
	b = int(random.randrange(0,255))
	#draw the pixel to the image
	img_draw.point((x,y), (r,g,b))
	#convert the image from RGB888 to RGB565
	outdata = image_to_rgb565_bytes(img)
	setup_time_elapsed = time.perf_counter() - setup_time_start

	#print timing info on the console
	loop_count += 1
	if loop_count % 20 == 0:
		#fps
		fps = 1.0 / ((time.perf_counter() - fps_time) / 20)
		fps_time = time.perf_counter()
		#
		print("")
		print("loop-count: {}".format(loop_count))
		print("setup-time: {:.3f}mS".format(setup_time_elapsed * 1000.0))
		print(" wait-time: {:.3f}mS".format(wait_time_elapsed * 1000.0))
		print("       fps: {:.3f}".format(fps))

	#now wait until pervious display list is empty before continuing
	wait_time_start = time.perf_counter()
	eve.fifo_wait_until_empty()
	wait_time_elapsed = time.perf_counter() - wait_time_start

	#send RGB565 data to EVE's RAM_G
	send_data8(outdata)

	#start the display list
	eve.send_command(eve.defs.EVE_ENC_CMD_DLSTART)
	#set the default clear color to black
	eve.send_command(eve.defs.EVE_ENC_CLEAR_COLOR_RGB(0,0,0))
	#clear the screen - this and the previous prevent artifacts between lists
	eve.send_command(eve.defs.EVE_ENC_CLEAR(1,1,1))

	#display the RGB565 data from RAM_G using a bitmap handle
	eve.send_command(eve.defs.EVE_ENC_BITMAP_HANDLE(0))
	eve.set_bitmap(0, eve.defs.EVE_FORMAT_RGB565, IMAGE_SIZE[0], IMAGE_SIZE[1])
	eve.send_command(eve.defs.EVE_ENC_COLOR_RGB(255,255,255))
	eve.send_command(eve.defs.EVE_ENC_BEGIN(eve.defs.EVE_BEGIN_BITMAPS))
	eve.send_command(eve.defs.EVE_ENC_VERTEX2F(0, 0))
	eve.send_command(eve.defs.EVE_ENC_END())

	#instruct the graphics processor to process the display list
	eve.send_command(eve.defs.EVE_ENC_DISPLAY())
	#make this list active
	eve.send_command(eve.defs.EVE_ENC_CMD_SWAP)
	#update the ring buffer pointer so the graphics processor starts executing
	eve.update_fifo()
	#done, endlessly loop back (ctrl-c me :P)

############################################################################

