# To-Do List App

import json


def add_task():
    new_task = input("Masukkan task baru anda: ")
    print("Untuk prioritas task dapat anda dapat mengisi dengan : high/low/medium")
    task_prio = input("Masukkan prioritas task anda: ")
    task = {
        'nama' : new_task,
        'prio' : task_prio,
        'status' : "to do"
    }

    with open('todo.txt', 'a') as file:
        new_task = json.dumps(task)
        file.write(new_task + "\n")

def view_task(input):
    with open(input, 'r') as file:
        tasks = file.readlines()
        print("Berikut merupakan To-Do List: ")
        for task in tasks:
            temp = json.loads(task)
            print("Nama: ", temp['nama'], "|", "Prioritas: ", temp['prio'], "|", "Status: ", temp["status"])
    
def delete_task():
    delete_task = input('Masukkan nama task yang ingin anda hapus: ')
    with open('todo.txt', 'r') as file:
        tasks = file.readlines()
        for task in tasks:
            temp = json.loads(task)

            if temp['nama'] == delete_task:
                tasks.remove(task)
                break
    with open('todo.txt', 'w') as new_file:
        new_file.writelines(tasks)
    print(f"Berhasil menghapus task {delete_task} !")
    view_task("todo.txt")

def change_status():
    view_task("todo.txt")
    change_task = input('Masukkan nama task yang statusnya ingin anda rubah: ')
    with open('todo.txt', 'r') as file:
        tasks = file.readlines()
        all_tasks = []
        status = ""
        for task in tasks:
            temp = json.loads(task)

            if temp['nama'] == change_task:
                if temp['status'] == "to do":
                    temp['status'] = "in progress"
                    status = "in progress"
                elif temp['status'] == "in progress":
                    temp['status'] = "finished"
                    status = "finished"
                else:
                    temp['status'] = "finished"
                    status = "finished"
            
            all_tasks.append(json.dumps(temp) + "\n")

    with open('todo.txt', 'w') as new_file:
        new_file.writelines(all_tasks)
    print(f"Anda berhasil mengubah status task {change_task} menjadi {status}")  
    view_task("todo.txt")

def filter_task():
    print("Untuk prioritas task dapat anda dapat mengisi dengan : to do/in progress/finished")
    choose_task = input('Masukkan task berdasarkan status task: ')
    with open('todo.txt', 'r') as file:
        tasks = file.readlines()
        choosen_tasks = []
        for task in tasks:
            temp = json.loads(task)

            if temp['status'] == choose_task:
                choosen_tasks.append(json.dumps(temp) + "\n")
    with open('filter.txt', 'w') as new_file:
        new_file.writelines(choosen_tasks)
    view_task('filter.txt')

def presentase_task():
    with open('todo.txt', 'r') as file:
        tasks = file.readlines()
        count_task = 0
        for task in tasks:
            temp = json.loads(task)

            if temp['status'] == "finished":
                count_task += 1
        
        presentase = count_task / len(tasks) * 100
    print(f"Presentase task yang telah selesai adala {presentase} %")
    

while True:
    print("")
    print("Selamat daatang di aplikasi To-Do List")
    print("Silahkan memilih mode yang ada di bawah ini")
    print("1. Menambahkan task")
    print("2. Menampilkan task")
    print("3. Menghapus task")
    print("4. Mengganti status task")
    print("5. Filter task sesuai status")
    print("6. Presentase task yang sudah selesai")
    print("7. Keluar dari aplikasi")

    mode = input("Masukkan mode yang anda pilih: ")
    if mode == "1":
        add_task()
    elif mode == "2":
        view_task("todo.txt")
    elif mode == "3":
        delete_task()
    elif mode == "4":
        change_status()
    elif mode == "5":
        filter_task()
    elif mode == "6":
        presentase_task()
    elif mode == "7":
        print("Terimakasi!")
        break
    else:
        print("Anda harus memasukka nilai antara 1-5")
