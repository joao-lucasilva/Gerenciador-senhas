import sqlite3

conn = sqlite3.connect('passwords.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS tbl_users (
        service  TEXT NOT NULL,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    );
''')

def menu():
    print('****************************')
    print('*i - inserir nova senha    *')
    print('*l - listar serviços salvos*')
    print('*r - recuperar uma senha   *')
    print('*s - sair                  *')
    print('****************************')

def insert_password(service, username, password):
    cursor.execute(f'''
        INSERT INTO tbl_users (service, username, password)
        VALUES ('{service}','{username}','{password}')
    ''')
    conn.commit()

def show_services():
    cursor.execute('''
        SELECT service FROM tbl_users;
    ''')
    for service in cursor.fetchall():
        print('Serviço: ',service)

def get_passwords(service):
    cursor.execute(f'''
        SELECT username, password FROM tbl_users
        WHERE service = '{service}'
    ''')
    if cursor.rowcount == 0:
        print('Serviço não encontrado')
        print('Use l para verificar os serviços')
    else:
        for user in cursor.fetchall():
            print(user)

while True:
    menu()
    user_option = input('Digite uma opção: ')
    if user_option not in ['l', 'i', 'r', 's']:
        print('Opção inváida! Selecione uma das opções do menu')
        continue
    if user_option == 's':
        break
    if user_option == 'i':
        service = input('Digite o nome do serviço: ')
        username = input('Digite o nome de usuário: ')
        password = input('Digite a senha desse serviço: ')
        insert_password(service, username, password)
        print('Inserido com sucesso!')
    elif user_option == 'l':
        show_services()
    elif user_option == 'r':
        service = input('Digite o serviço: ')
        get_passwords(service)

conn.close()