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

# Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
- Integrasi Data.
  - *Data delivery* memungkinkan integrasi data dari berbagai sumber ke dalam satu platform. Hal ini berguna untuk memastikan semua data yang diperlukan tersedia dan dapat diakses dengan mudah.
- Efisiensi Performa.
  - Dengan *data delivery* yang efektif, inidapat mengurangi latensi sehingga data dapat dikirimkan dengan cepat dan efisien.
- *security and compliance*.
  - *Data delivery* yang baik harus memastikan keamanan data sesuai dengan regulasi yang berlaku. Hal ini berguna untuk malindungi data dari akses tidak sah.
- Pengalaman Pengguna.
  - Jika *data delivery* yang digunakan efisien, maka hal ini akan meningkatkan pengalaman pengguna dengan memberikan respons yang cepat dan meminimalkan waktu tunggu.
 
# Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Lebih baik atau tidaknya antara XML dan JSON tergantung pada kebutuhan. Untuk pengembangan aplikasi web modern dan komunikasi API, JSON lebih baik karena sifatnya yang ringan, sederhana, dan kemudahan dalam integrasi dengan JavaScript. 
Namun, jika proyek memerlukan struktur data yang lebih kompleks, dukungan validasi skema, atau penggunaan atribut dalam elemen data, XML bisa menjadi pilihan yang lebih tepat. XML lebih kompatibel dengan sistem lama dan unggul dalam menangani markup dokumen.
## JSON lebih populer dibandungkan dengan XML karena beberapa alasan yaitu:
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

# Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Method is_valid() digunakan untuk memvalidasi isi input dari form tersebut. Jika form valid, maka akan mengembalikan True, lalu data akan disimpan ke dalam database menggunakan method form.save().

# Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
- `csrf_token` adalah token yang berfungsi sebagai *security*. Token ini di *generate* secara acak oleh Django untuk setiap permintaan form. Token ini ditanamkan ke dalam form dan dikirim bersama data saat form disubmit. Django kemudian memeriksa apakah token ini cocok dengan yang diharapkan (berdasarkan sesi pengguna). Jika token tidak cocok atau tidak ada, permintaan akan ditolak. Ini memastikan bahwa permintaan form benar-benar berasal dari situs yang sama bukan dari situs pihak ketiga yang mencoba memalsukan permintaan pengguna.
- Jika kita tidak menambahkan `csrf_token` pada form Django, aplikasi kita dapat terkena serangan  Cross-Site Request Forgery (CSRF). Ini merupakan sebuah serangan eksploitasi web yang membuat pengguna tanpa sadar mengirim sebuah permintaan atau *request* ke *website* melalui *website* yang sedang digunakan saat itu. Dari situ aplikasi web akan mengeksekusi *request* tersebut yang sebenarnya bukan keinginan dari pengguna.
- Penyerang dapat memanfaaatkan CSRF untuk mengarahkan pengguna ke halaman palsu dengan phising berbentuk pesan atau teks untuk meyakinkan pengguna agar mengklik *exploit*  URL tersebut. URL ini sudah disematkan kode yang berisi perintah tertentu sesuai dengan keinginan dari pelaku. Setelah URL di klik, maka perintah akan langsung berjalan baik itu mengganti password, perintah transfer, atau juga perintah lainnya yang berbahaya. Karena permintaan datang dari sesi pengguna yang valid, server dapat mengeksekusi permintaan tersebut jika tidak ada perlindungan CSRF.

# Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step.
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
## Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.
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
# Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman
1. XML
   ![capturexml](https://github.com/user-attachments/assets/a9bb62ed-6529-4357-b250-2430d57abd10)
2. JSON
   ![capturejson](https://github.com/user-attachments/assets/540c5a61-28e4-451a-9fcc-be618d877fc5)

3. XML by ID
   ![capturexmlid](https://github.com/user-attachments/assets/f15d050b-e1db-49be-9dc3-133df57fc4c1)

4. JSON by ID
   ![capturejsonid](https://github.com/user-attachments/assets/39a56b39-9b09-42a8-b246-72d13e7e0115)


## Referensi
* DEV. (2021). _Django Web Framework (Python)_. Diakses pada 10 September 2024, dari https://dev.to/ivanadokic/django-web-framework-python-ebn
* Niagahoster. (2022). _Belajar Django, Framework Python yang Kian Populer_. Diakses pada 10 September 2024, dari [https://dev.to/ivanadokic/django-web-framework-python-ebn](https://www.niagahoster.co.id/blog/django-framework/)
* djangostars. (2024). _Top 14 Pros of Using Django for Python Web Development_. Diakses pada 10 September 2024, dari https://djangostars.com/blog/top-14-pros-using-django-web-development/
* biznetgio. (2023). _Mengenal GIT, Definisi, Fungsi, hingga Manfaatnya Bagi Programmer_. Diakses pada 10 September 2024, dari [https://djangostars.com/blog/top-14-pros-using-django-web-development/](https://www.biznetgio.com/news/apa-itu-git)
