#!/usr/bin/python
import time
import sphero_driver
import sys
sp = sphero_driver.Sphero()

sp.connect()
#sp.set_raw_data_strm(40, 1 , 0, False)

#sp.start()
sp.set_rgb_led(255,0,0,0,False)
time.sleep(1)
sp.set_rgb_led(0,255,0,0,False)
time.sleep(1)
sp.set_rgb_led(0,0,255,0,False)
time.sleep(1)
#sp.set_heading(180, False)
#time.sleep(3)
sp.roll(100, 0, 1, False)
time.sleep(1)
sp.roll(100, 90, 1, False)
time.sleep(1)
sp.roll(100, 180, 1, False)
time.sleep(1)
sp.roll(100, 270, 1, False)
time.sleep(1)
#sphero.join()
#sphero.disconnect()
sys.exit(1)



