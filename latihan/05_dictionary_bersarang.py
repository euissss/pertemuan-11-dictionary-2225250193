mahasiswa = {
    "A001": {"nama": "Ayu", "nilai": 85},
    "A002": {"nama": "Budi", "nilai": 78},
    "A003": {"nama": "Citra", "nilai": 92}
}

print(mahasiswa["A002"]["nama"])
print(mahasiswa["A003"]["nilai"])

rekap = {
    "Ayu": [80, 85, 90],
    "Budi": [70, 75, 78]
}

print(rekap["Ayu"])
print(sum(rekap["Ayu"]) / len(rekap["Ayu"]))