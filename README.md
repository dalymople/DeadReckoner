# DeadReckoner
This is a carrier board for the U-blox NEO-M8U GNSS (multi-constelation support) module with the worlds first untethered dead reckoning capability. This provides far superior location accuracy in areas of poor signal coverage. This module also contains a backup battery which allows the module to start navigating immediately on startup (if it has not been moved since shutdown).
See [the U-blox website](https://www.u-blox.com/en/product/neo-m8u-module) for more info.

## Guides
See the wiki for guides on using this module...

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
- Supply voltage 5V, via the 40 Pin header pins 2, 4 Gnd via pins 6, 9, 14, 20, 25, 30, 34, 39
- Current requirement max 67mA, typical 29mA
- Digital IO voltage, 3V3
- Dimensions 65mm x 35mm
- Time to first fix: cold start 26 to 57s, hot start 1.5s
- Horizontal position accuracy: 2.5m
- Velocity accuracy: 0.5m/s
- Heading accuracy: 1 degree
- Position error during signal loss: 10% distance travelled (<60sec signal loss)
- Operational limits: dynamics ≤ 4 g, altitude 50,000 m, velocity 500 m/s

## Interfaces
This pcb has an inbuilt raspberry 40 pin header for direct connection to a Raspberry Pi. The NEO-M8U supports the following connections:
- I2C / TWI / DDC (Pi I2C bus 1) **default**
- 3.3V UART (Pi '/dev/serial0')
- SPI (Pi SPI bus 0)
- Micro USB (No connection to header)
- External interrupt (Pi GPIO 11)
- Pulse per second (Pi GPIO 13)
- Reset (Pi GPIO 15)
- Power LED
- USB LED
- Pulse per second LED

If the default connections are not suitable for your application you can solder wires to the pads provided for each signal.

## Jumpers
By default the I2C port is the only signal connected to the header, however solder jumpers are provided for connecting the other signals through the header, the jumper have no effect on the solder pads for each signal. 
**NB.** The SPI bus is physically connected to the UART and I2C bus, please use the below compatability matrix for which jumpers should be closed [x], open [ ] or no effect `-`.

| **Jumper**  	| I2C 	| UART 	| SPI 	|
|-------------	|-----	|------	|-----	|
| JP1 (D_SEL) 	| [ ]  	| [ ]  	| [x] 	|
| JP2         	| -   	| -    	| -   	|
| JP3         	| [x] default 	| -    	| [ ]  	|
| JP4         	| [x] default 	| -    	| [ ]  	|
| JP5         	| -   	| [x]  	| [ ]  	|
| JP6         	| -   	| [x]  	| [ ]  	|
| JP7         	| -   	| -    	| -   	|
| JP8         	| -   	| -    	| -   	|
| JP9         	| -   	| -    	| -   	|
| JP10        	| [ ]  	| -    	| [x] 	|
| JP11        	| -   	| [ ]  	| [x] 	|
| JP12        	| -   	| [ ]  	| [x] 	|
| JP13        	| [ ]  	|      	| [x] 	|

## USB Connection
The NEO-M8U has a full speed USB 2.0 host and the micro USB connector allows the module to be connected to a computer. When connected the device will enumerate as a COM port, U-blox website for more information and for USB drivers. **NB.** The usb port will not function unless the module is powered.

## Errors and Ommissions
**Version 1**
- No errors or ommissions have been found for this board. Please submitt an issue if you find any problems with the module.
