def main():
    pilihan = menu_utama()
    if pilihan == "1":
        I0, waktu, material, ketebalan = pengaturan_simulasi()
        print("\nPengaturan berhasil disimpan!")
        print(f"I0={I0}, waktu={waktu}, material={material}, ketebalan={ketebalan}")
    elif pilihan == "2":
        I0 = float(input("Masukkan intensitas awal (mSv): "))
        jarak = float(input("Masukkan jarak (m): "))
        waktu = int(input("Masukkan waktu simulasi (detik): "))
        print("Pilihan material:", ", ".join(MATERIALS.keys()))
        material = input("Pilih material shielding: ").lower()
        ketebalan = float(input("Masukkan ketebalan pelindung (cm): "))
        simulasi_eksterna(I0, jarak, waktu, material, ketebalan)
    else:
        print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
