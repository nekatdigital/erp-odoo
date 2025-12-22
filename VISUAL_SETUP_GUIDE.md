# 🎨 VISUAL SETUP GUIDE - ODOO WARUNG

> Panduan visual untuk memahami setup flow dan architecture

---

## 1️⃣ SYSTEM ARCHITECTURE

```
┌─────────────────────────────────────────────────────────────┐
│                    BROWSER / INTERFACE                      │
│              (Chrome, Firefox, Safari)                      │
│         http://localhost:8069                               │
│  ┌──────────────────────┬──────────────────────┐           │
│  │   MANAGER/ADMIN      │    KASIR 1 & 2       │           │
│  │  Full Dashboard      │  POS Interface       │           │
│  │  Reports & Settings  │  Transaksi           │           │
│  └──────────────────────┴──────────────────────┘           │
└────────────────────────────────────────────────────────────┘
                              ↓
┌────────────────────────────────────────────────────────────┐
│                   ODOO SERVER (localhost)                   │
│  ┌────────────────────────────────────────────────────┐    │
│  │  MODULES                                           │    │
│  │  ├─ Point of Sale (POS)                           │    │
│  │  ├─ Accounting                                    │    │
│  │  ├─ Inventory                                     │    │
│  │  ├─ Sales                                         │    │
│  │  └─ Contacts                                      │    │
│  └────────────────────────────────────────────────────┘    │
└────────────────────────────────────────────────────────────┘
                              ↓
┌────────────────────────────────────────────────────────────┐
│              POSTGRESQL DATABASE (warung_a)                │
│  ┌──────────────┬──────────────┬──────────────┐           │
│  │   Products   │   Accounts   │  Customers   │           │
│  │   Stock      │  Transactions│  Suppliers   │           │
│  │   Categories │  Invoices    │  Users       │           │
│  └──────────────┴──────────────┴──────────────┘           │
└────────────────────────────────────────────────────────────┘
                              ↓
┌────────────────────────────────────────────────────────────┐
│                  HARDWARE (OPTIONAL)                        │
│  ├─ Receipt Printer (untuk struk)                          │
│  ├─ Barcode Scanner (untuk input produk)                   │
│  └─ Additional Monitor (untuk better view)                 │
└────────────────────────────────────────────────────────────┘
```

---

## 2️⃣ USER & ROLE HIERARCHY

```
                    ┌─────────────────┐
                    │  ADMINISTRATOR  │
                    │  (Pemilik/Owner)│
                    └────────┬────────┘
                             │
              ┌──────────────┼──────────────┐
              ↓              ↓              ↓
         ┌─────────┐  ┌──────────┐  ┌──────────┐
         │ MANAGER │  │ KASIR 1  │  │ KASIR 2  │
         │         │  │          │  │          │
         │ Full    │  │ POS Only │  │ POS Only │
         │ Access  │  │ Limited  │  │ Limited  │
         └────┬────┘  └──────────┘  └──────────┘
              │
         ┌────┴─────────────────────┐
         │  CAN ACCESS:             │
         ├─ Dashboard              │
         ├─ Reports                │
         ├─ Settings               │
         ├─ Products               │
         ├─ Accounting             │
         ├─ Inventory              │
         └─ User Management        │

         KASIR CAN ONLY ACCESS:
         ├─ POS Session
         ├─ Product List (Read)
         └─ Daily Closing
```

---

## 3️⃣ DAILY WORKFLOW

