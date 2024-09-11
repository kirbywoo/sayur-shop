Link PWS : https://eva-yunia-sayurshop.pbp.cs.ui.ac.id

# 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step
## Membuat sebuah proyek Django baru:
  - Pertama, membuat direktori pada computer lokal dengan nama aplikasi E-Commerce (sayur-shop).
  - Buka command prompt pada direktori sayur-shop.
  - Agar aplikasi tidak bertabrakan dengan versi lain yang ada pada komputer kita, kita akan mengaktifkan virtual environment untuk mengisolasi package dan dependencies.
    Pada cmd kita menjalankan perintah `env\Scripts\activate` lalu pada terminal akan muncul tulisan `env` yang menandakan virtual environment aktif.
    Di dalam direktori sayur-shop kita membuat file requirements.txt yang berisikan dependencies (modul, library, atau komponen lain yang diperlukan perangkat lunak)
    Isi requirements.txt:
    ```txt
    django
    gunicorn
    whitenoise
    psycopg2-binary
    requests
    urllib3
    ```
  - Melakukan installasi terhadap dependencies dengan perintah `pip install -r requirements.txt` pada cmd. Pastikan virtual environment sudah aktif
  - Buat proyek Django dengan nama `sayur-shop` dengan menjalankan perintah `django-admin startproject sayur-shop .` pada cmd
  - Buka file `settings.py` yang berada pada direktori proyek `sayur-shop`
    Tambahkan string berikut:
    ```
    ...
    ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
    ...
    ```
    Perintah tersebut merupakan daftar host yang diizinkan untuk mengakses web. Ini berarti kita memberi izin pada local host.
  - Menjalankan perintah `python manage.py runserver` pada cmd untuk menjalankan server Django.
  - Buka http://localhost:8000 untuk mengecek apakah aplikasi Django telah berhasil dibuat. Jika muncul animasi roket, ini berarti aplikasi Django telah berhasil dibuat.
  - Setelah proyek Django berhasil dibuat, hentikan server dengan `ctrl+c` lalu nonaktifkan virtual environment dengan perintah `deactivate` pada cmd.
  - Unggah proyek sayur-shop ke repositori GitHub dengan cara membuat sebuah repositori baru bernama sayur-shop lalu atur visibilitas nya menjadi public. 
  - Buka cmd pada direktori sayur-shop dan jalankan perintah `git init` untuk inisialisasi direktori lokal `sayur-shop` sebagai repositori git. 
  - Konfigurasi autentikasi dengan menjalankan perintah:
    ```
    git credential-manager configure
    git config --global credential.credentialStore wincredman
    git config --list (untuk memastikan konfigurasi telah diatur dengan benar pada repositori lokal)
    ```
  - Buat branch Utama bernama main dengan menjalankan perintah `git branch -M main`.
  - Menghubungkan dengan repositori di GitHub dengan perintah `git remote add origin https://github.com/kirbywoo/sayur-shop.git`
  - Buat berkas `.gitignore` untuk konfigurasi berkas-berkas dan direktori-direktori mana yang harus diabaikan oleh Git
  - Lakukan add, commit, dan push dengan menjalankan perintah
    ```
    git add .
    git commit -m "initialize gitignore"
    git push origin main
    ```

## Membuat aplikasi dengan nama main pada proyek tersebut
  - Buka cmd pada direktori utama sayur-shop lalu aktifkan virtual environment dengan perintah `env\Scripts\activate`
  - Buat aplikasi main dengan perintah `python manage.py startapp main`. Direktori ini berisi struktur awal aplikasi Django
  - Buka file settings.py yang berada di dalam direktori proyek sayur-shop
  - Mendaftarkan aplikasi main ke dalam proyek dengan cara menambahkan string `'main'` sebagai elemen paling akhir pada variabel INSTALLED_APPS
  - Buat direktori templates di dalam direktori aplikasi main
  - Di dalam direktori templates buat file html bernama main.html
    Isi dari file main.html yaitu:
    ```
    <h1>Sayur Shop</h1>
    
    <h5>Name: </h5>
    <p>Eva Yunia Aliyanshah</p>
    <h5>Class: </h5>
    <p>PBP C</p>
    ```
  - Coba membuka file main.html di peramban web

## Melakukan routing pada proyek agar dapat menjalankan aplikasi main
  - Konfigurasi routing URL proyek dengan menambahkan rute URL dalam urls.py yang berada di dalam direktori proyek sayur-shop.
    ```
    Impor fungsi include dari django.urls
    ...
    from django.urls import path, include
    ...
    ```
  - Lalu tambahkan rute URL:
      ```python
      urlpatterns = [
          ...
          path('', include('main.urls')),
          ...
      ]
      ```
      Ini berguna untuk mengarahkan ke tampilan main di dalam variabel urlpatterns.
      urls.py pada proyek mengarahkan rute URL tingkat proyek dan dapat mengimpor rute URL dari berkas urls.py dan aplikasi-aplikasi.
      Hal ini memungkinkan aplikasi dalam proyek Django untuk bersifat modular dan terpisah

## Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib name, price, description
  - Buka berkas models.py pada direktori aplikasi main
  - Isi berkas models.py dengan nama Product dan memiliki atribut name, price, description, stock, dan image:
    ```python
    from django.db import models

    class Product(models.Model):
        name = models.CharField(max_length=255)
        price = models.IntegerField()
        description = models.TextField()
        stock = models.IntegerField()
        image = models.ImageField()
    ```
  - Melakukan migrasi model yang berguna melacak perubahan pada model basis data
    Jalankan perintah 'python manage.py makemigrations' untuk membuat migrasi model dan
    perintah 'python manage.py migrate' untuk menerapkan migrasi ke dalam basis data lokal

## Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
  - Buka berkas views.py yang berada di dalam direktori aplikasi main
  - Import fungsi render dari modul django.shortcuts 'from django.shortcuts import render'
  - Tambahkan fungsi show_main berikut:
    ```python
    def show_main(request):
        context = {
            'name': 'Eva Yunia Aliyanshah',
            'class': 'PBP C'
        }
    
        return render(request, "main.html", context)
    ```
    Fungsi ini akan mengatur permintaan HTTP dan mengembalikan tampilan yang sesuai.
    context adalah dictionary yang berisi data untuk dikirimkan ke tampilan.
    return render(request, "main.html", context) berguna untuk me-render tampilan main.html dengan menggunakan fungsi render
  - Melakukan modifikasi pada template main.html agar dapat menampilkan data yang telah diambil dari model.
  - Buka berkas main.html dalam direktori template pada direktori main, lalu ubah nama dan kelas menjadi struktur kode Django yang sesuai untuk menampilkan data
    ```
    <h1>Sayur Shop</h1>

    <h5>Name: </h5>
    <p>{{ name }}</p>
    <h5>Class: </h5>
    <p>{{ class }}</p>
    ```

## Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py
  - Membuat berkas urls.py di dalam direktori aplikasi main
  - Isi file urls.py dengan:
    ```
    from django.urls import path
    from main.views import show_main
    
    app_name = 'main'
    
    urlpatterns = [
        path('', show_main, name='show_main'),
      ]
    ```
    File urls.py pada aplikasi mengatur rute URL spesifik untuk fitur-fitur dalam aplikasi

## Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet
  - Buka website PWS pada https://pbp.cs.ui.ac.id dan lakukan login
  - Pada homepage, klik tombol 'Create New Project'
  - Isi Project Name dengan sayurshop lalu klik tombol 'Create New Project'
  - Akan muncul informasi mengenai Project Credentials dan Project Command. Simpan informasi ini pada notes pribadi
  - Pada settings.py dalam direktori proyek sayur-shop, tambahkan URL deployment PWS pada ALLOWED_HOSTS
    ```
    ...
    ALLOWED_HOSTS = ["localhost", "127.0.0.1", "eva-yunia-sayurshop.pbp.cs.ui.ac.id"]
    ...
    ```
  - Lakukan git add, commit, dan push intuk menyimpan perubahan ini ke repositori Github
    git add .
    git commit -m "adding PWS URL"
    git push -u origin main
  - Jalankan perintah yang terdapat pada informasi Project Command pada halaman PWS
    git remote add pws http://pbp.cs.ui.ac.id/eva.yunia/sayurshop
    git branch -M master
    git push pws master
  - jalankan perintah 'git branch -M main' untuk kembali mengubah nama branch utama menjadi main
  - Klik proyek sayur-shop pada side bar situs PWS. Lihat status deployment proyek.
    Jika 'Building' artinya masih dalam proses deployment
    Jika 'Running' artinya proyek kamu sudah bisa diakses pada URL deployment
    Jika 'Failed' artinya gagal mendeploy proyek

