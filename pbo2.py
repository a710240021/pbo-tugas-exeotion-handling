def convert_to_int(string):
    result = int(string)
    return result
try:
    umur =  input('Masukkan umur kamu : ')
    umur5tahunlagi = convert_to_int(umur) + 5
    print(f"Umur kamu 5 tahun lagi adalah ", umur5tahunlagi)
except ValueError:
    print("tipe data yang anda masukkan salah")