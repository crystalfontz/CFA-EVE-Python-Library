
#EXTRAS
EVE_CHIP_ID_ADDRESS = 0x000C0000
EVE_CMD_SIZE = 0x04
EVE_HCMD_ACTIVE = 0x00
EVE_HCMD_STANDBY = 0x41
EVE_HCMD_SLEEP = 0x42
EVE_HCMD_PWRDOWN = 0x50
EVE_HCMD_CLKINT = 0x48
EVE_HCMD_CLKEXT = 0x44
EVE_HCMD_CLK48M = 0x62
EVE_HCMD_CLK36M = 0x61
EVE_HCMD_CORERESET = 0x68

#FT810 / FT811 / FT812 / FT813
EVE_LOW_FREQ_BOUND              = 58800000   # = 98% of 60Mhz

EVE_RAM_CMD                     = 0x00308000 # = 3178496
EVE_RAM_CMD_SIZE                = 4*1024
EVE_RAM_DL                      = 0x00300000 # = 3145728
EVE_RAM_DL_SIZE                 = 8*1024
EVE_RAM_G                       = 0x00000000 # = 0
EVE_RAM_G_SIZE                  = 1024*1024
EVE_RAM_REG                     = 0x00302000 # = 3153920
EVE_RAM_TOP                     = 0x00304000 # = 3162112
EVE_RAM_ROMSUB                  = 0x0030A000 # = 3186688
#EVE_RAM_BIST                    = 0x00380000 # = 3670016
EVE_ROMFONT_TABLEADDRESS        = 0x002FFFFC # = 3145724
#EVE_RAM_ERR_REPORT              = 0x00309800 # = 3184640

