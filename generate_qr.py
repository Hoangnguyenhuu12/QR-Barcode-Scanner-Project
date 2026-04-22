import csv
import qrcode
import os

def generate_qr_from_csv(csv_filename="products.csv", output_dir="generated_qrcodes"):
    """Đọc file CSV và tạo mã QR cho từng ID sản phẩm."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    try:
        with open(csv_filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                product_id = row['id']
                # Khởi tạo và lưu mã QR
                qr_img = qrcode.make(product_id)
                output_path = os.path.join(output_dir, f"{product_id}.png")
                qr_img.save(output_path)
                
        print(f"[XONG] Đã tạo mã QR thành công trong thư mục: '{output_dir}'")
    except FileNotFoundError:
        print(f"[LỖI] Không tìm thấy file {csv_filename}. Hãy chạy file generate_data.py trước.")

if __name__ == "__main__":
    generate_qr_from_csv()