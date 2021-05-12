# this file contains all components needed to merge images to a video
import cv2
import os


# constants
IMAGES_FOLDER = os.path.join(os.path.dirname(__file__), "data", "images")
VIDEOS_FOLDER = os.path.join(os.path.dirname(__file__), "data", "videos")


def image_to_video(image_paths, save_to=os.path.join(VIDEOS_FOLDER, "_test_video.mp4")):
    """
    merges all given images to a video
    """

    size = cv2.imread(image_paths[0]).shape[1::-1]

    out = cv2.VideoWriter(save_to, cv2.VideoWriter_fourcc(*"mp4v"), 12, size)

    for image_path in image_paths:
        out.write(cv2.imread(image_path))
    
    out.release()


if __name__ == "__main__":
    image_to_video(
        [os.path.join(IMAGES_FOLDER, f"_test_image_{i}.png") for i in range(25)],
        os.path.join(VIDEOS_FOLDER, "_test_video.mp4")
    )
