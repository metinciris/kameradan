import cv2
import pytesseract
import os
import re
import pyperclip
import pygame  # pygame'i ekledik
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw, ImageFont

# Tesseract konumunu ve tessdata yolunu belirtin
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
os.environ['TESSDATA_PREFIX'] = r'C:\Program Files\Tesseract-OCR\tessdata'

# Pygame ile ses çalma işlevini başlat
pygame.mixer.init()

# Global değişkenler
cap = None
paused = False
year_suffix = '24'  # Yıl ekini burada tanımlayın
found_text = ""  # Bulunan metni saklamak için

def find_report_number(text):
    pattern = r'\b\d{5}/' + year_suffix + r'\b'  # 5 haneli sayı ve yıl eki
    match = re.search(pattern, text)
    if match:
        return match.group()
    return None

def update_frame():
    global paused, cap, found_text
    if cap is not None and not paused:
        # Kameradan bir kare yakala
        ret, frame = cap.read()
        
        if ret:
            # Görüntüyü gri tonlamaya çevir
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # Metin tanıma
            custom_config = r'--oem 3 --psm 6'
            text = pytesseract.image_to_string(gray, config=custom_config)

            # Tüm tanınan metni yazdır
            print(f"Bulunan metin: {text.strip()}")

            # Rapor numarasını ara
            report_number = find_report_number(text)

            # Görüntüyü tkinter ile göster
            img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            draw = ImageDraw.Draw(img)
            # Font ayarlama (Windows için)
            font = ImageFont.truetype("arial.ttf", 36)

            if report_number:
                print("Bulunan rapor numarası:", report_number)
                pyperclip.copy(report_number)  # Metni panoya kopyala
                found_text = report_number
                print("Rapor numarası panoya kopyalandı.")
                
                # mp3 dosyasını çal
                pygame.mixer.music.load(r'C:\pyton\childok.mp3')  # MP3 dosyasını yükle
                pygame.mixer.music.play()  # Ses dosyasını oynat
                
                color = (0, 255, 0)  # Yeşil
                draw.text((10, 10), report_number, font=font, fill=color)
                paused = True

            imgtk = ImageTk.PhotoImage(image=img)
            video_label.imgtk = imgtk
            video_label.configure(image=imgtk)

    # Her 10 ms'de bir update_frame fonksiyonunu çalıştır
    root.after(10, update_frame)

def toggle_pause():
    global paused, found_text
    paused = not paused
    if paused:
        pause_button.config(text="Devam")
    else:
        pause_button.config(text="Durdur")
        found_text = ""  # Devam ederken önceki metni temizle

def quit_program():
    global cap
    if cap is not None:
        cap.release()
    root.destroy()

def select_camera():
    global cap
    if cap is not None:
        cap.release()
    cap_index = selected_camera.get()
    cap = cv2.VideoCapture(cap_index)
    print(f"Kamera {cap_index} seçildi.")

    # Kamera kontrolü, doğru çalışıp çalışmadığını kontrol et
    if not cap.isOpened():
        print(f"Kamera {cap_index} açılmadı.")
    else:
        print(f"Kamera {cap_index} başarılı şekilde açıldı.")

# Tkinter GUI
root = Tk()
root.title("Kamera İzleme ve OCR")

# Kamera seçimi
selected_camera = IntVar(value=1)  # Varsayılan olarak 1 numaralı kamera seçili
camera_label = ttk.Label(root, text="Kamera Seçimi:")
camera_label.pack()

camera_options = ttk.Combobox(root, textvariable=selected_camera)
camera_options['values'] = [0, 1, 2]  # Kamera indeksleri (daha fazla kamera varsa artırabilirsiniz)
camera_options.pack()

select_button = ttk.Button(root, text="Kamerayı Seç", command=select_camera)
select_button.pack()

# Video görüntüsü için label
video_label = ttk.Label(root)
video_label.pack()

# Durdur/Devam butonu
pause_button = ttk.Button(root, text="Devam", command=toggle_pause)
pause_button.pack()

# Çıkış butonu
exit_button = ttk.Button(root, text="Çıkış", command=quit_program)
exit_button.pack()

# Başlangıçta kamera seçimi yap
select_camera()

# Ana döngüyü başlat
update_frame()
root.mainloop()
