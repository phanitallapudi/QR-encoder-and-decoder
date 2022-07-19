
import os
import pyqrcode
import png
import webbrowser

from PIL import Image
from pyzbar import pyzbar
from tkinter import Tk
from tkinter.filedialog import askopenfilename

try:
    print("To create a QR press 1\nTo decode a qr press 2\nTo exit press q\n")
    print("*******************************************\n")

    act = input("Enter the command: ")                                          #Taking input from the user to perform next opertion
    if act == '1':                                                              #If the input is '1', then user will be asked for content to create a QR Code
        print("\n*******************************************\n")                #Content of QR will be entered here
        s = input("Enter the URL: ")

        url = pyqrcode.create(s)                                                #After the content given by the user, pyqrcode module is used to create the qr

        url.png('myqr.png', scale = 18)
        loc = os.getlogin()
        z = 'Users'
        print("jpg file created under C:\{}\{}".format(z,loc))
        print("\n*******************************************\n")
       
        afterfilecreate = input("Would you like to open the file(Y/N): ").lower()#Here if the input given by user is 'Y', then the created QR code will be open

        if afterfilecreate == 'y':                                               #########################Read this below line########################
            img = Image.open('myqr.png')                                         #Please change mentioned default user name as the whatever output you get from os.getlogin()
            img.show()                                                           #########################Read this above line########################
        else:
            quit()

    elif act == '2':                                                             #If the input in first stage is '2', then the operation is going to decode the QR

        Tk().withdraw()                                                          #we don't want a full GUI, so keep the root window from appearing
        filename = askopenfilename()                                             #A windows will be open to select the file to decode the QR

        if filename[-3:] == 'png':                                              #If the file selected in above process is a png file, then it will continue the process
            image = Image.open(filename)                                        
            qr_code = pyzbar.decode(image)[0]
            data = qr_code.data.decode("utf-8")                                 #using UTF-8, we are decoding the content of the QR.
            print("\n*******************************************\n")
            print(data)

            if data[-3:] == 'com':                                              #If the content contains 'com', in the last letters, then it will be considered as an external link and will be redirected to that link
                print("\n*******************************************\n")
                print("Redirecting to link present in the QR")
                webbrowser.open(data)
            
        
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

except FileNotFoundError:
    print("selected file is not found, please check the file destination!!!")