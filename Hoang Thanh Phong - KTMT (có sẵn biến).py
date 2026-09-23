# BÀI THỰC HÀNH TỔNG HỢP

students = [
    {"ho_ten": "Hoang Thanh Phong", "mssv": "SV001", "diem": [8, 7, 9]},
    {"ho_ten": "Ngo Ta Phuoc Lam", "mssv": "SV002", "diem": [4, 5, 4]},
    {"ho_ten": "Nguyen Khoi Nguyen", "mssv": "SV003", "diem": [9, 8, 10]},
    {"ho_ten": "Huynh Dinh Danh", "mssv": "SV004", "diem": [6, 7, 5]},
    {"ho_ten": "Duong Gia Cat Luong", "mssv": "SV005", "diem": [11, 8, 7]},  # Không hợp lệ
    {"ho_ten": "Tran The Luat", "mssv": "SV006", "diem": [3, 4, 5]}
]


# 1. Lọc sinh viên có điểm hợp lệ trong khoảng [0, 10]

students_valid = []

for sv in students:
    if all(0 <= diem <= 10 for diem in sv["diem"]):
        students_valid.append(sv)

print("DANH SÁCH SINH VIÊN HỢP LỆ")
for i, sv in enumerate(students_valid, 1):
    print(f"{i}. {sv['ho_ten']}");


# 2. Tính ĐTB cho sinh viên hợp lệ

for sv in students_valid:
    sv["dtb"] = sum(sv["diem"]) / len(sv["diem"])


# 3. Phân loại sinh viên

def phan_loai(dtb):
    if dtb >= 8:
        return "Giỏi"
    elif dtb >= 6.5:
        return "Khá"
    elif dtb >= 5:
        return "Trung bình"
    else:
        return "Yếu"


for sv in students_valid:
    sv["xep_loai"] = phan_loai(sv["dtb"])


# 4. Thống kê số lượng sinh viên theo nhóm

thong_ke = {
    "Giỏi": 0,
    "Khá": 0,
    "Trung bình": 0,
    "Yếu": 0
}

for sv in students_valid:
    thong_ke[sv["xep_loai"]] += 1

print("\nTHỐNG KÊ XẾP LOẠI")
for loai, so_luong in thong_ke.items():
    print(f"{loai}: {so_luong} sinh viên")


# 5. In danh sách sinh viên yếu (ĐTB < 5)
#    kèm số điểm cần bù để đạt 5

print("\nDANH SÁCH SINH VIÊN YẾU")

for sv in students_valid:
    if sv["dtb"] < 5:
        diem_can_bu = 5 - sv["dtb"]

        print(
            f"MSSV: {sv['mssv']} | "
            f"Họ tên: {sv['ho_ten']} | "
            f"ĐTB: {sv['dtb']:.2f} | "
            f"Cần bù: {diem_can_bu:.2f}"
        )


# 6. Truy xuất sinh viên có ĐTB cao nhất

sv_cao_nhat = max(students_valid, key=lambda sv: sv["dtb"])

print("\nSINH VIÊN CÓ ĐTB CAO NHẤT")
print(f"Họ tên : {sv_cao_nhat['ho_ten']}")
print(f"MSSV   : {sv_cao_nhat['mssv']}")
print(f"Điểm   : {sv_cao_nhat['diem']}")
print(f"ĐTB    : {sv_cao_nhat['dtb']:.2f}")
print(f"Xếp loại: {sv_cao_nhat['xep_loai']}")
