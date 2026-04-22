# Intelligent Real-Time Barcode & QR Code Scanner

A real-time barcode and QR code scanning application using Python, OpenCV, and pyzbar. Built for the CPV301 course at HCM FPT University.

## Features
- Live webcam scanning for QR codes, CODE128, and EAN13 barcodes
- Adaptive Gaussian Thresholding for robust detection under poor lighting
- Product lookup against a local CSV database
- Duplicate scan prevention via runtime scan history

## Project Structure
```
├── QR_Barcode_Project.py              # Main real-time scanner application
├── generate_data.py                   # Generate mock product database (products.csv)
├── generate_qr.py                     # Generate QR code images from the database
├── requirements.txt
├── QR_Barcode_Report.pdf              # Detailed technical report
├── QR-Barcode_Presentation.pdf        # Project presentation slides
└── README.md
```

## Setup & Usage

### 1. Install dependencies
pip install -r requirements.txt

### 2. Generate the mock database
python generate_data.py

### 3. (Optional) Generate QR code images
python generate_qr.py

### 4. Run the scanner
python QR_Barcode_Project.py

## Controls
| Key | Action |
|-----|--------|
| `q` | Quit the application |

## Authors
Group 8 — AI1904, HCM FPT University
- Nguyen Huu Hoang (leader)
- Hoang Phuc Binh
- Tran Khoi Nguyen
- Mai Tran Hao
