from PIL import Image,ImageDraw, ImageFont


def add_watermark(input_image,output_image,text):
    orginal_image = Image.open(input_image)
    water_mark_img = Image.new("RGBA",orginal_image.size)
    watermark_draw =ImageDraw.Draw(water_mark_img)
    font =ImageFont.truetype('arial.ttf',100)
    width,height =orginal_image.size
    watermark_draw.text((0,height/2),text=text,fill=(255,255,255,140),font=font)

    water_marked_image = Image.alpha_composite(im1=orginal_image.convert("RGBA"),im2=water_mark_img)
    water_marked_image.save(output_image,"PNG")
    print("Watermarked Image Genarated")


input_image = 'input.jpeg'
output_image ='output.png'
text = input("Enter Your Watermakr Text")


add_watermark(input_image,output_image,text)
