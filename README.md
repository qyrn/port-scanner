# 🔍 Port Scanner

## 📄 Description

Scanner de ports en Python qui détecte les ports ouverts sur une cible et tente de récupérer le banner des services.

## 🚀 Usage

```
python3 scanner.py --host ... --start . --end ....
```

## 💡 Exemples

```
> python3 scanner.py --host scanme.nmap.org --start 1 --end 1024

Port 22 ouvert
Port 80 - Banner: HTTP/1.1 200 OK
...
Date: Sun, 22 Mar 2026 15:27:18 GMT
Server: Apache/2.4.7 (Ubuntu)
Accept-Ranges: bytes
Vary: Accept-Encoding
Connection: close
Content-Type: text/html