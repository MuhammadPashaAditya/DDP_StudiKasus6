Nama : Muhammad Pasha Aditya
NIM : 2609116085
Kelas : C
Soal : Ganjil

# Sistem Pencatatan Nilai Mahasiswa

## Deskripsi
Program ini dibuat untuk mencatat dan melihat data nilai mahasiswa menggunakan **Python** dan **JSON**.
Data disimpan di file `catatnilai.json`, sehingga data yang sudah ditambahkan tetap ada walaupun program dijalankan kembali.

## Fitur
Program memiliki 3 menu utama:

1. **Tampilkan Data Nilai**
   Menampilkan seluruh data mahasiswa yang ada di file JSON.

2. **Tambah Data Nilai**
   Menambahkan data mahasiswa baru berupa NIM, nama, mata kuliah, dan nilai.

3. **Keluar**
   Menghentikan program.

## Ini beberapa dokumentasi Output Program
<img width="1366" height="768" alt="Screenshot (76)" src="https://github.com/user-attachments/assets/730a0a3b-8e6f-4c33-868a-98e5e107c3dc" />
<img width="1366" height="768" alt="Screenshot (76)" src="https://github.com/user-attachments/assets/871725df-30f7-4578-b67a-68cc9fa68f46" />
<img width="1366" height="768" alt="Screenshot (78)" src="https://github.com/user-attachments/assets/29d03505-75f3-44cb-8adb-a9624b4c6071" /> Disini terlihat bahwa nilai di JSON juga ikut terupdate



## Penjelasan Singkat Kode

### Import JSON

```python
import json
```

Digunakan agar Python dapat membaca dan menyimpan data dalam format JSON.

### Membaca Data

```python
data = json.load(file)
```

Digunakan untuk mengambil data yang sudah tersimpan di dalam file JSON.

### Menambahkan Data

```python
data.append(data_baru)
```

Digunakan untuk menambahkan data mahasiswa baru tanpa menghapus data sebelumnya.

### Menyimpan Data

```python
json.dump(data, file, indent=4)
```

Digunakan untuk menyimpan data yang sudah ditambahkan ke file JSON.

### While Loop

```python
while True:
```

Digunakan agar menu program terus berjalan sampai user memilih menu **Keluar**.

## Data JSON

File `catatnilai.json` berisi data nilai mahasiswa seperti berikut:

```json
[
    {
        "nim": "2609116002",
        "nama": "Azzam",
        "mata_kuliah": "filsafat cina",
        "nilai": 85
    },
    {
        "nim": "2609116001",
        "nama": "Pasha",
        "mata_kuliah": "Filsafat barat",
        "nilai": 90
    },
    {
        "nim": "2609116003",
        "nama": "Asep",
        "mata_kuliah": "Filsafat Prabowo",
        "nilai": 95.0
    }
]
```

Data tersebut merupakan data yang tersimpan di file JSON yang digunakan oleh program.

## Hasil Pengujian

Program diuji dengan cara:

* Menampilkan data yang sudah ada.
* Menambahkan data mahasiswa baru.
* Menyimpan data ke file JSON.
* Menjalankan program kembali.
* Mengecek apakah data baru masih tersimpan.

Hasilnya, data yang sudah ditambahkan tetap tersimpan setelah program dijalankan kembali.


Program ini menggunakan konsep dasar Python seperti **list, dictionary, fungsi, `if-else`, `while loop`, `append()`, dan JSON** untuk membuat sistem pencatatan nilai mahasiswa sederhana.
