# DeadReckoner
This is a series of carrier boards for the U-blox NEO-M8U GNSS (multi-constelation support) module with the worlds first untethered dead reckoning capability. These boards provide far superior location accuracy in areas of poor signal coverage. The modules also contains a backup battery which allows it to start navigating immediately on startup (if it has not been moved since shutdown).
See [the U-blox website](https://www.u-blox.com/en/product/neo-m8u-module) for more info.

## Module Versions
There are two versions of the DeadReckoner Module;
1. The original version based on a Raspberry Pi form factor
2. A new compact model that allows for custom connections.

## Quick Start
See [the wiki](https://github.com/dalymople/DeadReckoner/wiki) for guides on using these modules.

## NEO-M8U Specs
The module provides:
- Independent of any electrical connection to the car
- Positioning accuracy in dense cities and covered areas
- Complete positioning solution with integrated 3D sensors
- Compatible with all modules of the NEO family
- Real‑time positioning update rate of up to 20 Hz
- Professional grade module
- Immediate navigation on startup (with backup battery)

## PCB Specifications
- Supply voltage 5V or 3V3 (5V only on the Raspberry Pi version)
- Current requirement max 67mA, typical 29mA
- Digital IO voltage, 3V3
- Dimensions 65mm x 35mm (RPi) 52mm x 36.5mm (Compact)
- Time to first fix: cold start 26 to 57s, hot start 1.5s
- Horizontal position accuracy: 2.5m
- Velocity accuracy: 0.5m/s
- Heading accuracy: 1 degree
- Position error during signal loss: 10% distance travelled (<60sec signal loss)
- Operational limits: dynamics ≤ 4 g, altitude 50,000 m, velocity 500 m/s

## Interfaces
The NEO-M8U supports the following connections:
- I2C / TWI / DDC **default**
- 3.3V UART
- SPI
- Micro USB (No connection to header)
- External interrupt
- Pulse per second
- Reset
- Power LED
- USB LED (Only on RPi version)
- Pulse per second LED

## Errors and Ommissions
**Version 2**
- No errors or ommissions have been found for this board. Please submitt an issue if you find any problems with the module.
