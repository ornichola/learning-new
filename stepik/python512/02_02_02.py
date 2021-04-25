"""
[STEPIK]
Python: основы и применение https://stepik.org/512
02_02_01 Ошибки и исключения
"""

"""
Алиса владеет интересной информацией, которую хочет заполучить Боб.
Алиса умна, поэтому она хранит свою информацию в зашифрованном файле.
У Алисы плохая память, поэтому она хранит все свои пароли в открытом виде в текстовом файле.

Бобу удалось завладеть зашифрованным файлом с интересной информацией и файлом с паролями, но он не смог понять 
какой из паролей ему нужен. Помогите ему решить эту проблему.

Алиса зашифровала свою информацию с помощью библиотеки simple-crypt.
Она представила информацию в виде строки, и затем записала в бинарный файл результат работы метода simplecrypt.encrypt.

Вам необходимо установить библиотеку simple-crypt, и с помощью метода simplecrypt.decrypt узнать, к
акой из паролей служит ключом для расшифровки файла с интересной информацией.

Ответом для данной задачи служит расшифрованная интересная информация Алисы.

Файл с информацией  # -> 
Файл с паролями     # -> 

Примечание:
Для того, чтобы считать все данные из бинарного файла, можно использовать, например, следующий код:
with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()
"""


import simplecrypt

with open('02_02_02_passwords.txt', 'r') as f:
    passwords = f.read().splitlines()

decrypts = list()
with open('02_02_02_encrypted.bin', 'rb') as crypt:
    data = crypt.read()
    for password in passwords:
        try:
            decrypted = simplecrypt.decrypt(password, data)
            break
        except simplecrypt.DecryptionException:
            continue

print(f'Decrypted with password {password}')
print(decrypted)

with open('02_02_02_decrypted.bin', 'wb') as decrypt:
    decrypt.write(decrypted)
