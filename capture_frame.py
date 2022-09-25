import argparse
import os
import glob
import cv2

def main_function(user_os, frame_interval):

    video_path = "video/*.mp4"

    for bb, file_name in enumerate(glob.glob(video_path)):

        name_wo_format = file_name.split('.')[0]

        if user_os == "windows":
            name_wo_path = name_wo_format.split('\\')[-1]
        else:
            name_wo_path = name_wo_format.split('/')[-1]

        cap = cv2.VideoCapture(file_name)
        frame_save_idx = 0
        frame_passed = 0

        while cap.isOpened():

            success, frame = cap.read()

            try:
                cv2.imshow(file_name, frame)

            except Exception as e:
                pass

            try:
                if not os.path.isdir(f"frame/{name_wo_path}"):
                    os.mkdir(f"frame/{name_wo_path}")
                else:
                    pass

                if frame_passed > int(frame_interval):
                    cv2.imwrite(f"frame/{name_wo_path}/{name_wo_path}_{frame_save_idx}.jpg", frame)
                    print(f"saved frame [{name_wo_path}_{frame_save_idx}.jpg]...")
                    frame_passed = 0
                    frame_save_idx += 1

            except Exception as e:
                print(e)
                break

            if cv2.waitKey(1) == 27:
                print("interrupted by user")
                break

            frame_passed += 1
        
        print("saved all frames")
        cv2.destroyAllWindows()
        cap.release()

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--os", required=True)
    parser.add_argument("--frame", default=10)
    args = parser.parse_args()

    main_function(args.os, args.frame)