# 📚 ODOO WARUNG - COMPLETE DOCUMENTATION INDEX

> Sistem Kasir & Pembukuan untuk UMKM Warung Indonesia

---

## 🎯 OVERVIEW

Dokumentasi lengkap untuk setup dan operasional sistem kasir Odoo 18.0 community edition untuk warung dengan banyak produk dan 2 karyawan.

**Target Market:** Pemilik warung UMKM usia 50an dengan ~2 karyawan

---

## 📑 DOKUMENTASI TERSEDIA

### 🚀 1. **QUICK_START.md** - Mulai dalam 5 Menit
**Untuk:** Yang ingin cepat langsung praktik  
**Waktu:** 5-10 menit  
**Isi:**
- Setup database Odoo
- Import produk
- Buat POS session
- Verifikasi checklist
- Troubleshooting cepat

👉 **[Mulai di sini jika ingin cepat setup](QUICK_START.md)**

---

### 📖 2. **SETUP_WARUNG.md** - Panduan Lengkap Step-by-Step
**Untuk:** Setup komprehensif dengan penjelasan detail  
**Waktu:** 2-3 jam (untuk setup + test)  
**Isi:**
- Persiapan awal (hardware, software)
- Instalasi & konfigurasi database
- Module POS lengkap (payment, printer, categories)
- Module Accounting (chart of accounts, tax, journal)
- Inventory management (warehouse, stock, alert)
- User management & akses control
- Testing checklist
- Laporan untuk manager

👉 **[Setup lengkap ada di sini](SETUP_WARUNG.md)**

---

### 👨‍💼 3. **PANDUAN_KASIR_SIMPLE.md** - Training untuk Karyawan
**Untuk:** Karyawan yang akan mengoperasikan kasir  
**Waktu:** 1-2 jam training + practice  
**Isi:**
- Login ke aplikasi
- Buka kasir (opening)
- Input transaksi customer
- Payment (tunai/kartu/transfer)
- Tutup kasir (closing)
- Troubleshooting masalah umum
- Tips & checklist harian

👉 **[Kasir & karyawan baca ini](PANDUAN_KASIR_SIMPLE.md)**

---

## 🛠️ FILE & TOOLS

### Scripts Automation

#### `setup_warung.py`
Script otomasi untuk setup database dan modules Odoo.

**Cara pakai:**
```bash
cd /workspaces/erp-odoo
python3 setup_warung.py --db-name warung_a
```

**Options:**
- `--db-name` : Nama database (default: warung_a)
- `--odoo-path` : Path Odoo (default: /workspaces/erp-odoo)
- `--skip-postgres` : Skip PostgreSQL setup
- `--no-modules` : Skip module installation

---

#### `create_templates.py`
Script untuk generate template CSV untuk import data.

**Cara pakai:**
```bash
python3 create_templates.py
```

**Menghasilkan:**
- `TEMPLATES/01_IMPORT_PRODUK_TEMPLATE.csv`
- `TEMPLATES/02_CHART_OF_ACCOUNTS_TEMPLATE.csv`
- `TEMPLATES/03_SUPPLIER_TEMPLATE.csv`

---

### Template Files

#### `/TEMPLATES/01_IMPORT_PRODUK_TEMPLATE.csv`
Template CSV untuk import produk ke Odoo.

**Cara pakai:**
1. Edit file di Excel dengan produk warung Anda
2. Di Odoo: Product → Import → Upload file
3. Klik Import

**Fields yang tersedia:**
- Product Name (nama produk)
- Category (kategori)
- Type (storable/consumable)
- Price (harga jual)
- Cost (harga beli)
- Barcode (opsional)
- UoM (unit of measure)
- Stock Quantity (stok awal)
- Min Stock (stok minimal alert)

---

#### `/TEMPLATES/02_CHART_OF_ACCOUNTS_TEMPLATE.csv`
Template untuk Chart of Accounts pembukuan.

**Included accounts:**
- Revenue accounts (penjualan)
- Cost of Goods Sold
- Expense accounts
- Asset accounts
- Liability accounts

**Setup:** Manual di Odoo atau via import

---

#### `/TEMPLATES/03_SUPPLIER_TEMPLATE.csv`
Template untuk supplier/vendor data.

**Fields:**
- Supplier Name
- Contact Person
- Phone & Email
- Address
- Payment Terms
- Tax ID

---

## 🏗️ PROJECT STRUCTURE

