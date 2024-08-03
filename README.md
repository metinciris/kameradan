# kameradan
Basılı raporu kameraya göstererek numarasını bulup hafızaya alma. Patoloji için öncelikle.

![Screenshot_2]([https://github.com/username/test/assets/108919293/d8206e8b-5c62-49f9-94e4-19b9d9d5c6e6](https://github.com/metinciris/kameradan/blob/main/okuma.jpeg))
https://github.com/metinciris/kameradan/blob/main/okuma.jpeg

### README.md

```markdown
# Camera-Based OCR for Report Number Detection

This project is a Python application that uses OpenCV and Tesseract OCR to detect and recognize report numbers from camera feeds in real-time. The application is designed to recognize numbers in the format `XXXXX/24`, where `XXXXX` is a 5-digit number between 10000 and 99999, and `/24` indicates the year.

## Features

- Real-time OCR from a camera feed
- Automatic detection of report numbers in a specified format
- User interface for camera selection and pause/resume functionality
- Display of recognized text on the video feed
- Automatic copying of recognized report numbers to clipboard

## Requirements

- Python 3.x
- OpenCV
- Tesseract OCR
- Tkinter (for GUI)
- Pillow (for image processing)
- Pyperclip (for clipboard operations)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/yourrepository.git
   cd yourrepository
   ```

2. **Install required packages:**
   You can install the required packages using pip:
   ```bash
   pip install opencv-python pytesseract pillow pyperclip
   ```

3. **Install Tesseract OCR:**
   - Download and install Tesseract OCR from [here](https://github.com/tesseract-ocr/tesseract).
   - Make sure to update the `pytesseract.pytesseract.tesseract_cmd` in the script to point to your Tesseract installation path.

## Usage

1. **Run the application:**
   ```bash
   python kamera.pyw
   ```

2. **Select the camera:**
   - By default, the application selects camera index 1. You can change the camera by selecting a different index from the dropdown in the GUI.

3. **Detection:**
   - The application will detect report numbers in real-time from the video feed. The detected numbers will be displayed on the video feed and copied to the clipboard.

4. **Pause/Resume:**
   - Use the "Devam" button to pause the detection and "Durdur" to resume.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
```

