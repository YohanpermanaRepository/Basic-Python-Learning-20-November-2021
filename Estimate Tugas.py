tugasmatkul = set()
tugaspraktikum = set()
tugasselesai = set()

for abc in range(4):
    if abc == 0:
        print("=" * 8, "MINGGU Ke-", abc + 1, "=" * 8)
        n = str(input("Adakah Tugas Matkul di Minggu ini? (y/t)"))
        if n == "y":
            a = int(input("Ada Berapa Tugas Matkul di Minggu ini?"))
            if a > 0 :
                for x in range(a):
                    matkul = input("Masukkan Tugas Mata Kuliahnya :")
                    tugasmatkul.add(matkul)
                print("="*8,"Tugas Matkul Ana Adalah","="*8)
                for tampiltugasmatkul in tugasmatkul:
                    print("=> ",tampiltugasmatkul)
            elif a <= 0 :
                pass
            b = int(input("Ada Berapa Tugas Praktikum di Minggu ini?"))
            if b > 0 :
                for x in range(b):
                    prak = input("Masukkan Tugas Praktikumnya :")
                    tugaspraktikum.add(prak)
                print("=" * 8, "Tugas Praktikum Ana Adalah", "=" * 8)
                for tampiltugasprak in tugaspraktikum:
                    print("=> ", tampiltugasprak)
                print("="*8,"Tugas Keseluruhan nya","="*8)

                tugasall = tugasmatkul.union(tugaspraktikum)
                for tampiltugasall in tugasall :
                    print("=> ", tampiltugasall)
            elif b <= 0 :
                tugasall = tugasmatkul.union(tugaspraktikum)
                for tampiltugasall in tugasall:
                    print("=> ", tampiltugasall)
                pass
        elif n == "t":
            pass
    elif abc >= 0:
        print("=" * 8, "MINGGU Ke-",abc+1, "=" * 8)
        c = str(input("Adakah Tugas yang Sudah Dikerjakan ? (ada/tidak)"))
        if c == "ada":
            d = int(input("Ada berapa tugas yang sudah diselesaikan?"))
            for z in range(d):
                selesai = input("Menyelesaikan Tugas apa ?")
                tugasselesai.add(selesai)
                tugasall = (tugasmatkul.union(tugaspraktikum) - tugasselesai)
            print("=" * 4, "LIST TUGAS YANG BELUM DIKERJAKAN", "=" * 4)
            for tampiltugasall in tugasall:
                print("=> ", tampiltugasall)
        elif c == "tidak":
            print("=" * 4, "LIST TUGAS YANG BELUM DIKERJAKAN", "=" * 4)
            tugasall = (tugasmatkul.union(tugaspraktikum) - tugasselesai)
            for tampiltugasall in tugasall:
                print("=> ", tampiltugasall)
        else:
            print("Salah Inputan!!")

        q = str(input("Adakah Tambahan tugas? (ada/tidak)"))
        if q == "ada":
            a = int(input("Ada Berapa Tambahan Tugas Matkul di Minggu Ini?"))
            if a > 0:
                for x in range(a):
                    matkul = input("Masukkan Tugas Mata Kuliahnya :")
                    tugasmatkul.add(matkul)
                    tugasmatkul = tugasmatkul - tugasselesai
                print("=" * 8, "Tugas Matkul Ana Adalah", "=" * 8)
                for tampiltugasmatkul in tugasmatkul:
                    print("=> ", tampiltugasmatkul)
            elif a <= 0:
                pass
            b = int(input("Ada Berapa Tambahan Tugas Praktikum di Minggu Ini?"))
            if b > 0:
                for x in range(b):
                    prak = input("Masukkan Tugas Praktikumnya :")
                    tugaspraktikum.add(prak)
                    tugaspraktikum = tugaspraktikum - tugasselesai
                print("=" * 8, "Tugas Praktikum Ana Adalah", "=" * 8)
                for tampiltugasprak in tugaspraktikum:
                    print("=> ", tampiltugasprak)
                print("=" * 8, "Tugas Keseluruhan nya", "=" * 8)

                tugasall = (tugasmatkul.union(tugaspraktikum) - tugasselesai)
                for tampiltugasall in tugasall:
                    print("=> ", tampiltugasall)
            elif b <= 0:
                print("=" * 4, "LIST TUGAS YANG BELUM DIKERJAKAN", "=" * 4)
                tugasall = (tugasmatkul.union(tugaspraktikum) - tugasselesai)
                for tampiltugasall in tugasall:
                    print("=> ", tampiltugasall)
                pass
        elif n == "t":
            pass
print("="*5,"TERIMAKASIH TELAH MENCOBA PROGRAM SAYA","="*5)