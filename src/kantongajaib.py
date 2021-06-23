import datetime 
#-------------------------F01---------------------------------------#

def register():
  regis=open("user.csv","a")
  count=len(open("user.csv").readlines())
  nama=str(input("Masukan nama: ")).capitalize()
  username=str(input("Masukan username: "))
  #username perlu divalidkan unik belum ada di user.csv
  mem=[[1 for i in range(6)]for j in range(count)]
  baca=open("user.csv").readlines()
  sama=False
  for i in range(count):
    arr=[]
    temp=""
    for huruf in baca[i]:
      if huruf==";":
        arr.append(temp)
        temp=""
      else:
        temp+=huruf
    if temp:
      arr.append(temp)
    mem[i]=arr
  for i in range (count):
      if mem[i][1]==username:
        sama=True
  while sama:
    print("Username sudah digunakan, silahkan ubah username anda.")
    username=str(input("Masukan username: "))
    itung=0
    for i in range (count):
      if mem[i][1]==username:
        itung+=1
    if itung==0:
      sama=False
  password=str(input("Masukan password: "))
  password = hashing(password)
  alamat=str(input("Masukan alamat: "))
  data=[str(count),username,nama,alamat,password,"User"]
  regis.writelines(";".join(data))
  regis.writelines("\n")
  print("user "+str(username)+" telah berhasil register ke dalam Kantong Ajaib.")

#-------------------------F02---------------------------------------#
def user():
  user=open("user.csv","r")
  user_array=user.readlines()
  user.close()
  trim_user_array = [["" for l in range(6)]for k in range(len(user_array))]
  l = 0
  k = 0
  for i in range(len(user_array)):
    for j in range(len(user_array[i])):
      if user_array[i][j] != ';':
        trim_user_array[k][l] += user_array[i][j]
      elif user_array[i][j] == ';':
        l += 1
    k += 1
    l = 0
  return trim_user_array
    
def login():
  print(">>> login")
    
  username = str(input("Masukan username: "))
  password = str(input("Masukan password: "))
  password = hashing(password)

  Login = False
  for k in range(1,len(user())):
    if username == user()[k][1] and password == user()[k][4]:
      Login = True
      idrole = [user()[k][0],user()[k][5]]
      
  if(Login):
    print("Halo "+username+"! Selamat datang di Kantong Ajaib.")
    return idrole
  else:
    print("Maaf, username atau password salah")
    idrole = ["0",""]
    return idrole


#-------------------------F03---------------------------------------#
def gadget():
  gadget = open("gadget.csv","r")
  gadget_array=gadget.readlines()
  gadget.close()
  trim_gadget_array = [["" for l in range(6)]for k in range(len(gadget_array))]
  l = 0
  k = 0
  for i in range(len(gadget_array)):
    for j in range(len(gadget_array[i])):
      if gadget_array[i][j] != ';':
        trim_gadget_array[k][l] += gadget_array[i][j]
      elif gadget_array[i][j] == ';':
        l += 1
    k += 1
    l = 0
  return trim_gadget_array

def data_gadget(urutan):
  print("Nama            :" ,gadget()[urutan][1])
  print("Deskripsi       :" ,gadget()[urutan][2])
  print("Jumlah          :" ,gadget()[urutan][3])
  print("Rarity          :" ,gadget()[urutan][4])
  print("Tahun ditemukan :" ,gadget()[urutan][5])

def carirarity():
  rarity = str(input("Masukkan rarity: "))
  cari = False
  print()
  print("Hasil pencarian:\n")
  for k in range(1,len(gadget())):
    if rarity == gadget()[k][4]:
      data_gadget(k)
      cari = True

  if not(cari):
    print("Tidak ada gadget yang ditemukan")

#-------------------------F04---------------------------------------#
def caritahun():
  tahun = str(input("Masukkan tahun: "))
  kategori = str(input("Masukkan kategori: "))
  cari = False
  print()
  print("Hasil pencarian:\n")
  if kategori == "=":
    for k in range(1,len(gadget())):
      if tahun == gadget()[k][5]:
        data_gadget(k)
        cari = True
  elif kategori == ">":
    for k in range(1,len(gadget())):
      if tahun < gadget()[k][5]:
        data_gadget(k)
        cari = True
  elif kategori == ">=":
    for k in range(1,len(gadget())):
      if tahun <= gadget()[k][5]:
        data_gadget(k)
        cari = True
  elif kategori == "<":
    for k in range(1,len(gadget())):
      if tahun > gadget()[k][5]:
        data_gadget(k)
        cari = True
  elif kategori == "<=":
    for k in range(1,len(gadget())):
      if tahun >= gadget()[k][5]:
        data_gadget(k)
        cari = True

  if not(cari):
    print("Tidak ada gadget yang ditemukan")
#caritahun()
# nanti bakal ku buat dekomposisinya
#-------------------------F05---------------------------------------#
def consumable():
  consumable = open("consumable.csv","r")
  consumable_array=consumable.readlines()
  trim_consumable_array = [["" for l in range(5)]for k in range(len(consumable_array))]
  l = 0
  k = 0
  for i in range(len(consumable_array)):
    for j in range(len(consumable_array[i])):
      if consumable_array[i][j] != ';':
        trim_consumable_array[k][l] += consumable_array[i][j]
      elif consumable_array[i][j] == ';':
        l += 1
    k += 1
    l = 0
  return trim_consumable_array

def sama_item(id_item):
  sama = False
  if id_item[0] == "G":
    for i in range(1, len(gadget())):
      if id_item == gadget()[i][0]:
        sama = True
  elif id_item[0] == "C":
    for i in range(1, len(consumable())):
      if id_item == consumable()[i][0]:
        sama = True
  return sama


def tambah_item():
  # Prosedure yang berfungsi untuk menambahkan item ke dalam inventori
  # input (gadget) = ID, Nama , Deskripsi, Jumlah, Rarity, Tahun
  # input (consumable) = ID, Nama, Deskripsi, Jumlah, Rarity
  # output = penambahan item ke inventori
  id_item = input("Masukkan ID: ")

  gadget = open("gadget.csv", "a")
  consumable = open("consumable.csv", "a")
  if not (sama_item(id_item)):
    if (id_item[0] == "G"):
      nama_item = input("Masukkan Nama: ")
      deskripsi_item = input("Masukkan Deskripsi: ")
      jumlah_item = input("Masukkan Jumlah: ")
      if int(jumlah_item) > 0:
        rarity_item = input("Masukkan Rarity: ")
        if rarity_item != 'C' and rarity_item != 'B' and rarity_item != 'A' and rarity_item != 'S':
          print("Input rarity tidak valid!")
        else:
          tahun_item = input("Masukkan tahun di temukan: ")
          if int(tahun_item) > 0:
            gadget.write(";".join([id_item, nama_item, deskripsi_item, jumlah_item, rarity_item, tahun_item]) + "\n")
            print("Item berhasil ditambahkan ke database")
          else:
            print("Input tahun tidak valid!")
      else:
        print("Input jumlah tidak valid!")
    elif (id_item[0] == "C"):
      nama_item = input("Masukkan Nama: ")
      deskripsi_item = input("Masukkan Deskripsi: ")
      jumlah_item = input("Masukkan Jumlah: ")
      if int(jumlah_item) > 0:
        rarity_item = input("Masukkan Rarity: ")
        if rarity_item != 'C' and rarity_item != 'B' and rarity_item != 'A' and rarity_item != 'S':
          print("Input rarity tidak valid!")
        else:
          consumable.write(";".join([id_item, nama_item, deskripsi_item, jumlah_item, rarity_item]) + "\n")
          print("Item berhasil ditambahkan ke database")
      else:
        print("Input jumlah tidak valid!")
    elif (id_item[0] != "G" and id_item[0] != "C"):
      print("\nGagal menambahkan item karena ID tidak valid")
  else:
    print("\nGagal menambahkan item karena ID sudah ada")

