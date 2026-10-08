import json

nama_file = r"C:\ApasProjek\catatnilai.json"

#membaca data dari file JSON
def baca_data():
    try:
        with open(nama_file, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    return data

#tampilkan seluruh data nilai
def tampilkan_data():
    data = baca_data()

    if len(data) == 0:
        print("\nBelum ada data nilai.")
    else:
        print("\n=== DATA NILAI MAHASISWA ===")

        for i, mahasiswa in enumerate(data, start=1):
            print(f"\nData ke-{i}")
            print(f"NIM       : {mahasiswa['nim']}")
            print(f"Nama      : {mahasiswa['nama']}")
            print(f"Mata Kuliah : {mahasiswa['mata_kuliah']}")
            print(f"Nilai     : {mahasiswa['nilai']}")

#tambah data baru
def tambah_data():
    data = baca_data()

    print("\n=== TAMBAH DATA NILAI ===")

    nim = input("Masukkan NIM: ")
    nama = input("Masukkan nama mahasiswa: ")
    mata_kuliah = input("Masukkan mata kuliah: ")
    nilai = float(input("Masukkan nilai: "))

    data_baru = {
        "nim": nim,
        "nama": nama,
        "mata_kuliah": mata_kuliah,
        "nilai": nilai
    }

    data.append(data_baru)

    with open(nama_file, "w") as file:
        json.dump(data, file, indent=4)

    print("\nData nilai berhasil ditambahkan dan disimpan. ")

while True:
        print("\n==================================")
        print(" SISTEM PENCATATAN NILAI MAHASISWA ")
        print("====================================")
        print("1. Tampilkan Data Nilai ")
        print("2. Tambah Data Nilai ")
        print("3. Keluar ")

        pilihan = input("pilih menu: ")

        if pilihan == "1":
            tampilkan_data()

        elif pilihan == "2":
            tambah_data()

        elif pilihan == "3":
            print("Terima kasih telah menggunakan program ini. ")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih menu yang tersedia. ")        