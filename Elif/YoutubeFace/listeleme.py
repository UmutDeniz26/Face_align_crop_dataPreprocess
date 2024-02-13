import os

# Veri setinin bulunduğu dizin
dataset_path = "./Elif/YoutubeFace/YoutubeFace"

# Çıktı dosyasının adı
output_file = './Elif/YoutubeFace/output_NewYoutube.txt'

counter = 0
#print(os.listdir("./Elif/YoutubeFace/aligned_images_DB2"))

# Dosya açma işlemi
with open(output_file, 'w') as file:
    #file.write('personname_klasor_img\n')
    # Ana dizindeki klasörleri listele
    sorted_listdir = sorted(os.listdir(dataset_path))

    for person_name in sorted_listdir:
        person_path = os.path.join(dataset_path, person_name)

        # Klasörleri kontrol et ve içerisindeki dosyaları listele
        if os.path.isdir(person_path):
           # file.write(f'{person_name}')

            # Person'a ait tüm alt klasörlerdeki görselleri listele
            person_images = []

            sorted_subfolder = sorted(os.listdir(person_path))

            for subfolder_name in sorted_subfolder:
                subfolder_path = os.path.join(person_path, subfolder_name)

                if os.path.isdir(subfolder_path):
                    # Alt klasördeki dosyaları listele

                    sorted_subfolderpath = sorted(os.listdir(subfolder_path))
                    for image_file in sorted_subfolderpath:
                        person_number = f'{counter:05d}'
                        image_file = image_file.split('.')
                        if len(image_file) > 2:
                            number_between_dots = image_file[-2]
                        else:
                            print("Noktalar arasında bir sayı bulunamadı.")
                        person_images.append(f'\t {person_number}_{subfolder_name}_{number_between_dots}')

            # Person'a ait tüm görselleri tek bir satırda listeleyerek yaz
            file.write('\n'.join(person_images))
            file.write('\n')

            counter += 1

# Bilgileri içeren txt dosyası oluşturuldu
print(f'Liste oluşturuldu ve {output_file} adında kaydedildi.')