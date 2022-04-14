# Adafruit Thermal Printer Library (Python 3)

During a Raspberry PI project, I wanted to connect the [Adafruit Mini Thermal Receipt Printer](https://www.adafruit.com/product/597) directly to the Raspberry PI. Therfore, I ported the [existing Arduino C library](https://github.com/adafruit/Adafruit-Thermal-Printer-Library) to Python 3.

The main usage of the library is currently for our [Gify-Box](https://github.com/informatik-mannheim/gify-box).


## Required Libraries

This library uses the following other libraries:

* qrcode[pil]
* imageio
* pyserial
* PIL
