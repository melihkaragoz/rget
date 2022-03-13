import sys,os,wget
username = "kullanici_adi"			# kullanici adinizi buraya "tirnak icinde" girin.
password = "sifre"	# kullanici sifrenizi buraya "tirnak icinde" girin.
host="https://mefasis.com/fileserver"
try:
	param,file = sys.argv[1],sys.argv[2]
	new_dir,sp_ch,list_dir,dest_dir="","","",""
	upFile = True
	if(param =="--create"):
		new_dir="&newdir=1"
		dest_dir="&destdir=/"+sys.argv[2]
		if(username!="" and password!=""): os.system(f"curl -X GET '{host}/upload.php?user={username}&pass={password}{new_dir}{dest_dir}'")
	elif(param == "--list"):
		list_dir="&list=2"
		dest_dir="&destdir="+sys.argv[2]
		if(username!="" and file!=""): os.system(f"curl -X GET '{host}/upload.php?user={username}&pass={password}{dest_dir}{list_dir}'")
	elif(param == "--get"):
		getFile=sys.argv[2]
		if(getFile != "/"): sp_ch = "/"
		file_name = wget.download(host+"/uploads/"+username+sp_ch+getFile)
		print("\n"+file_name+" adli dosya indirildi.")
	elif(param == "--push"):
		dest_dir="&destdir="+sys.argv[3]
		if(sys.argv[3][0] != "/"): dest_dir = "&destdir=/"+sys.argv[3]
		if(username!="" and file!=""): os.system(f"curl -F 'uploadedfile=@{file}' '{host}/upload.php?user={username}&pass={password}{dest_dir}{new_dir}{list_dir}'")
		else: raise ValueError()
except:
	print("""\n Kullanim : \n \n \
rget --push <dosya_adi>  <hedef_dizin>        : belirtilen dosyayi sisteme yukler.\n \
rget --push <dosya_adi>  <hedef_dizin>        : <hedef_dizin> adinda bir klasor olusturup dosyayi icine koyar.\n \
rget --create <yeni_klasor>        		: <yeni_klasor> adinda bir klasor olusturur.\n \
rget --list /<listelenecek_dizin>	    	: belirtilen dizindeki dosyaları ve klasorleri listeler\n \
	""")