EVE_REG_ANA_COMP                = 0x00302184 # = 3154308
EVE_REG_ANALOG                  = 0x0030216C # = 3154284
EVE_REG_BIST_EN                 = 0x00302174 # = 3154292
EVE_REG_BUSYBITS                = 0x003020E8 # = 3154152
EVE_REG_CLOCK                   = 0x00302008 # = 3153928
EVE_REG_CMD_DL                  = 0x00302100 # = 3154176
EVE_REG_CMD_READ                = 0x003020F8 # = 3154168
EVE_REG_CMD_WRITE               = 0x003020FC # = 3154172
EVE_REG_CMDB_SPACE              = 0x00302574 # = 3155316
EVE_REG_CMDB_WRITE              = 0x00302578 # = 3155320
EVE_REG_CPURESET                = 0x00302020 # = 3153952
EVE_REG_CRC                     = 0x00302178 # = 3154296
EVE_REG_CSPREAD                 = 0x00302068 # = 3154024
EVE_REG_CTOUCH_EXTENDED         = 0x00302108 # = 3154184
EVE_REG_CTOUCH_TOUCH0_XY        = 0x00302124 # = 3154212
EVE_REG_CTOUCH_TOUCH1_XY        = 0x0030211C # = 3154204
EVE_REG_CTOUCH_TOUCH2_XY        = 0x0030218C # = 3154316
EVE_REG_CTOUCH_TOUCH3_XY        = 0x00302190 # = 3154320
EVE_REG_CTOUCH_TOUCH4_X         = 0x0030216C # = 3154284
EVE_REG_CTOUCH_TOUCH4_Y         = 0x00302120 # = 3154208
EVE_REG_CYA_TOUCH               = 0x00302168 # = 3154280
EVE_REG_DATESTAMP               = 0x00302564 # = 3155300
EVE_REG_DITHER                  = 0x00302060 # = 3154016
EVE_REG_DLSWAP                  = 0x00302054 # = 3154004
EVE_REG_FRAMES                  = 0x00302004 # = 3153924
EVE_REG_FREQUENCY               = 0x0030200C # = 3153932
EVE_REG_GPIO                    = 0x00302094 # = 3154068
EVE_REG_GPIO_DIR                = 0x00302090 # = 3154064
EVE_REG_GPIOX                   = 0x0030209C # = 3154076
EVE_REG_GPIOX_DIR               = 0x00302098 # = 3154072
EVE_REG_HCYCLE                  = 0x0030202C # = 3153964
EVE_REG_HOFFSET                 = 0x00302030 # = 3153968
EVE_REG_HSIZE                   = 0x00302034 # = 3153972
EVE_REG_HSYNC0                  = 0x00302038 # = 3153976
EVE_REG_HSYNC1                  = 0x0030203C # = 3153980
EVE_REG_ID                      = 0x00302000 # = 3153920
EVE_REG_INT_EN                  = 0x003020AC # = 3154092
EVE_REG_INT_FLAGS               = 0x003020A8 # = 3154088
EVE_REG_INT_MASK                = 0x003020B0 # = 3154096
EVE_REG_MACRO_0                 = 0x003020D8 # = 3154136
EVE_REG_MACRO_1                 = 0x003020DC # = 3154140
EVE_REG_MEDIAFIFO_READ          = 0x00309014 # = 3182612
EVE_REG_MEDIAFIFO_WRITE         = 0x00309018 # = 3182616
EVE_REG_OUTBITS                 = 0x0030205C # = 3154012
EVE_REG_PATCHED_ANALOG          = 0x00302170 # = 3154288
EVE_REG_PATCHED_TOUCH_FAT     = 0x0030216C # = 3154284
EVE_REG_PCLK                    = 0x00302070 # = 3154032
EVE_REG_PCLK_POL                = 0x0030206C # = 3154028
EVE_REG_PLAY                    = 0x0030208C # = 3154060
EVE_REG_PLAYBACK_FORMAT         = 0x003020C4 # = 3154116
EVE_REG_PLAYBACK_FREQ           = 0x003020C0 # = 3154112
EVE_REG_PLAYBACK_LENGTH         = 0x003020B8 # = 3154104
EVE_REG_PLAYBACK_LOOP           = 0x003020C8 # = 3154120
EVE_REG_PLAYBACK_PLAY           = 0x003020CC # = 3154124
EVE_REG_PLAYBACK_READPTR        = 0x003020BC # = 3154108
EVE_REG_PLAYBACK_START          = 0x003020B4 # = 3154100
EVE_REG_PWM_DUTY                = 0x003020D4 # = 3154132
EVE_REG_PWM_HZ                  = 0x003020D0 # = 3154128
EVE_REG_RENDERMODE              = 0x00302010 # = 3153936
EVE_REG_ROMSUB_SEL              = 0x003020F0 # = 3154160
EVE_REG_ROTATE                  = 0x00302058 # = 3154008
EVE_REG_SNAPFORMAT              = 0x0030201C # = 3153948
EVE_REG_SNAPSHOT                = 0x00302018 # = 3153944
EVE_REG_SNAPY                   = 0x00302014 # = 3153940
EVE_REG_SOUND                   = 0x00302088 # = 3154056
EVE_REG_SPI_EARLY_TX            = 0x0030217C # = 3154300
EVE_REG_SPI_WIDTH               = 0x00302188 # = 3154312
EVE_REG_SWIZZLE                 = 0x00302064 # = 3154020
EVE_REG_TAG                     = 0x0030207C # = 3154044
EVE_REG_TAG_X                   = 0x00302074 # = 3154036
EVE_REG_TAG_Y                   = 0x00302078 # = 3154040
EVE_REG_TAP_CRC                 = 0x00302024 # = 3153956
EVE_REG_TAP_MASK                = 0x00302028 # = 3153960
EVE_REG_TOUCH_ADC_MODE          = 0x00302108 # = 3154184
EVE_REG_TOUCH_CHARGE            = 0x0030210C # = 3154188
EVE_REG_TOUCH_DIRECT_XY         = 0x0030218C # = 3154316
EVE_REG_TOUCH_DIRECT_Z1Z2       = 0x00302190 # = 3154320
EVE_REG_TOUCH_FAT             = 0x00302170 # = 3154288
EVE_REG_TOUCH_MODE              = 0x00302104 # = 3154180
EVE_REG_TOUCH_OVERSAMPLE        = 0x00302114 # = 3154196
EVE_REG_TOUCH_RAW_XY            = 0x0030211C # = 3154204
EVE_REG_TOUCH_RZ                = 0x00302120 # = 3154208
EVE_REG_TOUCH_RZTHRESH          = 0x00302118 # = 3154200
EVE_REG_TOUCH_SCREEN_XY         = 0x00302124 # = 3154212
EVE_REG_TOUCH_SETTLE            = 0x00302110 # = 3154192
EVE_REG_TOUCH_TAG               = 0x0030212C # = 3154220
EVE_REG_TOUCH_TAG_XY            = 0x00302128 # = 3154216
EVE_REG_TOUCH_TAG1              = 0x00302134 # = 3154228
EVE_REG_TOUCH_TAG1_XY           = 0x00302130 # = 3154224
EVE_REG_TOUCH_TAG2              = 0x0030213C # = 3154236
EVE_REG_TOUCH_TAG2_XY           = 0x00302138 # = 3154232
EVE_REG_TOUCH_TAG3              = 0x00302144 # = 3154244
EVE_REG_TOUCH_TAG3_XY           = 0x00302140 # = 3154240
EVE_REG_TOUCH_TAG4              = 0x0030214C # = 3154252
EVE_REG_TOUCH_TAG4_XY           = 0x00302148 # = 3154248
EVE_REG_TOUCH_TRANSFORM_A       = 0x00302150 # = 3154256
EVE_REG_TOUCH_TRANSFORM_B       = 0x00302154 # = 3154260
EVE_REG_TOUCH_TRANSFORM_C       = 0x00302158 # = 3154264
EVE_REG_TOUCH_TRANSFORM_D       = 0x0030215C # = 3154268
EVE_REG_TOUCH_TRANSFORM_E       = 0x00302160 # = 3154272
EVE_REG_TOUCH_TRANSFORM_F       = 0x00302164 # = 3154276
EVE_REG_TRACKER                 = 0x00309000 # = 3182592
EVE_REG_TRACKER_1               = 0x00309004 # = 3182596
EVE_REG_TRACKER_2               = 0x00309008 # = 3182600
EVE_REG_TRACKER_3               = 0x0030900C # = 3182604
EVE_REG_TRACKER_4               = 0x00309010 # = 3182608
EVE_REG_TRIM                    = 0x00302180 # = 3154304
EVE_REG_VCYCLE                  = 0x00302040 # = 3153984
EVE_REG_VOFFSET                 = 0x00302044 # = 3153988
EVE_REG_VOL_PB                  = 0x00302080 # = 3154048
EVE_REG_VOL_SOUND               = 0x00302084 # = 3154052
EVE_REG_VSIZE                   = 0x00302048 # = 3153992
EVE_REG_VSYNC0                  = 0x0030204C # = 3153996
EVE_REG_VSYNC1                  = 0x00302050 # = 3154000