```
/workspaces/erp-odoo/
├── QUICK_START.md                    ⭐ Mulai di sini
├── SETUP_WARUNG.md                   📖 Panduan lengkap
├── PANDUAN_KASIR_SIMPLE.md           👨‍💼 Training kasir
├── README_DOCUMENTATION.md           📚 File ini
├── setup_warung.py                   🛠️ Script automation
├── create_templates.py               🛠️ Generate templates
├── TEMPLATES/
│   ├── 01_IMPORT_PRODUK_TEMPLATE.csv
│   ├── 02_CHART_OF_ACCOUNTS_TEMPLATE.csv
│   ├── 03_SUPPLIER_TEMPLATE.csv
│   └── README.md
├── addons/
│   ├── point_of_sale/               (POS Module)
│   ├── account/                     (Accounting Module)
│   ├── stock/                       (Inventory Module)
│   └── ...
└── odoo-bin                         (Odoo executable)
```

---

## 🚀 QUICKSTART FLOW

### Untuk Pemilik Warung (yang ingin cepat setup):

```
1. [QUICK_START.md] - 5 menit
   ↓ (Baca & jalankan 5 langkah)
   
2. [SETUP_WARUNG.md] - 2-3 jam
   ↓ (Setup detail + test transaksi)
   
3. [PANDUAN_KASIR_SIMPLE.md] - 1-2 jam
   ↓ (Training kasir Anda)
   
4. GO LIVE! 🎉
   ↓ (Real operations)
   
5. Daily: Review laporan harian
   ↓ (Monitor revenue, stok, cash)
```

### Untuk Karyawan Kasir:

```
1. [PANDUAN_KASIR_SIMPLE.md] - 1-2 jam
   ↓ (Baca panduan + simulasi)
   
2. Manager certification
   ↓ (Manager verifikasi sudah paham)
   
3. GO LIVE! ✓
   ↓ (Mulai kerja di kasir)
   
4. Daily checklist
   ↓ (Ikuti prosedur harian)
```

---

## 💡 FITUR UTAMA YANG DICAKUP

### Point of Sale (POS) ✓
- [x] Desktop/Web interface (bukan hanya mobile)
- [x] Unlimited products (cocok untuk warung banyak produk)
- [x] Multiple payment methods (tunai, kartu, transfer)
- [x] Receipt printing
- [x] Cash control & opening/closing
- [x] Multi-user/multi-cashier
- [x] Daily sales report

### Accounting (Pembukuan) ✓
- [x] Auto-sync dari POS transactions
- [x] Chart of accounts
- [x] Journal entries
- [x] Daily/Monthly reports
- [x] Cash flow tracking
- [x] Tax calculation (PPN)
- [x] Supplier management

### Inventory (Stok) ✓
- [x] Real-time stock tracking
- [x] Minimum stock alerts
- [x] Stock adjustments
- [x] Stock by warehouse
- [x] Product categories
- [x] Initial stock setup
- [x] Stock reports

### User Management ✓
- [x] Multi-user login
- [x] Access control per role
- [x] Kasir (POS only)
- [x] Manager (full access)
- [x] Admin (system admin)
- [x] Session timeout for security

---

## 📊 EXPECTED OUTPUTS SETELAH SETUP

### Harian (Daily)
- ✓ Laporan penjualan per kasir
- ✓ Total revenue
- ✓ Payment breakdown (tunai vs metode lain)
- ✓ Stock deduction

### Bulanan (Monthly)
- ✓ Total sales revenue
- ✓ Cost of goods sold
- ✓ Gross profit
- ✓ Operating expenses
- ✓ Net profit/loss
- ✓ Cash position
- ✓ Aging payables (hutang supplier)

---

## ⚙️ REQUIREMENTS

### Hardware Minimum
```
Untuk 1-2 user:
├── RAM: 2GB
├── Storage: 20GB
└── CPU: Quad Core

Untuk 3+ user:
├── RAM: 4GB
├── Storage: 50GB
└── CPU: Quad Core+
```

### Software
- PostgreSQL 14+
- Python 3.10+
- Linux/Windows/macOS
- Modern Browser (Chrome, Firefox, Edge)

### Optional Hardware
- Thermal receipt printer 80mm
- Barcode scanner
- Additional monitors
- Network printer

---

## 🔐 SECURITY NOTES

```
PENTING:
- ✓ Ganti password admin setelah first login
- ✓ Set strong password untuk semua user
- ✓ Enable session timeout (auto logout)
- ✓ Backup database regularly
- ✓ Jangan share password antar user
- ✓ Lock screen saat pergi dari kasir

PRODUCTION READY:
- ✓ Use HTTPS/SSL jika akses remote
- ✓ Firewall rules untuk limit access
- ✓ Regular database backups
- ✓ User activity logging
- ✓ Audit trail untuk cash transactions
```

---

