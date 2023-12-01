# Welcome to Flask App Running with Ansible
by Aloisius Gonzaga Yovelix Waskita Ardell

## Clone Repository
Untuk mendapatkan contoh app.py dan requirement.txt nya, kita dapat melakukan clone dari repository sebagai berikut
```
$ git clone https://github.com/rrw-bangunindo/btj-academy
```

## Simple Task
1. [Pada example python app, tambahkan beberapa routing kemudian custom port yang di listen (Default 5000)](https://github.com/AloisiusVelix/btj-academy/blob/main/flask_apps/README.md#custom-route-dan-port-example-python-apps)
2. [Buatlah satu playbook dengan beberapa task yaitu:
a. Menyalin file dari local ke server btj-academy
b. Build docker image untuk example python app
c. Jalankan container yang sudah di build](https://github.com/AloisiusVelix/btj-academy/blob/main/flask_apps/README.md#playbook-to-run-python-apps)

## Custom Route dan Port Example Python Apps
Setelah kita melakukan clone repository, kita akan mengubah routing dan juga port dari app.py sebagai berikut:
```
from flask import Flask
app = Flask(__name__)

@app.route('/Velix')
def hello_velix():
    return 'Hello, Velix!'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5555)
```
Pada program di atas telah dilakukan beberapa perubahan. Route telah diatur ke URL '/Velix'
dan aplikasi akan berjalan di port 5555

## Playbook to Run Python Apps
Selanjutnya kita diarahkan untuk membuat playbook yang akan menjalankan python apps di server btj-academy.bangunindo.io. Pada direktori yang sama kita akan membuat playbook.yaml dan inventory.yaml. Selain itu, kita juga akan membuat Dockerfile untuk build image dan menjalankan app.py dalam container.

```
$ touch inventory.yaml
```
```
$ touch playbook.yaml
```
```
$ touch Dockerfile
```

#### Inventory
Dalam inventory.yaml, kita akan menambahkan beberapa properti sebagai berikut:
```
all:
  hosts:
    btj-academy:
      ansible_host: 10.184.0.100
  vars:
    remote_path: /home/aloisiusgonzaga/python-apps
    local_path: /zaga
    image_name: zaga-apps:latest
    container_name: zagaapps
```
#### Playbook
Dalam playbook.yaml, kita akan menambahkan beberapa properti untuk me-copy file dari direktori lokal kita ke server btj-academy, build image berdasarkan Dockerfile, dan menjalankan container sesuai dengan image yang telah kita buat. Berikut beberapa properti yang diperlukan pada playbook.yaml:
```
- name: Copy, Deploy and Run Flask App with Docker
  hosts: btj-academy
  become: true

  tasks:
    - name: Copy app.py to btj-academy's server
      copy:
        src: "{{ local_path }}/app.py"
        dest: "{{ remote_path }}/app.py"
      become: true

    - name: Copy requirement.txt to btj-academy's server
      copy:
        src: "{{ local_path }}/Dockerfile"
        dest: "{{ remote_path }}/Dockerfile"
      become: true

    - name: Copy Dockerfile to btj-academy's server
      ansible.builtin.copy:
        src: "{{ local_path }}/requirements.txt"
        dest: "{{ remote_path }}/requirements.txt"
      become: true

    - name: Build image for app.py
      docker_image:
        name: "{{ image_name }}"
        build:
          path: "{{ remote_path }}/"
          dockerfile: "{{ remote_path }}/Dockerfile"
          pull: yes
        source: build

    - name: Run docker container
      docker_container:
        name: "{{ container_name }}"
        image: "{{ image_name }}"
        ports:
          - "5555:5555"
        detach: yes
      become: true
```
#### Dockerfile
Dalam Dockerfile, kita akan menambahkan beberapa properti sebagai berikut:
```
FROM python:3.9-alpine

WORKDIR /app

COPY . .

RUN pip install -r requirement.txt

CMD ["python", "app.py"]
```
Setelah semua file dibuat kita dapat menjalankan playbook dengan perintah ansible sebagai berikut:
```
$ ansible-playbook playbook.yaml -i inventory.yaml --user aloisiusgonzaga
```
Setelah semua task berhasil dijalankan kita dapat mengakses hasil dari aplikasi yang kita buat dengan masuk ke https://btj-academy.bangunindo.io:5555/Velix

