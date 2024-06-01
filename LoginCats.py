from chafa import *
from chafa.loader import Loader
import sys
import glob
import random

if __name__ == "__main__":
    catDir = sys.argv[1]
    if catDir == "":
        print("No image direction is specified!")
    else:
        config = chafa.CanvasConfig()

        files = glob.glob(catDir+"*")
        catImages = []
        # You can expend this list as you see fit
        # I dont recommend adding animated format like gif because it will not be displayed correctly
        imageExt = ["png","jpg","jpeg"]
        for file in files:
            if file.split(".")[-1] in imageExt:
                catImages.append(file)
        if len(catImages) > 0:
            image = Loader(random.choice(catImages))

            #You should change this values if image is stretched out
            config.height = 40
            config.width  = 40

            config.calc_canvas_geometry(
                image.width,
                image.height,
                # You should correct the ratio below.
                # This ration represents the width of your current font size divided by its height.
                # 13/30 work good with Meslo fonts
                # 11/24 work good with Jetbrains Mono
                # Unless your font have info on its font ratio you can only find you right ration by trial
                13/30
            )

            canvas = chafa.Canvas(config)

            canvas.draw_all_pixels(image.pixel_type,image.get_pixels(),image.width,image.height,image.rowstride)

            print(canvas.print().decode())
            
            #An optional space for message after the printing of the image
            if len(sys.argv) > 2:
                print(sys.argv[2])
        else:
            print("Something wrong happened while opening images at : " + sys.argv[1])