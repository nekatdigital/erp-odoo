#!/usr/bin/env python3
"""
Generate Excel Template untuk Input Produk Warung di Odoo
Buat file Excel yang bisa di-import langsung ke Odoo
"""

import csv
from pathlib import Path

def create_product_import_template():
    """Create CSV template for product import"""
    
    csv_content = """Product Name,Category,Type,Price (IDR),Cost (IDR),Barcode,UoM,Stock Quantity,Min Stock,Notes
Teh Botol 500ml,Minuman,Storable,5000,2500,,Unit,25,10,Minuman kemasan
Teh Botol 1L,Minuman,Storable,9000,4000,,Unit,15,5,Minuman kemasan
Larutan Jamu,Minuman,Storable,3000,1200,,Unit,30,15,Minuman tradisional
Kopi Nescafe,Minuman,Storable,15000,8000,,Unit,20,10,Kopi sachet
Nasi Goreng,Makanan,Storable,15000,6000,,Pcs,10,5,Makanan siap saji
Nasi Kuning,Makanan,Storable,12000,4500,,Pcs,8,3,Makanan siap saji
Bakso,Makanan,Storable,12000,5000,,Porsi,12,5,Makanan siap saji
Lumpia,Makanan,Storable,2000,800,,Pcs,40,20,Makanan ringan
Perkedel,Makanan,Storable,1500,600,,Pcs,50,25,Makanan ringan
Rokok Sampoerna,Rokok,Storable,30000,25000,,Bungkus,50,20,Rokok filter
Rokok Catur,Rokok,Storable,28000,23000,,Bungkus,45,20,Rokok filter
Rokok Marlboro,Rokok,Storable,32000,27000,,Bungkus,40,15,Rokok filter
Gula 1kg,Kebutuhan,Storable,12000,8000,,Kg,15,5,Bahan dapur
Minyak Goreng 2L,Kebutuhan,Storable,25000,18000,,Botol,8,3,Bahan dapur
Garam 250gr,Kebutuhan,Storable,3000,1500,,Pcs,20,10,Bumbu masak
Cabe Rawit (100gr),Kebutuhan,Storable,5000,2500,,Pcs,15,5,Bumbu masak
Baterai AA,Elektronik,Storable,8000,4000,,Pcs,30,10,Elektronik
Baterai AAA,Elektronik,Storable,5000,2500,,Pcs,25,10,Elektronik
Kartu Memori 32GB,Elektronik,Storable,45000,25000,,Pcs,5,2,Elektronik
Pulpen Biru,Alat Tulis,Storable,2000,1000,,Pcs,50,20,Alat tulis
Buku Tulis,Alat Tulis,Storable,8000,4000,,Pcs,20,10,Alat tulis
Pensil HB,Alat Tulis,Storable,2500,1200,,Pcs,40,20,Alat tulis
"""
    
    return csv_content

def create_accounting_template():
    """Create chart of accounts template"""
    
    csv_content = """Account Code,Account Name,Account Type,Description
100001,Cash,Bank,Kas di tangan
100002,Bank BCA,Bank,Rekening Bank BCA
100003,Inventory,Asset,Nilai stok barang
100004,Furniture & Fixtures,Asset,Peralatan toko
100005,Accumulated Depreciation,Asset,Depresiasi peralatan
200001,Accounts Payable - Suppliers,Liability,Hutang ke supplier
200002,Payable - Tax,Liability,Hutang pajak
200003,Short-term Loan,Liability,Pinjaman jangka pendek
300001,Owner's Capital,Equity,Modal pemilik
300002,Retained Earnings,Equity,Laba ditahan
400001,Sales Revenue - Food,Income,Penjualan makanan
400002,Sales Revenue - Beverages,Income,Penjualan minuman
400003,Sales Revenue - Tobacco,Income,Penjualan rokok
400004,Sales Revenue - Supplies,Income,Penjualan kebutuhan sehari-hari
400005,Sales Revenue - Electronics,Income,Penjualan elektronik
500001,COGS - Food,Cost of Goods,Harga pokok makanan
500002,COGS - Beverages,Cost of Goods,Harga pokok minuman
500003,COGS - Tobacco,Cost of Goods,Harga pokok rokok
500004,COGS - Supplies,Cost of Goods,Harga pokok kebutuhan
600001,Salary Expense,Expense,Biaya gaji karyawan
600002,Electricity Expense,Expense,Biaya listrik
600003,Water Expense,Expense,Biaya air
600004,Internet Expense,Expense,Biaya internet
600005,Rent Expense,Expense,Biaya sewa toko
600006,Phone Expense,Expense,Biaya telepon
600007,Equipment Maintenance,Expense,Biaya perawatan peralatan
600008,Office Supplies,Expense,Biaya alat tulis kantor
600009,Miscellaneous Expense,Expense,Biaya lain-lain
700001,Bank Fees,Expense,Biaya bank
700002,Interest Expense,Expense,Biaya bunga
"""
    
    return csv_content

def create_supplier_template():
    """Create supplier/vendor template"""
    
    csv_content = """Supplier Name,Supplier Type,Contact Person,Phone,Email,Address,Payment Terms,Tax ID
PT Supplier Makanan,Company,Budi,081234567890,budi@supplier.co.id,Jl. Industri Jakarta,30 hari,12.345.678.9-012.345
CV Minuman Segar,Company,Adi,082234567890,adi@minuman.co.id,Jl. Perdagangan Surabaya,14 hari,98.765.432.1-098.765
Distributor Rokok Merpati,Company,Rudi,083234567890,rudi@rokok.co.id,Jl. Niaga Medan,Cash,56.789.012.3-456.789
Toko Bahan Dapur,Company,Siti,084234567890,siti@bahandapur.co.id,Jl. Pasar Jakarta,7 hari,34.567.890.1-234.567
Distributor Elektronik Jaya,Company,Hendra,085234567890,hendra@elektronik.co.id,Jl. Pembangunan Bandung,30 hari,23.456.789.0-123.456
"""
    
    return csv_content

def create_files():
    """Create all template files"""
    
    odoo_path = Path("/workspaces/erp-odoo")
    templates_dir = odoo_path / "TEMPLATES"
    templates_dir.mkdir(exist_ok=True)
    
    # Create Product Template
    with open(templates_dir / "01_IMPORT_PRODUK_TEMPLATE.csv", "w", encoding="utf-8") as f:
        f.write(create_product_import_template())
    print(f"✓ Created: 01_IMPORT_PRODUK_TEMPLATE.csv")
    
    # Create Accounting Template
    with open(templates_dir / "02_CHART_OF_ACCOUNTS_TEMPLATE.csv", "w", encoding="utf-8") as f:
        f.write(create_accounting_template())
    print(f"✓ Created: 02_CHART_OF_ACCOUNTS_TEMPLATE.csv")
    
    # Create Supplier Template
    with open(templates_dir / "03_SUPPLIER_TEMPLATE.csv", "w", encoding="utf-8") as f:
        f.write(create_supplier_template())
    print(f"✓ Created: 03_SUPPLIER_TEMPLATE.csv")
    
    # Create README
    readme = """# TEMPLATES UNTUK SETUP WARUNG

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
"""
    
    with open(templates_dir / "README.md", "w", encoding="utf-8") as f:
        f.write(readme)
    print(f"✓ Created: README.md")
    
    print(f"\n✓ All templates created in: {templates_dir}")

if __name__ == "__main__":
    create_files()
    print("\n✓ Template files ready to use!")
