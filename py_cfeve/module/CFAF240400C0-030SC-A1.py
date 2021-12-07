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

#EVE Device Type
EVE_DEVICE = 811

# EVE Clock Speed
EVE_CLOCK_SPEED = 60000000

# Touch
TOUCH_RESISTIVE = False
TOUCH_CAPACITIVE = True
TOUCH_GOODIX_CAPACITIVE = False

# Define RGB output pins order, determined by PCB layout
LCD_SWIZZLE = 2

# Define active edge of PCLK. Observed by scope:
#  0: Data is put out coincident with falling edge of the clock.
#     Rising edge of the clock is in the middle of the data.
#  1: Data is put out coincident with rising edge of the clock.
#     Falling edge of the clock is in the middle of the data.
LCD_PCLKPOL = 0

# LCD drive strength: 0=5mA, 1=10mA
LCD_DRIVE_10MA = 0

# Spread Spectrum on RGB signals. Probably not a good idea at higher
# PCLK frequencies.
LCD_PCLK_CSPREAD = 0

#This is not a 24-bit display, so dither
LCD_DITHER = 1

# Pixel clock divisor
LCD_PCLK = 5

#----------------------------------------------------------------------------
# Frame_Rate = 60Hz / 16.7mS
#----------------------------------------------------------------------------
# Horizontal timing
# Target 60Hz frame rate, using the largest possible line time in order to
# maximize the time that the EVE has to process each line.
HPX = 240	# Horizontal Pixel Width
HSW = 1		# Horizontal Sync Width
HBP = 47	# Horizontal Back Porch
HFP = 16	# Horizontal Front Porch
HPP = 1		# Horizontal Pixel Padding
			# FTDI needs at least 1 here
# Define the constants needed by the EVE based on the timing
# Active width of LCD display
LCD_WIDTH = HPX
# Start of horizontal sync pulse
LCD_HSYNC0 = HFP
# End of horizontal sync pulse
LCD_HSYNC1 = HFP+HSW
# Start of active line
LCD_HOFFSET = HFP+HSW+HBP
# Total number of clocks per line
LCD_HCYCLE = HPX+HFP+HSW+HBP+HPP

#----------------------------------------------------------------------------
# Vertical timing
VLH = 400	# Vertical Line Height
VS = 1		# Vertical Sync (in lines)
VBP = 24	# Vertical Back Porch
VFP = 7		# Vertical Front Porch
VLP = 1		# Vertical Line Padding
			# FTDI needs at least 1 here
# Define the constants needed by the EVE based on the timing
# Active height of LCD display
LCD_HEIGHT = VLH
# Start of vertical sync pulse
LCD_VSYNC0 = VFP
# End of vertical sync pulse
LCD_VSYNC1 = VFP+VS
# Start of active screen
LCD_VOFFSET = VFP+VS+VBP
# Total number of lines per screen
LCD_VCYCLE = VLH+VFP+VS+VBP+VLP