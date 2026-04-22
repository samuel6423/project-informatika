# Project Informatika

## Introduction

This project serves as a comprehensive resource for understanding key concepts in computer science and information technology. It aims to provide insights into various topics through examples and explanations. 

## Features
- Data structures and algorithms
- Programming languages
- Software development methodologies

## Ako spustiť a používať stránku

### 1. Spustenie lokálneho servera
Pre správne fungovanie aplikácie je potrebné spustiť Flask server, ktorý spracováva požiadavky na generovanie obrázkov a prepojenie s backendom (`ves.py`).

1. Otvorte terminál (príkazový riadok) v priečinku s projektom.
2. Aktivujte virtuálne prostredie, ktoré sa nachádza v priečinku `venv`:
   - Na Linuxe/macOS: `source venv/bin/activate`
   - Na Windows: `venv\Scripts\activate`
3. Následne spustite server zadaním príkazu:
   ```bash
   python server.py
   ```
4. V termináli by sa mala zobraziť správa, že server úspešne beží: `Server beží na adrese: http://127.0.0.1:5000`

### 2. Otvorenie webovej stránky
1. Otvorte váš preferovaný webový prehliadač.
2. Do adresného riadku zadajte nasledujúcu lokálnu adresu:
   ```
   http://127.0.0.1:5000
   ```

### 3. Používanie stránky
1. Po načítaní stránky sa vám zobrazí unikátne vizuálne prostredie s padajúcimi znakmi Matrixu.
2. V závislosti od politiky vášho prehliadača sa môže spustiť **hudba na pozadí**. Ak prehliadač blokuje automatické prehrávanie (autoplay), hudba začne hrať ihneď po prvej interakcii (napr. kliknutí) so stránkou.
3. Do stredového **textového poľa** napíšte alebo vložte váš kód (príkazy) vo formáte VES.
4. Pre spustenie generovania kliknite na tlačidlo. 
5. Server spracuje zadaný kód a vygenerovaný obrázok sa obratom vizualizuje priamo v rozhraní pod textovým poľom.
