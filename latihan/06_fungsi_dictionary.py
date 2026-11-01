def cari_mahasiswa(data, nim):
    return data.get(nim)

def ubah_nilai(data, nim, nilai_baru):
    if nim in data:
        data[nim]["nilai"] = nilai_baru
        return True
    return False

mahasiswa = {
    "A001": {"nama": "Ayu", "nilai": 85},
    "A002": {"nama": "Budi", "nilai": 78}
}

hasil = cari_mahasiswa(mahasiswa, "A002")
print(hasil)

ubah_nilai(mahasiswa, "A002", 90)
print(mahasiswa)