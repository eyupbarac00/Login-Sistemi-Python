import time

print("| Kullanıcı girişi V1 |")

kullanıcıadları = open("kullanici.txt", "r").read()

login = input("Kullanıcı adınızı giriniz... \n")

if login == kullanıcıadları:
  pass

else:
  print("Kullanıcı Bulunamadı")
  time.sleep(5)
  exit

sifreler = open("sifreler.txt", "r").read()

time.sleep(.5)
login1 = input("Şifrenizi giriniz... \n")
if login1 == sifreler:
  print("Kontrol ediliyor... bekleyiniz...")
  time.sleep(3)
  print("Giriş onaylandı!")
  
