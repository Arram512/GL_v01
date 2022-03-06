from PIL import Image
import images2gif

frames = images2gif.readGif('g1.gif', False)
for frame in frames:
	frame.thumbnail((900, 900), Image.ANTIALIAS)

images2gif.writeGif('tumban.gif', frames)

