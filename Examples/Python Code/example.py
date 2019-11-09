"""An example of how to use the light parser for parsing UBX messages from a serial device."""

import serial
import light_ubx_parser


def run():
    port = serial.Serial('/dev/serial0', baudrate=9600, timeout=0.1)
    port.open()

    parser = light_ubx_parser.LightParser(port)

    parser.register_msg_type(0x01, 0x07, 'NAV_PVT', 'LHBBBBBBLlBBBBllllLLlllllLLHxxxxxxlhH',
                             'iTOW', 'year', 'month', 'day', 'hour', 'min', 'sec', 'valid',
                             'tAcc', 'nano', 'fixType', 'flags', 'flags2', 'numSV', 'lon',
                             'lat', 'height', 'hMSL', 'hAcc', 'vAcc', 'velN', 'velE', 'velD',
                             'gSpeed', 'headMot', 'sAcc', 'headAcc', 'pDOP', 'headVeh',
                             'magDec', 'magAcc')

    parser.register_msg_type(0x01, 0x05, 'NAV_ATT', 'LBxxxlllLLL', 'iTOW', 'version', 'roll',
                             'pitch', 'heading', 'accRoll', 'accPitch', 'accHeading')

    print("Starting to listen for UBX packets")

    while True:
        try:
            msg = parser.receive_message()
            print(msg)

        except (ValueError, IOError) as err:
            print(err)

        finally:
            port.close()


if __name__ == '__main__':
    run()
