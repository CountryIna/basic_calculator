print("\033[0;30;45m == BASIC CALCULATOR == \033[0m")

# Membuat Fungsi untuk Cek Koma
def input_angka(pesan):
    while True:
        nilai = input(pesan)

        #Cek Jika Pakai Koma
        if "," in nilai:
            print("⚠️ Gunakan Titik (.) buka Koma (,)")
            continue
        try:
            return float(nilai)
        except ValueError:
            print("\033[2;34;40m Input Harus Angka! \033[0m")

# List Operator
operator = None
while operator != 0:
    print("\n Pilih Operator ")
    print("1. ➕ Tambah")
    print("2. ➖ Kurang")
    print("3. ✖ Kali")
    print("4. ➗ Bagi")
    print("0. Keluar")

    # Memilih Operator
    try:
        operator = int(input("Input Menu (1/2/3/4/0) : "))
    except ValueError:
        print("\033[2;34;40m Input Harus Angka! \033[0m")
        continue

    if operator == 0:
        print("\n 🤝 Terimakasih")
        break
    elif operator not in [1, 2, 3, 4]:
        print("\033[2;34;40m Menu tidak ada. Silakan coba lagi \033[0m")
        continue

    # Input
    A1 = input_angka("Masukkan Angka Pertama : ")
    A2 = input_angka("Masukkan Angka Kedua : ")

    #Logika Perhitungan
    if operator == 1:
        hasil = A1 + A2
        operator = "+"
    elif operator == 2:
        hasil = A1 - A2
        operator = "-"
    elif operator == 3:
        hasil = A1 * A2
        operator = "x"
    elif operator == 4:
        if A2 != 0:
            hasil = A1 / A2
            operator = "/"
        else:
            hasil = "Tak Terhingga"
            operator = "/"

    #Hasil
    print("\n", "="*8, "HASIL", "="*8)
    print(f"{A1} {operator} {A2} = {hasil}")
