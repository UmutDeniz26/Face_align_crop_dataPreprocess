import numpy as np
import os
import cv2
def main(npy_folder_path):
    data = np.load(npy_folder_path)
    data2 = np.load("esogu_sets_meta_10_people.npy", allow_pickle=True)
    print("\n\n\n",npy_folder_path)
    print(data.shape)

    for index,path in enumerate(data["mask"]):
        path = os.path.join("UMUT/src/final_datasets/", path)
        if index%1000==0:
            print("Counter: ",index," Path: ",path)
        try:
            if os.path.exists(path):
                True
            else:
                print("Path is not valid: ", path)
                exit()
        except:
            print("Path is not valid: ", path)
            exit()

    #print(data2)
    print(data2.shape)
    #print(data_concat)
    try:
        data_concat = np.concatenate((data, data2))
        print("Concatenation is successful")
    except:
        print("Concatenation is not successful")
    #print(data_concat)


if __name__ == '__main__':
    #main("UMUT/src/npy/YoutubeVideos_Info.npy")
    #main("UMUT/src/final_datasets/AFW/AFW_Info.npy")
    #main("UMUT/src/final_datasets/CASIA-FaceV5_BMP_FOLDERED_Info/CASIA-FaceV5_BMP_FOLDERED_Info.npy")
    #main("UMUT/src/final_datasets/HELEN_Info/HELEN_Info.npy")
    #main("UMUT/src/final_datasets/LFW/LFW_Info.npy")
    #main("UMUT/src/final_datasets/LFPW_Info/LFPW_Info.npy")
    pass
