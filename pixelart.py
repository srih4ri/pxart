#!/usr/bin/env python
import sys
import Image
import ImageDraw


def get_color(region):
    area_bx = 0
    w,h = region.size
    for i in range(0,w):
        for j in range(0,h):
            pix = region.getpixel((i,j))
            area_bx += sum(pix)/3
    return area_bx/(region.size[0]*region.size[1])


def pixelize(region):
    "Fill a given region with color calculated for that region"
    px_color = get_color(region)
    draw_region = ImageDraw.Draw(region)
    draw_region.rectangle([0,0,pixel_size[0],pixel_size[1]],fill=px_color)
    return region

def pixel_art(image,px_size):
    "Produce pixel art of an image"
    px_w,px_h = px_size
    width,height = image.size
    px_art = Image.new('RGB',(width,height))
    for x in range(0,width,px_w):
        for y in range(0,height,px_h):
            box = (x,y,x+px_w,y+px_h)
            region = image.crop(box)
            pixel = pixelize(region)
            px_art.paste(pixel,box)
    return px_art

if __name__ == "__main__":
    img = Image.open(sys.argv[1])
    pixel_size = [int(sys.argv[2]),int(sys.argv[3])]
    art = pixel_art(img,pixel_size)
    art.show()
    art.save(img.filename+'_pixel_art.jpg')
