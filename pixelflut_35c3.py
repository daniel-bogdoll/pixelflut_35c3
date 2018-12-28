import socket
HOST = '151.217.40.82'
PORT = 1234
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
send = sock.sendall

def pixel(x,y,r,g,b,a=255):
    if a == 255:
        command = 'PX %d %d %02x%02x%02x\n' % (x,y,r,g,b) 
        send(command.encode('utf-8'))
    else:
        command = 'PX %d %d %02x%02x%02x%02x\n' % (x,y,r,g,b,a)
        send(command.encode('utf-8'))

from PIL import Image
im = Image.open('image.png').convert('RGB')
im.thumbnail((200,300), Image.ANTIALIAS)
_,_,w,h = im.getbbox()  
while True:
    for x in range(w):
        for y in range(h):
            r,g,b = im.getpixel((x,y))
            pixel(x,y,r,g,b)
