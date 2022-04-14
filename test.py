"""
Test code for the Python library.
"""

import imageio as iio
import adafruit_thermal as at
import time

printer = at.AdafruitThermal(None)
printer.begin()

printer.print_qr_code("Hello World")

# Test Barcodes

print("Testing barcodes")

printer.justify('C')
printer.bold_on()
printer.println("BARCODE EXAMPLES\n")
printer.bold_off()
printer.justify('L')
printer.print("UPC-A:")
printer.print_barcode("123456789012", printer.BARCODE_UPC_A)
printer.print("EAN-13:")
printer.print_barcode("1234567890123", printer.BARCODE_EAN13)
printer.print("EAN-8:")
printer.print_barcode("12345678", printer.BARCODE_EAN8)
printer.print("CODE 39:")
printer.print_barcode("ADAFRUT", printer.BARCODE_CODE39)
printer.print("ITF:")
printer.print_barcode("1234567890", printer.BARCODE_ITF)
printer.print("CODABAR:")
printer.print_barcode("1234567890", printer.BARCODE_CODABAR)
printer.print("CODE 93:")
printer.print_barcode("ADAFRUIT", printer.BARCODE_CODE93)
printer.print("CODE128:")
printer.print_barcode("Adafruit", printer.BARCODE_CODE128)
printer.feed(2)
printer.set_default()

# Charsets
def dump(printer):
    printer.println("        01234567  89ABCDEF")
    major = 0
    while major < 16:
        printer.print("     ")
        printer.print(str(major))
        printer.print("- ")
        minor = 0
        while minor < 16:
            c = (major << 4) | minor
            if c < 32:
                c = ' '  # Skip control codes!
            printer.write(c)

            if minor == 7:
                printer.print("  ")

            minor += 1

        printer.println()


print("Testing charsets")

printer.underline_on()
printer.println("CHARACTER SET EXAMPLE\n")
printer.underline_off()

printer.println("DEFAULT CHARSET & CODE PAGE:")
dump(printer)
printer.println("\nNORWAY CHARSET w/")
printer.println("KATAKANA CODEPAGE:")
printer.set_charset(printer.CHARSET_NORWAY)
printer.set_codePage(printer.CODEPAGE_KATAKANA)
dump(printer)
printer.feed(2)
printer.set_default()

# Printer Test

print("Printer test")

# Font options
printer.set_font('B')
printer.println("FontB")
printer.println("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
printer.set_font('A')
printer.println("FontA (default)")
printer.println("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

# Test inverse on & off
printer.inverse_on()
printer.println("Inverse ON")
printer.inverse_off()

# Test character double-height on & off
printer.double_height_on()
printer.println("Double Height ON")
printer.double_height_off()

# Set text justification (right, center, left) -- accepts 'L', 'C', 'R'
printer.justify('R')
printer.println("Right justified")
printer.justify('C')
printer.println("Center justified")
printer.justify('L')
printer.println("Left justified")

# Test more styles
printer.bold_on()
printer.println("Bold text")
printer.bold_off()

printer.underline_on()
printer.println("Underlined text")
printer.underline_off()

printer.set_size('L')  # Set type size, accepts 'S', 'M', 'L'
printer.println("Large")
printer.set_size('M')
printer.println("Medium")
printer.set_size('S')
printer.println("Small")

printer.justify('C')
printer.println("normal\nline\nspacing")
printer.set_line_height(50)
printer.println("Taller\nline\nspacing")
printer.set_line_height()  # Reset to default
printer.justify('L')

# Barcode examples:
# CODE39 is the most common alphanumeric barcode:
printer.print_barcode("ADAFRUT", printer.BARCODE_CODE39)
printer.set_barcode_height(100)
# Print UPC line on product barcodes:
printer.print_barcode("123456789123", printer.BARCODE_UPC_A)

printer.sleep()  # Tell printer to sleep
time.sleep(3) # Sleep 3 seconds
printer.wake()  # MUST wake() before printing again, even if reset
printer.set_default()  # Restore printer to defaults
