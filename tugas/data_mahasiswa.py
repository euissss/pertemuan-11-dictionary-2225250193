def cari_mahasiswa(data, nim):
    return data.get(nim)


def tambah_mahasiswa(data, nim, nama, nilai):
    if nim not in data:
        data[nim] = {
            "nama": nama,
            "nilai": nilai
        }
        return True
    return False


def ubah_nilai(data, nim, nilai_baru):
    if nim in data:
        data[nim]["nilai"] = nilai_baru
        return True
    return False


def rata_rata(data):
    if not data:
        return 0

    total = 0

    for mahasiswa in data.values():
        total += mahasiswa["nilai"]

    return total / len(data)


mahasiswa = {
    "A001": {"nama": "Ayu", "nilai": 85},
    "A002": {"nama": "Budi", "nilai": 78},
    "A003": {"nama": "Citra", "nilai": 92},
    "A004": {"nama": "Deni", "nilai": 75},
    "A005": {"nama": "Eka", "nilai": 88}
}

# Mencari mahasiswa
print("Pencarian:")
print(cari_mahasiswa(mahasiswa, "A002"))
print(cari_mahasiswa(mahasiswa, "A010"))

# Menambah mahasiswa
tambah_mahasiswa(mahasiswa, "A006", "Fani", 80)

# Mengubah nilai
ubah_nilai(mahasiswa, "A002", 90)

# Menampilkan seluruh data
print("\nData Mahasiswa:")

for nim, data in mahasiswa.items():
    print(nim, data)

# Menghitung rata-rata
print("\nRata-rata nilai:", rata_rata(mahasiswa))