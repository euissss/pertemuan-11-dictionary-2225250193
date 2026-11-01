data = {
    "nama": "Ayu",
    "nilai": 85,
    "kelas": "A"
}

print("Menampilkan key:")
for key in data:
    print(key)

print("Menampilkan value:")
for value in data.values():
    print(value)

print("Menampilkan key dan value:")
for key, value in data.items():
    print(f"{key}: {value}")