def n():
    from PIL import Image


fn = "sobaken.jpg"
with Image.open(fn) as img:
    img.load()

img.show()
width, height = img.size
f = img.format
m = img.mode

print("sh:", width)
print("v:", height)
print("f:", f)
print("m:", m)


def n1():
    from PIL import Image
    fn = "sobaken.jpg"
    with Image.open(fn) as img:
        img.load()
    ni = img.resize((img.width // 3, img.height // 3))
    ni.save("r_s.jpg")

    converted_img = img.transpose(Image.FLIP_TOP_BOTTOM)
    converted_img.save("image_fs_top.jpg")
    converted_img = img.transpose(Image.FLIP_LEFT_RIGHT)
    converted_img.save("image_fs_lr")


def n2():
    from PIL import Image, ImageFilter
    fn = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]
    for file in fn:
        with Image.open(fn) as img:
            img.load()
            ni = img.filter(ImageFilter.CONTOUR)
            ni.save("n_" + file)


def n3():
    from PIL import Image
    w = "watermark.png"
    with Image.open(w) as img_w:
        img_w.load()
    fn = "sobaken.jpg"
    with Image.open(fn) as img:
        img.load()
    img.paste(img_w, (10, 120), img_w)
    img.save("s_w.jpg")

