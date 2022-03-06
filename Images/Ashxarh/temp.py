import os
from PIL import Image

for item in os.listdir():
	if "ա" in item:
		os.remove(item)
