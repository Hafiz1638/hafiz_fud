Hafiz_FUD - Python Obfuscator & Payload Protector

Bu araç, Python tabanlı payload veya scriptlerin statik analiz araçları (AV/EDR) tarafından tespit edilmesini zorlaştırmak amacıyla geliştirilmiş bir obfuscation (kod karartma) ve encryption (şifreleme) aracıdır. Kodun okunabilirliğini bozarak ve çalışma zamanında (runtime) bellekte çözülmesini sağlayarak analiz süreçlerini karmaşıklaştırır.
 Özellikler

    Çok Katmanlı Karartma: Kodun mantığını bozmadan değişken ve fonksiyon yapılarını gizler.

    Fernet Entegrasyonu: Payload'u güçlü şifreleme algoritmalarıyla sarmalar.

    Runtime Execution: Şifrelenmiş kod disk üzerinde değil, çalışma anında bellekte çözülerek yürütülür.

    Anti-Analiz: Statik imza tabanlı taramalardan kaçınmak için dinamik kod üretimi yapar.
🛠️Kurulum

Öncelikle gerekli kütüphanelerin sisteminizde yüklü olduğundan emin olun:
Bash

pip install cryptography

Projeyi klonlayın:
Bash

git clone https://github.com/Hafiz1638/hafiz_fud.git
cd hafiz_fud

 Kullanım

Aracı çalıştırmak için terminal üzerinden şu komutu kullanabilirsiniz:
Bash

python main.py

    Program sizden gizlemek istediğiniz .py dosyasının yolunu isteyecektir.

    İşlem tamamlandığında, output klasörü altında şifrelenmiş ve karartılmış yeni dosyanız oluşturulacaktır.

Yasal Uyarı

Bu araç yalnızca eğitim ve etik hackerlık (White Hat) faaliyetleri kapsamında, yetkili sızma testleri için geliştirilmiştir. Zararlı faaliyetlerde kullanılması durumunda tüm sorumluluk kullanıcıya aittir. Geliştirici, kötüye kullanım durumunda sorumluluk kabul etmez.
