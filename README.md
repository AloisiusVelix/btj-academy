# Welcome to To Do Apps
by Aloisius Gonzaga Yovelix Waskita Ardell

## Clone
use this : 
```
git clone https://github.com/AloisiusVelix/btj-academy.git
```

## Simple Task
* [Buatlah image dari aplikasi sederhana yang sudah dibuat.](https://github.com/AloisiusVelix/btj-academy/buat-image)
* [Jalankan image tersebut sebagai container dan berjalan pada port 8081](https://github.com/AloisiusVelix/btj-academy/jalankan-image)
* [Berapakah IP docker container whoami?](https://github.com/AloisiusVelix/btj-academy/IP-whoami)
* [Apa isi dari file yang tersembunyi dari docker container whoami? Clue: Volume Mounting](https://github.com/AloisiusVelix/btj-academy/hidden-file-whoami)
* [Image apa yang digunakan pada docker container whoami?](https://github.com/AloisiusVelix/btj-academy/image-whoami)

## Buat Image
Masuk ke directory btj-academy, di dalamnya buatlah Dockerfile dengan konten sebagai berikut :
```
FROM python:3.9

WORKDIR /app

COPY . .

EXPOSE 8081

CMD ["python", "todoapps.py"]
```

Selanjutnya untuk membuat image dapat menggunakan kode berikut:
```
docker build -t todoapps:v1.1 .
```

Untuk Mengecek apakah images berhasil dibuat dapat menggunakan kode berikut:
```
docker images
```

## Jalankan Image
Setelah image berhasil dibuat, kita dapat menjalankannya dengan port 8081 dengan kode berikut:
```
 docker run -it -d -p 8081:8081 --name <nama container> todoapps:v1.1
```

Untuk mengetahui container sudah berjalan atau belum dapat menggunakan kode berikut:
```
docker ps
```
## IP Whoami
Pada VM terdapat container dengan nama whoami. Untuk mengetahui IP dari container tersebut dapat menggunakan kode berikut:
```
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' whoami
```
Hasil :
```
172.17.0.2
```

## Hidden File Whoami
Untuk mencari file tersembunyi terlebih dahulu kita mengenerate informasi dari container whoami dengan kode berikut
```
docker inspect f301b98cba61
```
Ditemukan bahwa :
```
"Mounts":  [
	{  
		"Type":  "bind",  
		"Source":  "/home/local/.docker",  
		"Destination":  "/tmp/system",  
		"Mode":  "",  
		"RW":  true,  
		"Propagation":  "rprivate"  
	} 
],
```
Dari sini kita dapat menjelajahi isi dari volume tersebut dengan kode berikut :
```
docker exec -it f301b98cba61 /bin/sh
```
Setelah masuk kita mendapati ternyata terdapat file bernama whoami. Untuk membukanya kita dapat menggunakan kode berikut:
```
cat /tmp/system/whoami
```
Hasil :
```
Oofooni1eeb9aengol3feekiph6fieve
```

## Image Whoami
Untuk melihat image yang digunakan oleh docker container whoami dapat menggunakan kode berikut:
```
docker ps
```
Hasil :
```
secret:aequaix9De6dii1ay4HeeWai2obie6Ei
```
