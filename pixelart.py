#!/usr/bin/env python
import sys
import Image
import ImageDraw
from collections import defaultdict
import os

def my_getcolors(reg):
    w,h = reg.size
    color_map = defaultdict(int)
    for i in range(0,w):
        for j in range(0,h):
            pix = reg.getpixel((i,j))
            if color_map[pix] == 0:
                color_map[pix] = 1 
            else: 
                color_map[pix] += 1
#For some reason i hate the following line of code
    return {v:k for k, v in color_map.items()}

def get_color(region):
    'Return average color of a region'   
    color_dist = my_getcolors(region)
    max_color = color_dist[max(color_dist.keys())]
    return max_color


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
    art.save('pixelised_'+os.path.basename(img.filename))
