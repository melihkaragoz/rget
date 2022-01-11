import sys,wget

try:
	username = sys.argv[1]
	file = sys.argv[2]
	sp_ch = ""
	if(file[0] != "/"): sp_ch = "/"
	file_name = wget.download("https://melihkaragoz.com/fileserver/uploads/"+username+sp_ch+file)
	print("\n"+file_name+" adli dosya indirildi.")
except:
	print("kullanim : rget <kullanici_adi> <klasor/dosya_adi>")

