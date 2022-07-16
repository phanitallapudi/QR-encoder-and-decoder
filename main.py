import pyqrcode
import png
import os
from PIL import Image
import stat

try:
    print("To create a QR press 1\nTo decode a qr press 2\nTo exit press q\n")
    print("*******************************************\n")

    act = input("Enter the command: ")
    if act == '1':
        print("\n*******************************************\n")
        s = input("Enter the URL: ")

        url = pyqrcode.create(s)

        url.png('myqr.png', scale = 18)
        loc = os.getlogin()
        z = 'Users'
        print("jpg file created under C:\{}\{}".format(z,loc))

    elif act == '2':
        from pyzbar import pyzbar
        from tkinter import Tk
        from tkinter.filedialog import askopenfilename

        Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
        filename = askopenfilename()

        if filename[-3:] == 'png':
            image = Image.open(filename)
            qr_code = pyzbar.decode(image)[0]
            data = qr_code.data.decode("utf-8")
            print("\n*******************************************\n")
            print(data)
        
        else:
            print("The file should be a png file not a {}".format(filename[-3:]))

    elif act == 'q' or act == 'Q':
        print("Exited successfully")
        quit()

    else:
        print("\n*******************************************\n")
        print("Unknown input!")

except KeyboardInterrupt:
    print("\n*******************************************\n")
    print("Keyboard Interrupt")
    quit()
    
except IndexError:
    print("\n*******************************************\n")
    print("Index error occured, please check the input")

    sfd = input("Press q to exit and c to continue: ").lower()

    if sfd == 'q':
        loop = False
    elif sfd == 'c':
        pass
    else:
        print("\n*******************************************\n")
        print("Unknown command!")