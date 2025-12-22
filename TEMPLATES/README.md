# TEMPLATES UNTUK SETUP WARUNG

File-file template untuk memudahkan input data ke Odoo.

## Cara Menggunakan:

### 1. PRODUK (01_IMPORT_PRODUK_TEMPLATE.csv)
1. Buka file di Excel atau Google Sheets
2. Edit data produk warung Anda (nama, harga, stok, dll)
3. SAVE
4. Di Odoo: Product > Import > Upload file ini
5. Map columns jika ada yang berbeda
6. Klik "Import"

### 2. CHART OF ACCOUNTS (02_CHART_OF_ACCOUNTS_TEMPLATE.csv)
1. Buka file di Excel
2. Adjust account codes sesuai kebutuhan
3. SAVE
4. Di Odoo: Accounting > Configuration > Chart of Accounts
5. Buat accounts sesuai template ini

### 3. SUPPLIER (03_SUPPLIER_TEMPLATE.csv)
1. Buka file di Excel
2. Edit supplier data Anda
3. SAVE
4. Di Odoo: Contacts > Import > Upload file ini
5. Klik "Import"

## NOTES:
- Gunakan format CSV (comma-separated)
- Encoding: UTF-8 (untuk karakter Indonesia)
- Hindari cell dengan "," langsung (gunakan quotes)
- Backup original file sebelum dimodifikasi

---
Created: December 2025
Version: 1.0
