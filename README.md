Link PWS : http://eva-yunia-sayurshop.pbp.cs.ui.ac.id
# Tugas 2
## 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step
### Membuat sebuah proyek Django baru:
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

### Membuat aplikasi dengan nama main pada proyek tersebut
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

#$# Melakukan routing pada proyek agar dapat menjalankan aplikasi main
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

### Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib name, price, description
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

### Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
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

### Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py
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

### Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet
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

## 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
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

## 3. Jelaskan fungsi git dalam pengembangan perangkat lunak!
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
## 4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
  - Karena Django didasarkan pada python, dimana bahasa ini merupakan bahasa pemrograman tingkat tinggi, dinamis, dan terinterpretasi yang lebih mudah dipelajari oleh _programmer_ pemula.
  - Karena Django merupakan framework yang lengkap karena menyediakan semua fitur yang diperlukan untuk membangun aplikasi yang lengkap secara langsung (filosofi '_Batteries Included_').
  - Django memungkinkan kita untuk menerapkan konsep MVT. Konsep ini memungkinkan pemula untuk mengorganisasi dan mengelola kode dengan lebih terstruktur.
  - Django memiliki dokumentasi yang luas dan komunitas yang besar. Ini sangat membantu bagi pemula yang mungkin sering menghadapi masalah atau memiliki pertanyaan, mereka dapat dengan mudah mencari tutorial, forum diskusi, dan sumber daya untuk dipelajari.
  - Django merupakan framework yang bersifat open source yang berarti bebas untuk diakses, dugunakan, dan dimodifikasi tanpa mengeluarkan biaya untuk membeli lisensi.
## 5. Mengapa model pada Django disebut sebagai ORM?
  - Model pada Django disebut sebagai ORM (Object-Relational Mapping) karena fungsinya sebagai jembatan antara database relasional dan objek dalam kdoe Python.
  - Pada Django memungkinkan pengembang untuk bekerja dengan database tanpa harus menulis SQL.
  - Setiap tabel di database direpresentasikan sebagai kelas model. Tiap kolom pada tabel menunjukkan atribut kelas dan tiap baris merepresentasikan objek dari kelas tersebut.

# TUGAS 3
## Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
- Integrasi Data.
  - *Data delivery* memungkinkan integrasi data dari berbagai sumber ke dalam satu platform. Hal ini berguna untuk memastikan semua data yang diperlukan tersedia dan dapat diakses dengan mudah.
- Efisiensi Performa.
  - Dengan *data delivery* yang efektif, inidapat mengurangi latensi sehingga data dapat dikirimkan dengan cepat dan efisien.
- *security and compliance*.
  - *Data delivery* yang baik harus memastikan keamanan data sesuai dengan regulasi yang berlaku. Hal ini berguna untuk malindungi data dari akses tidak sah.
- Pengalaman Pengguna.
  - Jika *data delivery* yang digunakan efisien, maka hal ini akan meningkatkan pengalaman pengguna dengan memberikan respons yang cepat dan meminimalkan waktu tunggu.
 
## Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Lebih baik atau tidaknya antara XML dan JSON tergantung pada kebutuhan. Untuk pengembangan aplikasi web modern dan komunikasi API, JSON lebih baik karena sifatnya yang ringan, sederhana, dan kemudahan dalam integrasi dengan JavaScript. 
Namun, jika proyek memerlukan struktur data yang lebih kompleks, dukungan validasi skema, atau penggunaan atribut dalam elemen data, XML bisa menjadi pilihan yang lebih tepat. XML lebih kompatibel dengan sistem lama dan unggul dalam menangani markup dokumen.
### JSON lebih populer dibandingkan dengan XML karena beberapa alasan yaitu:
#### Sintaks yang lebih ringkas dan sederhana
Menggunakan sintaks yang lebih sederhana dengan pasangan key-value. Ini membuat JSON lebih mudah dibaca dan ditulis, baik oleh manusia maupun oleh mesin. Contoh sintaks JSON:
    ```
    {"person": {"name": "John Doe", "age": 30}}
    ```
    Sedangkan  XML memiliki elemen-elemen dengan tag pembuka dan penutup yang cenderung membuatnya lebih panjang dan kompleks.
    Contoh sintaks XML:
    ```
    <person age="30">John Doe</person>
    ```
#### Keterbacaan
Umumnya JSON  lebih mudah dibaca dan dipahami oleh manusia karena formatnya yang lebih sederhana. Sedangkan pada xml memilki struktur tag yang lebih kompleks menjadikannya lebih sulit untuk dibaca terutama pada dokumen yang besar. 
#### Integrasi dengan JavaScript
JSON adalah format data yang secara native didukung oleh JavaScript, sehingga membuatnya sangat cocok untuk pengembangan web dan API yang berbasis JavaScript. JSON bisa langsung diparsing dan digunakan dalam JavaScript tanpa memerlukan tambahan library atau proses tambahan.
#### Dukungan Tipe Data
JSON mendukung tipe data dasar seperti string, angka, array, dan objek, serta lebih sederhana untuk kebanyakan kasus penggunaan umum. JSON langsung mencerminkan struktur data tanpa memerlukan definisi tipe yang eksplisit. Sedangkan XML memerlukan definisi tipe secara eksplisit dan mendukung struktur data yang lebih kompleks, sehingga menjadikannya lebih rumit dan berlebihan untuk penggunaan yang lebih sederhana.
#### Ukuran Data
JSON lebih hemat ruang karena tidak memiliki tag pembuka dan penutup yang rumit seperti XML. Ini membuat data dalam JSON lebih kecil dan lebih cepat ditransfer.

## Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Method is_valid() digunakan untuk memvalidasi isi input dari form tersebut. Saat form menerima data (melalui request POST, misalnya), Django akan memeriksa apakah data tersebut memenuhi semua aturan validasi yang telah ditetapkan di dalam form. Jika semua validasi lulus, is_valid() akan mengembalikan True, yang berarti data dalam form dianggap valid dan siap diproses lebih lanjut. Sebaliknya, jika ada kesalahan dalam validasi, method ini akan mengembalikan False. Setelah is_valid() mengembalikan True, maka data akan disimpan ke dalam database menggunakan method form.save().

## Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
- `csrf_token` adalah token yang berfungsi sebagai *security*. Token ini di *generate* secara acak oleh Django untuk setiap permintaan form. Token ini ditanamkan ke dalam form dan dikirim bersama data saat form disubmit. Django kemudian memeriksa apakah token ini cocok dengan yang diharapkan (berdasarkan sesi pengguna). Jika token tidak cocok atau tidak ada, permintaan akan ditolak. Ini memastikan bahwa permintaan form benar-benar berasal dari situs yang sama bukan dari situs pihak ketiga yang mencoba memalsukan permintaan pengguna.
- Jika kita tidak menambahkan `csrf_token` pada form Django, aplikasi kita dapat terkena serangan  Cross-Site Request Forgery (CSRF). Ini merupakan sebuah serangan eksploitasi web yang membuat pengguna tanpa sadar mengirim sebuah permintaan atau *request* ke *website* melalui *website* yang sedang digunakan saat itu. Dari situ aplikasi web akan mengeksekusi *request* tersebut yang sebenarnya bukan keinginan dari pengguna.
- Penyerang dapat memanfaaatkan CSRF untuk mengarahkan pengguna ke halaman palsu dengan phising berbentuk pesan atau teks untuk meyakinkan pengguna agar mengklik *exploit*  URL tersebut. URL ini sudah disematkan kode yang berisi perintah tertentu sesuai dengan keinginan dari pelaku. Setelah URL di klik, maka perintah akan langsung berjalan baik itu mengganti password, perintah transfer, atau juga perintah lainnya yang berbahaya. Karena permintaan datang dari sesi pengguna yang valid, server dapat mengeksekusi permintaan tersebut jika tidak ada perlindungan CSRF.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step.
### Membuat input form untuk menambahkan objek model pada app sebelumnya.
1. Membuat *file* baru di direktori main bernama `forms.py` untuk membuat struktur `form` yang menerima data Product. 
    Isi dari file `forms.py`
   ```
   from django.forms import ModelForm
   from main.models import Product

   class ProductEntryForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "stock", "rating"]
   ```
   Fields kita isi dengan name, price, description, stock, dan rating bersesuaian dengan yang didefinisikan dalam model pada `models.py`.
2.  Menambahkan import redirect dari modul django.shortcuts, import ProductEntryForm dan mengimport Product pada berkas `views.py`.
3.  Membuat fungsi baru pada file `views.py` bernama `create_product_entry` untuk menghasilkan form yang dapat menambahkan data produk secara otomatis ketika data di submit dari form. Nantinya fungsi ini akan merender sebuah file HTML yang bernama `create_product_entry.html`
4.  Lalu mengubah fungsi `show_main` menjadi:
     ```
     def show_main(request):
      product_entries = Product.objects.all()
  
      context = {
          'name': 'Eva Yunia Aliyanshah',
          'class': 'PBP C',
          'product_entries' : product_entries
      }
  
      return render(request, "main.html", context)
     ```
     Disini kita menambahkan `product_entries = Product.objects.all()` method ini berguna untuk mengambil seluruh objek Product yang tersimpan pada database.
5.  Pada file `urls.py` yang ada pada direktori main kita tambahkan import fungsi `create_product_entry` dan tambahkan path URL ke variabel urlpatterns
    ```
    from django.urls import path
    from main.views import show_main, create_product_entry

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
        path('create-product-entry', create_product_entry, name='create_product_entry'),
    ]
    ```
6.  Membuat file HTML dengan nama `create_product_entry.html` pada direktori main/templates untuk membuat halaman yang memungkinkan pengguna menambahkan entri produk baru melalui form yang dihasilkan oleh Django
7.  Menambahkan kode pada main.html untuk menampilkan data produk dalam format tabel serta membuat tombol “Add New Product Entry”
    ```
    {% extends 'base.html' %}
    {% block content %}
    <h1>Sayur Shop</h1>
    
    <h5>Name: </h5>
    <p>{{ name }}</p>
    <h5>Class: </h5>
    <p>{{ class }}</p>
    
    {% if not product_entries %}
    <p>Belum ada data product pada sayur shop.</p>
    {% else %}
    <table>
      <tr>
        <th>Product Name</th>
        <th>Price</th>
        <th>Description</th>
        <th>Stock</th>
        <th>Rating</th>
      </tr>
    
    
      {% for Product in product_entries %}
      <tr>
        <td>{{Product.name}}</td>
        <td>{{Product.price}}</td>
        <td>{{Product.description}}</td>
        <td>{{Product.stock}}</td>
        <td>{{Product.rating}}</td>
      </tr>
      {% endfor %}
    </table>
    {% endif %}
    
    <br />
    
    <a href="{% url 'main:create_product_entry' %}">
      <button>Add New Product Entry</button>
    </a>
    {% endblock content %}
    ```
   Pada kode tersebut merupakan template yang mewarisi base.html.
   - Jika tidak ada entri produk (`{% if not product_entries %}`), ditampilkan pesan "Belum ada data product pada sayur shop."
   - Jika ada entri produk, ditampilkan dalam bentuk tabel dengan kolom **Nama Produk**, **Harga**, **Deskripsi**, **Stok**, dan **Rating**.
   - Terdapat tombol `Add New Product Entry`  yang mengarahkan pengguna ke halaman `main:create_product_entry`

### Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.
- Setelah input form dan objek model sudah selesai di buat, selanjutnya buat fungsi pada views untuk mengembalikan data dalam bentuk  XML, JSON, XML by ID, dan JSON by ID.
- Import HttpResponse dan Serializer pada views.py. HttpResponse digunakan untuk mengirimkan data dalam format XML atau JSON ketika fungsi show_xml dan show_json dipanggil. serializers digunakan untuk mengubah (serialize) objek query Django menjadi format tertentu seperti XML atau JSON.
- Berikut merupakan fungsi dari masing-masing views:
  ```
  def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

  def show_json(request):
      data = Product.objects.all()
      return HttpResponse(serializers.serialize("json", data), content_type="application/json")
  
  def show_xml_by_id(request, id):
      data = Product.objects.filter(pk=id)
      return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
  
  def show_json_by_id(request, id):
      data = Product.objects.filter(pk=id)
      return HttpResponse(serializers.serialize("json", data), content_type="application/json")
  ```
### Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.
- Setelah membuat fungsi pada views.py, tambahkan import fungsi show_xml, show_json, show_xml_by_id, show_json_by_id pada `urls.py` yang berada pada direktori `main`.
- Tambahkan path url dalam urlpatterns untuk mengakses fungsi yang sudah diimport
  ```
  urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product-entry', create_product_entry, name='create_product_entry'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
  ]
  ```
  Path ini memungkinkan pengguna untuk mengambil data produk dalam format XML atau JSON, baik seluruh produk atau produk tertentu berdasarkan ID yang dimasukkan dalam URL
## Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman
1. XML
   ![capturexml](https://github.com/user-attachments/assets/a9bb62ed-6529-4357-b250-2430d57abd10)
2. JSON
   ![capturejson](https://github.com/user-attachments/assets/540c5a61-28e4-451a-9fcc-be618d877fc5)

3. XML by ID
   ![capturexmlid](https://github.com/user-attachments/assets/f15d050b-e1db-49be-9dc3-133df57fc4c1)

4. JSON by ID
   ![capturejsonid](https://github.com/user-attachments/assets/39a56b39-9b09-42a8-b246-72d13e7e0115)

# Tugas 4
## 1. Apa perbedaan antara HttpResponseRedirect() dan redirect()
Sebenarnya kegunaan antara `HttpResponseRedirect()` dan `redirect()` sama saja yaitu untuk mengalihkan (redirect) ke URL lain. `redirect()` merupakan _shortcut_ atau _helper function_ dari `HttpResponseRedirect()`. Namun perbedaannya terletak pada argumen yang dapat diterima. `HttpResponseRedirect()` hanya dapat menerima argumen berupa URL saja, sedangkan `redirect()` dapat menerima model, view, atau url.

## 2. Jelaskan cara kerja penghubungan model Product dengan User!
Di dalam file models.py, kita harus menghubungkan model Product dengan model User menggunakan ForeignKey, yang memungkinkan setiap produk terkait dengan pengguna tertentu. Misalnya:
```
user = models.ForeignKey(User, on_delete=models.CASCADE)
```
Cara kerja:
* Field `user = models.ForeignKey(User, on_delete=models.CASCADE)` membuat hubungan satu-ke-banyak antara `Product` dan `User`. Artinya, setiap produk dihubungkan dengan seorang user tertentu, dan satu user bisa memiliki banyak produk.
* `on_delete=models.CASCADE` berarti jika pengguna dihapus, maka semua produk yang terkait dengan pengguna tersebut juga akan dihapus dari database.
Saat membuat produk baru, kita perlu memastikan bahwa produk tersebut terkait dengan pengguna yang sedang login. Di dalam file views.py, kita mengubah kode pada fungsi create_product_entry
```
product_entry = form.save(commit=False)
product_entry.user = request.user
product_entry.save()
```
Cara kerja:
* `commit=False` digunakan untuk membuat objek produk dari form tanpa langsung menyimpannya ke database.
* Setelah itu, field `user` diisi dengan `request.user`, yaitu user yang sedang terotorisasi atau sedang login.
* Setelah user ditetapkan, objek disimpan ke database menggunakan `product.save()`.
Agar pengguna hanya melihat produk yang mereka buat sendiri, filter produk berdasarkan user yang sedang login dengan menambahkan value `user=request.user` pada product_entries pada fungsi show_main, lalu tambahkan `'name': request.user.username,` pada context
```
def show_main(request):
    product_entries = Product.objects.filter(user=request.user)

    context = {
         'name': request.user.username,
         ...
    }
```
Cara kerja:
* `Product.objects.filter(user=request.user)` hanya mengambil produk yang dimiliki oleh pengguna yang sedang login.
* Field `request.user.username` digunakan untuk menampilkan nama pengguna yang sedang login di halaman list.
Karena kita melakukan perubahan pada file models, maka kita harus melakukan migrasi model. Proses `makemigrations` akan membuat file migrasi untuk menambahkan hubungan ForeignKey ke model `Product`. `migrate` akan menerapkan perubahan tersebut ke dalam database.

Untuk mengecek apakah kita sudah berhasil menghubungkan model Product dengan User kita dapat menjalankan server dan membuat akun baru serta login. Selanjutnya membuat produk dan lihat apakah produk yang kita buat hanya muncul pada akun pengguna yang sesuai.

## 3. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
### Perbedaan antara authentication dan authorization
Authentication merupakan proses untuk memverifikasi identitas pengguna. Server akan mengecek siapa user yang saat ini sedang login. Contohnya pada saat pengguna melakukan login, setelah otentikasi berhasil, pengguna diaggap "authenticated" atau terverifikasi. Sedangkan Authorization merupakan proses untuk memeriksa apakah pengguna memiliki izin atau hak akses terhadap data atau aksi tertentu. Pengguna yang berhasil login mungkin diizinkan untuk melihat halaman profil mereka, tetapi mungkin tidak diizinkan untuk mengakses halaman admin.
### apakah yang dilakukan saat pengguna login?
* Login merupakan proses authentication. Ketika pengguna memasukkan username dan password, Django memverifikasi apakah kredensial tersebut benar. Jika valid, pengguna dianggap terautentikasi, dan Django akan membuat sesi pengguna (menggunakan cookie).
* Selama sesi ini, pengguna dapat mengakses halaman atau sumber daya yang diizinkan berdasarkan hasil dari pengecekan Authorization.
### Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
1. Authentication pada Django
   * Django menyediakan mekanisme otentikasi bawaan melalui model `User` yang ada di `django.contrib.auth.models`.
   * Fungsi login di Django menggunakan `authenticate` dan `login` yang disediakan oleh Django untuk memverifikasi pengguna dan mengelola sesi.
   * `authenticate` digunakan untuk memverifikasi kombinasi username dan password. Jika cocok, `login` digunakan untuk memulai sesi dengan menyimpan informasi pengguna yang terautentikasi.
3. Authorization pada Django
   * Django menggunakan permissions dan groups untuk mengatur hak akses atau otorisasi.
   * Django juga menyediakan dekorator seperti @login_required untuk membatasi akses ke halaman tertentu hanya kepada pengguna yang sudah login (authenticated).

## 4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
Django mengingat pengguna yang telah login menggunakan sesi dan cookies. Sesi digunakan untuk melacak informasi terkait pengguna yang sedang login. Setelah pengguna telah terautentikasi, maka Django akan membuat *session record* di server dan menghubungkan sesi tersebut dengan pengguna yang terautentikasi. Tiap pengguna memiliki *session* ID yang unik. Setelah itu, *session* ID disimpan dalam sebuah cookie yang dikirimkan ke browser pengguna atau yang disebut sebagai *session cookie*. Setiap kali pengguna mengirimkan permintaan baru (misalnya membuka halaman lain), browser akan mengirim kembali cookie tersebut ke server, dan Django menggunakan session ID yang ada di cookie untuk mencari data sesi pengguna di server. Jika session ID cocok, Django tahu bahwa pengguna tersebut masih terautentikasi.

### Kegunaan lain dari cookie
* Melakukan personalisasi konten situs web untuk pengguna, seperti menampilkan produk atau penawaran tertentu berdasarkan riwayat penelusuran mereka.
* Mengingat preferensi pengguna, seperti bahasa atau ukuran font, untuk meningkatkan pengalaman *browsing* mereka.
* Melacak perilaku pengguna, seperti halaman mana yang mereka kunjungi atau berapa lama mereka berada di situs web, untuk membantu pemilik situs web memahami audiens mereka dengan lebih baik.
* Menyimpan pengaturan website - cookie akan mengingat preferensi pengaturan yang pengguna terapkan pada suatu situs web. Misalnya pengaturan terkait bahasa atau notifikasi.

### Apakah semua cookies aman digunakan?
Tidak semua cookie aman digunakan. Meskipun cookie dapat menyediakan banyak manfaat, mereka juga dapat menimbulkan risiko keamanan dan privasi jika tidak digunakan dengan benar.
Beberapa risiko potensial terkait dengan cookie:
* Risiko keamanan : Cookie bisa saja rentan terjadap peretasan dan eksploitasi oleh oknum yang tidak bertanggung jawab. Jika cookie tidak terjamin dengan benar, peretas dapat mendapatkan akses ke informasi sensitif/pribadi kita.
* CSRF : Cookie juga bisa menjadi bagian dari serangan **CSRF**, di mana pengguna secara tidak sadar mengirim permintaan berbahaya ke situs web tempat mereka sudah login.
* Third-party Cookies : Cookie ini berasal dari domain selain yang sedang dikunjungi oleh pengguna. Ini sering dimanfaatkan oleh perusahaan iklan untuk melacak pengguna diberbagai situs.

## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
### Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.
#### Mengimplementasikan fungsi registrasi
- Mengaktifkan *virtual environment,* lalu pada `views.py` yang ada pada subdirektori `main` tambahkan *import* `UserCreationForm` dan `messages`.
- Buat fungsi register pada `views.py` yang berfungsi untuk menghasilkan formulir registrasi secara otomatis dan menghasilkan akun pengguna ketika data di-*submit* dari form.
- Membuat berkas HTML bernama `register.html` pada direktori main/templates.
- Mengimpor fungsi register pada *file* `urls.py` yang ada pada subdirektori `main`, lalu tambahkan *path url* ke dalam `urlpatterns` untuk mengakses fungsi yang sudah diimpor.
#### Membuat Fungsi Login
- Tambahkan import `authenticate`, `login`, dan `AuthenticationForm` pada `views.py`
- Buat fungsi `login_user` ke dalam `views.py`. yang berfungsi untuk mengautentikasi pengguna yang ingin *login*.
- Buat berkas HTML dengan nama `login.html` pada direktori `main/templates`
- Mengimpor fungsi login_user pada *file* `urls.py` yang ada pada subdirektori `main`, lalu tambahkan *path url* ke dalam `urlpatterns` untuk mengakses fungsi yang sudah diimpor.
#### Membuat Fungsi Logout
- Tambahkan *import* `logout` pada `views.py`
- Buat fungsi logout_user yang berfungsi untuk melakukan mekanisme logout.
- Menambahkan tombol logout pada berkas `main.html`
- Mengimpor fungsi logout_user pada *file* `urls.py` yang ada pada subdirektori `main`, lalu tambahkan *path url* ke dalam `urlpatterns` untuk mengakses fungsi yang sudah diimpor.
### Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.
- Lakukan register untuk membuat akun pengguna, disini kita membuat 2 akun baru.
- Setelah berhasil register akun, lakukan login dengan menginput *username* dan *password* pada halaman login.
- Buat masing-masing 3 *entry* data per akun menggunakan model yang sudah dibuat sebelumnya.
### Menghubungkan model Product dengan User.
- Pada `models.py` import User dan tambahkan `user = models.ForeignKey(User, on_delete=models.CASCADE)` dalam *class* Product.
- Tambahkan kode berikut pada `views.py` di dalam fungsi `create_product_entry`
  ```
  product_entry = form.save(commit=False)
  product_entry.user = request.user
  product_entry.save()
  ```
- Pada fungsi `show_main` ubah value product_entries menjadi `mood_entries = MoodEntry.objects.filter(user=request.user)` dan tambahkan `'name': request.user.username,` di dalam context.
- Lakukan migrasi model dengan menjalankan perintah `python manage.py makemigrations` dan `python manage.py migrate`
- Pada `settings.py` import os dan ubah variabel DEBUG dengan `DEBUG = not PRODUCTION` dan tambahkan `PRODUCTION = os.getenv("PRODUCTION", False)`
### Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.
- Tambahkan *import* `login_required` pada `views.py`  dan dekorator `@login_required(login_url='/login')` diatas fungsi `show_main` untuk meretriksi akses halaman main
- Tambahkan pula import `HttpResponseRedirect`, `reverse`, dan `datetime`
- Pada fungsi `login_user`, tambahkan fungsionalitas menambahkan *cookie* yang bernama `last_login` untuk melihat kapan terakhir kali pengguna melakukan *login*. Caranya adalah dengan mengganti kode yang ada pada blok `if form.is_valid()` seperti ini:
  ```
  def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
  ```
- Tambahkan `'last_login': request.COOKIES['last_login'],` pada fungsi `show_main` di dalam variabel `context`.
- Ubah fungsi `logout_user` menjadi:
  ```
  def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
  ```
- Pada *file* `main.html` tambahkan `<h5>Sesi terakhir login: {{ last_login }}</h5>` setelah tombol *logout* untuk menampilkan data *last login*
- Runserver menggunakan perintah `python manage.py runserver`

# Tugas 5
## 1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
1. **Inline styles**: Gaya yang diterapkan langsung pada elemen HTML menggunakan atribut **`style`**. Ini memiliki prioritas tertinggi dengan nilai specificity 1000.
2. **ID selector**: Selector yang menggunakan ID elemen, misalnya **`#header`**. Ini memiliki nilai specificity 100.
3. **Class selector**: Selector yang menggunakan kelas, misalnya **`.menu`**, serta pseudo-class dan attribute selector. Ini memiliki nilai specificity 10.
4. **Element selector**: Selector yang menggunakan nama elemen, misalnya **`p`** atau **`h1`**. Ini memiliki nilai specificity 1

## 2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
- **Meningkatkan Pengalaman Pengguna**: Dengan responsive design, situs web dapat menyesuaikan tampilannya sesuai dengan ukuran layar perangkat yang digunakan, baik itu desktop, tablet, atau smartphone. Ini membuat pengguna dapat dengan mudah membaca informasi/tampilan yang ada pada website kita.
- **Efisiensi Biaya**: Mengembangkan satu versi situs web yang responsif lebih efisien dibandingkan membuat versi terpisah untuk desktop dan mobile. Ini bisa mengurangi biaya pemeliharaan dan pengembangan sebuah website.
- **SEO (Search Engine Optimization):** Google memberikan peringkat lebih tinggi pada situs web yang mobile-friendly. Dengan responsive design, situs web kita lebih berpeluang untuk muncul di hasil pencarian yang lebih tinggi yang dapat meningkatkan visibilitas dan trafik website.
- **Meningkatkan fungsional situs web**: Dengan banyaknya variasi ukuran layar yang tersedia (ponsel, tablet, laptop, monitor besar), responsive design memastikan situs web tetap terlihat baik dan fungsional pada semua resolusi tersebut.
Contoh Aplikasi yang Sudah Menerapkan Responsive Design:
Google: Semua layanan Google, termasuk mesin pencari, Gmail, dan Google Drive, menggunakan responsive design untuk memastikan pengalaman pengguna yang konsisten di semua perangkat.
X: Platform media sosial ini juga menggunakan responsive design untuk memberikan pengalaman pengguna yang optimal di desktop dan perangkat mobile.

Belum Menerapkan Responsive Design:
Beberapa Situs Web Lokal: Masih ada banyak situs web lokal di Indonesia seperti situs web pemerintah yang belum menerapkan responsive design, sehingga tampilan mereka tidak optimal ketika diakses melalui perangkat mobile.

## 3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
### **1. Margin**
Margin mengontrol ruang di luar batas (border) elemen, memisahkan elemen dari elemen lain di sekitarnya, sehingga menambah jarak antar elemen. Ini membuat tata letak yang lebih teratur dan mencegah elemen saling bertumpukan.
**Contoh Implementasi**
```
cssmargin: 10px; */* Menambahkan margin sebesar 10 piksel di semua sisi */*
```
### **2. Border**
Border adalah garis yang mengelilingi konten elemen HTML, memberikan batas visual yang jelas di sekitar elemen tersebut. Ini dapat membantu kita untuk menyajikan data dengan visual yang lebih jelas.
**Contoh Implementasi**
```
cssborder: 1px solid black; */* Menambahkan border 1 piksel dengan garis solid berwarna hitam */*
```
### **3. Padding**
Padding mengatur ruang di dalam batas (border) elemen, menciptakan jarak antara konten dan batas. Ini membuat konten lebih mudah dibaca dan tidak terlalu dekat dengan border, memberikan tampilan yang lebih bersih.
**Contoh Implementasi**
```
csspadding: 10px; */* Menambahkan padding sebesar 10 piksel di semua sisi */*
```
## 4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
### 1. Flex Box (Flexible Box)
Flex Box adalah sebuah mode pengaturan layout pada CSS yang digunakan untuk mengatur elemen atau container beserta item didalamnya pada halaman web. Flex Box memungkinkan kita untuk membuat struktur layout yang responsif dan fleksibel tanpa menggunakan float atau positioning.
Kegunaan Flex Box:
* Mengatur Elemen Responsif: Flex Box memungkinkan kita untuk mengatur elemen-elemen dalam satu baris atau kolom, serta membuat mereka responsif terhadap perubahan ukuran layar.
* Pengaturan Aligment: Flex Box menyediakan berbagai properti untuk mengatur aligment elemen, seperti flex-direction, justify-content, dan align-items.
* Mengatasi Ruang Kosong: Flex Box dapat mengatasi ruang kosong dengan menggunakan properti flex-wrap untuk membuat elemen-elemen yang tidak muat dalam satu baris ke baris berikutnya.

Contoh Implementasi:
```
<div class="container">
  <div>Item 1</div>
  <div>Item 2</div>
  <div>Item 3</div>
</div>

.container {
  display: flex;
  flex-direction: row; /* Default: row */
  justify-content: space-between; /* Distribusi ruang di antara item */
}
```
### 2. Grid Layout
Grid Layout adalah sebuah mode pengaturan layout pada CSS yang memungkinkan kita untuk membuat struktur grid yang kompleks dan responsif. Grid Layout memungkinkan kita untuk mengatur elemen-elemen dalam grid yang terdiri dari baris dan kolom.
Kegunaan Grid Layout:
* Mengatur Struktur Grid: Grid Layout memungkinkan kita untuk membuat struktur grid yang kompleks dengan menggunakan properti seperti grid-template-columns dan grid-template-rows.
* Pengaturan Elemen: Grid Layout memungkinkan kita untuk mengatur elemen-elemen dalam grid dengan menggunakan properti seperti grid-column dan grid-row.
* Responsif: Grid Layout dapat membuat struktur grid yang responsif terhadap perubahan ukuran layar.

Contoh Implementasi:
```
<div class="grid-container">
  <div class="grid-item">Item 1</div>
  <div class="grid-item">Item 2</div>
  <div class="grid-item">Item 3</div>
</div>

.grid-container {
  display: grid;
  grid-template-columns: repeat(3, 1fr); /* Tiga kolom dengan ukuran sama */
  grid-template-rows: repeat(2, 100px); /* Dua baris dengan ukuran 100px */
}
```

## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step
### Implementasi fungsi untuk menghapus dan mengedit product
* Buat fungsi delete_product pada views.py yang ada pada subdirektori main yang menerima parameter request dan id pada urls.py yang ada pada folder main import fungsi delete_product dan tambahkan path url
  ```
  path('delete/<uuid:id>', delete_product, name='delete_product'),
  ```
* pada file main.html kita menambahkan kode ini
  ```
  <td>
        <a href="{% url 'main:edit_product' Product.pk %}">
            <button>
                Delete
            </button>
        </a>
    </td>
  ```
* Selanjutnya buat fungsi edit_product pada views.py yang ada pada subdirektori main yang menerima parameter request dan id
* Tambahkan import reverse dan HttpResponseRedirect pada views.py
* Buat file HTML baru dengan nama `edit_product.html`
* Setelah itu tambahkan juga fungsi  `edit_product` dan path url fungsi tersebut
  ```
  path('edit-product/<uuid:id>', edit_product, name='edit_product'),
  ```
* Lalu tambahkan potongan kode berikut di main.html
  ```
  <tr>
      ...
      <td>
          <a href="{% url 'main:edit_product' Product.pk %}">
              <button>
                  Edit
              </button>
          </a>
      </td>
  </tr>
  ```
### Kustomisasi desain pada template HTML yang telah dibuat pada tugas-tugas sebelumnya menggunakan CSS atau CSS framework (seperti Bootstrap, Tailwind, Bulma)
* Buatlah file global.css di /static/css pada root directory
* Agar style CSS yang ditambahkan di global.css dapat digunakan dalam template Django, kita perlu menambahkan file tersebut ke base.html.
* Menambahkan custom styling ke global.css
* Selanjutnya saya melakukan styling menggunakan tailwind pada main.html, login.html, register.html, edit_product.html, create_product_entry.html, card_product.html, card_info.html
### Membuat navigation bar
* agar navigation bar menjadi responsive, kita juga melakukan pengaturan untuk device mobile
* Ini merupakan tampilan web saya yang sudah di settings agar responsive
  ![image](https://github.com/user-attachments/assets/90cd9781-9dd2-4db8-ab90-68fa1df3a8b9)

# Tugas 6
## 1. Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!
- **Menjadikan web kita interaktif.** JavaScript memungkinkan interaksi antarmuka pengguna yang dinamis dan responsif. Dengan JavaScript, kita dapat merespon tindakan pengguna, seperti mengklik tombol, mengisi *form*, memvalidasi input pengguna, menampilkan pesan peringatan, atau memicu tindakan lainnya berdasarkan interaksi pengguna.
- **Manipulasi dan kontrol DOM**. JavaScript memungkinkan manipulasi elemen HTML dan struktur halaman menggunakan DOM (Document Object Model). Kita dapat membuat perubahan pada elemen HTML secara dinamis berdasarkan kondisi atau interaksi pengguna. Contohnya seperti, menambahkan, menghapus, atau memodifikasi elemen HTML.
- **Validasi *form* pada *client-side.*** JavaScript memungkinkan validasi *form* pada *client-side* sebelum data dikirim ke server. Dengan menggunakan JavaScript, kita dapat memberikan umpan balik instan kepada pengguna tentang kesalahan input sebelum data dikirim..
- **Meningkatkan visual website.** JavaScript juga berfungsi untuk membuat animasi, efek visual, dan perubahan tampilan halaman yang menarik. Dengan memanfaatkan bahasa pemrograman ini, kita dapat membuat animasi perpindahan elemen, perubahan warna, efek transparansi, dan masih banyak lagi.
- **Memungkinkan Pemanggilan HTTP AJAX**. JavaScript memungkinkan pemanggilan asinkron ke server menggunakan teknik  AJAX (Asynchronous JavaScript and XML). Dengan AJAX, kita dapat mengambil dan mengirim data ke server tanpa harus memuat ulang seluruh halaman. Hal ini memungkinkan pengembangan aplikasi web yang responsif dan dapat memperbarui konten secara dinamis.

## 2. Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?
Fungsi `await` ketika kita menggunakan `fetch()` berfungsi untuk memastikan JavaScript menunggu hasil dari operasi `async` sebelum melanjutkan eksekusi ke kode berikutnya. 

Jika kita tidak menggunakan `await` pada `fetch()` maka `fetch()` akan langsung mengembalikan *promise* dan kode berikutnya akan dieksekusi sebelum permintaan fetch selesai. Ini bisa jadi menyebabkan kode kita gagal atau tidak berfungsi  seperti yang diharapkan karena kita akan mendapatkan respons promise, bukan dengan hasil respons yang aktual.

## 3. Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST?
Decorator csrf_exempt membuat Django tidak perlu mengecek keberadaan csrf_token pada POST request yang dikirimkan ke fungsi view tersebut. Secara default, Django mengharuskan setiap permintaan POST, PUT, PATCH, dan DELETE yang memodifikasi data dikirim bersama token CSRF. Tetapi, jika kita tidak menyertakan CSRF token dalam request AJAX, Django akan menolak permintaan tersebut dan mengembalikan error, karena mekanisme CSRF protection aktif secara default. maka dari itu kita menggunakan decorator @csrf_exempt pada view yang menangani request AJAX tersebut. 

## 4. Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?
Pembersihan (sanitasi) data input pengguna tidak boleh hanya dilakukan di frontend, tetapi juga sangat penting dilakukan di backend. Alasan utamanya adalah keamanan. Pengguna dapat memanipulasi atau menonaktifkan validasi di frontend melalui alat pengembang pada browser, sehingga memungkinkan mereka mengirimkan data yang berbahaya atau tidak valid ke server. Tanpa pembersihan di backend, aplikasi rentan terhadap serangan seperti SQL Injection atau Cross-Site Scripting (XSS), yang dapat membahayakan sistem. Backend memiliki kontrol penuh dan tidak bisa dimanipulasi oleh pengguna, sehingga validasi di backend memastikan data diproses dengan aman dan konsisten. Selain itu, backend sering menerima permintaan dari berbagai sumber selain frontend resmi, seperti aplikasi mobile atau API pihak ketiga, sehingga validasi di backend menjamin bahwa semua data yang masuk sesuai dengan harapan. Sementara validasi di frontend berguna untuk memperbaiki pengalaman pengguna dengan memberikan respons cepat atas kesalahan input, hal ini tidak bisa dijadikan satu-satunya lapisan perlindungan. Backend juga harus melindungi data yang disimpan di server dan database dari kemungkinan serangan atau data yang tidak sesuai. Oleh karena itu, validasi dan sanitasi di backend wajib dilakukan untuk menjaga keamanan, integritas, dan konsistensi data.

## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
- Menambahkan import pada views.py
  ```
  from django.views.decorators.csrf import csrf_exempt
  from django.views.decorators.http import require_POST
  ```
- Membuat fungsi add_product_entry_ajax pada views.py
- Lalu tambahkan fungsi tersebut pada urls.py dengan mengimport dan menambahkan path pada urlpatterns
- Untuk menampilkan data product entry dengan fetch() API kita menghapus kode ini:
  ```
  product_entries = Product.objects.filter(user=request.user)
  'product_entries': product_entries,
  ```
- Ubah baris pertama pada fungsi `show_json` dan `show_xml` menjadi `data = Product.objects.filter(user=request.user)`
- Pada file main.html hapus bagian _block conditional_ product_entries dan ubah menjadi
  `<div id="product_entry_cards"></div>`
- Buat block <script> di bagian bawah sebelum {% endblock content %}) dan membuat fungsi baru pada block <script> tersebut dengan nama getProductEntries dan refreshProductEntries
- Implementasikan modal (Tailwind) pada aplikasi untuk membuat modal sebagai form untuk menambahkan mood.
- Menambahkan tombol Add New Product Entry by ajax untuk melakukan penambahan data dengan AJAX
- Membuat fungsi addProductEntry untuk menambahkan data berdasarkan input ke basis data secara AJAX
- Menambahkan event listener pada form yang ada di modal untuk menjalankan fungsi addProductEntry
- Untuk melindungi aplikasi dari ross Site Scripting (XSS), kita mengimpor `strip_tags` pada views.py dan forms.py
- Lalu tambahkan juga fungsi `strip_tags` pada data product dan description
  ```
  name = strip_tags(request.POST.get("name"))
  description = strip_tags(request.POST.get("description"))
  ```
- Menambahkan method clean_product dan clean_description pada forms.py
- Bersihkan data dengan DOMPurify dengan menambahkan kode berikut pada block meta yang ada di main.html
  ```
  <script src="https://cdn.jsdelivr.net/npm/dompurify@3.1.7/dist/purify.min.js"></script>
  ```
- Setelah itu menambahkan kode berikut pada refreshProductEntries
  ```
  const name = DOMPurify.sanitize(item.fields.name);
  const description = DOMPurify.sanitize(item.fields.description);
  ```

### Referensi
* DEV. (2021). _Django Web Framework (Python)_. Diakses pada 10 September 2024, dari https://dev.to/ivanadokic/django-web-framework-python-ebn
* Niagahoster. (2022). _Belajar Django, Framework Python yang Kian Populer_. Diakses pada 10 September 2024, dari [https://dev.to/ivanadokic/django-web-framework-python-ebn](https://www.niagahoster.co.id/blog/django-framework/)
* djangostars. (2024). _Top 14 Pros of Using Django for Python Web Development_. Diakses pada 10 September 2024, dari https://djangostars.com/blog/top-14-pros-using-django-web-development/
* biznetgio. (2023). _Mengenal GIT, Definisi, Fungsi, hingga Manfaatnya Bagi Programmer_. Diakses pada 10 September 2024, dari [https://djangostars.com/blog/top-14-pros-using-django-web-development/](https://www.biznetgio.com/news/apa-itu-git)
* Apidog. (2024). _XML vs JSON: A Comprehensive Comparison of Differences_. Diakses pada 16 September 2024, dari https://apidog.com/articles/xml-vs-json/. 
* AWS. (2023). _Apa Perbedaan antara JSON dan XML?_. Diakses pada 16 September 2024, dari https://aws.amazon.com/id/compare/the-difference-between-json-xml/. 
* axway. (2020). _API Formats: Why JSON won over XML_. Diakses pada 16 September 2024, dari https://blog.axway.com/learning-center/apis/api-management/why-json-won-over-xml#why-json-won-over-xml.
* stackoverflow. (2013). _What the difference between using Django redirect and HttpResponseRedirect?_. Diakses pada 25 September 2024, dari https://stackoverflow.com/questions/13304149/what-the-difference-between-using-django-redirect-and-httpresponseredirect
* cmlabs. (2022). _Apa itu Browser Cookie? Pengertian, Fungsi, Jenis, & Isinya_. Diakses pada 25 September 2024, dari https://cmlabs.co/id-id/seo-terms/browser-cookie