def EVE_ENC_ALPHA_FUNC(func,ref):
	return ((0x9 << 24)|(((func) & 0x7) << 8)|(((ref) & 0xff) << 0))
def EVE_ENC_BEGIN(prim):
	return ((0x1f << 24)|(((prim)&15) << 0))
def EVE_ENC_BITMAP_HANDLE(handle):
	return ((0x5 << 24)|(((handle) & 0x1f) << 0))
def EVE_ENC_BITMAP_LAYOUT_H(linestride,height):
	return ((0x28 << 24)|(((linestride) & 0x3) << 2)|(((height) & 0x3) << 0))
def EVE_ENC_BITMAP_LAYOUT(format,linestride,height):
	return ((0x7 << 24)|(((format) & 0x1f) << 19)|(((linestride) & 0x3ff) << 9)|(((height) & 0x1ff) << 0))
def EVE_ENC_BITMAP_SIZE_H(width,height):
	return ((0x29 << 24)|(((width) & 0x3) << 2)|(((height) & 0x3) << 0))
def EVE_ENC_BITMAP_SIZE(filter,wrapx,wrapy,width,height):
	return ((0x8 << 24)|(((filter) & 0x1) << 20)|(((wrapx) & 0x1) << 19)|(((wrapy) & 0x1) << 18)|(((width) & 0x1ff) << 9)|(((height) & 0x1ff) << 0))
