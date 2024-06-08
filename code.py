import time

import analogio
import board

FWD = analogio.AnalogIn(board.A3)
REF = analogio.AnalogIn(board.A2)

# i2c = busio.I2C(scl=board.GP27, sda=board.GP26)

# si5351 = adafruit_si5351.SI5351(i2c)


def _voltage(device):
    return device.value / 65535 * device.reference_voltage


def setFrequency(frequency, si5351):
    xtalFreq = XTAL_FREQ
    divider = int(900000000 / frequency)
    if divider % 2:
        divider -= 1
    pllFreq = divider * frequency
    mult = int(pllFreq / xtalFreq)
    f = int(pllFreq % xtalFreq)
    f *= 1048575
    f /= xtalFreq
    num = int(f)
    denom = 1048575
    si5351.pll_a.configure_fractional(mult, num, denom)
    si5351.clock_0.configure_integer(si5351.pll_a, divider)


# si5351.outputs_enabled = True
# setFrequency(((144) * 1000), si5351)
print(str(FWD.reference_voltage))

while True:
    print("FWD: V:" + str(_voltage(FWD)))
    print("REF: V:" + str(_voltage(REF)))
    #    print("Measured Frequency: {0:0.3f} MHz".format(si5351.clock_0.frequency / 1000000))
    time.sleep(1)


#    if mode == 'peak':
#        SmartPWR.rf1_ppower()
#    if mode == 'average':
#        SmartPWR.rf1_apower()
#
#    if SmartPWR.btn.value is False:
#        print('btn')
#        if mode is 'peak':
#            mode = 'average';
#            OLED.printTitle("AVG  Pwr")
#        elif mode is 'average':
#            mode = 'peak'
#            OLED.printTitle("PEAK Pwr")
#        time.sleep(.5)
