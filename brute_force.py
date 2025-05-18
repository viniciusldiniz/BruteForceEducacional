import sys

def brute_force_login(username, wordlist_path, correct_password):
    try:
        with open(wordlist_path, 'r', encoding='utf-8') as f:
            passwords = f.read().splitlines()
    except FileNotFoundError:
        print(f"Arquivo de wordlist '{wordlist_path}' não encontrado.")
        sys.exit(1)

    print(f"🔍 Iniciando ataque brute-force para o usuário '{username}'...
")

    for attempt, password in enumerate(passwords, 1):
        print(f"Tentativa {attempt}: {password}")
        if password == correct_password:
            print(f"✅ Senha encontrada: '{password}'")
            return

    print("❌ Senha não encontrada na wordlist.")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Uso: python brute_force.py <usuario> <caminho_da_wordlist> <senha_correta>")
        sys.exit(1)

    username = sys.argv[1]
    wordlist_path = sys.argv[2]
    correct_password = sys.argv[3]

    brute_force_login(username, wordlist_path, correct_password)
