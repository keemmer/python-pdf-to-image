from pdf2image import convert_from_path

images = convert_from_path('i1.pdf',500)
for image in images:
    image.save('page.jpg','JPEG')
