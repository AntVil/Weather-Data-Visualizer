# this file contains all components needed to merge images to a video
import imageio
import os


def image_to_video(image_paths, save_to):
    """
    merges all given images to a video
    """

    video_writer = imageio.get_writer(save_to, fps=6)

    for image_path in image_paths:
        video_writer.append_data(imageio.imread(image_path))
    
    video_writer.close()


if __name__ == "__main__":
    image_folder = os.path.join(os.path.dirname(__file__), "data", "testing", "image")

    image_to_video(
        [os.path.join(image_folder, file) for file in os.listdir(image_folder)],
        os.path.join(os.path.dirname(__file__), "data", "testing", "video", "_test_video.mp4")
    )
