from tabulate import tabulate
Track = [
["Fitur","Implementasi","NIM Desainer","NIM Coder","NIM Tester"],
["F01","function register()","16520225","16520225",""],
["F02","procedure user(), procedure login()","16520145","16520145",""],
["F03","procedure gadget(), function data_gadget(urutan), function carirarity()","16520145","16520145",""],
["F04","function caritahun()","16520145","16520145",""],
["F05","function tambahitem()","16520465,16520145","16520465,16520145",""],
["F06","procedure consumable(), function hapus(urutan,trim_array,namafile), function hapusitem()","16520145","16520145",""],
["F07","function ubahjumlah()","16520465","16520465",""],
["F08","function pinjam_gadget()","16520465","16520465",""],
["F09","procedure tulis_gadget(urutan,namafile,trim_array,angka_awal,jumlah_kembali), function kembalikan_gadget","16520145","16520145",""],
["F10","function minta_consumable()","16520465","16520465",""],
["F11","procedure pinjam_gadget(), procedure riwayat_pinjam(trim_array), function data_peminjaman_gadget(urutan), function riwayat_pinjam_gadget()","16520145","16520145",""],
["F12","function riwayat_kembalikan_gadget()","16520465","16520465",""],
["F13","function riwayat_ambil()","16520465","16520465",""],
["F14","function load_data()","","16520165",""],
["F15","function save()","16520465","16520465",""],
["F16","function help()","16520225","16520225",""],
["F17","function exit()","16520225","16520225",""],
["B01","function hashing()","16520225","16520225",""],
["B02","function kembalikan_parsial_gadget()","16520145","16520145",""],
["B03","function gacha()","16520225","16520225",""]
]
print(tabulate(Track))