```
PAGI (OPENING)
───────────────

08:00 AM
  │
  └─→ Kasir Login
         ↓
      [Buka Browser]
      [Login username/password]
         ↓
      [Click "Point of Sale"]
      [Click "Kasir Warung"]
         ↓
      [OPEN SESSION Button]
      [Input modal awal: Rp. 100.000]
      [Confirm]
         ↓
      ✓ SIAP MELAYANI CUSTOMER


SIANG (OPERATION)
─────────────────

09:00 - 16:00 (Sepanjang hari)
  │
  └─→ Repeat untuk setiap customer:
         │
         ├─ Customer bilang order
         │    ↓
         ├─ Kasir klik produk (qty sesuai)
         │    ↓
         ├─ Verify daftar (sesuai order?)
         │    ↓
         ├─ Click [BAYAR]
         │    ↓
         ├─ Pilih payment method
         │    ↓
         ├─ Input uang / verifikasi
         │    ↓
         ├─ Print struk
         │    ↓
         └─ Berikan struk + barang/kembalian


SORE (CLOSING)
───────────────

17:00 (Jam tutup)
  │
  └─→ Kasir:
         │
         ├─ Hitung semua uang tunai
         │  (Jumlah fisik di tangan)
         │    ↓
         ├─ Buka menu "CLOSE SESSION"
         │    ↓
         ├─ Input jumlah uang fisik
         │    ↓
         ├─ [CONFIRM CLOSING]
         │    ↓
         ├─ Review laporan otomatis
         │  (Total penjualan hari ini)
         │    ↓
         ├─ Print/Screenshot laporan
         │    ↓
         └─ Serahkan ke Manager:
               • Uang tunai
               • Laporan print
               • Struk (jika ada)
                  ↓
              Manager verify & catat


SORE (MANAGER REVIEW)
──────────────────────

17:30
  │
  └─→ Manager Login
         ↓
      [Click Dashboard/Reports]
         ↓
      [Review Daily Report]
         │
         ├─ Total penjualan hari ini
         ├─ Payment breakdown
         ├─ Stok berkurang berapa
         ├─ Profit/Loss estimation
         └─ Any issue dari kasir?
         ↓
      [File report / Backup data]
```

---

## 4️⃣ DATA FLOW - TRANSAKSI KASIR

```
CUSTOMER DATANG
      ↓
KASIR INPUT ORDER (klik produk)
      ↓
      ┌─────────────────────────────┐
      │  DATA TERSIMPAN DI SISTEM:  │
      │                             │
      │  ✓ Item yang dipilih        │
      │  ✓ Quantity                 │
      │  ✓ Harga (dari master)      │
      │  ✓ Total                    │
      └─────────────────────────────┘
      ↓
KASIR CLICK [BAYAR]
      ↓
      ┌─────────────────────────────┐
      │  PAYMENT PROCESSING:        │
      │                             │
      │  ✓ Payment method dipilih   │
      │  ✓ Uang/ref diterima        │
      │  ✓ Kembalian dihitung       │
      └─────────────────────────────┘
      ↓
[CONFIRM PAYMENT]
      ↓
      ┌──────────────────────────────────┐
      │  TRANSACTION COMPLETE!           │
      │                                  │
      │  Automatic dalam sistem:        │
      │  ✓ Receipt printed              │
      │  ✓ Stok berkurang               │
      │  ✓ Revenue dicatat              │
      │  ✓ Cash masuk ke kas            │
      │  ✓ Accounting entry dibuat      │
      │  ✓ Customer data (jika ada)    │
      └──────────────────────────────────┘
      ↓
ORDER BARU
```

---

## 5️⃣ POS SCREEN LAYOUT

