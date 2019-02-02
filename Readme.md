This repo is for the Raspberry Pi instructional presentation.
It contains demo code to show how to interface to various hardware

The current demo RPi is an RPi Zero W with the following pinouts:

 | Use      | BCM |   Name  | Mode | V | Physical| V | Mode | Name    | BCM | Use    |
 |---|---|---|---|---|---|---|---|---|---|---|
 |         |     |   -3.3v |      | - |  1 - 2  | - |      | 5v      |     |        |
 | 3xs SDA |   2 |   SDA.1 | ALT0 | 1 |  3 - 4  |   |      | 5V      |     |        |
 | 3xs SCL |   3 |   SCL.1 | ALT0 | 1 |  5 - 6  |   |      | Gnd     |     |        |
 | 3LED-R  |   4 | GPIO. 7 |   IN | 1 |  7 - 8  | 1 | ALT0 | TxD     | 14  |        |
 |         |     |    Gnd  |      |   |  9 - 10 | 1 | ALT0 | RxD     | 15  |        |
 | 3LED-G  |  17 | GPIO. 0 |   IN | 0 | 11 - 12 | 0 | IN   | GPIO. 1 | 18  |L298N-1 |
 | 3LED-B  |  27 | GPIO. 2 |   IN | 0 | 13 - 14 |   |      | Gnd     |     |        |
 | DSP4-d  |  22 | GPIO. 3 |   IN | 0 | 15 - 16 | 0 | IN   | GPIO. 4 | 23  |L298N-2 |
 |         |     |    3.3v |      |   | 17 - 18 | 0 | IN   | GPIO. 5 | 24  |UL2k3-4 |
 | UL2k3-3 |  10 |    MOSI | ALT0 | 0 | 19 - 20 |   |      | Gnd     |     |        |
 |         |   9 |    MISO | ALT0 | 0 | 21 - 22 | 0 | IN   | GPIO. 6 | 25  |Srvo    |
 |         |  11 |    SCLK | ALT0 | 0 | 23 - 24 | 1 | ALT0 | CE0     | 8   |UL2k3-1 |
 |         |     |     Gnd |      |   | 25 - 26 | 1 | ALT0 | CE1     | 7   |UL2k3-2 |
 |         |   0 |   SDA.0 |   IN | 1 | 27 - 28 | 1 | IN   | SCL.0   | 1   |        |
 | NOSw    |   5 | GPIO.21 |   IN | 1 | 29 - 30 |   |      | Gnd     |     |        |
 | TSw     |   6 | GPIO.22 |   IN | 1 | 31 - 32 | 0 | IN   | GPIO.26 | 12  | DSP1-d |
 | DSP1-c  |  13 | GPIO.23 |   IN | 0 | 33 - 34 |   |      | Gnd     |     |        |
 | DSP2-c  |  19 | GPIO.24 |   IN | 0 | 35 - 36 | 0 | IN   | GPIO.27 | 16  | DSP2-d |
 | DSO3-c  |  26 | GPIO.25 |   IN | 0 | 37 - 38 | 0 | IN   | GPIO.28 | 20  | DSP3-d |
 |         |     |     Gnd |      |   | 39 - 40 | 0 | IN   | GPIO.29 | 21  | DSP4-c |
 
 3LED - LED \
 NOSw - Normally Open, Momentary Switch \
 TSw - Normally Open, Toggle Switch \
 DSP1 - VMA425 LED Display \
 DSP2 - VMA425 LED Display \
 DSP3 - VMA425 LED Display \
 DSP4 - WMA425 LED Display \
 L298N - Dual H-Bridge \
 Rly - Relay Module \
 ULN2k3 - 5v Stepper Driver \
 TLC548 - A/D Converter \
 3xs - 3 Axis Accelorator \
 
