# Welcome to Ansible
by Aloisius Gonzaga Yovelix Waskita Ardell

## Simple Task
1. [Buatlah sebuah inventory, pada inventory tersebut mendefinisikan daftar variables dan hosts](https://github.com/AloisiusVelix/btj-academy/tree/main/ansible#inventory)
2. [Buatlah satu playbook dengan task menjalankan sebuah doker container dengan kriteria yaitu terdapat image, port dan environtment variables](https://github.com/AloisiusVelix/btj-academy/tree/main/ansible#playbook)

## Inventory
Untuk membuat sebuah inventory, kita dapat menambahkan file inventory.yaml dengan konten sebagai berikut:
```
all:
  hosts:
    btj-academy:
      ansible_host: 10.184.0.100
  vars:
    image: todoapps:v1.1
    name: zaga
```

## Playbook
Untuk membuat playbook untuk menjalankan sebuah docker container yang sudah ada dalam server (todoapps:v1:1), kita dapat menambahkan file playbook.yaml dengan konten:
```
- name: Deploy Docker Container
  hosts: btj-academy
  become: true
  tasks:
    - name: Run Docker Container
      docker_container:
        name: "{{ name }}"
        image: "{{ image }}"
        state: started
        ports:
          - "80"
        env:
          NAME: "{{ name }}"
          IMAGE: "{{ image }}"
        detach: true
        interactive: true
        tty: true
```
Untuk menjalankan tasks dalam playbook.yaml yang merujuk pada inventory.yaml kita dapat menggunakan kode berikut:
```
ansible-playbook -i inventory.yaml playbook.yaml
```

Dengan cara ini, kita berhasil menjalankan docker container todoapps:v1.1 dalam server.

## Tambahan
Untuk menjalankan program di lokal dengan OS Windows yang tidak dapat menjalankan ansible secara langsung, kita dapat membuat docker container yang ketika dijalankan dapat mengeksekusi program-program ansible.

Berikut untuk Dockerfile yang dapat digunakan:
```
FROM ubuntu:latest
ENV ANSIBLE_VERSION 2.9.17
RUN apt-get update; \
    apt-get install -y gcc python3; \
    apt-get install -y python3-pip; \
    apt-get install -y vim telnet; \
    apt-get clean all
RUN pip3 install --upgrade pip; \
    pip3 install "ansible==${ANSIBLE_VERSION}"; \
    pip3 install ansible
```
