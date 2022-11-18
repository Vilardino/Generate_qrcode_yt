# Importing library
import qrcode
 
with open('links.txt','r') as a:
    links = a.readlines()

# Data to be encoded

for i in links:
    # Encoding data using make() function
    print(i)
    img = qrcode.make(i)
    lixo,png = i.split('=')
    # Saving as an image file
    img.save('.\\QR\\'+png[:-2]+'.png')

img = qrcode.make('https://youtube.com/playlist?list=PLXP-A8qzEKQO0qE-eBqqRcaDkpMVyvH4Q')
lixo,png = i.split('=')
# Saving as an image file
img.save('playlist.png')