This repo is for the Raspberry Pi instructional presentation.
It contains demo code to show how to interface to various hardware

The current demo RPi is an RPi Zero W with the following pinouts:

 +----------+-----+---------+------+---+---Pi 2---+---+------+---------+-----+--------+&nbsp;
 | Use      | BCM |   Name  | Mode | V | Physical | V | Mode | Name    | BCM | Use    |&nbsp;
 +----------+-----+---------+------+---+----++----+---+------+---------+-----+--------+&nbsp;
 |          |     |    3.3v |      |   |  1 || 2  |   |      | 5v      |     |        |&nbsp;
 | 3xs SDA  |   2 |   SDA.1 | ALT0 | 1 |  3 || 4  |   |      | 5V      |     |        |&nbsp;
 | 3xs SCL  |   3 |   SCL.1 | ALT0 | 1 |  5 || 6  |   |      | 0v      |     |        |&nbsp;
 |          |   4 | GPIO. 7 |   IN | 1 |  7 || 8  | 1 | ALT0 | TxD     | 14  |        |&nbsp;
 |          |     |      0v |      |   |  9 || 10 | 1 | ALT0 | RxD     | 15  |        |&nbsp;
 |          |  17 | GPIO. 0 |   IN | 0 | 11 || 12 | 0 | IN   | GPIO. 1 | 18  |        |&nbsp;
 |          |  27 | GPIO. 2 |   IN | 0 | 13 || 14 |   |      | 0v      |     |        |&nbsp;
 |          |  22 | GPIO. 3 |   IN | 0 | 15 || 16 | 0 | IN   | GPIO. 4 | 23  |        |&nbsp;
 |          |     |    3.3v |      |   | 17 || 18 | 0 | IN   | GPIO. 5 | 24  |        |&nbsp;
 |          |  10 |    MOSI | ALT0 | 0 | 19 || 20 |   |      | 0v      |     |        |&nbsp;
 |          |   9 |    MISO | ALT0 | 0 | 21 || 22 | 0 | IN   | GPIO. 6 | 25  |        |&nbsp;
 |          |  11 |    SCLK | ALT0 | 0 | 23 || 24 | 1 | ALT0 | CE0     | 8   |        |&nbsp;
 |          |     |      0v |      |   | 25 || 26 | 1 | ALT0 | CE1     | 7   |        |&nbsp;
 |          |   0 |   SDA.0 |   IN | 1 | 27 || 28 | 1 | IN   | SCL.0   | 1   |        |&nbsp;
 |          |   5 | GPIO.21 |   IN | 1 | 29 || 30 |   |      | 0v      |     |        |&nbsp;
 |          |   6 | GPIO.22 |   IN | 1 | 31 || 32 | 0 | IN   | GPIO.26 | 12  |        |&nbsp;
 |          |  13 | GPIO.23 |   IN | 0 | 33 || 34 |   |      | 0v      |     |        |&nbsp;
 |          |  19 | GPIO.24 |   IN | 0 | 35 || 36 | 0 | IN   | GPIO.27 | 16  |        |&nbsp;
 |          |  26 | GPIO.25 |   IN | 0 | 37 || 38 | 0 | IN   | GPIO.28 | 20  |        |&nbsp;
 |          |     |      0v |      |   | 39 || 40 | 0 | IN   | GPIO.29 | 21  |        |&nbsp;
 +----------+-----+---------+------+---+----++----+---+------+---------+-----+--------+&nbsp;
 | Use      | BCM |   Name  | Mode | V | Physical | V | Mode | Name    | BCM | Use    |&nbsp;
 +----------+-----+---------+------+---+---Pi 2---+---+------+---------+-----+--------+&nbsp;
 &nbsp;
 3xs - 3 Axis Accelorator