#-------------------------F06---------------------------------------#
def consumable():
  consumable = open("consumable.csv","r")
  consumable_array=consumable.readlines()
  trim_consumable_array = [["" for l in range(5)]for k in range(len(consumable_array))]
  l = 0
  k = 0
  for i in range(len(consumable_array)):
    for j in range(len(consumable_array[i])):
      if consumable_array[i][j] != ';':
        trim_consumable_array[k][l] += consumable_array[i][j]
      elif consumable_array[i][j] == ';':
        l += 1
    k += 1
    l = 0
  return trim_consumable_array

    
def hapus(urutan,trim_array,namafile):
  print("Apakah anda yakin ingin menghapus", end = " ")
  print(trim_array[urutan][1], end = " ")
  yakin_hapus = str(input("(Y/N)? "))
  if yakin_hapus == 'y' or yakin_hapus == 'Y':
    trim_array.pop(urutan)
    string_data = ""
    for var in trim_array:
      string_data += ";".join(var)
    file = open(namafile,"w")
    file.write(string_data)
    file.close()
    print("\n")
    print("Item telah berhasil dihapus dari database.")
  else:
    print("Item tidak berhasil dihapus dari database.")


def hapusitem():

  id_item = str(input("Masukan ID item: "))
  hapus_gadget = False
  hapus_consumable = False
  found = False
  if id_item[0] == 'G':
    k = 1
    while k < len(gadget()) and not(hapus_gadget):
      if id_item == gadget()[k][0]:
        hapus_gadget = True
        hapus(k,gadget(),"gadget.csv")
        found = True
      k += 1
  elif id_item[0] == 'C':
    k = 1
    while k < len(consumable()) and not(hapus_consumable):
      if id_item == consumable()[k][0]:
        hapus_consumable = True
        hapus(k,consumable(),"consumable.csv")
        found = True
      k += 1
  else:
    found = True
    print("Masukkan ID tidak valid!.")
  if found == False :
    print("\n")
    print("Tidak ada item dengan ID tersebut")
#-------------------------F07---------------------------------------#

def ubah_jumlah():
  
  gadget = open("gadget.csv","r")
  gadget_array=gadget.readlines()
  gadget.close()
  trim_gadget_array = [["" for l in range(6)]for k in range(len(gadget_array))]
  l = 0
  k = 0
  for i in range(len(gadget_array)):
    for j in range(len(gadget_array[i])):
      if gadget_array[i][j] != ';':
        trim_gadget_array[k][l] += gadget_array[i][j]
      elif gadget_array[i][j] == ';':
        l += 1
    k += 1
    l = 0

  consumable = open("consumable.csv","r")
  consumable_array=consumable.readlines()
  trim_consumable_array = [["" for l in range(5)]for k in range(len(consumable_array))]
  l = 0
  k = 0
  for i in range(len(consumable_array)):
    for j in range(len(consumable_array[i])):
      if consumable_array[i][j] != ';':
        trim_consumable_array[k][l] += consumable_array[i][j]
      elif consumable_array[i][j] == ';':
        l += 1
    k += 1
    l = 0  

  id_item = str(input("Masukkan ID: "))
  found = False
  if (id_item[0] == "G"):
      for i in range (len(trim_gadget_array)):
        for j in range (6):
          if trim_gadget_array[i][j] == id_item:
            found = True
            tambahan = int(input("Masukkan Jumlah: "))
            if (int(trim_gadget_array[i][3])+tambahan) < 0:
              print("\n")
              print(str(abs(tambahan))+" "+ str(trim_gadget_array[i][1]) +" gagal dibuang karena stok kurang. Stok sekarang: " + str(trim_gadget_array[i][3]) +" (< "+str(abs(tambahan))+")" )
            else:
              trim_gadget_array[i][3] = str(int(int(trim_gadget_array[i][3])+ tambahan))
              string_gadget = ""
              for gadget_array in trim_gadget_array:
                string_gadget += ";".join(gadget_array)
              gadget = open("gadget.csv","w")
              gadget.write(string_gadget)
              gadget.close()
              print("\n")
              if tambahan >= 0: 
                print(str(tambahan) +" "+trim_gadget_array[i][1] + " berhasil ditambahkan. Stok sekarang: " + str(trim_gadget_array[i][3]))
              else:
                print(str(abs(tambahan)) +" "+trim_gadget_array[i][1] + " berhasil dibuang. Stok sekarang: " + str(trim_gadget_array[i][3]))
  elif (id_item[0] == "C"):
      for i in range(len(trim_consumable_array)):
        for j in range(len(trim_consumable_array[i])):
          if trim_consumable_array[i][j] == id_item:
            found = True
            tambahan = int(input("Masukkan Jumlah: "))
            if (int(trim_consumable_array[i][3])+tambahan) < 0:
              print("\n")
              print(str(abs(tambahan))+" "+ str(trim_consumable_array[i][1]) +" gagal dibuang karena stok kurang. Stok sekarang: " + str(trim_consumable_array[i][3]) +" (< "+str(abs(tambahan))+")" )
            else:
              trim_consumable_array[i][3] = str(int(int(trim_consumable_array[i][3])+tambahan))
              string_consumable = ""
              for consumable_array in trim_consumable_array:
                string_consumable += ";".join(consumable_array)
              consumable = open("consumable.csv","w")
              consumable.write(string_consumable)
              consumable.close()
              print("\n")
              if tambahan >= 0:
                print(str(tambahan)+" "+trim_consumable_array[i][1]+" berhasil ditambahkan. Stok sekarang: "+str(trim_consumable_array[i][3]))
              else:
                print(str(abs(tambahan))+" "+trim_consumable_array[i][1]+" berhasil dibuang. Stok sekarang: "+str(trim_consumable_array[i][3]))
          
  if found == False:
    print("\n")
    print("Tidak ada item dengan ID tersebut!")   


#-------------------------F08---------------------------------------#


from datetime import date


