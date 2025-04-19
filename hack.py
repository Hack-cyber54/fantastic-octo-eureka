print("\033[1;31mHack akun Free Fire BY FARHAAN ALI\n")
print("\033[1;36m⚠Warning⚠")
print("Ini hanya sekadar hiburan\n")

def hack():
        print("\033[1;32m")
        User = input("Masukan nama user: ")
        Password = input("Masukan Password: ")
        Nickname = input("Masukan Nickname; ")
        Id = int(input("Masukan Id: "))
        Hack = User, Password, Nickname, Id
        print(Hack)

def succes():
    print("\033[1;33m")
    print(100*"Hack akun berhasil\n")
    print("Selamat anda berhasil hack akun masuk ke menu no 3 untuk lebih lanjut")

def emailpass():
    print("\033[0;32mLogin akun Google: ")
    print("Gmail: hack@gmail.com")
    print("Password: nandaganteng\n")
    print("Login akun Facebook: ")
    print("No/Username: Tidak ada")
    print("Password: Tidak ada\n")

while True :
      Hacker = int(input("\033[1;35mSilakan pilih opsi yang ada di bawah: \n\n\033[1;31m[1] Tekan angka 1 untuk memasukkan informasi akun target\n\033[1;32m[2]Tekan angka 2 untuk mulai hack akun\n\033[1;34m[3] Tekan angka 3 untuk melihat sandi dan password target\n\n\033[0;36m[0] Tekan tombol 0 untuk keluar\n\n\033[1;32m Silakan mulai hack: "))

      if(Hacker ==1):
        hack()
      elif(Hacker ==2):
          succes()
      elif(Hacker ==3):
          emailpass()
      else:
          break