def EVE_ENC_BITMAP_SOURCE(addr):
	return ((0x1 << 24)|(((addr) & 0x3FFFFF) << 0))
def EVE_ENC_BITMAP_TRANSFORM_A(p,a):
	return ((0x15 << 24)|((((a)) & 0x1FFFF) << 0))
def EVE_ENC_BITMAP_TRANSFORM_B(p,b):
	return ((0x16 << 24)|((((b)) & 0x1FFFF) << 0))
def EVE_ENC_BITMAP_TRANSFORM_C(c):
	return ((0x17 << 24)|((((c)) & 0xFFFFFF) << 0))
def EVE_ENC_BITMAP_TRANSFORM_D(p,d):
	return ((0x18 << 24)|((((d)) & 0x1FFFF) << 0))
def EVE_ENC_BITMAP_TRANSFORM_E(p,e):
	return ((0x19 << 24)|((((e)) & 0x1FFFF) << 0))
def EVE_ENC_BITMAP_TRANSFORM_F(f):
	return ((0x1a << 24)|((((f)) & 0xFFFFFF) << 0))
def EVE_ENC_BLEND_FUNC(src,dst):
	return ((0xb << 24)|(((src) & 0x7) << 3)|(((dst) & 0x7) << 0))
def EVE_ENC_CALL(dest):
	return ((0x1d << 24)|(((dest) & 0xFFFF) << 0))
def EVE_ENC_CELL(cell):
	return ((0x6 << 24)|(((cell) & 0x7f) << 0))
def EVE_ENC_CLEAR_COLOR_A(alpha):
	return ((0xf << 24)|(((alpha) & 0xff) << 0))
def EVE_ENC_CLEAR_COLOR_RGB(red,green,blue):
	return ((0x2 << 24)|(((red) & 0xff) << 16)|(((green) & 0xff) << 8)|(((blue) & 0xff) << 0))
def EVE_ENC_CLEAR_COLOR(c):
	return ((0x2 << 24)|(((c)) & 0x00ffffff))
def EVE_ENC_CLEAR_STENCIL(s):
	return ((0x11 << 24)|((((s)) & 0xff) << 0))
def EVE_ENC_CLEAR_TAG(s):
	return ((0x12 << 24)|((((s)) & 0xff) << 0))
def EVE_ENC_CLEAR(c,s,t):
	return ((0x26 << 24)|((((c)) & 0x1) << 2)|((((s)) & 0x1) << 1)|((((t)) & 0x1) << 0))
def EVE_ENC_COLOR_A(alpha):
	return ((0x10 << 24)|(((alpha) & 0xff) << 0))
def EVE_ENC_COLOR_MASK(r,g,b,a):
	return ((0x20 << 24)|((((r)) & 0x1) << 3)|((((g)) & 0x1) << 2)|((((b)) & 0x1) << 1)|((((a)) & 0x1) << 0))
def EVE_ENC_COLOR_RGB(red,green,blue):
	return ((0x4 << 24)|(((red) & 0xff) << 16)|(((green) & 0xff) << 8)|(((blue) & 0xff) << 0))
def EVE_ENC_COLOR(c):
	return ((0x4 << 24)|(((c)) & 0x00ffffff))
def EVE_ENC_DISPLAY():
	return ((0x0 << 24))
def EVE_ENC_END():
	return ((0x21 << 24))
def EVE_ENC_JUMP(dest):
	return ((0x1e << 24)|(((dest) & 0xFFFF) << 0))
def EVE_ENC_LINE_WIDTH(width):
	return ((0xe << 24)|(((width) & 0xFFF) << 0))
def EVE_ENC_MACRO(m):
	return ((0x25 << 24)|((((m)) & 0x1) << 0))
def EVE_ENC_NOP():
	return ((0x2d << 24))
def EVE_ENC_PALETTE_SOURCE(addr):
	return ((0x2a << 24)|(((addr) & 0x3FFFFF) << 0))
