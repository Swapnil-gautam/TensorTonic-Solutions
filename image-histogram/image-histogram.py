def image_histogram(image):
    """
    Compute the intensity histogram of a grayscale image.
    """
    # Write code here
    Hist = [0] * 256
    for i in range(len(image)):
        for j in range(len(image[0])):
            Hist[image[i][j]] += 1

    return Hist