## 📞 SUPPORT & RESOURCES

### Dokumentasi Online
- Odoo Official Docs: https://www.odoo.com/documentation/18.0/
- POS Module: https://www.odoo.com/documentation/18.0/applications/sales/point_of_sale.html
- Accounting: https://www.odoo.com/documentation/18.0/applications/finance/accounting.html

### Troubleshooting
Lihat bagian "Troubleshooting" di setiap dokumentasi untuk masalah umum.

### Community
- GitHub Discussions: https://github.com/odoo/odoo/discussions
- Stack Overflow: tag `odoo`

---

## 🎓 TRAINING MATERIALS

### Untuk Pemilik
1. Read: SETUP_WARUNG.md (lengkap)
2. Practice: Simulasi transaksi 10x
3. Learn: Review laporan daily 1 minggu
4. Master: Adjust pricing & inventory management

### Untuk Kasir
1. Read: PANDUAN_KASIR_SIMPLE.md
2. Watch: Video tutorial (jika ada)
3. Practice: Simulasi 20+ transaksi
4. Test: Closing & opening procedure
5. Certified: Manager sign-off

---

## 📈 NEXT STEPS SETELAH GO LIVE

```
Week 1:
- Monitor harian
- Fix bugs yang muncul
- Optimize based on usage
- Kasir comfortable with workflow

Week 2-4:
- Daily oversight
- Monthly report review
- Stock audit (physical count)
- Adjust settings if needed

Month 2-3:
- Optimize workflows
- Add features (jika ada kebutuhan)
- Advanced reporting
- Staff proficiency verification

Month 3+:
- Maintenance mode
- Regular backups
- Periodic review
- Plan for expansion (additional user/warung)
```

---

## 🆘 COMMON ISSUES & SOLUTIONS

| Issue | Reference |
|---|---|
| Database connection error | SETUP_WARUNG.md → Troubleshooting |
| Produk tidak muncul di POS | SETUP_WARUNG.md → Setup POS |
| Kasir tidak bisa login | SETUP_WARUNG.md → User Management |
| Cash tidak balance | PANDUAN_KASIR_SIMPLE.md → Closing |
| Printer not working | SETUP_WARUNG.md → Printer Config |
| Laporan tidak akurat | SETUP_WARUNG.md → Accounting Setup |

---

## 🎉 SUCCESS CRITERIA

Anda BERHASIL jika:

```
✓ Database running tanpa error
✓ POS session bisa dibuka & ditutup
✓ Transaksi bisa diproses (add item, pay, print receipt)
✓ Stok otomatis berkurang setiap transaksi
✓ Laporan harian menunjukkan akurat
✓ Kasir bisa login & operate independently
✓ Manager bisa review laporan
✓ Daily closing balance = physical cash
✓ Monthly report menunjukkan profit/loss
✓ Data terinput konsisten & akurat
```

---

## 📝 VERSION HISTORY

| Version | Date | Changes |
|---|---|---|
| 1.0 | Dec 2025 | Initial release |
| | | - QUICK_START.md |
| | | - SETUP_WARUNG.md |
| | | - PANDUAN_KASIR_SIMPLE.md |
| | | - Scripts & templates |

---

## 📄 LICENSE & DISCLAIMER

```
Dokumentasi ini dibuat untuk Odoo Community Edition 18.0.
Bebas digunakan & dimodifikasi sesuai kebutuhan.

Penting:
- Gunakan dengan tanggung jawab
- Test sebelum go-live
- Backup data regularly
- Konsultasi dengan IT jika ada kebutuhan khusus
```

---

## 📧 FEEDBACK & IMPROVEMENT

Dokumentasi ini dapat ditingkatkan! Jika ada:
- Bagian yang membingungkan
- Step yang missing
- Fitur yang perlu dijelaskan
- Translate ke bahasa lain
- Video tutorial

👉 Hubungi development team untuk improvement

---

## 🎯 TL;DR (Too Long; Didn't Read)

**Ingin setup cepat?**
→ Baca [QUICK_START.md](QUICK_START.md) (5 menit)

**Ingin setup lengkap?**
→ Baca [SETUP_WARUNG.md](SETUP_WARUNG.md) (2-3 jam)

**Karyawan Kasir?**
→ Baca [PANDUAN_KASIR_SIMPLE.md](PANDUAN_KASIR_SIMPLE.md) (1-2 jam)

---

**Happy selling! 🎉**  
Semoga Warung Anda lebih efisien dan profitable dengan Odoo POS!

*Last Updated: December 22, 2025*  
*Odoo Version: 18.0 Community Edition*  
*For: Indonesian UMKM Warung*