def EVE_ENC_POINT_SIZE(size):
	return ((0xd << 24)|(((size) & 0x1FFF) << 0))
def EVE_ENC_RESTORE_CONTEXT():
	return ((0x23 << 24))
def EVE_ENC_RETURN():
	return ((0x24 << 24))
def EVE_ENC_SAVE_CONTEXT():
	return ((0x22 << 24))
def EVE_ENC_SCISSOR_SIZE(width,height):
	return ((0x1c << 24)|(((width) & 0xFFF) << 12)|(((height) & 0xFFF) << 0))
def EVE_ENC_SCISSOR_XY(x,y):
	return ((0x1b << 24)|((((x)) & 0x7FF) << 11)|((((y)) & 0x7FF) << 0))
def EVE_ENC_STENCIL_FUNC(func,ref,mask):
	return ((0xa << 24)|(((func) & 0x7) << 16)|(((ref) & 0xff) << 8)|(((mask) & 0xff) << 0))
def EVE_ENC_STENCIL_MASK(mask):
	return ((0x13 << 24)|(((mask) & 0xff) << 0))
def EVE_ENC_STENCIL_OP(sfail,spass):
	return ((0xc << 24)|(((sfail) & 0x7) << 3)|(((spass) & 0x7) << 0))
def EVE_ENC_TAG_MASK(mask):
	return ((0x14 << 24)|(((mask) & 0x1) << 0))
def EVE_ENC_TAG(s):
	return ((0x3 << 24)|((((s)) & 0xff) << 0))
def EVE_ENC_VERTEX_FORMAT(frac):
	return ((0x27 << 24)|(((frac) & 0x7) << 0))
def EVE_ENC_VERTEX_TRANSLATE_X(x):
	return ((0x2b << 24)|((((x)) & 0x1FFFF) << 0))
def EVE_ENC_VERTEX_TRANSLATE_Y(y):
	return ((0x2c << 24)|((((y)) & 0x1FFFF) << 0))
def EVE_ENC_BITMAP_EXT_FORMAT(format):
	return ((46<<24)|(((format)&0x0FFFF)<<0))
def EVE_ENC_VERTEX2F(x,y):
	return ((0x1 << 30)|((((x)) & 0xffff) << 15)|((((y)) & 0xffff) << 0))
def EVE_ENC_VERTEX2II(x,y,handle,cell):
	return ((0x2 << 30)|((((x)) & 0x1ff) << 21)|((((y)) & 0x1ff) << 12)|(((handle) & 0x1f) << 7)|(((cell) & 0x7f) << 0))

