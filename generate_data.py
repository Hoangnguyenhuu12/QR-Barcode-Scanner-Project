import csv
import os

def create_mock_database(filename="products.csv"):
    """Tạo file cơ sở dữ liệu CSV chứa thông tin sản phẩm mẫu."""
    data = [
        ["8936214083022", "Bich giay an", "5000"],
        ["8935005801135", "Nuoc khoang Lavie 500ml", "10000"],
        ["8934564010323", "Mi tom Hao Hao chua cay", "4500"],
        ["8935049500544", "Coca Cola lon 320ml", "10000"],
        ["8934567890123", "Banh mi que chua cay", "15000"],
        ["8934567890124", "Sua tuoi Vinamilk 180ml", "8000"],
        ["8934567890125", "Snack Oishi vi tom", "6000"],
        ["8934567890126", "Keo cao su Sing-gum", "5000"],
        ["8934567890127", "Ca phe lon Birdy", "12000"]
    ]
    
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["id", "name", "price"])
        writer.writerows(data)
        
    print(f"[XONG] Đã tạo cơ sở dữ liệu mẫu tại: {filename}")

if __name__ == "__main__":
    create_mock_database()