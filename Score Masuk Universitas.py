#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

int main() {
    cout << "Program menghitung perkiraan skor tes masuk universitas" << endl;
    cout << "=====================================================" << endl;

    while (true) {
        vector<int> jawaban_benar;

        while (true) {
            int benar;
            cout << "Masukkan perkiraan jawaban benar pada Penalaran Umum (30 Soal): ";
            cin >> benar;

            if (benar <= 30) {
                jawaban_benar.push_back(benar);
                break;
            } else {
                cout << "Jumlah jawaban benar tidak boleh melebihi 30" << endl;
            }
        }

        while (true) {
            int benar;
            cout << "Masukkan perkiraan jawaban benar pada Pengetahuan dan Pemahaman Umum (20 Soal): ";
            cin >> benar;

            if (benar <= 20) {
                jawaban_benar.push_back(benar);
                break;
            } else {
                cout << "Jumlah jawaban benar tidak boleh melebihi 20" << endl;
            }
        }

        while (true) {
            int benar;
            cout << "Masukkan perkiraan jawaban benar pada Pemahaman Bacaan dan Menulis (20 Soal): ";
            cin >> benar;

            if (benar <= 20) {
                jawaban_benar.push_back(benar);
                break;
            } else {
                cout << "Jumlah jawaban benar tidak boleh melebihi 20" << endl;
            }
        }

        while (true) {
            int benar;
            cout << "Masukkan perkiraan jawaban benar pada Pengetahuan Kuantitatif (15 Soal): ";
            cin >> benar;

            if (benar <= 15) {
                jawaban_benar.push_back(benar);
                break;
            } else {
                cout << "Jumlah jawaban benar tidak boleh melebihi 15" << endl;
            }
        }

        while (true) {
            int benar;
            cout << "Masukkan perkiraan jawaban benar pada Literasi Bahasa Indonesia (30 Soal): ";
            cin >> benar;

            if (benar <= 30) {
                jawaban_benar.push_back(benar);
                break;
            } else {
                cout << "Jumlah jawaban benar tidak boleh melebihi 30" << endl;
            }
        }

        while (true) {
            int benar;
            cout << "Masukkan perkiraan jawaban benar pada Literasi Bahasa Inggris (20 Soal): ";
            cin >> benar;

            if (benar <= 20) {
                jawaban_benar.push_back(benar);
                break;
            } else {
                cout << "Jumlah jawaban benar tidak boleh melebihi 20" << endl;
            }
        }

            while (true) {
        int benar;
        cout << "Masukkan perkiraan jawaban benar pada Penalaran Matematika (20 Soal): ";
        cin >> benar;

        if (benar <= 20) {
            jawaban_benar.push_back(benar);
            break;
        } else {
            cout << "Jumlah jawaban benar tidak boleh melebihi 20" << endl;
        }
    }
    
    float nilai_total = (float) accumulate(jawaban_benar.begin(), jawaban_benar.end(), 0) / 155 * 1000;

    cout << "Perkiraan nilai Anda adalah: " << nilai_total << endl;

    cout << "Apakah Anda ingin mengulangi program ini? (Y/N): ";
    string ulang;
    cin >> ulang;

    if (ulang == "N" || ulang == "n") {
        break;
    }
}

return 0;
}
