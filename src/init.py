'''

	init.py

	This file sets up the display so that it's ready for use later in. This
	should make developing UI code a little easier, as none of the boilerplate
	stuff clutters up program code.

'''

# low-level hardware control stuff
import machine	# allows low level control of the hardware

spi_bus = machine.SPI.Bus(host=1, mosi=13, sck=14)	# defines what the SPI bus on this machine is (used for general communication between devices)

import lcd_bus	# handles controlling the LCD for us
display_bus = lcd_bus.SPIBus(spi_bus=spi_bus, freq=24_000_000, dc=2, cs=15)


# LVGL (graphics library) setup
import lvgl as lv
import ili9341	# this is the exact display we're using

display = ili9341.ILI9341(
	data_bus = display_bus,
	display_width = 320,
	display_height = 240,
	backlight_pin = 21,
	backlight_on_state = ili9341.STATE_PWM,
	color_space = lv.COLOR_FORMAT.RGB565,
	color_byte_order = ili9341.BYTE_ORDER_BGR,
	rgb565_byte_swap = 1
)

display.set_power(True)
display.init(1)

display._ORIENTATION_TABLE = (0xE0, 0x0, 0x0, 0x0)
display.set_rotation(lv.DISPLAY_ROTATION._0)

display.set_backlight(100)


# handles tasks (obviously)
import task_handler
task_handler.TaskHandler()
