from PIL import Image
import os


for filename in os.listdir(os.getcwd()+os.sep+"train_img"):
    # Load foreground image (image to be resized)
    foreground = Image.open(os.getcwd()+os.sep+"train_img"+os.sep+filename)

    # Define the size of the background image
    bg_width = 300  # Width of the background image
    bg_height = 300  # Height of the background image

    # Create a new white background image
    background = Image.new('RGB', (bg_width, bg_height), (255, 255, 255))  # White color

    # Dimensions of the foreground image
    fg_width, fg_height = foreground.size

    # Calculate aspect ratios
    bg_aspect_ratio = bg_width / bg_height
    fg_aspect_ratio = fg_width / fg_height

    # Determine how to resize the foreground image to match either width or height of the background
    if bg_aspect_ratio >= fg_aspect_ratio:
        # Resize based on height
        new_fg_height = bg_height
        new_fg_width = int(fg_width * (bg_height / fg_height))
    else:
        # Resize based on width
        new_fg_width = bg_width
        new_fg_height = int(fg_height * (bg_width / fg_width))

    # Resize the foreground image
    resized_foreground = foreground.resize((new_fg_width, new_fg_height))

    # Paste resized foreground onto the white background
    x_offset = (bg_width - new_fg_width) // 2
    y_offset = (bg_height - new_fg_height) // 2
    background.paste(resized_foreground, (x_offset, y_offset))

    # Save or display the composed image
    background.save("converted_files"+os.sep+"1_"+filename)
    background.show()