def pinjamgadget(nomor):
  pinjam_gadget = open("gadget_borrow_history.csv", "a")

  gadget = open("gadget.csv", "r")
  gadget_array = gadget.readlines()
  gadget.close()
  trim_gadget_array = [["" for l in range(6)] for k in range(len(gadget_array))]
  l = 0
  k = 0
  for i in range(len(gadget_array)):
    for j in range(len(gadget_array[i])):
      if gadget_array[i][j] != ';':
        trim_gadget_array[k][l] += gadget_array[i][j]
      elif gadget_array[i][j] == ';':
        l += 1
    k += 1
    l = 0

  pinjam_gadget = open("gadget_borrow_history.csv", "r")
  pinjam_gadget_array = pinjam_gadget.readlines()
  pinjam_gadget.close()
  trim_pinjam_gadget_array = [["" for l in range(5)] for k in range(len(pinjam_gadget_array))]
  l = 0
  k = 0
  for i in range(len(pinjam_gadget_array)):
    for j in range(len(pinjam_gadget_array[i])):
      if pinjam_gadget_array[i][j] != ';':
        trim_pinjam_gadget_array[k][l] += pinjam_gadget_array[i][j]
      elif pinjam_gadget_array[i][j] == ';':
        l += 1
    k += 1
    l = 0

  pinjam_gadget = open("gadget_borrow_history.csv", "a")

  id_item = input("Masukkan ID item: ")
  sedang_pinjam = False
  found = False
  if (id_item[0] == "G"):
    for i in range(len(trim_pinjam_gadget_array)):
      if nomor == trim_pinjam_gadget_array[i][1] and id_item == trim_pinjam_gadget_array[i][2] and (
              int(trim_pinjam_gadget_array[i][4]) != 0):
        sedang_pinjam = True

    if not (sedang_pinjam):
      for i in range(len(trim_gadget_array)):
        for j in range(6):
          if id_item == trim_gadget_array[i][j]:
            found = True
            hari_ini = date.today()
            tanggal_peminjaman = hari_ini.strftime("%d/%m/%Y")
            print("Tanggal peminjaman: " + str(tanggal_peminjaman))
            jumlah_peminjaman = int(input("Jumlah peminjaman: "))
            if int(trim_gadget_array[i][3]) < jumlah_peminjaman:
              print("\n")
              print("Item " + str(
                trim_gadget_array[i][1] + " gagal dipinjam, stok tidak mencukupi! Stok sekarang: " + str(
                  trim_gadget_array[i][3])))
            else:
              count = len(open("gadget_borrow_history.csv").readlines())
              pinjam_gadget.write(
                ";".join([str(count), nomor, str(trim_gadget_array[i][0]), tanggal_peminjaman, str(jumlah_peminjaman)]))
              pinjam_gadget.writelines("\n")
              pinjam_gadget.close()
              print("\n")
              print(
                "Item " + str(trim_gadget_array[i][1] + "(x" + str(jumlah_peminjaman) + ") telah berhasil dipinjam"))
              trim_gadget_array[i][3] = str(int(int(trim_gadget_array[i][3]) - jumlah_peminjaman))
              string_gadget = ""
              for gadget_array in trim_gadget_array:
                string_gadget += ";".join(gadget_array)
              gadget = open("gadget.csv", "w")
              gadget.write(string_gadget)
              gadget.close()
    else:
      found = True
      print("\n")
      print("Pinjam gadget gagal! Item ini sedang dipinjam")
  else:
    found = True
    print("\n")
    print("Pinjam gadget gagal! Masukan ID tidak valid.")

  if not (found):
    print("\n")
    print("Pinjam gadget gagal! Tidak ditemukan item dengan ID tersebut.")
#-------------------------F09---------------------------------------#
def tulis_gadget(urutan,namafile,trim_array,angka_awal,jumlah_kembali):
  if namafile == "gadget_borrow_history.csv":
    trim_array[urutan][4] = str(int(angka_awal)-int(jumlah_kembali))+"\n"
    string_data = ""
    for var in trim_array:
      string_data += ";".join(var)
    file = open(namafile,"w")
    file.write(string_data)
    file.close()
  elif namafile == "gadget.csv":
    trim_array[urutan][3] = str(int(angka_awal)+int(jumlah_kembali))
    string_data = ""
    for var in trim_array:
      string_data += ";".join(var)
    file = open(namafile,"w")
    file.write(string_data)
    file.close()


from datetime import date
def kembalikan_gadget(nomor):
  print("\n")
  array_baru = [["" for l in range(5)] for k in range(len(pinjam_gadget())-1)]
  #array_baru berisi id, id_peminjam, id gadget, nama gadget, jumlah gadget

  i = 0
  for k in range(1,len(pinjam_gadget())):
    for l in range(1,len(gadget())):
      if pinjam_gadget()[k][2] == gadget()[l][0] and int(pinjam_gadget()[k][4]) != 0 and nomor == pinjam_gadget()[k][1]:
        print(str(i+1)+". "+gadget()[l][1])
        array_baru[i] = [str(i+1),pinjam_gadget()[k][1],pinjam_gadget()[k][2],gadget()[l][1],str(int(pinjam_gadget()[k][4]))]
        i += 1
  print()

  kembali = False
  nomor_peminjaman = str(input("Masukan nomor peminjaman: "))
  for k in range(len(array_baru)):
    if nomor_peminjaman == array_baru[k][0]:
      hari_ini = date.today()
      tanggal_pengembalian = str(hari_ini.strftime("%d/%m/%Y")) 
      print("Tanggal pengembalian: "+ str(tanggal_pengembalian))
      print()
      print("Item "+array_baru[k][3]+" (x"+array_baru[k][4]+") "+"telah dikembalikan")
      kembalikan_gadget=open("gadget_return_history.csv","a")
      count=len(open("gadget_return_history.csv").readlines())
      array_kembali=[str(count),array_baru[k][1],array_baru[k][2],tanggal_pengembalian]
      kembalikan_gadget.writelines(";".join(array_kembali))
      kembalikan_gadget.writelines("\n")
      kembalikan_gadget.close()

      for l in range(1,len(pinjam_gadget())):
        if array_baru[k][2] == pinjam_gadget()[l][2]:
          tulis_gadget(l,"gadget_borrow_history.csv",pinjam_gadget(),array_baru[k][4],array_baru[k][4])
      for l in range(1,len(gadget())):
        if array_baru[k][2] == gadget()[l][0]:
          jumlah_awal = gadget()[l][3]
          tulis_gadget(l,"gadget.csv",gadget(),jumlah_awal,array_baru[k][4])
      kembali = True

  if not(kembali):
    print("Nomor peminjaman salah")

