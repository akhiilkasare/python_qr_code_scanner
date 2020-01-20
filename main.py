import pyqrcode

url = pyqrcode.create("www.instagram.com/akhiilkasare")

url.svg('uca-url.svg', scale=8)
print(url.terminal(quiet_zone=1))
