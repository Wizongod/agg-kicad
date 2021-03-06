"""
build_lib_ic.py
Copyright 2016 Adam Greig
Licensed under the MIT licence, see LICENSE file for details.

Generate symbols for generic black-box ICs etc.
"""

from __future__ import print_function, division

# Symbols configuration =======================================================
# Dictionary of dictionaries.
# Top keys are symbol names.
# Configuration format is:
# path: optional, sub-directory(s) to store the library in. Defaults to ".".
# designator: optional, default "IC", the default reference designator
# footprint: optional, an associated footprint to autofill
# datasheet: optional, a URL or path to a datasheet
# ordercodes: optional, list of (supplier, code) for supplier order codes
# description: description of the part, placed in the .dcm file
# pins: list of lists of left and right pin groups
#           (blocks of related pins with a space in-between).
#       Each group contains a list of tuples of:
#           (pin name, pin number, electrical type).
#       Number and name may be given as a string or an integer.
#       Electrical type must be a string out of:
#           in, out, bidi, tri, passive, unspec, pwrin, pwrout, oc, oe, nc.
#       These correspond to input, output, bidirectional, tristate, passive,
#           unspecified, power_input, power_output, open_collector,
#           open_emitter, and not_connected. They should be given as strings.

config = {

    # STM32F1xxCxUx, in UFQFPN48 package
    "STM32F1xxCxUx": {
        "path": "ic/microcontroller",
        "footprint": "agg:QFN-48-EP-ST",
        "datasheet": "http://www.st.com/st-web-ui/static/active/en"
                     "/resource/technical/document/datasheet/CD00161566.pdf",
        "ordercodes": [("Farnell", "2060891")],
        "description": "STM32F1 48 pin UFQFPN package",
        "pins": [
            [
                [
                    ("VBAT", 1, "pwrin"),
                    ("VDD", 24, "pwrin"),
                    ("VDD", 48, "pwrin"),
                    ("VDDIO2", 36, "pwrin"),
                    ("VDDA", 9, "pwrin"),
                ], [
                    ("VSSA", 8, "pwrin"),
                    ("VSS", 23, "pwrin"),
                    ("VSS", 47, "pwrin"),
                    ("VSS", 35, "pwrin"),
                    ("VSS", "EP", "pwrin"),
                ], [
                    ("BOOT0", 44, "in"),
                    ("NRST", 7, "in"),
                ], [
                    ("PC13", 2, "bidi"),
                    ("PC14", 3, "bidi"),
                    ("PC15", 4, "bidi"),
                ], [
                    ("PF0", 5, "bidi"),
                    ("PF1", 6, "bidi"),
                ],
            ], [
                [
                    ("PA0", 10, "bidi"),
                    ("PA1", 11, "bidi"),
                    ("PA2", 12, "bidi"),
                    ("PA3", 13, "bidi"),
                    ("PA4", 14, "bidi"),
                    ("PA5", 15, "bidi"),
                    ("PA6", 16, "bidi"),
                    ("PA7", 17, "bidi"),
                ], [
                    ("PA8", 29, "bidi"),
                    ("PA9", 30, "bidi"),
                    ("PA10", 31, "bidi"),
                    ("PA11", 32, "bidi"),
                    ("PA12", 33, "bidi"),
                    ("PA13", 34, "bidi"),
                    ("PA14", 37, "bidi"),
                    ("PA15", 38, "bidi"),
                ], [
                    ("PB0", 18, "bidi"),
                    ("PB1", 19, "bidi"),
                    ("PB2", 20, "bidi"),
                    ("PB3", 39, "bidi"),
                    ("PB4", 40, "bidi"),
                    ("PB5", 41, "bidi"),
                    ("PB6", 42, "bidi"),
                    ("PB7", 43, "bidi"),
                ], [
                    ("PB8", 45, "bidi"),
                    ("PB9", 46, "bidi"),
                    ("PB10", 21, "bidi"),
                    ("PB11", 22, "bidi"),
                    ("PB12", 25, "bidi"),
                    ("PB13", 26, "bidi"),
                    ("PB14", 27, "bidi"),
                    ("PB15", 28, "bidi"),
                ],
            ],
        ],
    },

    # STM32F0xxCxTx, in LQFP48 package
    "STM32F0xxCxTx": {
        "path": "ic/microcontroller",
        "footprint": "agg:LQFP-48",
        "datasheet": "http://www.st.com/st-web-ui/static/active/en"
                     "/resource/technical/document/datasheet/DM00090510.pdf",
        "ordercodes": [("Farnell", "2432094")],
        "description": "STM32F0 48 pin LQFP package",
        "pins": [
            [
                [
                    ("VBAT", 1, "pwrin"),
                    ("VDD", 24, "pwrin"),
                    ("VDD", 48, "pwrin"),
                    ("VDDIO2", 36, "pwrin"),
                    ("VDDA", 9, "pwrin"),
                ], [
                    ("VSSA", 8, "pwrin"),
                    ("VSS", 23, "pwrin"),
                    ("VSS", 47, "pwrin"),
                    ("VSS", 35, "pwrin"),
                ], [
                    ("BOOT0", 44, "in"),
                    ("NRST", 7, "in"),
                ], [
                    ("PC13", 2, "bidi"),
                    ("PC14", 3, "bidi"),
                    ("PC15", 4, "bidi"),
                ], [
                    ("PF0", 5, "bidi"),
                    ("PF1", 6, "bidi"),
                ],
            ], [
                [
                    ("PA0", 10, "bidi"),
                    ("PA1", 11, "bidi"),
                    ("PA2", 12, "bidi"),
                    ("PA3", 13, "bidi"),
                    ("PA4", 14, "bidi"),
                    ("PA5", 15, "bidi"),
                    ("PA6", 16, "bidi"),
                    ("PA7", 17, "bidi"),
                ], [
                    ("PA8", 29, "bidi"),
                    ("PA9", 30, "bidi"),
                    ("PA10", 31, "bidi"),
                    ("PA11", 32, "bidi"),
                    ("PA12", 33, "bidi"),
                    ("PA13", 34, "bidi"),
                    ("PA14", 37, "bidi"),
                    ("PA15", 38, "bidi"),
                ], [
                    ("PB0", 18, "bidi"),
                    ("PB1", 19, "bidi"),
                    ("PB2", 20, "bidi"),
                    ("PB3", 39, "bidi"),
                    ("PB4", 40, "bidi"),
                    ("PB5", 41, "bidi"),
                    ("PB6", 42, "bidi"),
                    ("PB7", 43, "bidi"),
                ], [
                    ("PB8", 45, "bidi"),
                    ("PB9", 46, "bidi"),
                    ("PB10", 21, "bidi"),
                    ("PB11", 22, "bidi"),
                    ("PB12", 25, "bidi"),
                    ("PB13", 26, "bidi"),
                    ("PB14", 27, "bidi"),
                    ("PB15", 28, "bidi"),
                ],
            ],
        ],
    },

    # STM32F0xxRxHx, in UFBGA64 package
    "STM32F0xxRxHx": {
        "path": "ic/microcontroller",
        "footprint": "agg:BGA-64-05P-ST",
        "datasheet": "http://www.st.com/st-web-ui/static/active/en"
                     "/resource/technical/document/datasheet/DM00115237.pdf",
        "ordercodes": [("Farnell", "2503242")],
        "description": "STM32F0 64 pin UFBGA package",
        "pins": [
            [
                [
                    ("VBAT", "B2", "pwrin"),
                    ("VDD", "D2", "pwrin"),
                    ("VDD", "E4", "pwrin"),
                    ("VDD", "E5", "pwrin"),
                    ("VDDIO2", "E6", "pwrin"),
                    ("VDDA", "H1", "pwrin"),
                ], [
                    ("VSSA", "F1", "pwrin"),
                    ("VSS", "C2", "pwrin"),
                    ("VSS", "D4", "pwrin"),
                    ("VSS", "D5", "pwrin"),
                    ("VSS", "D6", "pwrin"),
                ], [
                    ("BOOT0", "B4", "in"),
                    ("NRST", "E1", "in"),
                ], [
                    ("PF0", "C1", "bidi"),
                    ("PF1", "D1", "bidi"),
                ], [
                    ("PA0", "G2", "bidi"),
                    ("PA1", "H2", "bidi"),
                    ("PA2", "F3", "bidi"),
                    ("PA3", "G3", "bidi"),
                    ("PA4", "H3", "bidi"),
                    ("PA5", "F4", "bidi"),
                    ("PA6", "G4", "bidi"),
                    ("PA7", "H4", "bidi"),
                ], [
                    ("PA8", "D7", "bidi"),
                    ("PA9", "C7", "bidi"),
                    ("PA10", "C6", "bidi"),
                    ("PA11", "C8", "bidi"),
                    ("PA12", "B8", "bidi"),
                    ("PA13", "A8", "bidi"),
                    ("PA14", "A7", "bidi"),
                    ("PA15", "A6", "bidi"),
                ],
            ], [
                [
                    ("PB0", "F5", "bidi"),
                    ("PB1", "G5", "bidi"),
                    ("PB2", "G6", "bidi"),
                    ("PB3", "A5", "bidi"),
                    ("PB4", "A4", "bidi"),
                    ("PB5", "C4", "bidi"),
                    ("PB6", "D3", "bidi"),
                    ("PB7", "C3", "bidi"),
                ], [
                    ("PB8", "B3", "bidi"),
                    ("PB9", "A3", "bidi"),
                    ("PB10", "G7", "bidi"),
                    ("PB11", "H7", "bidi"),
                    ("PB12", "H8", "bidi"),
                    ("PB13", "G8", "bidi"),
                    ("PB14", "F8", "bidi"),
                    ("PB15", "F7", "bidi"),
                ], [
                    ("PC0", "E3", "bidi"),
                    ("PC1", "E2", "bidi"),
                    ("PC2", "F2", "bidi"),
                    ("PC3", "G1", "bidi"),
                    ("PC4", "H5", "bidi"),
                    ("PC5", "H6", "bidi"),
                    ("PC6", "F6", "bidi"),
                    ("PC7", "E7", "bidi"),
                ], [
                    ("PC8", "E8", "bidi"),
                    ("PC9", "D8", "bidi"),
                    ("PC10", "B7", "bidi"),
                    ("PC11", "B6", "bidi"),
                    ("PC12", "C5", "bidi"),
                    ("PC13", "A2", "bidi"),
                    ("PC14", "A1", "bidi"),
                    ("PC15", "B1", "bidi"),
                ], [
                    ("PD2", "B5", "bidi"),
                ]
            ],
        ],
    },

    # STM32F3xxCxTx, in LQFP48 package
    "STM32F3xxCxTx": {
        "path": "ic/microcontroller",
        "footprint": "agg:LQFP-48",
        "datasheet": "http://www.st.com/st-web-ui/static/active/en"
                     "/resource/technical/document/datasheet/DM00058181.pdf",
        "ordercodes": [("Farnell", "2333254")],
        "description": "STM32F3 48 pin LQFP package",
        "pins": [
            [
                [
                    ("VBAT", 1, "pwrin"),
                    ("VDD", 24, "pwrin"),
                    ("VDD", 48, "pwrin"),
                    ("VDD", 36, "pwrin"),
                    ("VDDA", 9, "pwrin"),
                ], [
                    ("VSSA", 8, "pwrin"),
                    ("VSS", 23, "pwrin"),
                    ("VSS", 47, "pwrin"),
                    ("VSS", 35, "pwrin"),
                ], [
                    ("BOOT0", 44, "in"),
                    ("NRST", 7, "in"),
                ], [
                    ("PC13", 2, "bidi"),
                    ("PC14", 3, "bidi"),
                    ("PC15", 4, "bidi"),
                ], [
                    ("PF0", 5, "bidi"),
                    ("PF1", 6, "bidi"),
                ],
            ], [
                [
                    ("PA0", 10, "bidi"),
                    ("PA1", 11, "bidi"),
                    ("PA2", 12, "bidi"),
                    ("PA3", 13, "bidi"),
                    ("PA4", 14, "bidi"),
                    ("PA5", 15, "bidi"),
                    ("PA6", 16, "bidi"),
                    ("PA7", 17, "bidi"),
                ], [
                    ("PA8", 29, "bidi"),
                    ("PA9", 30, "bidi"),
                    ("PA10", 31, "bidi"),
                    ("PA11", 32, "bidi"),
                    ("PA12", 33, "bidi"),
                    ("PA13", 34, "bidi"),
                    ("PA14", 37, "bidi"),
                    ("PA15", 38, "bidi"),
                ], [
                    ("PB0", 18, "bidi"),
                    ("PB1", 19, "bidi"),
                    ("PB2", 20, "bidi"),
                    ("PB3", 39, "bidi"),
                    ("PB4", 40, "bidi"),
                    ("PB5", 41, "bidi"),
                    ("PB6", 42, "bidi"),
                    ("PB7", 43, "bidi"),
                ], [
                    ("PB8", 45, "bidi"),
                    ("PB9", 46, "bidi"),
                    ("PB10", 21, "bidi"),
                    ("PB11", 22, "bidi"),
                    ("PB12", 25, "bidi"),
                    ("PB13", 26, "bidi"),
                    ("PB14", 27, "bidi"),
                    ("PB15", 28, "bidi"),
                ],
            ],
        ],
    },

    # STM32F4xxVxTx, in LQFP100 package
    "STM32F4xxVxTx": {
        "path": "ic/microcontroller",
        "footprint": "agg:LQFP-100",
        "datasheet": "http://www.st.com/st-web-ui/static/active/en"
                     "/resource/technical/document/datasheet/DM00037051.pdf",
        "ordercodes": [("Farnell", "2215224")],
        "description": "STM32F4 100 pin LQFP package",
        "pins": [
            [
                [
                    ("VBAT", 6, "pwrin"),
                    ("VDD", 11, "pwrin"),
                    ("VDD", 19, "pwrin"),
                    ("VDD", 28, "pwrin"),
                    ("VDD", 50, "pwrin"),
                    ("VDD", 75, "pwrin"),
                    ("VDD", 100, "pwrin"),
                    ("VDDA", 22, "pwrin"),
                    ("VREF+", 21, "pwrin"),
                ], [
                    ("VCAP_1", 49, "passive"),
                    ("VCAP_2", 73, "passive"),
                ], [
                    ("VSSA", 20, "pwrin"),
                    ("VSS", 10, "pwrin"),
                    ("VSS", 27, "pwrin"),
                    ("VSS", 74, "pwrin"),
                    ("VSS", 99, "pwrin"),
                ], [
                    ("BOOT0", 94, "in"),
                    ("NRST", 14, "in"),
                ], [
                    ("PH0", 12, "bidi"),
                    ("PH1", 13, "bidi"),
                ], [
                    ("PA0", 23, "bidi"),
                    ("PA1", 24, "bidi"),
                    ("PA2", 25, "bidi"),
                    ("PA3", 26, "bidi"),
                    ("PA4", 29, "bidi"),
                    ("PA5", 30, "bidi"),
                    ("PA6", 31, "bidi"),
                    ("PA7", 32, "bidi"),
                ], [
                    ("PA8", 67, "bidi"),
                    ("PA9", 68, "bidi"),
                    ("PA10", 69, "bidi"),
                    ("PA11", 70, "bidi"),
                    ("PA12", 71, "bidi"),
                    ("PA13", 72, "bidi"),
                    ("PA14", 76, "bidi"),
                    ("PA15", 77, "bidi"),
                ], [
                    ("PB0", 35, "bidi"),
                    ("PB1", 36, "bidi"),
                    ("PB2", 37, "bidi"),
                    ("PB3", 89, "bidi"),
                    ("PB4", 90, "bidi"),
                    ("PB5", 91, "bidi"),
                    ("PB6", 92, "bidi"),
                    ("PB7", 93, "bidi"),
                ], [
                    ("PB8", 95, "bidi"),
                    ("PB9", 96, "bidi"),
                    ("PB10", 47, "bidi"),
                    ("PB11", 48, "bidi"),
                    ("PB12", 51, "bidi"),
                    ("PB13", 52, "bidi"),
                    ("PB14", 53, "bidi"),
                    ("PB15", 54, "bidi"),
                ],
            ], [
                [
                    ("PC0", 15, "bidi"),
                    ("PC1", 16, "bidi"),
                    ("PC2", 17, "bidi"),
                    ("PC3", 18, "bidi"),
                    ("PC4", 33, "bidi"),
                    ("PC5", 34, "bidi"),
                    ("PC6", 63, "bidi"),
                    ("PC7", 64, "bidi"),
                ], [
                    ("PC8", 65, "bidi"),
                    ("PC9", 66, "bidi"),
                    ("PC10", 78, "bidi"),
                    ("PC11", 79, "bidi"),
                    ("PC12", 80, "bidi"),
                    ("PC13", 7, "bidi"),
                    ("PC14", 8, "bidi"),
                    ("PC15", 9, "bidi"),
                ], [
                    ("PD0", 81, "bidi"),
                    ("PD1", 82, "bidi"),
                    ("PD2", 83, "bidi"),
                    ("PD3", 84, "bidi"),
                    ("PD4", 85, "bidi"),
                    ("PD5", 86, "bidi"),
                    ("PD6", 87, "bidi"),
                    ("PD7", 88, "bidi"),
                ], [
                    ("PD8", 55, "bidi"),
                    ("PD9", 56, "bidi"),
                    ("PD10", 57, "bidi"),
                    ("PD11", 58, "bidi"),
                    ("PD12", 59, "bidi"),
                    ("PD13", 60, "bidi"),
                    ("PD14", 61, "bidi"),
                    ("PD15", 62, "bidi"),
                ], [
                    ("PE0", 97, "bidi"),
                    ("PE1", 98, "bidi"),
                    ("PE2", 1, "bidi"),
                    ("PE3", 2, "bidi"),
                    ("PE4", 3, "bidi"),
                    ("PE5", 4, "bidi"),
                    ("PE6", 5, "bidi"),
                    ("PE7", 38, "bidi"),
                ], [
                    ("PE8", 39, "bidi"),
                    ("PE9", 40, "bidi"),
                    ("PE10", 41, "bidi"),
                    ("PE11", 42, "bidi"),
                    ("PE12", 43, "bidi"),
                    ("PE13", 44, "bidi"),
                    ("PE14", 45, "bidi"),
                    ("PE15", 46, "bidi"),
                ],
            ],
        ],
    },

    # STM32L4xxJxYx, in WLCSP72 package
    "STM32L4xxJxYx": {
        "path": "ic/microcontroller",
        "footprint": "agg:WLCSP72",
        "datasheet": "http://www.st.com/st-web-ui/static/active/en"
                     "/resource/technical/document/datasheet/DM00108833.pdf",
        "ordercodes": [("Farnell", "2503302")],
        "description": "STM32L4 72 pin WLCSP package",
        "pins": [
            [
                [
                    ("VBAT", "B9", "pwrin"),
                    ("VDD", "A9", "pwrin"),
                    ("VDD", "J1", "pwrin"),
                    ("VDD", "J8", "pwrin"),
                    ("VDDIO2", "B6", "pwrin"),
                    ("VDDUSB", "A1", "pwrin"),
                ], [
                    ("VSS", "A8", "pwrin"),
                    ("VSS", "B1", "pwrin"),
                    ("VSS", "J2", "pwrin"),
                    ("VSS", "J9", "pwrin"),
                ], [
                    ("VDDA", "H9", "pwrin"),
                    ("VREF+", "G8", "in"),
                    ("VSSA", "G9", "pwrin"),
                ], [
                    ("BOOT0", "D7", "in"),
                    ("NRST", "E9", "in"),
                ], [
                    ("PH0", "D9", "bidi"),
                    ("PH1", "D8", "bidi"),
                ], [
                    ("PA0", "H8", "bidi"),
                    ("PA1", "G4", "bidi"),
                    ("PA2", "G6", "bidi"),
                    ("PA3", "H7", "bidi"),
                    ("PA4", "G5", "bidi"),
                    ("PA5", "H6", "bidi"),
                    ("PA6", "H5", "bidi"),
                    ("PA7", "H4", "bidi"),
                ], [
                    ("PA8", "E2", "bidi"),
                    ("PA9", "E3", "bidi"),
                    ("PA10", "D2", "bidi"),
                    ("PA11", "D1", "bidi"),
                    ("PA12", "C1", "bidi"),
                    ("PA13", "C2", "bidi"),
                    ("PA14", "B2", "bidi"),
                    ("PA15", "A2", "bidi"),
                ],
            ], [
                [
                    ("PB0", "J5", "bidi"),
                    ("PB1", "J4", "bidi"),
                    ("PB2", "J3", "bidi"),
                    ("PB3", "A6", "bidi"),
                    ("PB4", "C6", "bidi"),
                    ("PB5", "C7", "bidi"),
                    ("PB6", "B7", "bidi"),
                    ("PB7", "A7", "bidi"),
                ], [
                    ("PB8", "E7", "bidi"),
                    ("PB9", "E8", "bidi"),
                    ("PB10", "H3", "bidi"),
                    ("PB11", "G3", "bidi"),
                    ("PB12", "H1", "bidi"),
                    ("PB13", "H2", "bidi"),
                    ("PB14", "G2", "bidi"),
                    ("PB15", "G1", "bidi"),
                ], [
                    ("PC0", "F9", "bidi"),
                    ("PC1", "F8", "bidi"),
                    ("PC2", "F7", "bidi"),
                    ("PC3", "G7", "bidi"),
                    ("PC4", "J7", "bidi"),
                    ("PC5", "J6", "bidi"),
                    ("PC6", "F3", "bidi"),
                    ("PC7", "F1", "bidi"),
                ], [
                    ("PC8", "F2", "bidi"),
                    ("PC9", "E1", "bidi"),
                    ("PC10", "D3", "bidi"),
                    ("PC11", "C3", "bidi"),
                    ("PC12", "B3", "bidi"),
                    ("PC13", "B8", "bidi"),
                    ("PC14", "C9", "bidi"),
                    ("PC15", "C8", "bidi"),
                ], [
                    ("PD2", "A3", "bidi"),
                ], [
                    ("PG9", "A4", "bidi"),
                    ("PG10", "B4", "bidi"),
                    ("PG11", "C4", "bidi"),
                    ("PG12", "C5", "bidi"),
                    ("PG13", "B5", "bidi"),
                    ("PG14", "A5", "bidi"),
                ],
            ],
        ],
    },

    # STM32F4xxZxJx, in UFBGA144 10x10 package
    "STM32F4xxZxJx": {
        "path": "ic/microcontroller",
        "footprint": "agg:BGA-144-08P-ST",
        "datasheet": "http://www.st.com/st-web-ui/static/active/en"
                     "/resource/technical/document/datasheet/DM00141306.pdf",
        "ordercodes": [("Farnell", "2488316")],
        "description": "STM32F4 144 pin 10x10 UFBGA package",
        "pins": [
            [
                [
                    ("VDD", "D3", "pwrin"),
                    ("VDD", "F10", "pwrin"),
                    ("VDD", "F4", "pwrin"),
                    ("VDD", "F5", "pwrin"),
                    ("VDD", "F6", "pwrin"),
                    ("VDD", "F7", "pwrin"),
                    ("VDD", "F8", "pwrin"),
                    ("VDD", "F9", "pwrin"),
                    ("VDD", "G5", "pwrin"),
                    ("VDD", "G6", "pwrin"),
                    ("VDD", "G7", "pwrin"),
                    ("VBAT", "C2", "pwrin"),
                    ("VDDUSB", "C11", "pwrin"),
                ], [
                    ("VSS", "D2", "pwrin"),
                    ("VSS", "E6", "pwrin"),
                    ("VSS", "E7", "pwrin"),
                    ("VSS", "G10", "pwrin"),
                    ("VSS", "G4", "pwrin"),
                    ("VSS", "G8", "pwrin"),
                    ("VSS", "H6", "pwrin"),
                ], [
                    ("VDDA", "M1", "pwrin"),
                    ("VREF+", "L1", "in"),
                    ("VREF-", "K1", "in"),
                    ("VSSA", "J1", "pwrin"),
                ], [
                    ("VCAP_1", "H7", "passive"),
                    ("VCAP_2", "G9", "passive"),
                ], [
                    ("PDR_ON", "E5", "in"),
                    ("BOOT0", "D5", "in"),
                    ("BYPASS_REG", "H5", "in"),
                    ("NRST", "F1", "in"),
                ], [
                    ("PA0", "J2", "bidi"),
                    ("PA1", "K2", "bidi"),
                    ("PA2", "L2", "bidi"),
                    ("PA3", "M2", "bidi"),
                    ("PA4", "J3", "bidi"),
                    ("PA5", "K3", "bidi"),
                    ("PA6", "L3", "bidi"),
                    ("PA7", "M3", "bidi"),
                    ("PA8", "E12", "bidi"),
                    ("PA9", "D12", "bidi"),
                    ("PA10", "D11", "bidi"),
                    ("PA11", "C12", "bidi"),
                    ("PA12", "B12", "bidi"),
                    ("PA13", "A12", "bidi"),
                    ("PA14", "A11", "bidi"),
                    ("PA15", "A10", "bidi"),
                ], [
                    ("PB0", "L4", "bidi"),
                    ("PB1", "M4", "bidi"),
                    ("PB2", "J5", "bidi"),
                    ("PB3", "A7", "bidi"),
                    ("PB4", "A6", "bidi"),
                    ("PB5", "B6", "bidi"),
                    ("PB6", "C6", "bidi"),
                    ("PB7", "D6", "bidi"),
                    ("PB8", "C5", "bidi"),
                    ("PB9", "B5", "bidi"),
                    ("PB10", "M9", "bidi"),
                    ("PB11", "M10", "bidi"),
                    ("PB12", "M11", "bidi"),
                    ("PB13", "M12", "bidi"),
                    ("PB14", "L11", "bidi"),
                    ("PB15", "L12", "bidi"),
                ], [
                    ("PC0", "H1", "bidi"),
                    ("PC1", "H2", "bidi"),
                    ("PC2", "H3", "bidi"),
                    ("PC3", "H4", "bidi"),
                    ("PC4", "J4", "bidi"),
                    ("PC5", "K4", "bidi"),
                    ("PC6", "G12", "bidi"),
                    ("PC7", "F12", "bidi"),
                    ("PC8", "F11", "bidi"),
                    ("PC9", "E11", "bidi"),
                    ("PC10", "B11", "bidi"),
                    ("PC11", "B10", "bidi"),
                    ("PC12", "C10", "bidi"),
                    ("PC13", "A1", "bidi"),
                    ("PC14", "B1", "bidi"),
                    ("PC15", "C1", "bidi"),
                ],
            ], [
                [
                    ("PD0", "E10", "bidi"),
                    ("PD1", "D10", "bidi"),
                    ("PD2", "E9", "bidi"),
                    ("PD3", "D9", "bidi"),
                    ("PD4", "C9", "bidi"),
                    ("PD5", "B9", "bidi"),
                    ("PD6", "A8", "bidi"),
                    ("PD7", "A9", "bidi"),
                    ("PD8", "L9", "bidi"),
                    ("PD9", "K9", "bidi"),
                    ("PD10", "J9", "bidi"),
                    ("PD11", "H9", "bidi"),
                    ("PD12", "L10", "bidi"),
                    ("PD13", "K10", "bidi"),
                    ("PD14", "K11", "bidi"),
                    ("PD15", "K12", "bidi"),
                ], [
                    ("PE0", "A5", "bidi"),
                    ("PE1", "A4", "bidi"),
                    ("PE2", "A3", "bidi"),
                    ("PE3", "A2", "bidi"),
                    ("PE4", "B2", "bidi"),
                    ("PE5", "B3", "bidi"),
                    ("PE6", "B4", "bidi"),
                    ("PE7", "M7", "bidi"),
                    ("PE8", "L7", "bidi"),
                    ("PE9", "K7", "bidi"),
                    ("PE10", "J7", "bidi"),
                    ("PE11", "H8", "bidi"),
                    ("PE12", "J8", "bidi"),
                    ("PE13", "K8", "bidi"),
                    ("PE14", "L8", "bidi"),
                    ("PE15", "M8", "bidi"),
                ], [
                    ("PF0", "C3", "bidi"),
                    ("PF1", "C4", "bidi"),
                    ("PF2", "D4", "bidi"),
                    ("PF3", "E2", "bidi"),
                    ("PF4", "E3", "bidi"),
                    ("PF5", "E4", "bidi"),
                    ("PF6", "F3", "bidi"),
                    ("PF7", "F2", "bidi"),
                    ("PF8", "G3", "bidi"),
                    ("PF9", "G2", "bidi"),
                    ("PF10", "G1", "bidi"),
                    ("PF11", "M5", "bidi"),
                    ("PF12", "L5", "bidi"),
                    ("PF13", "K5", "bidi"),
                    ("PF14", "M6", "bidi"),
                    ("PF15", "L6", "bidi"),
                ], [
                    ("PG0", "K6", "bidi"),
                    ("PG1", "J6", "bidi"),
                    ("PG2", "J12", "bidi"),
                    ("PG3", "J11", "bidi"),
                    ("PG4", "J10", "bidi"),
                    ("PG5", "H12", "bidi"),
                    ("PG6", "H11", "bidi"),
                    ("PG7", "H10", "bidi"),
                    ("PG8", "G11", "bidi"),
                    ("PG9", "E8", "bidi"),
                    ("PG10", "D8", "bidi"),
                    ("PG11", "C8", "bidi"),
                    ("PG12", "B8", "bidi"),
                    ("PG13", "D7", "bidi"),
                    ("PG14", "C7", "bidi"),
                    ("PG15", "B7", "bidi"),
                ], [
                    ("PH0", "D1", "bidi"),
                    ("PH1", "E1", "bidi"),
                ],
            ],
        ],
    },

    # STM32F411CxUx
    "STM32F411CxUx": {
        "path": "ic/microcontroller",
        "footprint": "agg:QFN-48-EP-ST",
        "datasheet": "http://www.st.com/st-web-ui/static/active/en"
                     "/resource/technical/document/datasheet/DM00115249.pdf",
        "ordercodes": [("Farnell", "2456965")],
        "description": "STM32F4 48 pin UFQFN package",
        "pins": [
            [
                [
                    ("VBAT", 1, "pwrin"),
                    ("VDD", 24, "pwrin"),
                    ("VDD", 36, "pwrin"),
                    ("VDD", 48, "pwrin"),
                    ("VDDA", 9, "pwrin"),
                ], [
                    ("VSSA", 8, "pwrin"),
                    ("VSS", 23, "pwrin"),
                    ("VSS", 35, "pwrin"),
                    ("VSS", 47, "pwrin"),
                    ("VSS", "EP", "pwrin"),
                ], [
                    ("VCAP1", 22, "passive"),
                ], [
                    ("BOOT0", 44, "in"),
                    ("NRST", 7, "in"),
                ], [
                    ("PC13", 2, "bidi"),
                    ("PC14", 3, "bidi"),
                    ("PC15", 4, "bidi"),
                ], [
                    ("PH0", 5, "bidi"),
                    ("PH1", 6, "bidi"),
                ],
            ], [
                [
                    ("PA0", 10, "bidi"),
                    ("PA1", 11, "bidi"),
                    ("PA2", 12, "bidi"),
                    ("PA3", 13, "bidi"),
                    ("PA4", 14, "bidi"),
                    ("PA5", 15, "bidi"),
                    ("PA6", 16, "bidi"),
                    ("PA7", 17, "bidi"),
                ], [
                    ("PA8", 29, "bidi"),
                    ("PA9", 30, "bidi"),
                    ("PA10", 31, "bidi"),
                    ("PA11", 32, "bidi"),
                    ("PA12", 33, "bidi"),
                    ("PA13", 34, "bidi"),
                    ("PA14", 37, "bidi"),
                    ("PA15", 38, "bidi"),
                ], [
                    ("PB0", 18, "bidi"),
                    ("PB1", 19, "bidi"),
                    ("PB2", 20, "bidi"),
                    ("PB3", 39, "bidi"),
                    ("PB4", 40, "bidi"),
                    ("PB5", 41, "bidi"),
                    ("PB6", 42, "bidi"),
                    ("PB7", 43, "bidi"),
                ], [
                    ("PB8", 45, "bidi"),
                    ("PB9", 46, "bidi"),
                    ("PB10", 21, "bidi"),
                    ("PB12", 25, "bidi"),
                    ("PB13", 26, "bidi"),
                    ("PB14", 27, "bidi"),
                    ("PB15", 28, "bidi"),
                ],
            ],
        ]
    },

    # STM32F405RxTx
    "STM32F405RxTx": {
        "path": "ic/microcontroller",
        "footprint": "agg:LQFP-64",
        "datasheet": "http://www.st.com/st-web-ui/static/active/en"
                     "/resource/technical/document/datasheet/DM00037051.pdf",
        "ordercodes": [("Farnell", "2064363")],
        "description": "STM32F4 64 pin TQFP package",
        "pins": [
            [
                [
                    ("VBAT", 1, "pwrin"),
                    ("VDD", 19, "pwrin"),
                    ("VDD", 32, "pwrin"),
                    ("VDD", 48, "pwrin"),
                    ("VDD", 64, "pwrin"),
                    ("VDDA", 13, "pwrin"),
                ], [
                    ("VSSA", 12, "pwrin"),
                    ("VSS", 18, "pwrin"),
                    ("VSS", 63, "pwrin"),
                ], [
                    ("VCAP_1", 31, "passive"),
                    ("VCAP_2", 47, "passive"),
                ], [
                    ("NRST", 7, "in"),
                    ("BOOT0", 60, "in"),
                ], [
                    ("PH0", 5, "bidi"),
                    ("PH1", 6, "bidi"),
                ], [
                    ("PA0", 14, "bidi"),
                    ("PA1", 15, "bidi"),
                    ("PA2", 16, "bidi"),
                    ("PA3", 17, "bidi"),
                    ("PA4", 20, "bidi"),
                    ("PA5", 21, "bidi"),
                    ("PA6", 22, "bidi"),
                    ("PA7", 23, "bidi"),
                    ("PA8", 41, "bidi"),
                    ("PA9", 42, "bidi"),
                    ("PA10", 43, "bidi"),
                    ("PA11", 44, "bidi"),
                    ("PA12", 45, "bidi"),
                    ("PA13", 46, "bidi"),
                    ("PA14", 49, "bidi"),
                    ("PA15", 50, "bidi"),
                ],
            ], [
                [
                    ("PB0", 26, "bidi"),
                    ("PB1", 27, "bidi"),
                    ("PB2", 28, "bidi"),
                    ("PB3", 55, "bidi"),
                    ("PB4", 56, "bidi"),
                    ("PB5", 57, "bidi"),
                    ("PB6", 58, "bidi"),
                    ("PB7", 59, "bidi"),
                    ("PB8", 61, "bidi"),
                    ("PB9", 62, "bidi"),
                    ("PB10", 29, "bidi"),
                    ("PB11", 30, "bidi"),
                    ("PB12", 33, "bidi"),
                    ("PB13", 34, "bidi"),
                    ("PB14", 35, "bidi"),
                    ("PB15", 36, "bidi"),
                ], [
                    ("PC0", 8, "bidi"),
                    ("PC1", 9, "bidi"),
                    ("PC2", 10, "bidi"),
                    ("PC3", 11, "bidi"),
                    ("PC4", 24, "bidi"),
                    ("PC5", 25, "bidi"),
                    ("PC6", 37, "bidi"),
                    ("PC7", 38, "bidi"),
                    ("PC8", 39, "bidi"),
                    ("PC9", 40, "bidi"),
                    ("PC10", 51, "bidi"),
                    ("PC11", 52, "bidi"),
                    ("PC12", 53, "bidi"),
                    ("PC13", 2, "bidi"),
                    ("PC14", 3, "bidi"),
                    ("PC15", 4, "bidi"),
                ], [
                    ("PD2", 54, "bidi"),
                ]
            ]
        ]
    },

    # MPU-9250 9DoF IMU
    "MPU-9250": {
        "path": "ic/sensor",
        "footprint": "QFN-24-EP-MPU9250",
        "datasheet": "http://43zrtwysvxb2gf29r5o0athu.wpengine.netdna-cdn.com"
                     "/wp-content/uploads/2015/02/MPU-9250-Datasheet.pdf",
        "ordercodes": [
            ("RS", "883-7942"),
            ("DigiKey", "1428-1019-1-ND"),
        ],
        "description": "MPU-9250 9DoF IMU from InvenSense",
        "pins": [
            [
                [
                    ("VDD", 13, "pwrin"),
                    ("VDDIO", 8, "pwrin"),
                    ("RESV_VDDIO", 1, "in"),
                ], [
                    ("GND", 18, "pwrin"),
                    ("RESV_GND", 20, "in"),
                ], [
                    ("NC", 2, "nc"),
                    ("NC", 3, "nc"),
                    ("NC", 4, "nc"),
                    ("NC", 5, "nc"),
                    ("NC", 6, "nc"),
                    ("NC", 14, "nc"),
                    ("NC", 15, "nc"),
                    ("NC", 16, "nc"),
                    ("NC", 17, "nc"),
                    ("RESV_NC", 19, "nc"),
                ],
            ], [
                [
                    ("~CS", 22, "in"),
                    ("AD0/SD0", 9, "bidi"),
                    ("SCL/SCLK", 23, "in"),
                    ("SDA/SDI", 24, "in")
                ], [
                    ("REGOUT", 10, "passive"),
                    ("INT", 12, "oc"),
                    ("FSYNC", 11, "in"),
                ], [
                    ("AUX_CL", 7, "tri"),
                    ("AUX_DA", 21, "tri"),
                ],
            ],
        ],
    },

    # LTC3535 Dual DC-DC Converter
    "LTC3535": {
        "path": "ic/power",
        "footprint": "DFN-12-EP-LT",
        "datasheet": "http://cds.linear.com/docs/en/datasheet/3535fa.pdf",
        "ordercodes": [("Farnell", "1947922")],
        "description": "LTC3535 Dual DC-DC Converter",
        "pins": [
            [
                [
                    ("VIN1", 10, "pwrin"),
                    ("SW1", 2, "passive"),
                    ("~SHDN1", 11, "in"),
                ], [
                    ("VIN2", 7, "pwrin"),
                    ("SW2", 5, "passive"),
                    ("~SHDN2", 8, "in"),
                ], [
                    ("GND", 6, "pwrin"),
                    ("GND", 3, "pwrin"),
                    ("GND", "EP", "pwrin"),
                ]
            ], [
                [
                    ("VOUT1", 1, "pwrout"),
                    ("FB1", 12, "in"),
                ], [
                    ("VOUT2", 4, "pwrout"),
                    ("FB2", 9, "in"),
                ],
            ]
        ],
    },
    
    # LTC2983 Multi-Sensor High Accuracy Digital Temperature Measurement System
    "LTC2983": {
        "path": "ic/analogue",
        "footprint": "LQFP-48",
        "datasheet": "http://cds.linear.com/docs/en/datasheet/2983fc.pdf",
        "ordercodes": [("Farnell", "2461149")],
        "description": "Digital Temperature Measurement System",
        "pins": [
            [
                [
                    ("VDD", 2, "pwrin"),
                    ("VDD", 4, "pwrin"),
                    ("VDD", 6, "pwrin"),
                    ("VDD", 8, "pwrin"),
                    ("VDD", 45, "pwrin"),
                ], [
                    ("VREF_OUT", 13, "pwrout"),
                    ("VREF_P", 14, "pwrin"),
                    ("VREF_BYP", 11, "pwrout"),
                    ("LDO", 43, "pwrout"),
                ], [
                    ("~RESET", 42, "in"),
                    ("INT", 37, "out"),
                    ("SCK", 38, "in"),
                    ("SDO", 39, "out"),
                    ("SDI", 40, "in"),
                    ("~CS", 41, "in"),
                   
                ], [
                    ("NC", 10, "nc"),
                ], [
                    ("COM", 36, "in"),
                    ("GND", 1, "pwrin"),
                    ("GND", 3, "pwrin"),
                    ("GND", 5, "pwrin"),
                    ("GND", 7, "pwrin"),
                    ("GND", 9, "pwrin"),
                    ("GND", 12, "pwrin"),
                    ("GND", 15, "pwrin"),
                    ("GND", 44, "pwrin"),
                ]
            ], [
                [
                    ("Q1", 48, "pwrout"),
                    ("Q2", 47, "pwrout"),
                    ("Q3", 46, "pwrout"),
                ], [
                    ("CH1", 16, "in"),
                    ("CH2", 17, "in"),
                    ("CH3", 18, "in"),
                    ("CH4", 19, "in"),
                    ("CH5", 20, "in"),
                    ("CH6", 21, "in"),
                    ("CH7", 22, "in"),
                    ("CH8", 23, "in"),
                    ("CH9", 24, "in"),
                    ("CH10", 25, "in"),
                    ("CH11", 26, "in"),
                    ("CH12", 27, "in"),
                    ("CH13", 28, "in"),
                    ("CH14", 29, "in"),
                    ("CH15", 30, "in"),
                    ("CH16", 31, "in"),
                    ("CH17", 32, "in"),
                    ("CH18", 33, "in"),
                    ("CH19", 34, "in"),
                    ("CH20", 35, "in"),
                ],
            ]
        ],
    },
    

    # MCP2562 CAN Transceiver
    "MCP2562": {
        "path": "ic/interface",
        "footprint": "agg:DFN-8-EP-MICROCHIP",
        "datasheet": "http://ww1.microchip.com/downloads/en"
                     "/DeviceDoc/20005167C.pdf",
        "ordercodes": [("Farnell", ""), ("RS", "824-3135")],
        "description": "High Speed CAN Transceiver",
        "pins": [
            [
                [
                    ("VIO", 5, "pwrin"),
                    ("VDD", 3, "pwrin"),
                    ("VSS", 2, "pwrin"),
                    ("VSS", "EP", "pwrin"),
                    ("STBY", 8, "in"),
                ]
            ], [
                [
                    ("CANH", 7, "tri"),
                    ("CANL", 6, "tri"),
                    ("TXD", 1, "in"),
                    ("RXD", 4, "out"),
                ]
            ]
        ]
    },

    # ADL5324 RF Driver Amplifier
    "ADL5324": {
        "path": "ic/radio",
        "footprint": "agg:SOT-89-3",
        "datasheet": "http://www.analog.com/media/en"
                     "/technical-documentation/data-sheets/ADL5324.pdf",
        "ordercodes": [("Farnell", "2099794")],
        "description": "0.5W 400MHz-4GHz RF Driver Amplifier",
        "pins": [
            [
                [
                    ("RF_IN", 1, "in"),
                    ("GND", 2, "pwrin"),
                ],
            ], [
                [
                    ("RF_OUT", 3, "out"),
                ],
            ],
        ]
    },

    # ADL5320 RF Driver Amplifier
    "ADL5320": {
        "path": "ic/radio",
        "footprint": "agg:SOT-89-3",
        "datasheet": "http://www.analog.com/media/en"
                     "/technical-documentation/data-sheets/ADL5320.pdf",
        "ordercodes": [("Farnell", "2377141")],
        "description": "0.5W 400MHz-2.7GHz RF Driver Amplifier",
        "pins": [
            [
                [
                    ("RF_IN", 1, "in"),
                    ("GND", 2, "pwrin"),
                ],
            ], [
                [
                    ("RF_OUT", 3, "out"),
                ],
            ],
        ]
    },

    # SKYWORKS SKY65111-348LF RF Driver Amplifier
    "SKY65111-348LF": {
        "path": "ic/radio",
        "footprint": "agg:QFN-16-EP-SKYWORKS",
        "datasheet": "http://www.skyworksinc.com/uploads"
                     "/documents/200428E.pdf",
        "ordercodes": [("Farnell", "1753773")],
        "description": "2W 600-1100MHz RF Power Amplifier",
        "pins": [
            [
                [
                    ("VCC1", 4, "pwrin"),
                    ("VCC2", 15, "pwrin"),
                    ("VCC2", 16, "pwrin"),
                    ("VAPC1", 5, "pwrin"),
                    ("VAPC2", 6, "pwrin"),
                ], [
                    ("GND", 1, "pwrin"),
                    ("GND", 3, "pwrin"),
                    ("GND", 8, "pwrin"),
                    ("GND", 14, "pwrin"),
                    ("GND", "EP", "pwrin"),
                ], [
                    ("VREF", 7, "in"),
                ], [
                    ("RFIN", 2, "in"),
                ]
            ], [
                [
                    ("RFOUT/VCC3", 9, "out"),
                    ("RFOUT/VCC3", 10, "out"),
                    ("RFOUT/VCC3", 11, "out"),
                    ("RFOUT/VCC3", 12, "out"),
                ], [
                    ("OPEN", 13, "nc"),
                ],
            ],
        ]
    },

    # LTC3887 Dual Output DC/DC Controller
    "LTC3887": {
        "path": "ic/power",
        "footprint": "agg:QFN-40-EP-LTC-UJ",
        "datasheet": "http://cds.linear.com/docs/en/datasheet/3887fb.pdf",
        "ordercodes": [("Farnell", "2475658")],
        "description": "Dual Output PolyPhase Step-Down DC/DC Controller"
                       "with Digital Power System Management",
        "pins": [
            [
                [
                    ("V_IN", 35, "pwrin"),
                ], [
                    ("TG0", 38, "out"),
                    ("BOOST0", 37, "out"),
                    ("SW0", 39, "in"),
                    ("BG0", 36, "out"),
                ], [
                    ("I_SENSE_0+", 6, "in"),
                    ("I_SENSE_0-", 7, "in"),
                    ("V_SENSE_0+", 1, "in"),
                    ("V_SENSE_0-", 2, "in"),
                    ("TSNS0", 40, "in"),
                ], [
                    ("ITH_0", 5, "in"),
                ], [
                    ("SDA", 10, "tri"),
                    ("SCL", 9, "tri"),
                    ("~ALERT", 11, "out"),
                    ("RUN0", 14, "in"),
                    ("RUN1", 15, "in"),
                    ("SHARE_CLK", 24, "tri"),
                    ("SYNC", 8, "tri"),
                    ("WP", 23, "in"),
                ], [
                    ("V_OUT_0_CFG", 18, "in"),
                    ("V_OUT_1_CFG", 19, "in"),
                    ("FREQ_CFG", 20, "in"),
                    ("PHAS_CFG", 21, "in"),
                ]
            ], [
                [
                    ("INTVCC", 33, "pwrout"),
                ], [
                    ("TG1", 30, "out"),
                    ("BOOST1", 31, "out"),
                    ("SW1", 29, "in"),
                    ("BG1", 32, "out"),
                ], [
                    ("I_SENSE_1+", 3, "in"),
                    ("I_SENSE_1-", 4, "in"),
                    ("V_SENSE_1", 27, "in"),
                    ("TSNS1", 28, "in"),
                ], [
                    ("ITH_1", 26, "in"),
                ], [
                    ("~GPIO0", 12, "bidi"),
                    ("~GPIO1", 13, "bidi"),
                ], [
                    ("ASEL0", 16, "in"),
                    ("ASEL1", 17, "in"),
                ], [
                    ("VDD_33", 25, "pwrout"),
                    ("VDD_25", 22, "pwrout"),
                ], [
                    ("GND", 34, "pwrin"),
                    ("GND", "EP", "pwrin"),
                ]
            ]
        ]
    },

    # LTC4353 Dual Low Voltage Ideal Diode Controller
    "LTC4353": {
        "path": "ic/power",
        "footprint": "agg:DFN-16-EP-LTC-DE",
        "datasheet": "https://cds.linear.com/docs/en/datasheet/4353f.pdf",
        "ordercodes": [("Farnell", "2115909")],
        "description": "Dual Output Low Voltage Ideal Diode Controller",
        "pins": [
            [
                [
                    ("VCC", 14, "pwrin"),
                ], [
                    ("~EN1", 16, "in"),
                    ("~EN2", 1, "in"),
                ], [
                    ("NC", 2, "nc"),
                    ("NC", 3, "nc"),
                ], [
                    ("~ON_STAT1", 9, "out"),
                    ("~ON_STAT2", 8, "out"),
                ], [
                    ("GND", 15, "pwrin"),
                    ("GND", "EP", "pwrin"),
                ]
            ], [
                [
                    ("CPO1", 11, "passive"),
                    ("VIN1", 13, "pwrin"),
                    ("GATE1", 12, "out"),
                    ("OUT1", 10, "in"),
                ], [
                    ("CPO2", 6, "passive"),
                    ("VIN2", 4, "pwrin"),
                    ("GATE2", 5, "out"),
                    ("OUT2", 7, "in"),
                ]
            ]
        ]
    },
    
    # 24AA01 1K I2C Serial EEPROM   
    "24AA01": {
        "path": "ic/memory",
        "footprint": "agg:SOT-23-5",
        "datasheet": "http://ww1.microchip.com/downloads/en/DeviceDoc/21711c.pdf",
        "ordercodes": [("Farnell", "1331269")],
        "description": "1K I2C Serial EEPROM",
        "pins": [
            [
                [
                    ("VCC", 4, "pwrin"),
                ], [
                    ("GND", 2, "pwrin"),
                ]
            ], [
                [
                    ("SDA", 3, "tri"),
                    ("SCL", 1, "tri"),
                    ("WP", 5, "in"),
                ]
            ]
        ]
    },

    # MAX17435 Multi-chemistry Battery Charger with SMBus Communication
    "MAX17435": {
        "path": "ic/power",
        "footprint": "agg:QFN-24-EP-MAX",
        "datasheet": "https://datasheets.maximintegrated.com/en"
                     "/ds/MAX17435-MAX17535.pdf",
        "ordercodes": [("Farnell", "2516688")],
        "description": "Multi-chemistry battery charger with"
                       " SMBus communication",
        "pins": [
            [
                [
                    ("~ACOK", 10, "out"),
                    ("LDO", 4, "pwrout"),
                    ("EN", 24, "in"),
                    ("ADAPTLIM", 6, "out"),
                    ("ITHR", 20, "in"),
                    ("VCC", 22, "pwrin")
                ], [
                    ("SCL", 1, "oc"),
                    ("SDA", 2, "oc")
                ], [
                    ("CC", 17, "passive"),
                    ("IINP", 18, "out"),
                    ("VAA", 21, "passive"),
                    ("GND", 23, "pwrin"),
                    ("GND", "EP", "pwrin")
                ]
            ], [
                [
                    ("ACIN", 19, "in"),
                    ("DCIN", 3, "pwrin"),
                    ("PDSL", 14, "out"),
                    ("CSSP", 16, "in"),
                    ("CSSN", 15, "in")
                ], [
                    ("DHI", 9, "out"),
                    ("BST", 7, "passive"),
                    ("LX", 8, "passive"),
                    ("DLO", 5, "out")
                ], [
                    ("CSIP", 12, "in"),
                    ("CSIN", 11, "in"),
                    ("BATT", 13, "in")
                ]
            ]
        ]
    },
	
	# PCAL9538A Low-voltage 8-bit I2C-bus and SMBus low power I/O port with interrupt, reset, and Agile I/O
    "PCAL9538A": {
        "path": "ic/interface",
        "footprint": "agg:QFN-16-EP-NXP",
        "datasheet": "http://www.nxp.com/documents/data_sheet/PCAL9538A.pdf",
        "ordercodes": [("Farnell", "2428172")],
        "description": "Low-voltage and power 8-bit I2C SMBus expander",
        "pins": [
            [
                [
                    ("VDD", 14, "pwrin")
				], [
                    ("~RESET", 1, "in")
                ], [
                    ("~INT", 11, "oc"),
                    ("SCL", 12, "oc"),
                    ("SDA", 13, "oc")
                ], [
                    ("A0", 15, "in"),
                    ("A1", 16, "in")
                ], [
                    ("VSS", 6, "pwrin"),
                    ("VSS", "EP", "pwrin")
                ]
            ], [
                [
                    ("P0", 2, "bidi"),
                    ("P1", 3, "bidi"),
                    ("P2", 4, "bidi"),
                    ("P3", 5, "bidi"),
                ], [
                    ("P4", 7, "bidi"),
                    ("P5", 8, "bidi"),
                    ("P6", 9, "bidi"),
                    ("P7", 10, "bidi")
                ]
            ]
        ]
    },
    
    # TPS62152 Small Buck converter 3-17V in, fixed 3.3V 1A out, 2.5MHz
    "TPS62152": {
        "path": "ic/power",
        "footprint": "agg:QFN-16-EP-TI",
        "datasheet": "http://www.ti.com/lit/ds/symlink/tps62152.pdf",
        "ordercodes": [("Farnell", "2382918")],
        "description": "3.3Vout 1A, fixed, Buck Converter",
        "pins": [
            [
                [
                    ("PVIN", 11, "pwrin"),
                    ("PVIN", 12, "pwrin"),
                    ("AVIN", 10, "pwrin"),
                    ("EN", 13, "pwrin")
				], [
                    ("SS/TR", 9, "passive")
                ], [
                    ("DEF", 8, "in"),
                    ("FB", 5, "passive"),
                    ("AGND", 6, "pwrin"),
                    ("PGND", 15, "pwrin"),
                    ("PGND", 16, "pwrin"),
                    ("EP", "EP", "pwrin")
                ]
            ], [
                [
                    ("SW", 1, "pwrout"),
                    ("SW", 2, "pwrout"),
                    ("SW", 3, "pwrout")
                ], [
                    ("FSW", 7, "in"),
                    ("VOS", 14, "in"),
                    ("PG", 4, "out")
                ]
            ]
        ]
    },
}

