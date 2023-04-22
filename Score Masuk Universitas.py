print("Program menghitung perkiraan skor tes masuk universitas")

print("=====================================================")

while True:

    jawaban_benar = []

    while True:

        benar = int(input("Masukkan perkiraan jawaban benar pada Penalaran Umum (30 Soal): "))

        if benar <= 30:

            jawaban_benar.append(benar)

            break

        else:

            print("Jumlah jawaban benar tidak boleh melebihi 30")

    while True:

        benar = int(input("Masukkan perkiraan jawaban benar pada Pengetahuan dan Pemahaman Umum (20 Soal): "))

        if benar <= 20:

            jawaban_benar.append(benar)

            break

        else:

            print("Jumlah jawaban benar tidak boleh melebihi 20")

    while True:

        benar = int(input("Masukkan perkiraan jawaban benar pada Pemahaman Bacaan dan Menulis (20 Soal): "))

        if benar <= 20:

            jawaban_benar.append(benar)

            break

        else:

            print("Jumlah jawaban benar tidak boleh melebihi 20")

    while True:

        benar = int(input("Masukkan perkiraan jawaban benar pada Pengetahuan Kuantitatif (15 Soal): "))

        if benar <= 15:

            jawaban_benar.append(benar)

            break

        else:

            print("Jumlah jawaban benar tidak boleh melebihi 15")

    while True:

        benar = int(input("Masukkan perkiraan jawaban benar pada Literasi Bahasa Indonesia (30 Soal): "))

        if benar <= 30:

            jawaban_benar.append(benar)

            break

        else:

            print("Jumlah jawaban benar tidak boleh melebihi 30")

    while True:

        benar = int(input("Masukkan perkiraan jawaban benar pada Literasi Bahasa Inggris (20 Soal): "))

        if benar <= 20:

            jawaban_benar.append(benar)

            break

        else:

            print("Jumlah jawaban benar tidak boleh melebihi 20")

    while True:

        benar = int(input("Masukkan perkiraan jawaban benar pada Penalaran Matematika (20 Soal): "))

        if benar <= 20:

            jawaban_benar.append(benar)

            break

        else:

            print("Jumlah jawaban benar tidak boleh melebihi 20")

    nilai_total = sum(jawaban_benar) / sum([30, 20, 20, 15, 30, 20, 20]) * 1000

    print(f"Perkiraan nilai Anda adalah: {nilai_total}")

    ulang = input("Apakah Anda ingin mengulangi program ini? (Y/N): ")

    if ulang == 'N' or ulang == 'n':

        break