```
┌─────────────────────────────────────────────────────────────┐
│  KASIR WARUNG - POINT OF SALE INTERFACE                    │
├──────────────────┬────────────────────────────────────────┤
│                  │                                        │
│  KATEGORI:       │  DAFTAR TRANSAKSI SEKARANG            │
│  ┌────────────┐  │  ┌──────────────────────────────────┐ │
│  │ Makanan    │  │  │ Teh Botol 500ml                  │ │
│  │ Minuman    │  │  │   1x @ Rp.5.000  = Rp.5.000    │ │
│  │ Rokok      │  │  │                                  │ │
│  │ Kebutuhan  │  │  │ Nasi Goreng                      │ │
│  │ Elektronik │  │  │   2x @ Rp.15.000 = Rp.30.000  │ │
│  └────────────┘  │  │                                  │ │
│                  │  ├──────────────────────────────────┤ │
│  PRODUK TERSEDIA:│  │ SUBTOTAL        : Rp. 35.000    │ │
│  ┌────────────┐  │  │ PAJAK (PPN 11%) : Rp. 3.850     │ │
│  │ Teh Botol  │  │  │ ─────────────────────────────── │ │
│  │ Rp.5.000   │  │  │ TOTAL           : Rp. 38.850    │ │
│  │  [CLICK] ← ┼──┤  └──────────────────────────────────┘ │
│  └────────────┘  │                                        │
│  ┌────────────┐  │  ┌──────────────────────────────────┐ │
│  │Nasi Goreng │  │  │  [DELETE]  [BAYAR/CHECKOUT]    │ │
│  │Rp.15.000   │  │  │  [DISKON]  [PRINT PREVIEW]     │ │
│  │  [CLICK]   │  │  │  [HOLD]    [NEW ORDER]         │ │
│  └────────────┘  │  └──────────────────────────────────┘ │
│  ┌────────────┐  │                                        │
│  │Rokok Catur │  │                                        │
│  │Rp.30.000   │  │  ┌──────────────────────────────────┐ │
│  │  [CLICK]   │  │  │ PAYMENT METHODS:                │ │
│  └────────────┘  │  │ [TUNAI]  [KARTU] [TRANSFER]    │ │
│                  │  └──────────────────────────────────┘ │
│                  │                                        │
└──────────────────┴────────────────────────────────────────┘
```

---

## 6️⃣ PRODUCT DATABASE STRUCTURE

```
PRODUK DATABASE
═══════════════

┌─ PRODUK ID #001
│  ├─ Nama: Teh Botol 500ml
│  ├─ Kategori: Minuman
│  ├─ Harga Jual: Rp. 5.000
│  ├─ Harga Beli: Rp. 2.500
│  ├─ Stok Saat Ini: 25 pcs
│  ├─ Min Stock: 10 pcs
│  ├─ Barcode: 8998765432101 (opsional)
│  ├─ UoM: Pcs (Pieces)
│  └─ Aktif: ✓ YES
│
├─ PRODUK ID #002
│  ├─ Nama: Nasi Goreng
│  ├─ Kategori: Makanan
│  ├─ Harga Jual: Rp. 15.000
│  ├─ Harga Beli: Rp. 6.000
│  ├─ Stok Saat Ini: 10 pcs
│  ├─ Min Stock: 5 pcs
│  ├─ UoM: Porsi
│  └─ Aktif: ✓ YES
│
├─ PRODUK ID #003
│  ├─ Nama: Rokok Catur
│  ├─ Kategori: Rokok
│  ├─ Harga Jual: Rp. 30.000
│  ├─ Harga Beli: Rp. 23.000
│  ├─ Stok Saat Ini: 45 bungkus
│  ├─ Min Stock: 20 bungkus
│  ├─ Barcode: 8888765432101
│  └─ Aktif: ✓ YES
│
└─ ... (20+ produk lainnya)

SETIAP KALI TRANSAKSI:
├─ Stok otomatis berkurang
├─ Revenue dicatat
├─ COGS dihitung
├─ Profit calculated
└─ Alert jika stok < Min Stock
```

---

## 7️⃣ ACCOUNTING FLOW

```
TRANSAKSI POS
     │
     ↓
OTOMATIS CREATE ACCOUNTING ENTRY:
     │
     ├─ DEBIT: Kas/Bank (Asset)          Rp. 35.000
     │         (Uang masuk)
     │
     └─ CREDIT: Revenue (Income)         Rp. 35.000
               (Penjualan terjadi)
               │
               └─ Breakdown by category:
                  ├─ Minuman: Rp. 5.000
                  ├─ Makanan: Rp. 30.000
                  └─ ... (other categories)

     ↓
INVENTORY ADJUSTMENT:
     │
     ├─ DEBIT: COGS (Expense)            Rp. 8.500
     │        (Harga pokok berkurang)
     │
     └─ CREDIT: Inventory (Asset)        Rp. 8.500
               (Stok berkurang)

     ↓
PROFIT CALCULATION:
     │
     ├─ Revenue        : Rp. 35.000
     ├─ COGS          : Rp. (8.500)
     ├─ Gross Profit  : Rp. 26.500
     ├─ (Margin: 75.7%)
     │
     └─ (- Operating Expense)
         └─ Net Profit: Rp. XX.XXX

     ↓
LAPORAN OTOMATIS:
     ├─ Daily POS Report
     ├─ Cash Register Balance
     ├─ Income Statement
     ├─ Balance Sheet
     └─ Profit & Loss Report
```

