# 🚀 QUICK START - SETUP ODOO WARUNG (5 MENIT)

> Panduan cepat untuk mulai setup Odoo POS & Accounting

---

## ⚡ 5 LANGKAH SETUP CEPAT

### Langkah 1: Start Odoo Server (2 menit)

**Terminal di workspace:**
```bash
cd /workspaces/erp-odoo

# Jalankan Odoo dengan database warung_a
python3 odoo-bin -d warung_a --init=point_of_sale,account,stock,pos_sale

# Tunggu sampai muncul:
# [INFO] odoo.service.wsgi_server: Listening on http://0.0.0.0:8069
```

**Atau gunakan script automation:**
```bash
python3 setup_warung.py --db-name warung_a
```

✅ Odoo sudah running di: `http://localhost:8069`

---

### Langkah 2: Login & Setup Company (2 menit)

**Buka browser:**
```
URL: http://localhost:8069
Login: admin / admin
Database: warung_a
```

**Setup Company:**
1. Settings → Companies
2. Edit "My Company"
3. Ubah:
   - Name: `[NAMA WARUNG ANDA]`
   - Currency: `IDR`
   - Country: `Indonesia`
   - Timezone: `Asia/Jakarta`
4. Save

✅ Company siap

---

### Langkah 3: Import Produk (1 menit)

**Gunakan template yang sudah ada:**
1. Buka file: `/workspaces/erp-odoo/TEMPLATES/01_IMPORT_PRODUK_TEMPLATE.csv`
2. Edit dengan produk warung Anda (bisa di Excel)
3. Save

**Di Odoo:**
1. Point of Sale → Products
2. Klik tombol Import (↓)
3. Upload CSV
4. Map columns jika perlu
5. Klik "Import"

✅ Produk sudah di database

---

### Langkah 4: Setup POS Session (1 menit)

**Buat POS untuk kasir:**
1. Point of Sale → Configuration → POS
2. Klik "New"
3. Isi:
   - POS Name: `Kasir Warung [Nama Anda]`
   - Journal: `Sales`
   - Payment Methods: Enable Cash ✓
4. Save

✅ POS ready untuk digunakan

---

### Langkah 5: Buat User Kasir (1 menit)

**Buat akun untuk setiap kasir:**
1. Settings → Users
2. New
3. Isi:
   - Name: `[Nama Karyawan]`
   - Login: `kasir1` (atau `kasir2`)
   - Email: `kasir@warung.local`
   - Password: Set password
4. Groups: `Point of Sale User`
5. Save

✅ Kasir bisa login

---

## 🎯 VERIFICATION CHECKLIST

Sebelum go-live, pastikan:

```
✓ DATABASE SIAP
  ☐ Database warung_a sudah created
  ☐ Odoo running tanpa error
  ☐ Bisa login dengan admin

✓ COMPANY CONFIGURED
  ☐ Nama warung sudah set
  ☐ Currency = IDR
  ☐ Timezone = Asia/Jakarta

✓ PRODUK TERSEDIA
  ☐ Min. 10 produk sudah di import
  ☐ Harga sudah set
  ☐ Stok sudah input
  ☐ Category sudah organized

✓ POS READY
  ☐ POS Session created
  ☐ Payment methods enabled
  ☐ Receipt printer test (opsional)

✓ USER ACCOUNTS
  ☐ Admin password sudah diganti
  ☐ Min. 2 kasir accounts created
  ☐ Bisa login test sebagai kasir

✓ TEST TRANSACTION
  ☐ Login sebagai kasir
  ☐ Buka POS Session
  ☐ Buat test order 3-5 items
  ☐ Proses payment cash
  ☐ Close session
  ☐ Check laporan harian
```

---

## 📊 HASIL SETELAH SETUP

Setelah 5 langkah ini, Anda punya:

| Komponen | Status | Detail |
|---|---|---|
| **Database** | ✓ Ready | warung_a dengan modules POS, Accounting, Stock |
| **Company** | ✓ Ready | Nama warung, currency, timezone configured |
| **Products** | ✓ Ready | Min. 20 produk, harga, stok di sistem |
| **POS** | ✓ Ready | Kasir siap jalan, payment methods enabled |
| **Users** | ✓ Ready | Admin + min. 2 kasir, login works |
| **Accounting** | ⚠️ Manual | Perlu setup Chart of Accounts (lihat SETUP_WARUNG.md) |
| **Inventory** | ⚠️ Manual | Perlu setup initial stock (lihat SETUP_WARUNG.md) |

---

## 🔧 SETELAH QUICK START

Untuk setup yang lebih lengkap, baca:
- 📖 **[SETUP_WARUNG.md](SETUP_WARUNG.md)** - Panduan lengkap step-by-step
- 👨‍💼 **[PANDUAN_KASIR_SIMPLE.md](PANDUAN_KASIR_SIMPLE.md)** - Training untuk kasir

---

## 🎬 VIDEO SETUP (Jika Ada)

Dokumentasi lengkap dengan screenshot ada di:
```
/workspaces/erp-odoo/SETUP_WARUNG.md (Bagian "STEP BY STEP")
```

---

## 🆘 TROUBLESHOOTING CEPAT

| Issue | Solusi |
|---|---|
| Odoo tidak jalan | Check PostgreSQL running: `sudo service postgresql start` |
| Port 8069 sudah pakai | Kill process: `lsof -ti:8069 \| xargs kill -9` |
| Database error | Drop & recreate: `sudo -u postgres dropdb warung_a && createdb warung_a` |
| Admin password lupa | Reset di database atau create user baru |
| Produk tidak muncul di POS | Check "POS Available" field di product |
| Kasir tidak bisa login | Check password, groups, dan status |

---

## 📝 COMMAND CHEATSHEET

```bash
# Start Odoo
python3 odoo-bin -d warung_a

# Start dengan dev mode
python3 odoo-bin -d warung_a --dev=xml

# Background start
python3 odoo-bin -d warung_a &

# Check port
lsof -i :8069

# Kill Odoo
pkill -f odoo-bin

# Check PostgreSQL
sudo service postgresql status

# Database list
sudo -u postgres psql -l

# Create database
sudo -u postgres createdb warung_a --encoding UTF8

# Drop database
sudo -u postgres dropdb warung_a
```

---

## 📞 NEXT STEPS SETELAH QUICK START

```
1. ✓ QUICK START (ini) - 5 menit
2. 📖 Baca SETUP_WARUNG.md untuk detail
3. 👨‍💼 Training kasir dengan PANDUAN_KASIR_SIMPLE.md
4. 🧪 Test transaction selama 1-2 hari
5. 🚀 Go Live untuk live operations
6. 📊 Monitor laporan harian
7. 🔧 Maintenance & optimization
```

---

**⏱️ Waktu Setup:** ~10 menit (termasuk verification)  
**Difficulty:** Easy (guided steps)  
**Version:** Odoo 18.0 Community Edition  
**Last Updated:** December 2025
