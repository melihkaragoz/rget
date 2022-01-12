# rget
[ TR ] Dosya yönetim sistemi

[!!] pip install -r requirements.txt yazip gereken kütüphaneleri otomatik olarak kurabilirsiniz.
[!!] çalıştırmadan önce rget.py içine kullanıcı adı ve şifrenizi "tirnak icinde" yazmayı unutmayın

 - Serverda bulunan dosyalarınızı tek tıkla cihazınıza indirebilirsiniz.
 -Kullanımı : python3 rget.py --get "dosya"
 - Bilgisayarınızdaki herhangi bir dosyayı servera gönderebilir,
 -Kullanımı : python3 rget.py --push "yuklenecek_dosya"   "yuklenecegi_dizin"
 - Serverda yeni klasörler oluşturabilir,
 -Kullanımı : python3 rget.py --create "klasor adi"
 - Bu komut ile karşıdaki dosyalarınızı görüntüleyebilirsiniz.
 -Kullanımı : python3 rget.py --list "listelenecek_dizin"