#-------------------------F10---------------------------------------#
from datetime import date
def minta_consumable(nomor):
  consumable = open("consumable.csv","r")
  consumable_array=consumable.readlines()
  trim_consumable_array = [["" for l in range(5)]for k in range(len(consumable_array))]
  l = 0
  k = 0
  for i in range(len(consumable_array)):
    for j in range(len(consumable_array[i])):
      if consumable_array[i][j] != ';':
        trim_consumable_array[k][l] += consumable_array[i][j]
      elif consumable_array[i][j] == ';':
        l += 1
    k += 1
    l = 0
  
  minta_consumable = open("consumable_history.csv","a")

  id_item = input("Masukkan ID item: ")
  found = False
  if (id_item[0]=="C"):
    for i in range (len(trim_consumable_array)):
      for j in range (5):
        if trim_consumable_array[i][j] == id_item:
          found = True
          jumlah_permintaan = int(input("Jumlah : "))
          hari_ini = date.today()
          tanggal_permintaan = hari_ini.strftime("%d/%m/%Y")
          print("Tanggal permintaan: "+ str(tanggal_permintaan))
          if int(trim_consumable_array[i][3]) < jumlah_permintaan:
            print("\n")
            print("Item "+str(trim_consumable_array[i][1]+" gagal diminta, stok tidak mencukupi! stok sekarang :"+str(trim_consumable_array[i][3])))
          else:
            count=len(open("consumable_history.csv").readlines())
            minta_consumable.write(";".join([str(count),str(nomor),id_item,tanggal_permintaan,str(jumlah_permintaan)]))
            minta_consumable.writelines("\n")
            minta_consumable.close()
            print("\n")
            print("Item "+str(trim_consumable_array[i][1]+" (x"+str(jumlah_permintaan)+") telah berhasil diambil"))
            trim_consumable_array[i][3] = str(int(int(trim_consumable_array[i][3])-jumlah_permintaan))
            string_consumable = ""
            for consumable_array in trim_consumable_array:
              string_consumable += ";".join(consumable_array)
            consumable = open("consumable.csv","w")
            consumable.write(string_consumable)
            consumable.close()
  else:
    found = True
    print("\n")
    print("Minta consumable gagal! masukan id item tidak valid untuk consumable")
  if found == False:
    print("\n")
    print("Minta consumable gagal! tidak ditemukan consumable dengan ID tersebut")        


#-------------------------F11---------------------------------------#

def pinjam_gadget():
  pinjam_gadget=open("gadget_borrow_history.csv","r")
  pinjam_gadget_array=pinjam_gadget.readlines()
  pinjam_gadget.close()
  trim_pinjam_gadget_array = [["" for l in range(5)]for k in range(len(pinjam_gadget_array))]
  l = 0
  k = 0
  for i in range(len(pinjam_gadget_array)):
    for j in range(len(pinjam_gadget_array[i])):
      if pinjam_gadget_array[i][j] != ';':
        trim_pinjam_gadget_array[k][l] += pinjam_gadget_array[i][j]
      elif pinjam_gadget_array[i][j] == ';':
        l += 1
    k += 1
    l = 0
  return trim_pinjam_gadget_array


def riwayat_pinjam(trim_array):
  for i in range(1,len(trim_array)):
    for j in range(1,len(user())):
      if trim_array[i][1] == user()[j][0]:
        trim_array[i][1] = user()[j][2]

  for i in range(1,len(trim_array)):
    for j in range(1,len(gadget())):
      if trim_array[i][2] == gadget()[j][0]:
        trim_array[i][2] = gadget()[j][1]
  return trim_array



def data_peminjaman_gadget(urutan):
  print("ID Peminjaman      :",riwayat_pinjam(pinjam_gadget())[urutan][0])
  print("Nama Pengambil     :",riwayat_pinjam(pinjam_gadget())[urutan][1])
  print("Nama Gadget        :",riwayat_pinjam(pinjam_gadget())[urutan][2])
  print("Tanggal Peminjaman :",riwayat_pinjam(pinjam_gadget())[urutan][3])
  print("Jumlah             :",riwayat_pinjam(pinjam_gadget())[urutan][4])
  print()


from datetime import date
def riwayat_pinjam_gadget():

  array_pinjam = riwayat_pinjam(pinjam_gadget())
  lanjut = True
  while lanjut:
    if len(array_pinjam) >= 6:
      for i in range(len(array_pinjam)-1, len(array_pinjam)-6, -1):
        data_peminjaman_gadget(i)
        array_pinjam.pop(i)
      lihat_lagi = str(input("Apakah Anda ingin melihat riwayat lainnya (Y/N)? "))
      print()
      if lihat_lagi == "y" or lihat_lagi == "Y":
        lanjut = True
      else:
        lanjut = False
    else:
      for i in range(len(array_pinjam)-1, 0, -1):
        data_peminjaman_gadget(i)
      lanjut = False

  
#-------------------------F12---------------------------------------#

def riwayat_kembalikan_gadget():

  
  kembali_gadget=open("gadget_return_history.csv","r")
  kembali_gadget_array=kembali_gadget.readlines()
  kembali_gadget.close()
  trim_kembali_gadget_array = [["" for l in range(4)]for k in range(len(kembali_gadget_array))]
  l = 0
  k = 0
  for i in range(len(kembali_gadget_array)):
    for j in range(len(kembali_gadget_array[i])):
      if kembali_gadget_array[i][j] != ';':
        trim_kembali_gadget_array[k][l] += kembali_gadget_array[i][j]
      elif kembali_gadget_array[i][j] == ';':
        l += 1
    k += 1
    l = 0

  gadget = open("gadget.csv","r")
  gadget_array = gadget.readlines()
  gadget.close()
  trim_gadget_array = [["" for l in range(6)]for k in range(len(gadget_array))]
  l = 0
  k = 0
  for i in range(len(gadget_array)):
    for j in range(len(gadget_array[i])):
      if gadget_array[i][j] != ';':
        trim_gadget_array[k][l] += gadget_array[i][j]
      elif gadget_array[i][j] == ';':
        l += 1
    k += 1
    l = 0
  
  for i in range(1,len(trim_kembali_gadget_array)):
    for j in range(1,len(user())):
      if trim_kembali_gadget_array[i][1] == user()[j][0]:
        trim_kembali_gadget_array[i][1] = user()[j][2]

  for i in range(1,len(trim_kembali_gadget_array)):
    for j in range(1,len(trim_gadget_array)):
      if trim_kembali_gadget_array[i][2] == trim_gadget_array[j][0]:
        trim_kembali_gadget_array[i][2] = trim_gadget_array[j][1]
  
  print("\n")

  if len(trim_kembali_gadget_array) >= 6:
    for i in range(len(trim_kembali_gadget_array)-1, len(trim_kembali_gadget_array)-6, -1):
      print("ID Peminjaman        :",trim_kembali_gadget_array[i][0])
      print("Nama Pengambil       :",trim_kembali_gadget_array[i][1])
      print("Nama Gadget          :",trim_kembali_gadget_array[i][2])
      print("Tanggal Pengembalian :",trim_kembali_gadget_array[i][3])
      print()
  else:
    for i in range(len(trim_kembali_gadget_array)-1, 1, -1):
      print("ID Peminjaman        :",trim_kembali_gadget_array[i][0])
      print("Nama Pengambil       :",trim_kembali_gadget_array[i][1])
      print("Nama Gadget          :",trim_kembali_gadget_array[i][2])
      print("Tanggal Pengembalian :",trim_kembali_gadget_array[i][3])
      print()
#riwayat_kembali_gadget()
#-------------------------F13---------------------------------------#