# Other Constants =============================================================

# None yet.

# End Constants ===============================================================

import os
import sys


pin_types = {
    "in": "I",
    "out": "O",
    "bidi": "B",
    "tri": "T",
    "passive": "P",
    "unspec": "U",
    "pwrin": "W",
    "pwrout": "w",
    "oc": "C",
    "oe": "E",
    "nc": "N",
}


def geometry(conf):
    # width is twice the width required to accommodate the longest name
    longest_name = max(max(max(len(pin[0]) for pin in grp) for grp in side)
                       for side in conf['pins'])
    width = 2 * (longest_name + 1) * 50
    width += width % 200

    # height is the maximum required on either side
    left_pins = sum(len(x) for x in conf['pins'][0])
    right_pins = sum(len(x) for x in conf['pins'][1])
    left_groups = len(conf['pins'][0])
    right_groups = len(conf['pins'][1])

    height = 100 * max(
        left_pins + left_groups - 1, right_pins + right_groups - 1)

    # height must be an odd multiple of 0.1" or the grid breaks
    if (height // 100) % 2 == 0:
        height += 100

    # Pin length based on maximum pin number length
    longest_num = max(max(max(len(str(pin[1])) for pin in grp) for grp in side)
                      for side in conf['pins'])
    length = max(100, longest_num*50)
    # Ensure pins will align to a 100mil grid by making the part wider
    if length % 100 != 0:
        width += 100

    return width, height, length, left_groups


def fields(conf):
    width, height, _, lgroups = geometry(conf)
    field_x = -width//2
    field_y = height//2 + 50
    out = []

    # Designator at top
    out.append("F0 \"{}\" {} {} 50 H V L CNN".format(
        conf.get('designator', 'IC'), field_x, field_y))

    # Value/name at bottom
    out.append("F1 \"{}\" {} {} 50 H V L CNN".format(
        conf['name'], field_x, -field_y))

    # Either specify a footprint or just set its size, position, invisibility
    if "footprint" in conf:
        out.append("F2 \"{}\" {} {} 50 H I L CNN".format(
            conf['footprint'], field_x, -field_y-100))
    else:
        out.append("F2 \"\" {} {} 50 H I L CNN".format(field_x, -field_y-100))

    # Specify a datasheet if given
    if "datasheet" in conf:
        out.append("F3 \"{}\" {} {} 50 H I L CNN".format(
            conf['datasheet'], field_x, -field_y-200))
    else:
        out.append("F3 \"\" {} {} 50 H I L CNN".format(field_x, -field_y-200))

    # Order codes
    for idx, (supplier, code) in enumerate(conf.get("ordercodes", [])):
        out.append("F{} \"{}\" {} {} 50 H I L CNN \"{}\"".format(
            idx+4, code, field_x, -field_y-(300+idx*100), supplier))

    return out


def draw_pins(groups, x0, y0, direction, length):
    out = []
    pin_x = x0
    pin_y = y0
    for group in groups:
        for (name, num, t) in group:
            out.append("X {} {} {} {} {} {} 50 50 0 0 {}".format(
                name, num, pin_x, pin_y, length, direction, pin_types[t]))
            pin_y -= 100
        pin_y -= 100
    return out


def draw(conf):
    width, height, length, lgroups = geometry(conf)
    out = []
    out.append("DRAW")

    # Containing box
    out.append("S {} {} {} {} 0 1 0 f".format(
        -width//2, height//2, width//2, -height//2))

    # Pins
    x0 = -width//2 - length
    y0 = height//2 - 50
    out += draw_pins(conf['pins'][0], x0, y0, "R", length)
    out += draw_pins(conf['pins'][1], -x0, y0, "L", length)

    out.append("ENDDRAW")
    return out


def library(conf):
    out = []

    out.append("EESchema-LIBRARY Version 2.3")
    out.append("#encoding utf-8")
    out.append("#\n# {}\n#".format(conf['name']))
    out.append("DEF {} {} 0 40 Y Y 1 F N".format(
        conf['name'], conf.get('designator', 'IC')))

    out += fields(conf)
    out += draw(conf)

    out.append("ENDDEF\n#\n#End Library\n")
    return "\n".join(out)


def documentation(conf):
    out = []
    out.append("EESchema-DOCLIB\tVersion 2.0")
    out.append("$CMP {}".format(conf['name']))
    out.append("D {}".format(conf['description']))
    out.append("$ENDCMP\n")
    return "\n".join(out)


def main(libpath, verify=False):
    for name, conf in config.items():
        conf['name'] = name
        path = os.path.join(libpath, conf.get("path", ""), name.lower()+".lib")
        dcmpath = os.path.splitext(path)[0] + ".dcm"

        lib = library(conf)
        dcm = documentation(conf)

        if verify:
            print("Verifying", path)

        # Check if anything has changed
        if os.path.isfile(path):
            with open(path) as f:
                oldlib = f.read()
            if os.path.isfile(dcmpath):
                with open(dcmpath) as f:
                    olddcm = f.read()
                if lib == oldlib and dcm == olddcm:
                    continue

        # If so, either verification failed or write the new files
        if verify:
            return False
        else:
            with open(path, "w") as f:
                f.write(lib)
            with open(dcmpath, "w") as f:
                f.write(dcm)

    # If we finished and didn't return yet, verification has succeeded
    if verify:
        return True


if __name__ == "__main__":
    if len(sys.argv) == 2:
        libpath = sys.argv[1]
        main(libpath)
    elif len(sys.argv) == 3 and sys.argv[2] == "--verify":
        libpath = sys.argv[1]
        if main(libpath, verify=True):
            print("OK: all libs up-to-date.")
            sys.exit(0)
        else:
            print("Error: libs not up-to-date.", file=sys.stderr)
            sys.exit(1)
    else:
        print("Usage: {} <lib path>".format(sys.argv[0]))
        sys.exit(1)