EVE_ENC_CMD_APPEND              = 0xFFFFFF1E # = 4294967070
EVE_ENC_CMD_BGCOLOR             = 0xFFFFFF09 # = 4294967049
EVE_ENC_CMD_BITMAP_TRANSFORM    = 0xFFFFFF21 # = 4294967073
EVE_ENC_CMD_BUTTON              = 0xFFFFFF0D # = 4294967053
EVE_ENC_CMD_CALIBRATE           = 0xFFFFFF15 # = 4294967061
EVE_ENC_CMD_CLOCK               = 0xFFFFFF14 # = 4294967060
EVE_ENC_CMD_COLDSTART           = 0xFFFFFF32 # = 4294967090
EVE_ENC_CMD_CRC                 = 0xFFFFFF03 # = 4294967043
EVE_ENC_CMD_CSKETCH             = 0xFFFFFF35 # = 4294967093
EVE_ENC_CMD_DIAL                = 0xFFFFFF2D # = 4294967085
EVE_ENC_CMD_DLSTART             = 0xFFFFFF00 # = 4294967040
EVE_ENC_CMD_EXECUTE             = 0xFFFFFF07 # = 4294967047
EVE_ENC_CMD_FGCOLOR             = 0xFFFFFF0A # = 4294967050
EVE_ENC_CMD_GAUGE               = 0xFFFFFF13 # = 4294967059
EVE_ENC_CMD_GETMATRIX           = 0xFFFFFF33 # = 4294967091
EVE_ENC_CMD_GETPOINT            = 0xFFFFFF08 # = 4294967048
EVE_ENC_CMD_GETPROPS            = 0xFFFFFF25 # = 4294967077
EVE_ENC_CMD_GETPTR              = 0xFFFFFF23 # = 4294967075
EVE_ENC_CMD_GRADCOLOR           = 0xFFFFFF34 # = 4294967092
EVE_ENC_CMD_GRADIENT            = 0xFFFFFF0B # = 4294967051
EVE_ENC_CMD_HAMMERAUX           = 0xFFFFFF04 # = 4294967044
EVE_ENC_CMD_IDCT_DELETED        = 0xFFFFFF06 # = 4294967046
EVE_ENC_CMD_INFLATE             = 0xFFFFFF22 # = 4294967074
EVE_ENC_CMD_INT_RAMSHARED       = 0xFFFFFF3D # = 4294967101
EVE_ENC_CMD_INT_SWLOADIMAGE     = 0xFFFFFF3E # = 4294967102
EVE_ENC_CMD_INTERRUPT           = 0xFFFFFF02 # = 4294967042
EVE_ENC_CMD_KEYS                = 0xFFFFFF0E # = 4294967054
EVE_ENC_CMD_LOADIDENTITY        = 0xFFFFFF26 # = 4294967078
EVE_ENC_CMD_LOADIMAGE           = 0xFFFFFF24 # = 4294967076
EVE_ENC_CMD_LOGO                = 0xFFFFFF31 # = 4294967089
EVE_ENC_CMD_MARCH               = 0xFFFFFF05 # = 4294967045
EVE_ENC_CMD_MEDIAFIFO           = 0xFFFFFF39 # = 4294967097
EVE_ENC_CMD_MEMCPY              = 0xFFFFFF1D # = 4294967069
EVE_ENC_CMD_MEMCRC              = 0xFFFFFF18 # = 4294967064
EVE_ENC_CMD_MEMSET              = 0xFFFFFF1B # = 4294967067
EVE_ENC_CMD_MEMWRITE            = 0xFFFFFF1A # = 4294967066
EVE_ENC_CMD_MEMZERO             = 0xFFFFFF1C # = 4294967068
EVE_ENC_CMD_NUMBER              = 0xFFFFFF2E # = 4294967086
EVE_ENC_CMD_PLAYVIDEO           = 0xFFFFFF3A # = 4294967098
EVE_ENC_CMD_PROGRESS            = 0xFFFFFF0F # = 4294967055
EVE_ENC_CMD_REGREAD             = 0xFFFFFF19 # = 4294967065
EVE_ENC_CMD_ROMFONT             = 0xFFFFFF3F # = 4294967103
EVE_ENC_CMD_ROTATE              = 0xFFFFFF29 # = 4294967081
EVE_ENC_CMD_SCALE               = 0xFFFFFF28 # = 4294967080
EVE_ENC_CMD_SCREENSAVER         = 0xFFFFFF2F # = 4294967087
EVE_ENC_CMD_SCROLLBAR           = 0xFFFFFF11 # = 4294967057
EVE_ENC_CMD_SETBASE             = 0xFFFFFF38 # = 4294967096
EVE_ENC_CMD_SETBITMAP           = 0xFFFFFF43 # = 4294967107
EVE_ENC_CMD_SETFONT             = 0xFFFFFF2B # = 4294967083
EVE_ENC_CMD_SETFONT2            = 0xFFFFFF3B # = 4294967099
EVE_ENC_CMD_SETMATRIX           = 0xFFFFFF2A # = 4294967082
EVE_ENC_CMD_SETROTATE           = 0xFFFFFF36 # = 4294967094
EVE_ENC_CMD_SETSCRATCH          = 0xFFFFFF3C # = 4294967100
EVE_ENC_CMD_SKETCH              = 0xFFFFFF30 # = 4294967088
EVE_ENC_CMD_SLIDER              = 0xFFFFFF10 # = 4294967056
EVE_ENC_CMD_SNAPSHOT            = 0xFFFFFF1F # = 4294967071
EVE_ENC_CMD_SNAPSHOT2           = 0xFFFFFF37 # = 4294967095
EVE_ENC_CMD_SPINNER             = 0xFFFFFF16 # = 4294967062
EVE_ENC_CMD_STOP                = 0xFFFFFF17 # = 4294967063
EVE_ENC_CMD_SWAP                = 0xFFFFFF01 # = 4294967041
EVE_ENC_CMD_SYNC                = 0xFFFFFF42 # = 4294967106
EVE_ENC_CMD_TEXT                = 0xFFFFFF0C # = 4294967052
EVE_ENC_CMD_TOGGLE              = 0xFFFFFF12 # = 4294967058
EVE_ENC_CMD_TOUCH_TRANSFORM     = 0xFFFFFF20 # = 4294967072
EVE_ENC_CMD_TRACK               = 0xFFFFFF2C # = 4294967084
EVE_ENC_CMD_TRANSLATE           = 0xFFFFFF27 # = 4294967079
EVE_ENC_CMD_VIDEOFRAME          = 0xFFFFFF41 # = 4294967105
EVE_ENC_CMD_VIDEOSTART          = 0xFFFFFF40 # = 4294967104