def riwayat_ambil(): 

  
  minta_consumable=open("consumable_history.csv","r")
  minta_consumable_array=minta_consumable.readlines()
  minta_consumable.close()
  trim_minta_consumable_array = [["" for l in range(5)]for k in range(len(minta_consumable_array))]
  l = 0
  k = 0
  for i in range(len(minta_consumable_array)):
    for j in range(len(minta_consumable_array[i])):
      if minta_consumable_array[i][j] != ';':
        trim_minta_consumable_array[k][l] += minta_consumable_array[i][j]
      elif minta_consumable_array[i][j] == ';':
        l += 1
    k += 1
    l = 0

  consumable = open("consumable.csv", "r")
  consumable_array = consumable.readlines()
  trim_consumable_array = [["" for l in range(5)] for k in range(len(consumable_array))]
  l = 0
  k = 0
  for i in range(len(consumable_array)):
    for j in range(len(consumable_array[i])):
      if consumable_array[i][j] != ';':
        trim_consumable_array[k][l] += consumable_array[i][j]
      elif consumable_array[i][j] == ';':
        l += 1
    k += 1
    l = 0

  user=open("user.csv","r")
  user_array=user.readlines()
  user.close()
  trim_user_array = [["" for l in range(6)]for k in range(len(user_array))]
  l = 0
  k = 0
  for i in range(len(user_array)):
    for j in range(len(user_array[i])):
      if user_array[i][j] != ';':
        trim_user_array[k][l] += user_array[i][j]
      elif user_array[i][j] == ';':
        l += 1
    k += 1
    l = 0
  
  for i in range(1,len(trim_minta_consumable_array)):
    for j in range(1,len(trim_user_array)):
      if trim_minta_consumable_array[i][1] == trim_user_array[j][0]:
        trim_minta_consumable_array[i][1] = trim_user_array[j][2]

  for i in range(1,len(trim_minta_consumable_array)):
    for j in range(1,len(trim_consumable_array)):
      if trim_minta_consumable_array[i][2] == trim_consumable_array[j][0]:
        trim_minta_consumable_array[i][2] = trim_consumable_array[j][1]

  print("\n")

  if len(trim_minta_consumable_array) >= 6:
    for i in range(len(trim_minta_consumable_array)-1, len(trim_minta_consumable_array)-6, -1):
      print("ID Pengambilan       :",trim_minta_consumable_array[i][0])
      print("Nama Pengambil       :",trim_minta_consumable_array[i][1])
      print("Nama Consumable          :",trim_minta_consumable_array[i][2])
      print("Tanggal Pengembalian :",trim_minta_consumable_array[i][3])
      print("Jumlah               :",trim_minta_consumable_array[i][4])
      print()
  else:
    for i in range(len(trim_minta_consumable_array)-1, 1, -1):
      print("ID Peminjaman        :",trim_minta_consumable_array[i][0]) 
      print("Nama Pengambil       :",trim_minta_consumable_array[i][1])
      print("Nama Consumable          :",trim_minta_consumable_array[i][2])
      print("Tanggal Pengembalian :",trim_minta_consumable_array[i][3])
      print("Jumlah               :",trim_minta_consumable_array[i][4])
      print()
#riwayat_ambil()

#-------------------------F14---------------------------------------#
def load():
    import argparse
    import os
    parser = argparse.ArgumentParser()
    parser.add_argument("nama_folder", help="Nama folder yang berisi data untuk diakses",type=str)
    
    args = parser.parse_args()
    a = os.getcwd()

    print("Loading....")
    os.chdir(a+'\{}'.format(args.nama_folder))
    print('Selamat datang di "Kantong Ajaib!"')


#load data langsung di terminal
#usage : python kantongajaib.py <nama_folder>
#folder dan file kantongajaib.py harus ada di dir yang sama,
#misal keduanya ada di desktop
#-------------------------F15---------------------------------------#
import os.path
def string_file(nama_file):
    file = open(nama_file, "r")
    file_array = file.readlines()
    file.close()
    if (nama_file == 'gadget.csv'):
        trim_file_array = [["" for l in range(6)] for k in range(len(file_array))]
    elif (nama_file == 'consumable.csv'):
        trim_file_array = [["" for l in range(5)] for k in range(len(file_array))]
    elif nama_file == 'gadget_borrow_history.csv' :
        trim_file_array = [["" for l in range(5)] for k in range(len(file_array))]
    elif nama_file == 'gadget_return_history.csv' :
        trim_file_array = [["" for l in range(4)] for k in range(len(file_array))]
    elif nama_file == 'user.csv' :
        trim_file_array = [["" for l in range(6)] for k in range(len(file_array))]
    elif nama_file == 'consumable_history.csv' :
        trim_file_array = [["" for l in range(5)] for k in range(len(file_array))]
    l = 0
    k = 0
    for i in range(len(file_array)):
        for j in range(len(file_array[i])):
            if file_array[i][j] != ';':
                trim_file_array[k][l] += file_array[i][j]
            elif file_array[i][j] == ';':
                l += 1
        k += 1
        l = 0
    string_file = ""
    for file_array in trim_file_array:
        string_file += ";".join(file_array)
    return string_file

def tulis_csv(nama_file, folder_penyimpanan, string_data):
    f = open(folder_penyimpanan + "/" + nama_file, "w")
    f.write(string_data)
    f.close()

def save():
  folder_penyimpanan = input("Masukkan nama folder penyimpanan: ")
  if os.path.isdir(folder_penyimpanan):
    print("Saving...")
    print("Data telah disimpan pada folder "+str(folder_penyimpanan))
  else:
    os.mkdir(folder_penyimpanan)
    tulis_csv('consumable.csv', folder_penyimpanan, string_file('consumable.csv'))
    tulis_csv('consumable_history.csv', folder_penyimpanan, string_file('consumable_history.csv'))
    tulis_csv('gadget.csv', folder_penyimpanan, string_file('gadget.csv'))
    tulis_csv('gadget_borrow_history.csv', folder_penyimpanan, string_file('gadget_borrow_history.csv'))
    tulis_csv('gadget_return_history.csv', folder_penyimpanan, string_file('gadget_return_history.csv'))
    tulis_csv('user.csv', folder_penyimpanan, string_file('user.csv'))
    print("Saving...")
    print("Data telah disimpan pada folder "+str(folder_penyimpanan))

#-------------------------F16---------------------------------------#

def help(role):
  if role=="Admin":
    print("\n===================HELP===================")
    print("register - untuk melakukan registrasi user baru")
    print("carirarity - untuk melakukan pencarian gadget dengan rarity tertentu")
    print("caritahun - untuk melakukan pencarian gadget pada tahun tertentu")
    print("tambahitem - untuk menambahkan gadget")
    print("hapusitem - untuk menghapus gadget")
    print("ubahjumlah - untuk mengubah jumlah gadget")
    print("riwayatpinjam - untuk melihat riwayat peminjaman gadget")
    print("riwayatkembali - untuk melihat riwayat pengembalian gadget")
    print("riwayatambil - untuk melihat riwayat pengambilan consumable")
    print("save - untuk melakukan penyimpanan data")
    print("help - menampilkan bantuan")
    print("exit - berhenti menggunakan program Kantong Ajaib")
    print("==========================================\n")
  else:
    print("\n===================HELP===================")
    print("carirarity - untuk melakukan pencarian gadget dengan rarity tertentu")
    print("caritahun - untuk melakukan pencarian gadget pada tahun tertentu")
    print("pinjam - untuk meminjam gadget")
    print("kembalikan - untuk mengembalikan gadget")
    print("minta - untuk meminta consumable")
    print("gacha- meningkatkan rarity consumable")
    print("save - untuk melakukan penyimpanan data")
    print("help - menampilkan bantuan")
    print("exit - berhenti menggunakan program Kantong Ajaib")
    print("==========================================\n")
