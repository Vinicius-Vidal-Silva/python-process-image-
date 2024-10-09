from skimage.transform import resize

def resize_image(image, proportion):
    assert 0 <= proportion  <= 1, "Specify a valid proportion between 0 and 1."

    