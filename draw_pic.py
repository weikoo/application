from PIL import Image
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'.")

WIDTH = 150
HEIGHT = 50

def get_char(r,g,b,alpha = 256):
	if alpha ==0:
		return ' '
	length = len(ascii_char)
	gray = int(0.2126*r+0.7152*g+0.0722*b)
	unit = (256.0+1)/length
	return ascii_char[int(gray/unit)]

if __name__ == '__main__':
	img = 'C:/Users/Administrator/Desktop/z.jpg'
	im = Image.open(img)
	im = im.resize((WIDTH,HEIGHT),Image.NEAREST)
	txt = ""
	for i in range(HEIGHT):
		for j in range(WIDTH):
			txt +=get_char(*im.getpixel((j,i)))
		txt+='\n'
	print(txt)
	with open("C:/Users/Administrator/Desktop/2.txt",'w') as f:
		f.write(txt)