#-------------------------F17---------------------------------------#
def exit():
  print("Apakah anda mau melakukan penyimpanan file yang sudah diubah?")
  done=input("(Y/N) ").upper()
  jalan = True
  if done=="Y" :
    save()
    jalan=False
  elif done=="N":
    jalan=False
  else:
    while jalan:
      print("Input salah!\n")
      print("Apakah anda mau melakukan penyimpanan file yang sudah diubah?")
      done=input("(Y/N) ").upper()
      if done=="Y" :
        save()
        jalan=False
      elif done=="N":
        jalan=False

#-------------------------B01---------------------------------------#

def hashing(word):
  result = ""
  for letter in word :
    if letter in Alpha :
      num = (Alpha[letter])
      numplus = num + 9
      while int(numplus) >= 95 :
        numplus = int(numplus)% 95
      worddisplay = Alpha[numplus]
      result = result + str(worddisplay)
    else:
      result = result + letter
  return result

Alpha = {
  "`" : 0 , 0 : "naoveieh" ,
  "A" : 1 , 1 : "1248fbca" ,
  "B" : 2 , 2 : "9avd9abe" ,
  "C" : 3 , 3 : "aoivh3cas" ,
  "D" : 4 , 4 : "9813fhvn" ,
  "E" : 5 , 5 : "103fvca" ,
  "F" : 6 , 6 : "1038fh" ,
  "G" : 7 , 7 : "capog31m" ,
  "H" : 8 , 8 : "0v8a31" ,
  "I" : 9 , 9 : "a0v9h3f" ,
  "J" : 10 , 10 : "apoi3f1" ,
  "K" : 11 , 11 : "b029u424" ,
  "L" : 12 , 12 : "0avue8e24g" ,
  "M" : 13 , 13 : "vad9i0q0e3gf" ,
  "N" : 14 , 14 : "0183fucvna" ,
  "O" : 15 , 15 : "va98yqehv" ,
  "P" : 16 , 16 : "aovueqhvb" ,
  "Q" : 17 , 17 : "q90vucveq" ,
  "R" : 18 , 18 : "vquehvuiv" ,
  "S" : 19 , 19 : "quievqgeyvue" ,
  "T" : 20 , 20 : "qiuveqeyivq" ,
  "U" : 21 , 21 : "qoevuhqeuovq" ,
  "V" : 22 , 22 : "qivbqyev" ,
  "W" : 23 , 23 : "vauiveqiu" ,
  "X" : 24 , 24 : "auheviae" ,
  "Y" : 25 , 25 : "qwfhq" ,
  "Z" : 26 , 26 : "v089auvd" ,
  "a" : 27 , 27 : "zxc13" ,
  "b" : 28 , 28 : "ad7hebv" ,
  "c" : 29 , 29 : "9138fhvcn" ,
  "d" : 30 , 30 : "xhzeqf" ,
  "e" : 31 , 31 : "9248h" ,
  "f" : 32 , 32 : "mvowme" ,
  "g" : 33 , 33 : "183fiac" ,
  "h" : 34 , 34 : "vzdouvoqe" ,
  "i" : 35 , 35 : "3ifuoe" ,
  "j" : 36 , 36 : "voiewb" ,
  "k" : 37 , 37 : "b0w9ugri" ,
  "l" : 38 , 38 : "p13of[" ,
  "m" : 39 , 39 : "0b9r" ,
  "n" : 40 , 40 : "bmkwrb" ,
  "o" : 41 , 41 : "qi9o" ,
  "p" : 42 , 42 : "z-09ivdc" ,
  "q" : 43 , 43 : "qiefp" ,
  "r" : 44 , 44 : "qe9ipfe" ,
  "s" : 45 , 45 : "103urf" ,
  "t" : 46 , 46 : "biwrov" ,
  "u" : 47 , 47 : "1pokf" ,
  "v" : 48 , 48 : "mowklrb" ,
  "w" : 49 , 49 : "193if1" ,
  "x" : 50 , 50 : "smpbomwrb" ,
  "y" : 51 , 51 : "po3fkowv" ,
  "z" : 52 , 52 : "oiebvwmrv" ,
  "1" : 53 , 53 : "q/'w" ,
  "2" : 54 , 54 : ".[hrwebavp" ,
  "3" : 55 , 55 : "13fio" ,
  "4" : 56 , 56 : ";lmtin" ,
  "5" : 57 , 57 : "190u3v" ,
  "6" : 58 , 58 : "zmcv" ,
  "7" : 59 , 59 : "u948h" ,
  "8" : 60 , 60 : "9`dh1s" ,
  "9" : 61 , 61 : "/cmnv" ,
  "0" : 62 , 62 : "hk04-95" ,
  " " : 63 , 63 : "pokhe" ,
  "/" : 64 , 64 : "-cg0ni" ,
  "?" : 65 , 65 : "904t" ,
  "=" : 66 , 66 : "19-i3t" ,
  "." : 67 , 67 : "afeio" ,
  ">" : 68 , 68 : ">fbmlkd" ,
  "," : 69 , 69 : "2049t" ,
  "<" : 70 , 70 : "-d09ing" ,
  "'" : 71 , 71 : "opk35g" ,
  "\"" : 72 , 72 : "siorhn" ,
  ";" : 73 , 73 : "rmikogme" ,
  ":" : 74 , 74 : "o-wkr" ,
  "\\" : 75 , 75 : "whoipk" ,
  "|" : 76 , 76 : "mpwrohmwrh" ,
  "]" : 77 , 77 : "mpofr" ,
  "}" : 78 , 78 : "wrkpohw" ,
  "[" : 79 , 79 : "wadvpw" ,
  "{" : 80 , 80 : "mqegkimweg" ,
  "~" : 81 , 81 : "apmv" ,
  "+" : 82 , 82 : "opiwgk" ,
  "-" : 83 , 83 : "ber" ,
  "_" : 84 , 84 : "rgrt" ,
  ")" : 85 , 85 : ")\20ut4" ,
  "(" : 86 , 86 : "((!&T" ,
  "*" : 87 , 87 : "^%#!F" ,
  "&" : 88 , 88 : "9!HE@" ,
  "^" : 89 , 89 : "nv1039" ,
  "%" : 90 , 90 : ")CN!*#" ,
  "$" : 91 , 91 : "OQEN" ,
  "#" : 92 , 92 : "OUV*W" ,
  "@" : 93 , 93 : "*)VCY" ,
  "!" : 94 , 94 : "VUBEI07" ,
}