EVE_BEGIN_BITMAPS               = 0x00000001 # = 1
EVE_BEGIN_EDGE_STRIP_A          = 0x00000007 # = 7
EVE_BEGIN_EDGE_STRIP_B          = 0x00000008 # = 8
EVE_BEGIN_EDGE_STRIP_L          = 0x00000006 # = 6
EVE_BEGIN_EDGE_STRIP_R          = 0x00000005 # = 5
EVE_BEGIN_LINE_STRIP            = 0x00000004 # = 4
EVE_BEGIN_LINES                 = 0x00000003 # = 3
EVE_BEGIN_POINTS                = 0x00000002 # = 2
EVE_BEGIN_RECTS                 = 0x00000009 # = 9
EVE_BLEND_DST_ALPHA             = 0x00000003 # = 3
EVE_BLEND_ONE                   = 0x00000001 # = 1
EVE_BLEND_ONE_MINUS_DST_ALPHA   = 0x00000005 # = 5
EVE_BLEND_ONE_MINUS_SRC_ALPHA   = 0x00000004 # = 4
EVE_BLEND_SRC_ALPHA             = 0x00000002 # = 2
EVE_BLEND_ZERO                  = 0x00000000 # = 0
EVE_DLSWAP_DONE                 = 0x00000000 # = 0
EVE_DLSWAP_FRAME                = 0x00000002 # = 2
EVE_DLSWAP_LINE                 = 0x00000001 # = 1
EVE_FILTER_BILINEAR             = 0x00000001 # = 1
EVE_FILTER_NEAREST              = 0x00000000 # = 0
EVE_FORMAT_ARGB1555             = 0x00000000 # = 0
EVE_FORMAT_ARGB2                = 0x00000005 # = 5
EVE_FORMAT_ARGB4                = 0x00000006 # = 6
EVE_FORMAT_BARGRAPH             = 0x0000000B # = 11
EVE_FORMAT_L1                   = 0x00000001 # = 1
EVE_FORMAT_L2                   = 0x00000011 # = 17
EVE_FORMAT_L4                   = 0x00000002 # = 2
EVE_FORMAT_L8                   = 0x00000003 # = 3
EVE_FORMAT_PALETTED             = 0x00000008 # = 8
EVE_FORMAT_PALETTED4444         = 0x0000000F # = 15
EVE_FORMAT_PALETTED565          = 0x0000000E # = 14
EVE_FORMAT_PALETTED8            = 0x00000010 # = 16
EVE_FORMAT_RGB332               = 0x00000004 # = 4
EVE_FORMAT_RGB565               = 0x00000007 # = 7
EVE_FORMAT_TEXT8X8              = 0x00000009 # = 9
EVE_FORMAT_TEXTVGA              = 0x0000000A # = 10
EVE_INT_CMDEMPTY                = 0x00000020 # = 32
EVE_INT_CMDFLAG                 = 0x00000040 # = 64
EVE_INT_CONVCOMPLETE            = 0x00000080 # = 128
EVE_INT_G8                      = 0x00000012 # = 18
EVE_INT_L8C                     = 0x0000000C # = 12
EVE_INT_PLAYBACK                = 0x00000010 # = 16
EVE_INT_SOUND                   = 0x00000008 # = 8
EVE_INT_SWAP                    = 0x00000001 # = 1
EVE_INT_TAG                     = 0x00000004 # = 4
EVE_INT_TOUCH                   = 0x00000002 # = 2
EVE_INT_VGA                     = 0x0000000D # = 13
EVE_LINEAR_SAMPLES              = 0x00000000 # = 0
EVE_OPT_CENTER                  = 0x00000600 # = 1536
EVE_OPT_CENTERX                 = 0x00000200 # = 512
EVE_OPT_CENTERY                 = 0x00000400 # = 1024
EVE_OPT_FLAT                    = 0x00000100 # = 256
EVE_OPT_FULLSCREEN              = 0x00000008 # = 8
EVE_OPT_MEDIAFIFO               = 0x00000010 # = 16
EVE_OPT_MONO                    = 0x00000001 # = 1
EVE_OPT_NOBACK                  = 0x00001000 # = 4096
EVE_OPT_NODL                    = 0x00000002 # = 2
EVE_OPT_NOHANDS                 = 0x0000C000 # = 49152
EVE_OPT_NOHM                    = 0x00004000 # = 16384
EVE_OPT_NOPOINTER               = 0x00004000 # = 16384
EVE_OPT_NOSECS                  = 0x00008000 # = 32768
EVE_OPT_NOTEAR                  = 0x00000004 # = 4
EVE_OPT_NOTICKS                 = 0x00002000 # = 8192
EVE_OPT_RIGHTX                  = 0x00000800 # = 2048
EVE_OPT_SIGNED                  = 0x00000100 # = 256
EVE_OPT_SOUND                   = 0x00000020 # = 32
EVE_STENCIL_DECR                = 0x00000004 # = 4
EVE_STENCIL_INCR                = 0x00000003 # = 3
EVE_STENCIL_INVERT              = 0x00000005 # = 5
EVE_STENCIL_KEEP                = 0x00000001 # = 1
EVE_STENCIL_REPLACE             = 0x00000002 # = 2
EVE_STENCIL_ZERO                = 0x00000000 # = 0
EVE_TEST_ALWAYS                 = 0x00000007 # = 7
EVE_TEST_EQUAL                  = 0x00000005 # = 5
EVE_TEST_GEQUAL                 = 0x00000004 # = 4
EVE_TEST_GREATER                = 0x00000003 # = 3
EVE_TEST_LEQUAL                 = 0x00000002 # = 2
EVE_TEST_LESS                   = 0x00000001 # = 1
EVE_TEST_NEVER                  = 0x00000000 # = 0
EVE_TEST_NOTEQUAL               = 0x00000006 # = 6
EVE_TOUCHMODE_CONTINUOUS        = 0x00000003 # = 3
EVE_TOUCHMODE_FRAME             = 0x00000002 # = 2
EVE_TOUCHMODE_OFF               = 0x00000000 # = 0
EVE_TOUCHMODE_ONESHOT           = 0x00000001 # = 1
EVE_ULAW_SAMPLES                = 0x00000001 # = 1
EVE_VOL_ZERO                    = 0x00000000 # = 0
EVE_WRAP_BORDER                 = 0x00000000 # = 0
EVE_WRAP_REPEAT                 = 0x00000001 # = 1
EVE_ADC_DIFFERENTIAL            = 0x00000001 # = 1
EVE_ADC_SINGLE_ENDED            = 0x00000000 # = 0
EVE_ADPCM_SAMPLES               = 0x00000002 # = 2

EVE_REG_TOUCH_CONFIG            = 0x00302168 # = 3154280
EVE_CTOUCH_MODE_COMPATIBILITY   = 0x00000001 # = 1
EVE_CTOUCH_MODE_EXTENDED        = 0x00000000 # = 0