# 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
   ![1](https://github.com/user-attachments/assets/56ca110d-125b-4fa6-b288-a656b016cada)
   - User mengirimkan request ke aplikasi web django dalam bentuk URL
   - File urls.py akan memetakan URL yang diminta oleh pengguna ke fungsi view yang sesuai
   - Setelah menerima request dari urls.py, views melakukan logika seperti mengambil data dari model (database)
   - Setelah menjalankan logika dan memproses data, views.py akan menentukan template HTML mana yang harus ditampilkan pada user
   - View dapat membuat query ke model untuk mendapatkan data yang disimpan di database
   - Lalu data dikembalikan ke view untuk diproses dan ditampilkan
   - Django akan merender template HTML sebagai user interface
   - Setelah template HTML dirender, Django akan mengirimkan respon berupa halaman web ke pengguna berdasarkan data yang diambil dari model dan diproses oleh view
   
    >> Secara singkat, kaitan antara urls.py, views.py, models.py, dan berkas html:
    >> - Pengguna mengakses URL tertentu.
    >> - urls.py memetakan URL tersebut ke fungsi atau kelas di views.py.
    >> - views.py memproses permintaan, mengambil data dari models.py jika diperlukan, dan mengirimkan data tersebut ke template HTML.
    >> - Template HTML merender data menjadi halaman web yang dikirim kembali ke pengguna.

# 3. Jelaskan fungsi git dalam pengembangan perangkat lunak!
   - Git Memungkinkan tim developer berkolaborasi dalam pengembangan perangkat lunak.
     Tim developer dapat mengelola repositori bersama dan menggabungkan perubahan yang dilakukan seluruh anggota tim.
   - Git memungkinkan untuk melakukan branching dan merging.
     Fitur branch berguna untuk pengembangan secara paralel, kita dapat membuat cabang (branch) untuk mengerjakan fitur baru atau perbaikan tanpa mempengaruhi cabang utama (main branch). Setelah pekerjaan selesai, kita dapat menggabungkan perubahan (merge) kembali ke cabang utama.
   - Git memudahkan pengelolaan proyek.
     Git dapat digunakan untuk melakukan code review, yaitu peninjauan kode oleh anggota tim terkait kode yang dikirimkan.
     Selain itu, dengan menggunakan branch untuk setiap fitur atau perbaikan, Git memungkinkan isolasi pengembangan fitur, sehingga kita dapat mengurangi risiko konflik.
   - Git sebagai backup dan penyimpanan terpusat.
     Git menyimpan seluruh riwayat versi dalam repositori lokal dan, jika dikonfigurasi, juga di repositori remote.
     selain itu, Git memiliki kemampuan _Distributed Version Control System_ yang berarti tiap developer memilki salinan lengkap pada repositori komputer mereka. Ini memungkinkan pengembangan offline dan mengurangi risiko kehilangan data.
# 4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
  - Karena Django didasarkan pada python, dimana bahasa ini merupakan bahasa pemrograman tingkat tinggi, dinamis, dan terinterpretasi yang lebih mudah dipelajari oleh _programmer_ pemula.
  - Karena Django merupakan framework yang lengkap karena menyediakan semua fitur yang diperlukan untuk membangun aplikasi yang lengkap secara langsung (filosofi '_Batteries Included_').
  - Django memungkinkan kita untuk menerapkan konsep MVT. Konsep ini memungkinkan pemula untuk mengorganisasi dan mengelola kode dengan lebih terstruktur.
  - Django memiliki dokumentasi yang luas dan komunitas yang besar. Ini sangat membantu bagi pemula yang mungkin sering menghadapi masalah atau memiliki pertanyaan, mereka dapat dengan mudah mencari tutorial, forum diskusi, dan sumber daya untuk dipelajari.
  - Django merupakan framework yang bersifat open source yang berarti bebas untuk diakses, dugunakan, dan dimodifikasi tanpa mengeluarkan biaya untuk membeli lisensi.
# 5. Mengapa model pada Django disebut sebagai ORM?
  - Model pada Django disebut sebagai ORM (Object-Relational Mapping) karena fungsinya sebagai jembatan antara database relasional dan objek dalam kdoe Python.
  - Pada Django memungkinkan pengembang untuk bekerja dengan database tanpa harus menulis SQL.
  - Setiap tabel di database direpresentasikan sebagai kelas model. Tiap kolom pada tabel menunjukkan atribut kelas dan tiap baris merepresentasikan objek dari kelas tersebut.

## Referensi
* DEV. (2021). _Django Web Framework (Python)_. Diakses pada 10 September 2024, dari https://dev.to/ivanadokic/django-web-framework-python-ebn
* Niagahoster. (2022). _Belajar Django, Framework Python yang Kian Populer_. Diakses pada 10 September 2024, dari [https://dev.to/ivanadokic/django-web-framework-python-ebn](https://www.niagahoster.co.id/blog/django-framework/)
* djangostars. (2024). _Top 14 Pros of Using Django for Python Web Development_. Diakses pada 10 September 2024, dari https://djangostars.com/blog/top-14-pros-using-django-web-development/
* biznetgio. (2023). _Mengenal GIT, Definisi, Fungsi, hingga Manfaatnya Bagi Programmer_. Diakses pada 10 September 2024, dari [https://djangostars.com/blog/top-14-pros-using-django-web-development/](https://www.biznetgio.com/news/apa-itu-git)
