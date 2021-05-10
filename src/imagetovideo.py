# this file contains all components needed to merge images to a video
import cv2
import os


def image_to_video(*image_paths):
    """
    merges all given images to a video
    """

    size = cv2.imread(image_paths[0]).shape[1::-1]

    out = cv2.VideoWriter("video.avi", cv2.VideoWriter_fourcc(*"DIVX"), 1, size)

    for image_path in image_paths:
        out.write(cv2.imread(image_path))
    
    out.release()


if __name__ == "__main__":
    image_to_video(
        os.path.join(os.path.dirname(__file__), "data", "images", "image.jpg")
    )
