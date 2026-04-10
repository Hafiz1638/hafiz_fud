Hafiz_FUD - Python Kod Karartıcı Bu araç, yazdığın Python scriptlerini veya payloadlarını statik analizden (AV/EDR gibi) kaçırmak, kodun içeriğini meraklı gözlerden gizlemek için geliştirdiğim bir obfuscation ve encryption aracıdır. Kodunu tamamen tanınmaz hale getirir ve sadece çalışma anında bellekte açar. 
Ne Yapıyor Bu?

    Kodunu Çorbaya Çevirir: Değişkenleri ve fonksiyonları karartarak kodun okunabilirliğini yok eder.

    Fernet Şifreleme: Payload'u güçlü bir şekilde şifreler, anahtar olmadan kimse içini göremez.

    Bellekte Çalıştırma: Şifrelenmiş kod diske iz bırakmaz, doğrudan bellekte (exec) çözülüp çalışır.

    Analiz Engelleyici: Statik tarama yapan araçların imza yakalamasını zorlaştırır.
   Kurulum

Önce şu kütüphaneyi bir çekelim:
Bash

pip install cryptography

Sonra projeyi indir:
Bash

 git clone https://github.com/Hafiz1638/hafiz_fud.git
 cd hafiz_fud
 Nasıl Kullanılır?

Terminali aç ve yapıştır:
Bash

python main.py
⚠️ Uyarı (Önemli!)

Bu araç tamamen eğitim ve etik hackerlık (White Hat) çalışmaları için yapılmıştır. Gidip de başkasının canını yakmak için kullanmayın, sorumluluk tamamen sizde. Biz burada siber güvenlik araştırmacısıyız, unutmayın! ;)
