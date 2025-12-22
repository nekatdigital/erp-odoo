# 📋 PANDUAN SETUP ODOO POS & ACCOUNTING UNTUK WARUNG

> Dokumentasi komprehensif setup Odoo 18.0 untuk sistem kasir dan pembukuan warung

---

## 📖 DAFTAR ISI
1. [Persiapan Awal](#persiapan-awal)
2. [Instalasi & Konfigurasi Database](#instalasi--konfigurasi-database)
3. [Setup Module POS](#setup-module-pos)
4. [Setup Accounting](#setup-accounting)
5. [Setup Inventory](#setup-inventory)
6. [Management User & Akses](#management-user--akses)
7. [Testing & Go Live](#testing--go-live)
8. [Panduan Penggunaan Karyawan](#panduan-penggunaan-karyawan)

---

## 🖥️ PERSIAPAN AWAL

### Spesifikasi Minimal Hardware
```
WARUNG KECIL (1-2 user):
├── RAM: 2GB
├── Storage: 20GB
├── Processor: Quad Core
└── Network: Stable Internet 2Mbps

WARUNG MENENGAH (2-3 user):
├── RAM: 4GB
├── Storage: 50GB
├── Processor: Quad Core+
└── Network: Stable Internet 5Mbps
```

### Software Requirements
- ✅ Odoo 18.0 Community Edition (Gratis)
- ✅ PostgreSQL 14+
- ✅ Python 3.10+
- ✅ Linux/Windows/macOS

### Module yang Dibutuhkan
```
Core Modules:
├── point_of_sale (POS - Kasir)
├── account (Pembukuan)
├── stock (Stok Barang)
├── sale (Penjualan)
├── pos_restaurant (Optional: untuk warung makan)
└── pos_sale (Integrasi POS dengan Penjualan)

Modul Pendukung:
├── product (Produk)
├── contacts (Kontak/Supplier)
├── uom (Unit of Measure)
└── partner_autocomplete (Auto-complete partner)
```

---

## 🚀 INSTALASI & KONFIGURASI DATABASE

### Step 1: Verifikasi Install Odoo
```bash
# Cek versi Python
python3 --version

# Cek PostgreSQL
psql --version

# Test start Odoo
cd /workspaces/erp-odoo
python3 odoo-bin --help
```

### Step 2: Buat Database Baru untuk Warung
```bash
# Start PostgreSQL (jika belum running)
sudo service postgresql start

# Create database warung_a
sudo -u postgres createdb warung_a --encoding UTF8

# Start Odoo dengan database baru
python3 odoo-bin -d warung_a -i base,point_of_sale,account,stock,pos_sale
```

**Output Expected:**
```
✓ Database: warung_a
✓ Language: English (EN)
✓ Chart of Accounts: Standard (setup otomatis)
✓ Modules installed: point_of_sale, account, stock, pos_sale
```

### Step 3: Akses Odoo
```
URL: http://localhost:8069
Default Admin:
├── Login: admin
├── Password: admin
└── Company: My Company
```

---

## 🛍️ SETUP MODULE POS

### A. Konfigurasi Awal POS

#### 1. Setup Company/Toko
**Path:** `Settings > Companies`
```
Company Name        : WARUNG ANDA
Business Registration: (Nomor SITU/NIB jika ada)
Address            : Jl. Alamat Warung
Currency           : IDR (Indonesia Rupiah)
Timezone           : Asia/Jakarta
Country            : Indonesia
```

#### 2. Setup POS Session
**Path:** `Point of Sale > Configuration > POS`

```
BASIC INFO:
├── POS Name            : Kasir Warung [Nama Warung]
├── Company             : [Nama Warung]
├── Journal             : Sales
├── Opening Control     : ON (untuk pembukaan kasir)
├── Closing Control     : ON (untuk penutupan kasir)
└── Cash Control        : ON (verifikasi kas setiap hari)

PAYMENT METHOD:
├── Cash               : ✓ Enable
├── Kartu Kredit/Debit : ✓ Enable (opsional)
├── Transfer Bank      : ✓ Enable (opsional)
└── Custom Payment     : (Lihat Step B)

PRINTER:
├── Receipt Printer    : [Pilih jika punya printer thermal]
├── Kitchen Printer    : [Opsional untuk restoran]
└── Printer Width      : 80mm
```

#### 3. Kategori Produk
**Path:** `Product > Product Categories`

```
Contoh Kategori untuk Warung:
├── 📁 Makanan & Minuman
│   ├── Makanan Siap Saji
│   ├── Minuman Dingin
│   ├── Minuman Panas
│   └── Cemilan
├── 📁 Kebutuhan Sehari-hari
│   ├── Bumbu Masak
│   ├── Minyak & Gula
│   └── Perlengkapan Dapur
├── 📁 Rokok & Tembakau
├── 📁 Barang Elektronik
│   ├── Baterai
│   └── Kartu Memori
└── 📁 Lainnya
```

#### 4. Input Produk Ke POS
**Path:** `Point of Sale > Products`

```
DATA MINIMAL PRODUK:
├── Product Name      : Nama Produk (Max 30 karakter)
├── Category          : [Pilih kategori]
├── Type              : Storable (untuk produk fisik)
├── Price             : Harga Jual
├── Cost              : Harga Beli (untuk laporan profit)
├── Barcode           : [Opsional - untuk scanning]
├── UoM               : Unit (buah/box/dll)
├── Tracking          : [Lihat bagian Inventory]
└── POS Available     : ✓ ON

CONTOH ENTRY PRODUK:
ID  | Nama              | Category | Harga  | Stok
────┼──────────────────┼──────────┼────────┼─────
001 | Teh Botol 500ml   | Minuman  | 5.000  | 25
002 | Nasi Goreng       | Makanan  | 15.000 | 10
003 | Rokok Sampoerna   | Rokok    | 30.000 | 50
004 | Gula 1kg          | Kebutuhan| 12.000 | 15
```

#### B. Setup Payment Methods (Metode Pembayaran)
**Path:** `Point of Sale > Configuration > Payment Methods`

```
1. CASH (TUNAI)
   ├── Name              : Tunai
   ├── Payment Type      : Bank
   ├── Identify Customer : OFF
   ├── Verification      : ON (untuk pembukaan kasir)
   └── Journal           : Bank/Cash Journal

2. KARTU KREDIT (OPSIONAL)
   ├── Name              : Kartu Kredit
   ├── Payment Type      : Card
   ├── Identify Customer : ON
   └── Journal           : Card Journal

3. CUSTOM PAYMENT (JIKA ADA)
   ├── Name              : E-Wallet/Transfer
   ├── Payment Type      : Bank
   └── Identification    : ON
```

---

## 📊 SETUP ACCOUNTING

### A. Chart of Accounts (Pemetaan Akun)
**Path:** `Accounting > Configuration > Chart of Accounts`

```
AKUN MINIMUM UNTUK WARUNG:

1. REVENUE (Pendapatan):
   ├── 400001 - Penjualan Makanan
   ├── 400002 - Penjualan Barang Umum
   ├── 400003 - Penjualan Rokok
   └── 400999 - Penjualan Lainnya

2. COST OF GOODS SOLD (Harga Pokok):
   ├── 500001 - COGS Makanan
   ├── 500002 - COGS Barang
   └── 500003 - COGS Rokok

3. EXPENSE (Biaya):
   ├── 600001 - Biaya Gaji Karyawan
   ├── 600002 - Biaya Listrik
   ├── 600003 - Biaya Internet
   ├── 600004 - Biaya Air
   └── 600999 - Biaya Lainnya

4. ASSETS (Aset):
   ├── 100001 - Kas (Cash)
   ├── 100002 - Bank
   ├── 100003 - Inventory/Stok
   └── 100999 - Aset Lainnya

5. LIABILITY (Hutang):
   ├── 200001 - Hutang Supplier
   ├── 200002 - Hutang Pajak
   └── 200999 - Hutang Lainnya
```

### B. Tax Setup (Pajak)
**Path:** `Accounting > Configuration > Taxes`

```
UNTUK INDONESIA:

TAX: PPN 11% (Pajak Pertambahan Nilai)
├── Name               : PPN 11%
├── Type               : Sale
├── Tax Type           : Percentage
├── Amount             : 11%
├── Include in Price   : ON (jika sudah include)
└── Tax Code           : [Sesuai peraturan PPh22/23]

(Catatan: Sesuaikan dengan regulasi lokal/nasional Anda)
```

### C. Konfigurasi Journal
**Path:** `Accounting > Configuration > Journal`

```
JOURNAL UNTUK POS:

1. Sales Journal
   ├── Name     : Penjualan POS
   ├── Code     : POS
   ├── Type     : Sale
   ├── Default Debit Account  : Inventory
   └── Default Credit Account : Revenue

2. Bank/Cash Journal
   ├── Name     : Tunai
   ├── Code     : CASH
   ├── Type     : Bank
   ├── Account  : Kas/Bank Account
   └── Default Debit/Credit : Sesuai transaksi
```

---

## 📦 SETUP INVENTORY

### A. Warehouse Configuration
**Path:** `Inventory > Configuration > Warehouse`

```
SETUP DEFAULT WAREHOUSE:

Warehouse Name   : Gudang Utama
Address Location : [Alamat warung]
Partner          : [Nama warung]

Stock Location:
├── Main Stock   : Lokasi penyimpanan utama
├── Input Area   : Area penerimaan barang
└── Output Area  : Area pengiriman
```

### B. Stok Awal (Opening Stock)
**Path:** `Inventory > Overview > Inventory Adjustments`

```
UNTUK SETIAP PRODUK:
1. Buat "Initial Inventory" untuk stok saat go-live
2. Input quantity untuk setiap produk
3. Tentukan lokasi penyimpanan
4. Validate untuk mencatat ke sistem
```

### C. Minimum Stock Alert
**Path:** `Product > Edit Each Product > Inventory`

```
UNTUK SETIAP PRODUK:

Reorder Point      : [Jumlah minimal]
   Contoh: Teh Botol min 10 pcs

Can Be Expensed    : OFF
Tracking           : Lot/Serial (untuk barang tertentu)

CONTOH SETUP:
Produk              | Min Stok | Action
─────────────────────┼──────────┼────────────
Teh Botol 500ml     | 10       | Auto order
Nasi Goreng         | 5        | Auto order
Rokok Sampoerna     | 20       | Manual order
```

---

## 👥 MANAGEMENT USER & AKSES

### A. Buat User Karyawan
**Path:** `Settings > Users & Companies > Users`

```
USER 1 - KARYAWAN KASIR 1:
├── Login Name       : kasir1
├── Email            : kasir1@warung.local
├── Name             : [Nama Karyawan]
├── Password         : [Buat password kuat]
└── Action on Timeout: Close Session (untuk keamanan)

USER 2 - KARYAWAN KASIR 2:
├── Login Name       : kasir2
├── Email            : kasir2@warung.local
├── Name             : [Nama Karyawan]
├── Password         : [Buat password kuat]
└── Action on Timeout: Close Session
```

### B. Setup Access Level
**Path:** `Settings > Users & Companies > User Roles`

```
ROLE: KASIR (untuk karyawan)
├── POS Features
│   ├── Use POS         : ✓ ON
│   ├── Access Reports  : OFF
│   └── Access Settings : OFF
└── Restrictions
    ├── Dapat: Transaksi Penjualan, Stok
    └── Tidak Dapat: Setup, Accounting, Laporan Lanjutan

ROLE: MANAGER (untuk pemilik)
├── Full Access
│   ├── POS            : ✓ ON
│   ├── Accounting     : ✓ ON
│   ├── Inventory      : ✓ ON
│   ├── Reports        : ✓ ON
│   └── Settings       : ✓ ON
└── No Restrictions
```

### C. POS Session Permission
**Path:** `Point of Sale > Configuration > POS > Cashier Allowed`

```
UNTUK SETIAP KASIR:
- Izinkan kasir1 gunakan POS Kasir Warung ✓
- Izinkan kasir2 gunakan POS Kasir Warung ✓
- Izinkan admin gunakan semua POS ✓
```

---

## 🧪 TESTING & GO LIVE

### Pre-Launch Checklist

```
✓ DATABASE & USERS
  ☐ Database warung_a created
  ☐ User admin configured
  ☐ User kasir1 & kasir2 created
  ☐ Password secured

✓ POS CONFIGURATION
  ☐ POS Session created
  ☐ Payment methods configured
  ☐ Printer settings done (jika ada)
  ☐ Cash control enabled
  ☐ Journal linked correctly

✓ PRODUCTS & INVENTORY
  ☐ Min 20 products entered
  ☐ Categories organized
  ☐ Barcode set (opsional)
  ☐ Initial stock counted
  ☐ Minimum stock levels set

✓ ACCOUNTING
  ☐ Chart of accounts created
  ☐ Tax configured
  ☐ Journal settings done
  ☐ Bank account configured

✓ TESTING
  ☐ Test transaksi kasir
  ☐ Test payment methods
  ☐ Test inventory update
  ☐ Test laporan daily
  ☐ Test user login kasir1
  ☐ Test user login kasir2
```

### Test Transaction Flow
```
1. LOGIN sebagai kasir1
2. OPEN CASH (input modal tunai awal)
3. CREATE ORDER dengan 3-5 produk berbeda
4. TRY berbagai payment methods
5. PRINT receipt (test printer)
6. CHECK inventory updated
7. CLOSE CASH (buat laporan)
8. LOGIN sebagai manager - CHECK laporan
```

---

## 📚 PANDUAN PENGGUNAAN KARYAWAN

### Untuk Karyawan Umur 50an - Panduan Simple

#### SEBELUM MEMULAI KERJA

**Step 1: Login**
```
1. Buka browser (Chrome/Firefox)
2. Ketik: http://localhost:8069
3. Login dengan username & password Anda
   ├── Username: kasir1 (atau kasir2)
   └── Password: [yang diberikan manager]
4. Klik "Sign In"
```

**Step 2: Buka POS**
```
1. Di halaman utama, cari "Point of Sale"
2. Klik "Point of Sale > Kasir Warung"
3. Tunggu loading (±5 detik)
4. BUKA KASIR dengan klik tombol "OPEN SESSION"
5. INPUT jumlah uang awal kasir Anda
   Contoh: Rp. 100.000 (untuk kembalian customer)
6. Klik "Confirm"
```

---

#### SAAT ADA CUSTOMER (PROSES TRANSAKSI)

**Step 3: Buat Pesanan Baru**
```
1. Klik tombol "New Order" (atau screen kosong)
2. PILIH PRODUK dengan:
   
   CARA A - Klik Tombol Produk:
   ├── Lihat gambar/nama produk di layar
   ├── Klik produk yang dibeli customer
   ├── Otomatis qty 1 ditambah
   └── Klik lagi jika qty lebih dari 1
   
   CARA B - Ketik Barcode (jika ada barcode):
   ├── Siapkan barcode scanner/keyboard
   ├── Arahkan ke barcode produk
   ├── Scan atau ketik barcode
   └── Produk langsung masuk daftar
```

**Step 4: Verifikasi Pesanan**
```
1. Lihat DAFTAR PRODUK di sebelah kanan:
   
   Teh Botol 500ml        1x    Rp. 5.000
   Nasi Goreng            2x    Rp. 30.000
   ─────────────────────────────────────
   TOTAL:                        Rp. 35.000

2. JIKA SALAH:
   ├── Klik produk yang salah
   └── Klik "-" untuk kurangi qty (hingga 0 = hapus)

3. JIKA BENAR:
   └── Lanjut ke Step 5
```

**Step 5: PEMBAYARAN**
```
1. Klik tombol "PAYMENT" atau "CHECKOUT"

2. PILIH CARA PEMBAYARAN:
   
   ┌─────────────────────────┐
   │  Tunai      │  Transfer  │
   │  Kartu      │  E-Wallet  │
   └─────────────────────────┘

3. JIKA TUNAI:
   ├── Tulis uang yang diterima: Rp. 50.000
   ├── Sistem otomatis hitung kembalian
   ├── Verifikasi jumlah kembalian
   └── Berikan uang + struk ke customer

4. JIKA KARTU/TRANSFER:
   ├── Masukkan jumlah yang dibayar
   ├── Tunggu verifikasi (jika ada)
   └── Berikan struk ke customer
```

**Step 6: SELESAI**
```
1. Otomatis order selesai
2. Layar kembali ke "New Order" (kosong)
3. SIAP MELAYANI CUSTOMER BERIKUTNYA
```

---

#### AKHIR HARI KERJA (CLOSING)

**Step 7: Tutup Kasir**
```
1. Setelah semua customer selesai:
   ├── Hitung uang tunai yang ada di tangan
   ├── Buka aplikasi Odoo
   └── Cari "Point of Sale > Closing"

2. BUAT CLOSING REPORT:
   ├── POS yang digunakan: Kasir Warung
   ├── Input jumlah uang fisik: Rp. XXX.XXX
   ├── Sistem hitung selisih (jika ada)
   ├── Review laporan penjualan hari ini
   └── Klik "Close"

3. SUBMIT LAPORAN KE MANAGER
   ├── Screenshot atau print laporan
   ├── Catat tanggal, nama kasir
   └── Serahkan cash ke manager
```

---

### Tips Penting untuk Karyawan

```
⚠️ JANGAN:
   ✗ Logout tanpa close kasir
   ✗ Tinggalkan kasir tanpa lock screen
   ✗ Bagikan password dengan orang lain
   ✗ Hapus transaksi yang sudah selesai

✅ LAKUKAN:
   ✓ Lock screen saat pergi sejenak (Ctrl+Alt+Delete)
   ✓ Confirm setiap transaksi sebelum payment
   ✓ Hitung uang setelah close kasir
   ✓ Report error/masalah ke manager
   
⏰ URGENT CALL:
   Jika ada masalah, hubungi manager atau:
   ├── Restart aplikasi (Close + Open lagi)
   └── Restart komputer (jika benar-benar hang)
```

---

### Laporan untuk Manager

**Step 8: Akses Laporan Harian**
```
Path: Accounting > Dashboard / Reports

DAILY POS REPORT:
├── Total Penjualan: Rp. XXX.XXX
├── Jumlah Transaksi: XX
├── Payment Methods:
│   ├── Tunai: Rp. XXX
│   ├── Kartu: Rp. XXX
│   └── Transfer: Rp. XXX
├── Top Produk (paling terjual)
├── Stock Deduction (stok berkurang)
└── Profit/Loss (untung/rugi)

MONTHLY REPORT:
├── Total Revenue
├── COGS (Harga Pokok Penjualan)
├── Gross Profit
├── Expenses
├── Net Profit/Loss
└── Cash Position
```

---

## 🔧 TROUBLESHOOTING CEPAT

| Problem | Solusi |
|---------|--------|
| Login tidak bisa | Cek username/password, reset password |
| POS tidak loading | Refresh browser (F5), restart Odoo |
| Produk tidak muncul | Cek kategori, pastikan "POS Available" ON |
| Stok tidak update | Check inventory setting, validate dokumen |
| Laporan tidak akurat | Review Chart of Accounts, sync inventory |
| Printer tidak jalan | Check printer connection, setting di POS |
| Cash tidak balance | Review closing report, cek transaksi |

---

## 📞 SUPPORT & DOKUMENTASI

```
UNTUK BANTUAN LEBIH LANJUT:
├── Odoo Documentation: https://www.odoo.com/documentation
├── POS Documentation: https://www.odoo.com/documentation/18.0/applications/sales/point_of_sale.html
├── Accounting Docs: https://www.odoo.com/documentation/18.0/applications/finance/accounting.html
└── Community Forum: https://github.com/odoo/odoo/discussions
```

---

**Document Version:** 1.0  
**Created:** December 2025  
**For:** Warung UMKM Indonesia  
**Odoo Version:** 18.0 Community Edition

---
