import argparse
import os
import cv2
import numpy as np

def main_function(video_name):

    video_name = "20220926_132122.mp4"
    cap = cv2.VideoCapture(f"video/{video_name}")
    frame_idx = 0

    while cap.isOpened():

        success, frame = cap.read()

        try:
            cv2.imshow(video_name, frame)

        except Exception as e:
            pass

        try:
            if not os.path.isdir(f"frame/{video_name.split('.')[0]}"):
                os.mkdir(f"frame/{video_name.split('.')[0]}")
            else:
                pass

            cv2.imwrite(f"frame/{video_name.split('.')[0]}/{video_name.split('.')[0]}_{frame_idx}.jpg", frame)
            print(f"saved frame [{frame_idx}]...")
            frame_idx += 1

        except Exception as e:
            print(e)
            break

        if cv2.waitKey(1) == 27:
            print("interrupted by user")
            break
    
    print("saved all frames")
    cv2.destroyAllWindows()
    cap.release()

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--name", required=True)
    args = parser.parse_args()

    main_function(video_name=args.name)