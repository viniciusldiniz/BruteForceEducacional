# 🔐 Brute Force Educacional

Este é um script **educacional** que simula um ataque de força bruta para encontrar uma senha a partir de uma wordlist.

## 🚀 Como Usar

### 1. Pré-requisitos

- Python 3.x
- Um arquivo `.txt` com uma lista de senhas (uma por linha)

### 2. Executando o script

```bash
python brute_force.py <usuario> <caminho_da_wordlist> <senha_correta>
```

#### Exemplo:

```bash
python brute_force.py admin wordlist.txt 123456
```

## 📌 Exemplo de Saída

```
🔍 Iniciando ataque brute-force para o usuário 'admin'...

Tentativa 1: admin
Tentativa 2: password
Tentativa 3: 123456
✅ Senha encontrada: '123456'
```

## ⚠️ Aviso Legal

> Este script é apenas para **fins de aprendizado**.  
> Não utilize em sistemas reais sem autorização.  
> O uso indevido pode ser considerado crime de invasão de dispositivo ou rede.

## 📄 Licença

Distribuído sob a licença MIT.
