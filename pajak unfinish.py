print("Perhitungan Pajak Penghasilan 21")
b1 = input("Masukkan nominal gaji per bulan anda : \n")
gaji_input = int(b1) * 12
PTKP_input = input("Ketik sesuai Kondisi (1/2/3/4/5/6/7/8)\n(1)TK/0\n(2)TK/1\n(3)K/0\n(4)TK/2\n(5)TK/3\n(6)K/1\n(7)K/2\n(8)K/3\n")
if int(PTKP_input) == 1:
    a = 54_000_000
    tk1 = gaji_input - a
    if int(tk1) < 0:
        print("Tidak kena pajak")
    elif int(tk1) <= 60_000_000:
        hasil_tk1 = (tk1 * 5/100)/12
        print(int(hasil_tk1))

    elif int(tk1) <= 250_000_000:
        tk1 = tk1 - 60_000_000
        hasil_tk1 = 250_000 + (tk1 * 15/100)/12
        print(hasil_tk1)

    elif int(tk1) <= 500_000_000:
        tk1 = tk1 - 60_000_000 - 250_000_000
        hasil_tk1 = 250000 + 3125000 + (tk1 * 25 / 100) / 12
        print(round(hasil_tk1))
    else:
        tk1 = tk1 - 60_000_000 - 250_000_000 - 500_000_000
        hasil_tk1 = 250_000 + 3_125_000 +10_416_667 + (tk1 * 30 / 100) / 12
        print(round(hasil_tk1))
        
