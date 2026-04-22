import cv2
import csv
import numpy as np
from pyzbar.pyzbar import decode, ZBarSymbol
from PIL import Image, ImageDraw, ImageFont

def load_database(filename="products.csv"):
    """Tải dữ liệu từ file CSV vào Dictionary."""
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            return {row['id']: {"name": row['name'], "price": row['price']} for row in csv.DictReader(file)}
    except FileNotFoundError:
        print(f"[CẢNH BÁO] Không tìm thấy {filename}. Hệ thống sẽ quét mà không có CSDL cục bộ.")
        return {}

def main():
    product_db = load_database()
    scanned_codes = set()
    
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    print("="*60)
    print("HỆ THỐNG QUÉT MÃ ĐÃ KHỞI ĐỘNG | Bấm phím 'q' để thoát")
    print("="*60)

    font = ImageFont.load_default()

    while True:
        ret, frame = cap.read()
        if not ret: break

        # Tiền xử lý hình ảnh
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        thresh_frame = cv2.adaptiveThreshold(gray_frame, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

        # Giải mã kết hợp ảnh xám và ảnh đã xử lý threshold
        detected_codes = decode(thresh_frame, symbols=[ZBarSymbol.QRCODE, ZBarSymbol.CODE128, ZBarSymbol.EAN13])
        if not detected_codes: 
            detected_codes = decode(gray_frame, symbols=[ZBarSymbol.QRCODE, ZBarSymbol.CODE128, ZBarSymbol.EAN13])

        # Chuyển đổi sang PIL để chèn chữ không bị lỗi font
        cv2_im_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        pil_im = Image.fromarray(cv2_im_rgb)
        draw = ImageDraw.Draw(pil_im)

        for code in detected_codes:
            # Vẽ viền bao quanh mã
            pts = np.array([code.polygon], np.int32).reshape((-1, 1, 2))
            cv2.polylines(frame, [pts], True, (0, 255, 0), 3)

            code_data = code.data.decode("utf-8")
            display_text = ""

            # Kiểm tra dữ liệu giải mã
            is_new_scan = code_data not in scanned_codes
            
            if code_data in product_db:
                prod = product_db[code_data]
                display_text = f"SP: {prod['name']} - {prod['price']}VND"
                if is_new_scan:
                    print(f"\n[SẢN PHẨM] {prod['name']} | Giá: {prod['price']} VNĐ | Mã: {code_data}")
            
            elif code_data.startswith(("http://", "https://")):
                display_text = f"Web: {code_data[:15]}..." 
                if is_new_scan:
                    print(f"\n[LIÊN KẾT WEB] Link: {code_data} (Ctrl+Click để mở)") 
            
            else: 
                display_text = f"Moi: {code_data}"
                if is_new_scan:
                    print(f"\n[MÃ CHƯA BIẾT] {code_data} (Chưa có trong CSDL)")

            scanned_codes.add(code_data)

            # Đẩy text lên ảnh PIL
            x, y = code.polygon[0].x, code.polygon[0].y
            draw.text((x, y - 20), display_text, font=font, fill=(0, 255, 255))

        # Hiển thị
        if detected_codes:
            frame = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR)
            
        cv2.imshow("Intelligent Scanner", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()