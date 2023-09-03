from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


Pass = input("what is the master Password? ")
key = load_key()
fer = Fernet(key)

def melihat():
    with open("password.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("user:", user, "| password:", fer.decrypt(passw.encode()).decode(),)

def membuat():
    name = input("Nama Akun: ")
    pwd = input("Password: ")

    with open("password.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")



while True:
    
    mode = input("apakah kamu mau memilih membuat password baru atau melihat password yang sudah ada? (tulis membuat/melihat) press q to quit ").lower()

    if mode == "q":
        break
    if mode == "membuat":
        membuat()
    elif mode == "melihat":
        melihat()
    else:
        print("jawaban tidak dimengerti.")
        continue