#-------------------------B02---------------------------------------#
from datetime import date
def kembalikan_parsial_gadget(nomor):
  array_baru = [["" for l in range(5)] for k in range(len(pinjam_gadget())-1)]
  #array_baru berisi id, id_peminjam, id gadget, nama gadget, jumlah gadget

  i = 0
  for k in range(1,len(pinjam_gadget())):
    for l in range(1,len(gadget())):
      if pinjam_gadget()[k][2] == gadget()[l][0] and int(pinjam_gadget()[k][4]) != 0 and nomor == pinjam_gadget()[k][1]:
        print(str(i+1)+". "+gadget()[l][1])
        array_baru[i] = [str(i+1),pinjam_gadget()[k][1],pinjam_gadget()[k][2],gadget()[l][1],str(int(pinjam_gadget()[k][4]))]
        i += 1
  print()

  kembali = False
  nomor_peminjaman = str(input("Masukan nomor peminjaman: "))
  for k in range(len(array_baru)):
    if nomor_peminjaman == array_baru[k][0]:
      jumlah_pengembalian = int(input("Masukan jumlah pengembalian: "))
      if jumlah_pengembalian > 0 and jumlah_pengembalian <= int(array_baru[k][4]):
        hari_ini = date.today()
        tanggal_pengembalian = str(hari_ini.strftime("%d/%m/%Y")) 
        print("Tanggal pengembalian: "+ str(tanggal_pengembalian))
        print()
        print("Item "+array_baru[k][3]+" (x"+str(jumlah_pengembalian)+") "+"telah dikembalikan")
        kembalikan_gadget=open("gadget_return_history.csv","a")
        count=len(open("gadget_return_history.csv").readlines())
        array_kembali=[str(count),array_baru[k][1],array_baru[k][2],tanggal_pengembalian]
        kembalikan_gadget.writelines(";".join(array_kembali))
        kembalikan_gadget.writelines("\n")
        kembalikan_gadget.close()

        for l in range(1,len(pinjam_gadget())):
          if array_baru[k][2] == pinjam_gadget()[l][2]:
            tulis_gadget(l,"gadget_borrow_history.csv",pinjam_gadget(),array_baru[k][4],jumlah_pengembalian)
        for l in range(1,len(gadget())):
          if array_baru[k][2] == gadget()[l][0]:
            jumlah_awal = gadget()[l][3]
            tulis_gadget(l,"gadget.csv",gadget(),jumlah_awal,jumlah_pengembalian)
      
      else:
        print("\nJumlah pengembalian melebihi jumlah peminjaman")
      kembali = True

  if not(kembali):
    print("Nomor peminjaman salah")

#-------------------------B03---------------------------------------#
def gacha():
  count=len(open("consumable.csv").readlines())
  mem=[[1 for i in range(6)]for j in range(count)]
  itemgacha=[]
  hide=0
  baca=open("consumable.csv").readlines()
  for i in range(count):
    arr=[]
    temp=""
    for huruf in baca[i]:
      if huruf==";":
        arr.append(temp)
        temp=""
      else:
        temp+=huruf
    if temp:
      arr.append(temp)
    mem[i]=arr
    if mem[i][4]=="A\n":
      mem[i][4]="A"
    elif mem[i][4]=="B\n":
      mem[i][4]="B"
    elif mem[i][4]=="C\n":
      mem[i][4]="C"
    elif mem[i][4]=="S\n":
      mem[i][4]="S"
  for i in range(count-1):
    if int(mem[i+1][3])>0:
      itemgacha.append(mem[i+1])
  print("\n=========INVENTORY=========")
  for i in range(len(itemgacha)-hide):
    print(str(i+1)+". "+itemgacha[i][1]+" (Rarity "+itemgacha[i][4]+") ("+itemgacha[i][3]+")")
  print("===========================\n")
  pilih=int(input("Pilih consumable yang mau digunakan :"))
  while len(itemgacha)-hide<pilih or pilih==0:
    print("item tidak tersedia")
    print("\n=========INVENTORY=========")
    for i in range(len(itemgacha)-hide):
      print(str(i+1)+". "+itemgacha[i][1]+" (Rarity "+itemgacha[i][4]+") ("+str(itemgacha[i][3])+")")
    print("===========================\n")
    pilih=int(input("Pilih consumable yang mau digunakan :"))
  jumlah=int(input("Jumlah yang digunakan :"))
  while int(itemgacha[pilih-1][3])<jumlah:
    print("jumlah item tidak tersedia")
    print("\n=========INVENTORY=========")
    for i in range(len(itemgacha)-hide):
      print(str(i+1)+". "+itemgacha[i][1]+" (Rarity "+itemgacha[i][4]+") ("+str(itemgacha[i][3])+")")
    print("===========================\n")
    pilih=int(input("Pilih consumable yang mau digunakan :"))
    while len(itemgacha)-hide<pilih or pilih==0 :
      print("item tidak tersedia")
      print("\n=========INVENTORY=========")
      for i in range(len(itemgacha)-hide):
        print(str(i+1)+". "+itemgacha[i][1]+" (Rarity "+itemgacha[i][4]+") ("+str(itemgacha[i][3])+")")
      print("===========================\n")
      pilih=int(input("Pilih consumable yang mau digunakan :"))
    jumlah=int(input("Jumlah yang digunakan :"))
  print("\n"+itemgacha[pilih-1][1]+" (x"+str(jumlah)+") ditambahkan!")
  itemgacha[pilih-1][3]=int(itemgacha[pilih-1][3])-jumlah
  itemgacha[pilih-1][3]=str(itemgacha[pilih-1][3])
  if itemgacha[pilih-1][4]=="S":
    rare="S"
    rate=0.01*jumlah+50
  elif itemgacha[pilih-1][4]=="A":
    rare="S"
    rate=0.5*jumlah
  elif itemgacha[pilih-1][4]=="B":
    rare="A"
    rate=1*jumlah
  elif itemgacha[pilih-1][4]=="C":
    rare="B"
    rate=5*jumlah
  print("Chance mendapatkan rarity "+rare+" ("+str(rate)+"%)\n")
  if itemgacha[pilih-1][3]==0:
    temp=itemgacha[pilih-1]
    for i in range(len(itemgacha)-hide-pilih):
      itemgacha[pilih-1+i]=itemgacha[pilih+i]
    hide+=1
    itemgacha[len(itemgacha)-1]=temp
  if hide<len(itemgacha):
    lagi=input("Tambahkan item lagi?(Y/N) : ").upper()
  else:
    lagi="N"
  while lagi!="N":
    if lagi=="Y":
      print("\n=========INVENTORY=========")
      for i in range(len(itemgacha)-hide):
        print(str(i+1)+". "+itemgacha[i][1]+" (Rarity "+itemgacha[i][4]+") ("+str(itemgacha[i][3])+")")
      print("===========================\n")
      pilih=int(input("Pilih consumable yang mau digunakan :"))
      while len(itemgacha)-hide<pilih or pilih==0:
        print("item tidak tersedia")
        print("\n=========INVENTORY=========")
        for i in range(len(itemgacha)-hide):
          print(str(i+1)+". "+itemgacha[i][1]+" (Rarity "+itemgacha[i][4]+") ("+str(itemgacha[i][3])+")")
        print("===========================\n")
        pilih=int(input("Pilih consumable yang mau digunakan :"))
      jumlah=int(input("Jumlah yang digunakan :"))
      while int(itemgacha[pilih-1][3])<jumlah:
        print("jumlah item tidak tersedia")
        print("\n=========INVENTORY=========")
        for i in range(len(itemgacha)-hide):
          print(str(i+1)+". "+itemgacha[i][1]+" (Rarity "+itemgacha[i][4]+") ("+str(itemgacha[i][3])+")")
        print("===========================\n")
        pilih=int(input("Pilih consumable yang mau digunakan :"))
        while len(itemgacha)-hide<pilih or pilih==0 :
          print("item tidak tersedia")
          print("\n=========INVENTORY=========")
          for i in range(len(itemgacha)-hide):
            print(str(i+1)+". "+itemgacha[i][1]+" (Rarity "+itemgacha[i][4]+") ("+str(itemgacha[i][3])+")")
          print("===========================\n")
          pilih=int(input("Pilih consumable yang mau digunakan :"))
        jumlah=int(input("Jumlah yang digunakan :"))
      print("\n"+itemgacha[pilih-1][1]+" (x"+str(jumlah)+") ditambahkan!")
      itemgacha[pilih-1][3]=str(int(itemgacha[pilih-1][3])-jumlah)
      if itemgacha[pilih-1][4]=="S":
        rare="S"
        rate=0.01*jumlah+50
      elif itemgacha[pilih-1][4]=="A":
        rare="S"
        rate=0.5*jumlah
      elif itemgacha[pilih-1][4]=="B":
        rare="A"
        rate=1*jumlah
      elif itemgacha[pilih-1][4]=="C":
        rare="B"
        rate=5*jumlah
      print("Chance mendapatkan rarity "+rare+" ("+str(rate)+"%)\n")
      if itemgacha[pilih-1][3]==0:
        temp=itemgacha[pilih-1]
        for i in range(len(itemgacha)-hide-pilih):
          itemgacha[pilih-1+i]=itemgacha[pilih+i]
        hide+=1
        itemgacha[len(itemgacha)-1]=temp
      if hide<len(itemgacha):
        lagi=input("Tambahkan item lagi?(Y/N) : ").upper()
      else:
        lagi="N"
    else:
      print("input salah!")
      if hide<len(itemgacha):
        lagi=input("Tambahkan item lagi?(Y/N) : ").upper()
      else:
        lagi="N"
  #item pool
  #rarity S
  pools=[0 for i in range (100)]
  #rarity A
  poola=[0 for i in range (100)]
  #rarity B
  poolb=[0 for i in range (100)]
  #item rarity S
  pools[5]="Caviar"
  pools[43]="Foie Gras"
  #item rarity A
  poola[6]="Double Bacon Burger"
  poola[81]="Wagyu Steak"
  poola[35]="Panna Cotta"
  #item rarity B
  poolb[76]="Box Ind*mie"
  poolb[61]="Ch*tato"
  poolb[25]="S*lverqueen"
  poolb[13]="Teh Botol S*sro"
  #algo gacha
  rarity=rare
  dt = datetime.datetime.now()
  M= int(dt.strftime("%M"))
  H= int(dt.strftime("%H"))
  x= 5
  S= int(dt.strftime("%S"))
  chance = round(1+((S*H+M)%x))
  #base chance 1%
  #chance range 1%-6%
  chancegacha = round(rate)
  item=0
  print("\nRolling...\n")
  if rarity=="S":
    for i in range(chancegacha):
      if chance+i<100:
        item=pools[chance+i]
        if item!=0:
          break
      elif chance-i>0:
        item=pools[chance-i]
        if item!=0:
          break
      else:
        item=0
  elif rarity=="A":
    for i in range(chancegacha):
      if chance+i<100:
        item=poola[chance+i]
        if item!=0:
          break
      else:
        item=poola[chance-i]
        if item!=0:
          break
  elif rarity=="B":
    for i in range(chancegacha):
      if chance+i<100:
        item=poolb[chance+i]
        if item!=0:
          break
      else:
        item=poolb[chance-i]
        if item!=0:
          break
  if item==0:
    print("Gacha Failed")
  else:
    print("Selamat anda mendapatkan "+item+(" (x1)"))
    #deskripsi item
    if item=="Caviar":
      desc="Telur sturgeon yang diawetkan, harganya selangit"
    elif item=="Foie Gras":
      desc="Makanan mahal khas prancis yang terbuat dari hati angsa"
    elif item=="Double Bacon Burger":
      desc="Burger lezat dengan isi daging bacon 2 tingkat"
    elif item=="Wagyu Steak":
      desc="Steak yang terbuat dari daging sapi berkualitas tinggi"
    elif item=="Panna Cotta":
      desc="Hidangan penutup italia yang meleleh di mulut"
    elif item=="Box Ind*mie":
      desc="Makanan favorit anak kos, Ind*mie seleraku"
    elif item=="Ch*tato":
      desc="Life is never flat"
    elif item=="S*lverqueen":
      desc="Santai belum lengkap tanpa S*lverqueen"
    elif item=="Teh Botol S*sro":
      desc="Apapun makannya, minumnya teh botol S*sro"
    sama=False
    for i in range(len(itemgacha)):
      if itemgacha[i][1] == item :
        itemgacha[i][3]=str(int(itemgacha[i][3])+1)
        sama=True
        break
    if not(sama):
      reward=["C"+str(len(mem)),item,desc,"1",rare]
      mem.append(reward)
  tulis=open("consumable.csv","w")
  data=["id","nama","deskripsi","jumlah","rarity"]
  tulis.writelines(";".join(data))
  tulis.writelines("\n")

  for i in range(len(mem)-1):
    for j in range(len(itemgacha)):
      if mem[i+1][1]==itemgacha[j][1]:
        mem[i+1][3]=itemgacha[j][3]
        sama=True
    data=[]
    for k in range(5):
      data.append(mem[i+1][k])
    tulis.writelines(";".join(data))
    tulis.writelines("\n")
  tulis.close()
