import pdf2image

import glob

#a = glob.glob('*.pdf')
#for p in a:
from pdf2image import convert_from_path

# Store Pdf with convert_from_path function
images = convert_from_path('5.pdf')

for i in range(len(images)):
    # Save pages as images in the pdf
    images[i].save(str(i) + '.jpg', 'JPEG')

