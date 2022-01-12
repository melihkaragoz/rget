import sys,os,wget

password = "<sifrenizi girin>" # kullanici sifrenizi buraya "tirnak icinde" girin.

try:
	f=open("config.txt","r")
	password = f.readline().replace("\n","")
except:
	print("[!!] config.txt bulunamadi")

#host = "http://localhost:3030"
host="https://melihkaragoz.com/fileserver"
try:
	username = sys.argv[1]
	file = sys.argv[2]
	new_dir=""
	sp_ch=""
	list_dir=""
	upFile = True
	if(file =="--create"):
		file = "config.txt"
		new_dir="&newdir=1"
	elif(file == "--list"):
		file="config.txt"
		list_dir="&list=2"
	elif(file == "--get"):
		getFile=sys.argv[3]
		if(getFile != "/"): sp_ch = "/"
	dest_dir="&destdir="+sys.argv[3]
	if(sys.argv[3][0] != "/"): dest_dir = "&destdir=/"+sys.argv[3]
	if(username!="" and file!="" and file != "--get"): os.system(f"curl -F 'uploadedfile=@{file}' '{host}/upload.php?user={username}&pass={password}{dest_dir}{new_dir}{list_dir}'")
	elif(file=="--get"):
		file_name = wget.download("https://melihkaragoz.com/fileserver/uploads/"+username+sp_ch+getFile)
		print("\n"+file_name+" adli dosya indirildi.")
	else: raise ValueError()
except:
	print("\n   Kullanim : \n")
	print("   rpush <kullanici_adi> <dosya_adi>  <hedef_dizin>     : belirtilen dosyayi sisteme yukler.")
	print("   rpush <kullanici_adi> <dosya_adi>  <hedef_dizin>     : <hedef_dizin> adinda bir klasor olusturup dosyayi icine koyar.")
	print("   rpush <kullanici_adi> --create <yeni_klasor>         : sadece <yeni_klasor> adinda bir klasor olusturur.")
	print("   rpush <kullanici_adi> --list <listelenecek_dizin>    : belirtilen dizindeki dosyaları ve klasorleri listeler\n")