#--------------------Program UTAMA----------------------------------#

load()
jalanuser=False
jalanadmin=False
role=login()
if role[0] != "0":
  print("\nAnda terdaftar sebagai "+str(role[1]))

if role[1]=="User\n":
  jalanuser=True
elif role[1]=="Admin\n":
  jalanadmin=True

while jalanuser:
  perintah=input(">>> ").lower()
  if perintah=="carirarity":
    carirarity()
  elif perintah=="caritahun":
    caritahun()
  elif perintah=="pinjam":
    pinjamgadget(role[0])
  elif perintah=="kembalikan":
    kembalikan_gadget(role[0])
  elif perintah == "kembalikanparsial":
    kembalikan_parsial_gadget(role[0])
  elif perintah=="minta":
    minta_consumable(role[0])
  elif perintah=="save":
    save()
  elif perintah=="help":
    help("User")
  elif perintah=="exit":
    exit()
    jalanuser=False
  elif perintah=="gacha":
    gacha()
  else:
    print("\nPerintah tidak tersedia\n")

while jalanadmin:
  perintah=input(">>> ").lower()
  if perintah=="carirarity":
    carirarity()
  elif perintah=="register":
    register()
  elif perintah=="caritahun":
    caritahun()
  elif perintah=="tambahitem":
    tambah_item()
  elif perintah=="hapusitem":
    hapusitem()
  elif perintah=="ubahjumlah":
    ubah_jumlah()
  elif perintah=="riwayatpinjam":
    riwayat_pinjam_gadget()
  elif perintah=="riwayatkembali":
    riwayat_kembalikan_gadget()
  elif perintah=="riwayatambil":
    riwayat_ambil()
  elif perintah=="save":
    save()
  elif perintah=="help":
    help("Admin")
  elif perintah=="exit":
    exit()
    jalanadmin=False
  else:
    print("\nPerintah tidak tersedia\n")
