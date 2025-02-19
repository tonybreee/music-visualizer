import cv2
import numpy as np
import moviepy.editor as mp

def generate_visualization(audio_path, output_video_path, pixel_size, animation_type):
    # Dummy-Bild als Platzhalter (später: Albumcover extrahieren)
    img = np.ones((500, 500, 3), dtype=np.uint8) * 255

    # Verpixelung
    img = cv2.resize(img, (img.shape[1] // pixel_size, img.shape[0] // pixel_size))
    img = cv2.resize(img, (500, 500), interpolation=cv2.INTER_NEAREST)

    # Speichern als Video
    clip = mp.ImageSequenceClip([img for _ in range(100)], fps=24)
    audio = mp.AudioFileClip(audio_path)
    clip = clip.set_audio(audio)
    clip.write_videofile(output_video_path, codec="libx264")

    return output_video_path
