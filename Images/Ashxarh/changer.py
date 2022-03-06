from PIL import Image, ImageSequence

# Output (max) size
size = 800, 800

# Open source
im = Image.open("abovia.gif")

# Get sequence iterator
frames = ImageSequence.Iterator(im)

# Wrap on-the-fly thumbnail generator
def thumbnails(frames):
    for frame in frames:
        thumbnail = frame.copy()
        thumbnail.thumbnail(size, Image.ANTIALIAS)
        yield thumbnail

frames = thumbnails(frames)

# Save output
om = next(frames) # Handle first frame separately
om.info = im.info # Copy sequence info
om.save("abovia1.gif", save_all=True, append_images=list(frames), loop=0)
