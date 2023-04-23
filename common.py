import matplotlib.pyplot as plt
import numpy as np

def show_result(img, caption):
    plt.figure(figsize=(16,10))
    plt.title(caption)
    plt.imshow(img)
    plt.axis("off")
    plt.show()
