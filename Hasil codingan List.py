barang = []

while True:
	print('''
	1.menambah
	2.menghapus
	3.mengedit
	4.menampilkan
	5.memeriksa barang
	6.mencari index''')
	perintah = input("Masukkan Perintah: ")
	
	if perintah == '1' :
		tmb = input("Masukkan Barang: ")
		barang.append(tmb)
	elif perintah == '2' :
		index =int(input("masukkan index yang akan di hapus :"))
		barang.pop(index)
	elif perintah == '3' :
		edit = input("masukkan barang yang akan diedit: ")
		index = None
		for i in range(len(barang)):
			if barang [i] == edit:
				index = i
				
		if index == None:
			print("Barang tidak ditemukan.")
		else:
			barang [index] = input("masukkan barang yang baru: ")
	elif perintah == '4' :
		print(barang)
	elif perintah == '5' :
		cari = input("masukkan nama barang yang dicari: ")
		if cari in barang :
		   print("barang di temukan")
		else :
			print("barang tidak ditemukan")
	elif perintah == '6' :
	    cariz = input("masukkan barang yang dicari indexnya: ")
	    index = None
	    for i in range(len(barang)):
	    	if barang [i] == cariz:
	    		index = i
	    		
	    if index == None:
	    	print("barang ditemukan. ")
	    else :
	    	print("{} ada pada index ke - {}". format(cariz,index))
	else:
	    break
	    
	  
	  
print("Program Berhenti. Selamat Tinggal")