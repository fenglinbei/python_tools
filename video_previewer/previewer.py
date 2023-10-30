import os
import cv2

from typing import Optional

from utils import pad2square

preview_frames = 20
save_frame = True
video_path = "E:/资料/相片/2020-07-06 145911.mov"
save_dir = "./data/images/video_preview/"

def preview(path: str, preview_frames: int, save: bool = True, preview_size: int = 640, save_dir: Optional[str] = None):
    video = cv2.VideoCapture(path)

    frame_count = video.get(cv2.CAP_PROP_FRAME_COUNT)
    frame_skip = int(frame_count // preview_frames)

    video_name = video_path.split("/")[-1].split(".")[0].replace(" ", "_")
    save_dir = os.path.join(save_dir, video_name)
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    count = 0

    print(f"Processing frame count {count}")

    if video.isOpened():
        ret, frame = video.read()

        frame, _, _, _ = pad2square(frame, preview_size)

        if ret:
            if save:
                cv2.imwrite(os.path.join(save_dir, video_name + f"_{count}.jpg"), frame)
            else:
                cv2.imshow('Frame', frame)
    
    count += 1

    while video.isOpened():
        

        if not save:

            if cv2.waitKey(0) & 0xFF == ord('n'):

                print(f"Processing frame count {count}")
                ret, frame = video.read()
                
                if ret:
                    frame, _, _, _ = pad2square(frame, preview_size)
                    cv2.imshow('Frame', frame)

                    for i in range(frame_skip):
                        ret, frame = video.read()
                        if not ret:
                            break
                
                else:
                    break
            
            elif cv2.waitKey(0) & 0xFF == ord('q'):
                break
        else:

            print(f"Processing frame count {count}")
            ret, frame = video.read()
            
            if ret:
                frame, _, _, _ = pad2square(frame, preview_size)
                cv2.imwrite(os.path.join(save_dir, video_name + f"_{count}.jpg"), frame)
                count += 1

                for i in range(frame_skip):
                    ret, frame = video.read()
                    if not ret:
                        break
            else:
                break
            



    cv2.destroyAllWindows()
    video.release()

if __name__ == "__main__":
    preview(video_path, preview_frames, save=True, save_dir=save_dir)
