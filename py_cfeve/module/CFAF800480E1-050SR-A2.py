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
EVE_DEVICE = 817

# EVE Clock Speed
EVE_CLOCK_SPEED = 60000000

# Touch
TOUCH_RESISTIVE = True
TOUCH_CAPACITIVE = False
TOUCH_GOODIX_CAPACITIVE = False

# Define RGB output pins order, determined by PCB layout
LCD_SWIZZLE = 0

# Define active edge of PCLK. Observed by scope:
#  0: Data is put out coincident with falling edge of the clock.
#     Rising edge of the clock is in the middle of the data.
#  1: Data is put out coincident with rising edge of the clock.
#     Falling edge of the clock is in the middle of the data.
LCD_PCLKPOL = 1

# LCD drive strength: 0=5mA, 1=10mA
LCD_DRIVE_10MA = 0

# Spread Spectrum on RGB signals. Probably not a good idea at higher
# PCLK frequencies.
LCD_PCLK_CSPREAD = 0

#This is a 24-bit display, so no need to dither.
LCD_DITHER = 0

# Pixel clock divisor (based on 60MHz internal clock)
# 0 = disable
# 1 = 60MHz
# 2 = 30MHz
# 3 = 20MHz
# 4 = 15MHz
# 5 = 12MHz
# 6 = 10MHz
# 7 = 8.6MHz
# 8 = 7.5MHz
# etc
LCD_PCLK = 2

#----------------------------------------------------------------------------
# Frame_Rate = 60Hz / 16.7mS
#----------------------------------------------------------------------------
# Horizontal timing (minimum values from ILI6122_SPEC_V008.pdf page 45)
# Target 60Hz frame rate, using the largest possible line time in order to
# maximize the time that the EVE has to process each line.
HPX = 800	# Horizontal Pixel Width
HSW = 4		# Horizontal Sync Width (1~40)
HBP = 8		# Horizontal Back Porch (must be 46, includes HSW)
HFP = 8		# Horizontal Front Porch (16~210~354)
HPP = 178	# Horizontal Pixel Padding (tot=863: 862~1056~1200)
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
# Vertical timing (minimum values from ILI6122_SPEC_V008.pdf page 46)
VLH = 480	# Vertical Line Height
VS = 4		# Vertical Sync (in lines)  (1~20)
VBP = 8		# Vertical Back Porch (must be 23, includes VS)
VFP = 8		# Vertical Front Porch (7~22~147)
VLP = 1		# Vertical Line Padding (tot=511: 510~525~650)
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