---

## 8️⃣ MULTI-USER TRACKING

```
KASIR 1 (kasir1)
│
├─ Login: 08:00
├─ Open Session: Modal Rp. 100.000
├─ Transaksi 1-5: 09:00-12:00
│  ├─ Transaksi #1: Rp. 50.000 (10:30, kasir1)
│  ├─ Transaksi #2: Rp. 30.000 (11:15, kasir1)
│  └─ ... (3 more)
│
├─ Close Session: 12:00
│  └─ Total: Rp. 250.000 (5 transaksi)
│
└─ Logout: 12:05


KASIR 2 (kasir2)
│
├─ Login: 13:00
├─ Open Session: Modal Rp. 100.000
├─ Transaksi 6-12: 13:00-17:00
│  ├─ Transaksi #6: Rp. 45.000 (13:45, kasir2)
│  ├─ Transaksi #7: Rp. 60.000 (14:30, kasir2)
│  └─ ... (5 more)
│
├─ Close Session: 17:00
│  └─ Total: Rp. 500.000 (7 transaksi)
│
└─ Logout: 17:10


MANAGER REVIEW (admin/manager)
│
├─ Login anytime
├─ View Dashboard
│  ├─ Kasir 1: Rp. 250.000 (5 transaksi)
│  ├─ Kasir 2: Rp. 500.000 (7 transaksi)
│  └─ TOTAL: Rp. 750.000 (12 transaksi)
│
├─ View per-kasir performance
├─ View products sold per kasir
├─ View payment breakdown
└─ Generate reports
```

---

## 9️⃣ INVENTORY MANAGEMENT VISUAL

```
┌─────────────────────────────────────────────────────────────┐
│                 INVENTORY STATUS                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  STOK NORMAL:                                              │
│  ├─ Teh Botol      [████████░░] 20/25 (80%) ✓ NORMAL    │
│  ├─ Nasi Goreng    [████░░░░░░] 5/10  (50%) ⚠ WARNING  │
│  └─ Rokok Catur    [░░░░░░░░░░] 8/50  (16%) 🔴 LOW     │
│                                                             │
│  STOK TERLALU RENDAH (MIN STOCK ALERT):                  │
│  ├─ 🔴 Gula 1kg      : Current 4kg, Min 5kg               │
│  │                    → BUY MORE!                          │
│  │                                                         │
│  ├─ 🔴 Minyak 2L    : Current 2 botol, Min 3 botol       │
│  │                    → BUY MORE!                          │
│  │                                                         │
│  └─ 🔴 Rokok Catur  : Current 8, Min 20                  │
│                       → BUY MORE!                          │
│                                                             │
│  STOK NORMAL:                                              │
│  ├─ ✓ Kopi Nescafe : Current 18, Min 10 (AMAN)           │
│  ├─ ✓ Lumpia       : Current 35, Min 20 (AMAN)           │
│  └─ ✓ Baterai AA   : Current 28, Min 10 (AMAN)           │
│                                                             │
│  STOK OVERSTOCK (TERLALU BANYAK):                        │
│  ├─ ⚠ Pensil HB    : Current 100, Typical 40             │
│  │                   → DISCOUNT / PROMOTE                 │
│  │                                                         │
│  └─ ⚠ Buku Tulis   : Current 50, Typical 20              │
│                      → DISCOUNT / PROMOTE                 │
│                                                             │
└─────────────────────────────────────────────────────────────┘

ACTION NEEDED:
├─ 🔴 CRITICAL (Kurang dari minimum)
│  → Contact supplier segera
│  → Buat PO (Purchase Order)
│
├─ ⚠ WARNING (Mendekati minimum)
│  → Siapkan order untuk minggu depan
│
└─ ✓ NORMAL (Stok aman)
   → Lanjutkan operasional normal
```

