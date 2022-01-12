# rget
[ TR ] Dosya yönetim sistemi

<h3>Gereksinimler : </h3>
  - cURL <br>
  - wget  => pip3 install wget <br>
  - python <br>

<h2> [!!] çalıştırmadan önce rget.py içine kullanıcı adı ve şifrenizi "tirnak icinde" yazmayı unutmayın.</h2>

<h2>rget</h2>
<p>
 - Serverda bulunan dosyalarınızı tek tıkla cihazınıza indirebilirsiniz.
 <h5>Kullanımı : python3 rget.py --get "dosya" </h5>
 - Bilgisayarınızdaki herhangi bir dosyayı servera gönderebilir,
 <h5>Kullanımı : python3 rget.py --push "yuklenecek_dosya"   "yuklenecegi_dizin"  </h5>
 - Serverda yeni klasörler oluşturabilir,<br>
 <h5>Kullanımı : python3 rget.py --create "klasor adi"</h5>
 - Bu komut ile karşıdaki dosyalarınızı görüntüleyebilirsiniz.
 <h5>Kullanımı : python3 rget.py --list "listelenecek_dizin"  </h5>

</p>
