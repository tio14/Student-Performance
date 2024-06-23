# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut (nama fiktif) merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik.

### Permasalahan Bisnis
Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout. Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Masalah dropout di Jaya Jaya Institut merupakan tantangan yang signifikan yang perlu segera ditangani. Dropout tidak hanya mempengaruhi reputasi institusi tetapi juga berdampak negatif pada perkembangan pribadi dan akademik siswa yang terlibat. Penanganan yang tepat terhadap masalah ini dapat meminimalkan angka dropout dan meningkatkan kesuksesan akademik serta kepuasan siswa.

Salah satu langkah penting dalam mengatasi masalah dropout adalah dengan mengidentifikasi faktor-faktor yang mungkin menyebabkan siswa mengambil keputusan untuk keluar dari institusi. Beberapa faktor umum yang sering menjadi penyebab dropout meliputi masalah keuangan, tekanan akademik yang berlebihan, ketidakcocokan dengan lingkungan belajar, masalah pribadi atau keluarga, serta kurangnya dukungan sosial dan akademik.

Jaya Jaya Institut perlu mengembangkan sistem monitoring yang efektif untuk mendeteksi tanda-tanda awal siswa yang berisiko dropout. Hal ini dapat dilakukan dengan memanfaatkan data historis dan informasi akademik, perilaku belajar, dan interaksi siswa dengan dosen dan rekan-rekan sekelas. Analisis data yang cermat dapat membantu dalam mengidentifikasi pola-pola yang mengarah pada keputusan dropout.

Dengan pendekatan yang holistik dan berkelanjutan terhadap masalah dropout, Jaya Jaya Institut dapat membangun lingkungan pendidikan yang inklusif, mendukung semua siswa dalam mencapai potensi mereka, dan memastikan bahwa setiap siswa memiliki kesempatan yang adil untuk sukses dalam pendidikan mereka. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.

### Cakupan Proyek
- Mengidentifikasi faktor-faktor yang mempengaruhi siswa untuk melakukan dropout.
- Membuat aksi rekomendasi berdasarkan analisis data.
- Membuat dashboard untuk memudahkan stackholder dalam memahami data dan memantau performa siswa.
- Membuat solusi machine learning yang siap digunakan.

### Persiapan
Sumber data: [Student's Performance](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/README.md)

Setup environment:
```
conda create --name [env]
conda activate [env]
conda install --yes --file requirements.txt
```
Change "[env]" with your "environment_name"

## Business Dashboard
Terdapat Dashboard yang dapat diakses melalui [link berikut](https://student-performance-qf7phu8nvpyrv7r2cfmgku.streamlit.app/). Dashboard tersebut dapat digunakan untuk menganalisa data dengan melihat berbagai faktor yang diperkirakan mempengaruhi siswa untuk tidak menuntaskan studi (dropout). Terdapat dua menu utama yakni Dashboard dan Predict. 

Pada **menu Dashboard**, anda dapat melihat dan memonitor berbagai faktor tersebut. Terdapat filter berdasarkan Course pada bagian atas dashboard, sehingga anda dapat memfokuskan analisis pada satu atau beberapa course tertentu.

## Menjalankan Sistem Machine Learning
Sistem prediksi dari Machine Learning dapat diakses melalui komputer lokal dengan mengikuti petunjuk di bawah. Anda juga dapat mengaksesnya pada [link dashboard](https://student-performance-qf7phu8nvpyrv7r2cfmgku.streamlit.app/) yang telah disebutkan sebelumnya dengan membuka **menu Predict**.

```
conda activate [env]
streamlit run app.py
```

## Conclusion
Tingkat dropout dari institusi pendidikan ini terbilang cukup tinggi. Dengan perbandingan 2:3 dari siswa yang lulus. Jurusan (course) dengan tingkat dropout cukup tinggi terjadi pada jurusan management. Siswa yang mendaftar pada umur lebih dari 23 tahun berpotensi besar untuk tidak dapat menyelesaikan studi. 

Siswa yang menunggak membayar biaya kuliah berpeluang sangat tinggi untuk dropout. Faktanya 95% dari siswa yang menunggak mengalami dropout. Pada umumnya nilai siswa pada semester 1 tidak begitu berbeda dengan nilai pada semester 2. Siswa dengan perbedaan nilai pada semester 1 dan semester 2 cenderung tidak dapat menyelesaikan studinya.

### Rekomendasi Action Items
Berikut beberapa aksi yang direkomendasikan:
- Siswa yang berumur lebih dari 23 tahun saat mendaftar perlu lebih diperhatikan, karena mereka berpotensi tinggi untuk dropout. 
- Siswa yang menunggak membayar uang kuliah dapat dipanggil untuk melakukan konseling. Mungkin mereka memiliki masalah ekonomi dan beasiswa dapat menjadi solusi bagi mereka.
- Dosen akademik disarankan untuk memanggil siswa yang mengalami perubahan nilai yang cukup signifikan. Terutama saat nilai siswa menurun dibandingkan dengan nilai  semester sebelumnya.