---

## 🔟 PAYMENT METHOD FLOW

```
CUSTOMER READY TO PAY
     │
     ├─────────────────────────────────────┐
     │                                     │
     ↓                                     ↓
[TUNAI]                              [KARTU/TRANSFER]
     │                                     │
     ├─ Input uang yang diterima      ├─ Input jumlah pembayaran
     │  (Rp. 50.000)                  │  (Rp. 50.000)
     │                                │
     ├─ Sistem hitung kembalian       ├─ Cetak bukti/referensi
     │  (Rp. 50.000 - Rp. 35.000      │
     │   = Rp. 15.000)                ├─ Verifikasi status
     │                                │  (Pending/Confirmed/Failed)
     ├─ Berikan uang kembalian        │
     │                                ├─ Jika confirmed:
     └─ Transaksi selesai            │  - Print struk
                                      │  - Transaksi selesai
                                      │
                                      └─ Jika pending:
                                         - Tunggu konfirmasi
                                         - Catat sebagai pending
```

---

## 1️⃣1️⃣ BACKUP & DISASTER RECOVERY

```
DAILY BACKUP FLOW
══════════════════

Setiap hari (End of Day):
     │
     ├─ Database auto-backup
     │  (PostgreSQL dump)
     │
     ├─ Backup location:
     │  ├─ Local: /var/backups/odoo/
     │  ├─ External: USB/External Drive
     │  └─ Cloud: Google Drive / Dropbox (opsional)
     │
     └─ Retention: Keep 30 days backup
        (Dapat restore kapanpun jika ada issue)

DISASTER RECOVERY:
├─ Jika database crash → Restore dari backup
├─ Jika corrupted data → Rollback ke previous day
└─ Jika loss data → Can recover up to 30 days back
```

---

## 🎯 SETUP FLOWCHART

```
START
  │
  ├─→ [1] Prepare Hardware & Network
  │       └─→ Verify: Internet, DB Server, Power
  │
  ├─→ [2] Install PostgreSQL & Python
  │       └─→ Verify: psql --version, python3 --version
  │
  ├─→ [3] Setup Odoo Database (warung_a)
  │       └─→ Run: python3 setup_warung.py
  │
  ├─→ [4] Start Odoo Server
  │       └─→ Access: http://localhost:8069
  │
  ├─→ [5] Configure Company Settings
  │       └─→ Name, Currency (IDR), Timezone (Asia/Jakarta)
  │
  ├─→ [6] Import Products
  │       └─→ Use: TEMPLATES/01_IMPORT_PRODUK_TEMPLATE.csv
  │
  ├─→ [7] Setup POS Session
  │       └─→ Create: Kasir Warung [Nama]
  │
  ├─→ [8] Configure Accounting
  │       └─→ Chart of Accounts, Tax, Journal
  │
  ├─→ [9] Create User Accounts
  │       └─→ Admin, Kasir1, Kasir2
  │
  ├─→ [10] Setup Inventory
  │        └─→ Warehouse, Initial Stock, Min Stock Alert
  │
  ├─→ [11] Testing Phase
  │        ├─→ Test Login (all users)
  │        ├─→ Test POS Transaction
  │        ├─→ Test Closing & Reports
  │        └─→ Verify accuracy
  │
  ├─→ [12] Train Kasir
  │        ├─→ Login & Opening
  │        ├─→ Transaction Process
  │        ├─→ Payment Methods
  │        └─→ Closing Procedure
  │
  ├─→ [13] Go-Live Preparation
  │        ├─→ Backup database
  │        ├─→ Test all critical functions
  │        └─→ Notify all users
  │
  └─→ [14] GO LIVE!
       ├─→ Start daily operations
       ├─→ Monitor closely
       ├─→ Support available
       └─→ Success! 🎉
```

---

**Keep this visual guide nearby for quick reference!**
