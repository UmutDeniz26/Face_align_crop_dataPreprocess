import os
def calculate_average_img_size(folder_path):
    total_width = 0;total_height = 0;total_counter = 0
    for root_path, dir_names, file_names in os.walk(folder_path):
        for file_name in file_names:
            if file_name.endswith('.jpg'):
                img_path = os.path.join(root_path, file_name)
                img = cv2.imread(img_path)
                total_width += img.shape[1]
                total_height += img.shape[0]
                total_counter += 1
    Average_width = total_width/total_counter
    Average_height = total_height/total_counter
    Average_size = Average_width * Average_height
    return Average_size

import cv2

def verify_img_size(folder_path):
    for root_path, dir_names, file_names in os.walk(folder_path):
        if "Frontal" in root_path or "frontal" in root_path:
            continue
        if len(file_names)>4:
            average_size = calculate_average_img_size(root_path)
            
        for file_name in file_names:
            if file_name.endswith('.jpg'):
                img_path = os.path.join(root_path, file_name)
                img = cv2.imread(img_path)
                img_size = img.shape[0] * img.shape[1]
                differece = abs(img_size - average_size)
                if differece > average_size:
                    print(f"Image size is too large: {img_path} with size: {img_size}")

if __name__ == '__main__':
    verify_img_size("UMUT\database\AFW_FOLDERED_without_errors")