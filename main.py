import os
import pyqrcode
import png
import webbrowser
from PIL import Image
from pyzbar import pyzbar
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def create_qr_code():
    print("To create a QR, press 1")
    print("To decode a QR, press 2")
    print("To exit, press q")

    act = input("Enter the command: ")

    if act == '1':
        s = input("Enter the URL: ")

        url = pyqrcode.create(s)
        url.png('myqr.png', scale=18)
        loc = os.getlogin()
        z = 'Users'
        print("QR code created under C:\{}\{}".format(z, loc))

        afterfilecreate = input("Would you like to open the file? (Y/N): ").lower()

        if afterfilecreate == 'y':
            img = Image.open('myqr.png')
            img.show()
        else:
            quit()

    elif act == '2':
        Tk().withdraw()
        filename = askopenfilename()

        if filename[-3:] == 'png':
            image = Image.open(filename)
            qr_code = pyzbar.decode(image)[0]
            data = qr_code.data.decode("utf-8")
            print(data)

            if data[-3:] == 'com':
                print("Redirecting to link present in the QR")
                webbrowser.open(data)

        else:
            print("The file should be a png file, not a {}".format(filename[-3:]))

    elif act.lower() == 'q':
        print("Exited successfully")
        quit()

    else:
        print("Unknown input!")

try:
    create_qr_code()

except KeyboardInterrupt:
    print("Keyboard Interrupt")
    quit()

except IndexError:
    print("Index error occurred, please check the input")

except FileNotFoundError:
    print("Selected file is not found, please check the file destination!!!")
