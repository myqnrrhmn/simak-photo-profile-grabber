import requests
from PIL import Image
from io import BytesIO
import random
import string
import time
import itertools

academic_map = {
    "Teknik Mesin": 1,
    "Teknik Industri": 2,
    "Teknik Tekstil": 3,
    "Manajemen Industri": 4,
    "Teknik Informatika": 5
}

academic_program = input("Program studi: ")
academic_program = academic_map.get(academic_program)

if academic_program is None:
    print("Program studi tidak dikenali!")
    exit()

batch = input("Angkatan: ")

for i in range(0, 1000):  # ganti while dengan for agar lebih pythonic
    try:
        if i < 10:
            filename = f"700{i}.png"
        elif i < 100:
            filename = f"70{i}.png"
        else:
            filename = f"7{i}.png"

        url = f'https://simak.wastu.digital/assets/poto/mhs/{batch}/{academic_program}/{filename}?rand=460'
        response = requests.get(url)

        if response.status_code == 200:
            try:
                image = Image.open(BytesIO(response.content))

                if image.mode == 'RGBA':
                    image = image.convert('RGB')
                    
                random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
                image.save(f'{batch}-{academic_program}-image-{random_string}{i}.jpg')
                print(f"Fetched: {random_string}")
            except Exception as e:
                print(f"Gagal membuka/simpan gambar: {e}")
        else:
            print("Searching...")

        time.sleep(0.2)

    except requests.exceptions.RequestException as e:
        print(f"Gagal melakukan request ke-{i}: {e}")
