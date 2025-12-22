# 👨‍💼 PANDUAN KASIR - SIMPLE & MUDAH DIIKUTI

> **Untuk karyawan warung yang baru pertama kali menggunakan aplikasi kasir**

---

## 🔐 LOGIN KE APLIKASI

### Video Tutorial: 
[Tonton video cara login 2 menit di sini jika ada kesulitan]

### Langkah-langkah:

**1️⃣ Buka Browser**
```
Klik icon Chrome / Firefox di desktop
atau ketik di address bar: http://localhost:8069
```

**2️⃣ Masukkan Username & Password**
```
┌─────────────────────────────────┐
│ Username  : kasir1 (atau kasir2)│
│ Password  : [sesuai yang diberi] │
│ Database  : warung_a            │
└─────────────────────────────────┘
```

**3️⃣ Klik "Sign In"**
```
Tunggu halaman loading (5-10 detik)
```

---

## 💰 BUKA KASIR (SEBELUM MULAI KERJA)

### Langkah 1: Cari Menu POS
```
Halaman utama → Cari "Point of Sale"
│
└─→ Klik "Point of Sale" di sidebar kiri
    │
    └─→ Klik "Kasir Warung" atau nama POS Anda
```

### Langkah 2: Buka Sesi Kasir
```
┌─────────────────────────────────────────┐
│  Anda lihat tombol biru "OPEN SESSION"  │
│                                         │
│  ┌─────────────────────────────────┐   │
│  │  OPEN SESSION (tombol besar)    │   │
│  └─────────────────────────────────┘   │
└─────────────────────────────────────────┘
```

### Langkah 3: Input Modal Awal
```
Muncul dialog: "Berapa uang awal kasir Anda?"

Contoh: 
┌──────────────────────────────┐
│ Jumlah: 100000               │  (untuk kembalian customer)
│                              │
│ ┌────────────────────────────┐
│ │    CONFIRM (klik)          │
│ └────────────────────────────┘
└──────────────────────────────┘
```

✅ Sekarang kasir sudah BUKA dan siap melayani!

---

## 🛒 MELAYANI CUSTOMER (PROSES TRANSAKSI)

### Layar Kasir Terlihat Seperti Ini:
```
┌─────────────────────────────────────────────────────┐
│  KASIR WARUNG - Layar Utama                        │
├─────────────────────┬───────────────────────────────┤
│                     │  DAFTAR PRODUK (Belum ada)   │
│                     │                              │
│  PRODUK TERSEDIA:   │                              │
│  ┌────────────┐     │  ┌──────────────────────┐   │
│  │ Teh Botol  │     │  │ TOTAL: Rp. 0         │   │
│  │  Rp.5.000  │     │  │                      │   │
│  └────────────┘     │  └──────────────────────┘   │
│  ┌────────────┐     │  ┌──────────────────────┐   │
│  │ Nasi Goreng│     │  │  [BAYAR/CHECKOUT]    │   │
│  │ Rp.15.000  │     │  │       (tombol)       │   │
│  └────────────┘     │  └──────────────────────┘   │
│  ┌────────────┐     │                              │
│  │ Rokok Catur│     │  [+ Order Baru]             │
│  │ Rp.30.000  │     │                              │
│  └────────────┘     │                              │
└─────────────────────┴───────────────────────────────┘
```

### Transaksi Pertama - Step by Step:

**STEP 1️⃣: Customer bilang "Saya mau teh botol 1, nasi goreng 2"**

```
Anda: Klik tombol "Teh Botol" SATU KALI
Hasil: Daftar kanan → Teh Botol 1x  Rp. 5.000

Anda: Klik tombol "Nasi Goreng" DUA KALI
Hasil: Daftar kanan → Nasi Goreng 2x  Rp. 30.000

TOTAL SEKARANG: Rp. 35.000
```

**STEP 2️⃣: Verifikasi Pesanan**

```
Lihat daftar kanan:
┌─────────────────────────────┐
│ Teh Botol 500ml   1x Rp.5k  │
│ Nasi Goreng       2x Rp.30k │
├─────────────────────────────┤
│ TOTAL:             Rp.35.000│
└─────────────────────────────┘

❓ Benar? Lanjut ke STEP 3
❌ Salah? Klik produk yang salah → klik "-" untuk kurangi
```

**STEP 3️⃣: Customer Bayar**

```
Klik tombol besar "BAYAR" atau "CHECKOUT"
│
└─→ Muncul dialog pembayaran:
    
    ┌───────────────────────────────┐
    │ Pilih cara bayar:             │
    │                               │
    │ [TUNAI]  [KARTU]  [TRANSFER] │
    │                               │
    └───────────────────────────────┘
```

**STEP 4️⃣: Jika Customer Bayar TUNAI**

```
┌──────────────────────────────────┐
│ Input uang yang diterima dari    │
│ customer:                        │
│                                  │
│ Uang Diterima: 50000             │
│ (customer bayar Rp. 50.000)      │
│                                  │
│ Sistem hitung otomatis:          │
│ TOTAL   : Rp. 35.000             │
│ BAYAR   : Rp. 50.000             │
│ KEMBALIAN: Rp. 15.000 ✓          │
│                                  │
│ ┌──────────────────────────────┐ │
│ │  ACCEPT / TERIMA (tombol)    │ │
│ └──────────────────────────────┘ │
└──────────────────────────────────┘
```

**STEP 5️⃣: STRUK TERPILIH**

```
┌──────────────────────────────┐
│  WARUNG ANDA                 │
│  Jl. Contoh No. 123          │
│  Tlp: 08xx-xxxx-xxxx         │
├──────────────────────────────┤
│ Teh Botol 500ml              │
│   1x @ Rp.5.000  = Rp.5.000 │
│                              │
│ Nasi Goreng                  │
│   2x @ Rp.15.000 = Rp.30.000│
├──────────────────────────────┤
│ TOTAL        : Rp. 35.000    │
│ BAYAR        : Rp. 50.000    │
│ KEMBALIAN    : Rp. 15.000    │
├──────────────────────────────┤
│ Terima kasih!                │
│ Tanggal: 22/12/2025 14:30    │
│ Kasir: kasir1                │
└──────────────────────────────┘

✓ Struk otomatis print ke printer
✓ Serahkan struk ke customer
✓ Berikan uang kembalian
```

**STEP 6️⃣: Selesai!**

```
✅ Transaksi 1 selesai
✅ Layar kembali ke kosong (siap order baru)
✅ Stok otomatis berkurang di sistem
✅ Uang masuk ke kas warung
```

---

## 🔄 TRANSAKSI KEDUA DAN SETERUSNYA

Ulangi STEP 1-6 di atas untuk setiap customer.

**Tips:**
- Pastikan customer bilang jumlah dengan jelas sebelum klik produk
- Double-check daftar sebelum klik BAYAR
- Jangan sampai lupa catat nota kalau customer tidak pakai struk

---

## ⏰ AKHIR HARI - TUTUP KASIR

### Setelah jam tutup / tidak ada customer lagi:

**LANGKAH 1: Hitung Uang Fisik**
```
1. Siapkan semua uang tunai dari kasir
2. Hitung berapa jumlah total
3. Catat di kertas

Contoh hasil:
Uang awal       : Rp. 100.000
Uang masuk      : Rp. 1.050.000 (dari semua transaksi)
TOTAL SEKARANG  : Rp. 1.150.000
```

**LANGKAH 2: Buka Menu Closing**
```
Di aplikasi → Cari "Closing" atau "Close Session"
│
└─→ Klik tombol "CLOSE KASIR" atau "CLOSE SESSION"
```

**LANGKAH 3: Input Uang Fisik**
```
┌────────────────────────────────┐
│ Closing Kasir - Akhir Hari     │
├────────────────────────────────┤
│ Sistem hitung dari transaksi:  │
│ TOTAL seharusnya: Rp. 1.150k   │
│                                │
│ Uang fisik yang Anda hitung:   │
│ Input: 1150000                 │
│        (atau jumlah sesungguh) │
│                                │
│ ┌───────────────────────────┐  │
│ │  CONFIRM CLOSING          │  │
│ └───────────────────────────┘  │
└────────────────────────────────┘
```

**LANGKAH 4: Review Laporan**
```
Sistem tampilkan laporan:

┌──────────────────────────────┐
│  LAPORAN PENJUALAN HARI INI  │
├──────────────────────────────┤
│ Total penjualan    : Rp.1.050k
│ Jumlah transaksi   : 15 transaksi
│ Kasir              : kasir1
│ Tanggal            : 22/12/2025
│ Waktu buka-tutup   : 09:00 - 17:00
│ Stok Berkurang:
│  - Teh Botol: 10 pcs
│  - Nasi Goreng: 8 pcs
│  - Rokok: 5 bungkus
├──────────────────────────────┤
│ ✓ CLOSING BERHASIL
└──────────────────────────────┘
```

**LANGKAH 5: Serahkan Uang ke Manager**
```
1. Print atau screenshot laporan
2. Catat:
   ├── Tanggal
   ├── Nama kasir
   ├── Total uang
   └── Jam buka-tutup
3. Serahkan:
   ├── Semua uang tunai
   ├── Struk (jika ada yang fisis)
   └── Laporan print
4. Manager verifikasi dan catat
```

---

## ⚠️ JIKA ADA KESALAHAN

### Salah Input Saat Order

```
Customer bilang: "Ganti, mau yang ini bukan itu"

Anda:
1. Lihat daftar kanan
2. Cari produk yang salah
3. Klik tombol "-" untuk kurangi qty
4. Jika sudah 0 → produk hilang dari daftar
5. Klik produk yang benar
```

### Belum Bayar Tapi Produk Sudah Diklik

```
Solusi:
1. Jangan klik BAYAR dulu
2. Klik "-" untuk hapus produk yang salah
3. Jika semua salah → klik "Cancel Order" atau "Clear"
4. Mulai lagi dari awal

⚠️ JANGAN BAYAR dulu sebelum yakin!
```

### Sudah Bayar Tapi Ternyata Salah

```
Hubungi manager SEGERA!

Manager bisa:
- Return produk
- Buat refund/pengembalian uang
- Catat note di sistem
- Jangan hapus transaksi sendiri!
```

### Aplikasi Freeze / Macet

```
Solusi cepat:
1. Tunggu 10-15 detik (mungkin sedang loading)
2. Klik tombol "Reload" atau tekan F5
3. Jika masih macet → Lock screen
4. Hubungi manager
5. Manager bisa restart aplikasi
```

---

## 📱 SHORTCUT & TOMBOL PENTING

| Tombol / Shortcut | Fungsi | Kapan Digunakan |
|---|---|---|
| **[OPEN SESSION]** | Buka kasir | Pagi sebelum mulai |
| **Klik Produk** | Tambah ke daftar | Setiap customer order |
| **[-] Minus** | Kurangi qty | Salah input atau perubahan order |
| **[BAYAR/CHECKOUT]** | Pembayaran | Setelah order fix |
| **[TUNAI/KARTU/...]** | Pilih metode bayar | Saat pembayaran |
| **[CONFIRM]** | Konfirmasi | Banyak dialog |
| **[CLOSE SESSION]** | Tutup kasir | Akhir hari |
| **F5** | Refresh halaman | Jika slow/macet |
| **Ctrl+Alt+Delete** | Lock screen | Pergi sejenak |

---

## ✅ CHECKLIST HARIAN

### PAGI (Sebelum Buka)
- ☐ Login ke aplikasi
- ☐ Klik "OPEN SESSION"
- ☐ Input jumlah modal kas (biasanya Rp.100k-500k)
- ☐ Verifikasi semua produk sudah ada di list

### SIANG (Saat Melayani)
- ☐ Dengarkan order customer dengan baik
- ☐ Input produk dengan benar
- ☐ Verifikasi daftar sebelum bayar
- ☐ Berikan struk & kembalian dengan benar
- ☐ Jangan logout tanpa tutup kasir

### SORE (Akhir Hari)
- ☐ Hitung uang fisik
- ☐ Buka menu "CLOSE SESSION"
- ☐ Input jumlah uang yang dihitung
- ☐ Review laporan penjualan
- ☐ Serahkan uang + laporan ke manager
- ☐ Logout dari aplikasi

---

## 📞 HUBUNGI MANAGER JIKA:

```
⚠️ URGENT CALL:
├── Transaksi sudah bayar tapi system error
├── Aplikasi crash / tidak bisa buka
├── Ada customer complaint
├── Struk printer tidak jalan
├── Sudah tutup kasir tapi ada customer datang
└── Tidak yakin input produk

💬 NORMAL REPORT:
├── Serah laporan harian
├── Tanya tentang produk baru
├── Lapor stok hampir habis
└── Minta perubahan harga produk
```

---

## 💡 TIPS PENTING

```
✓ JANGAN PERNAH:
  ✗ Logout tanpa tutup kasir duluan
  ✗ Tinggalkan kasir terbuka tanpa awas
  ✗ Lupa kunci screen (Ctrl+Alt+Del) saat pergi
  ✗ Bagikan password dengan orang lain
  ✗ Hapus transaksi atau ubah data setelah bayar
  ✗ Catat transaksi di kertas tanpa aplikasi

✓ SELALU LAKUKAN:
  ✓ Dengarkan order customer dengan teliti
  ✓ Double-check sebelum klik BAYAR
  ✓ Lock screen kalau pergi dari kasir
  ✓ Report error ke manager SEGERA
  ✓ Hitung uang dengan teliti sebelum tutup
  ✓ Laporkan stok yang hampir habis
  
✓ INGAT:
  ✓ Manager bisa lihat semua transaksi Anda di laporan
  ✓ Aplikasi mencatat waktu dan jam tiap transaksi
  ✓ Semua uang harus masuk sistem, jangan private
  ✓ Customer adalah prioritas pertama
```

---

## 🎯 PRACTICE SCENARIO

**SIMULASI TRANSAKSI (Latihan sendiri sebelum go-live):**

```
Customer 1:
"Kak, saya mau teh botol 1, bakso 1, rokok catur 2"

Action Anda:
1. Klik "Teh Botol" - 1x
2. Klik "Bakso" - 1x
3. Klik "Rokok Catur" - 2x
4. Verifikasi daftar
5. Klik BAYAR
6. Customer bayar tunai Rp. 100k (totalnya Rp. 80k)
7. Input uang Rp. 100k
8. Sistem hitung kembalian Rp. 20k
9. Klik CONFIRM
10. Berikan struk & kembalian

---

Customer 2:
"2 indomie goreng, 1 teh tarik"

Action Anda:
[Ikuti cara yang sama seperti Customer 1]

---

Customer 3:
"Mau 1 rokok marlboro, tapi tunggu pembayaran pake transfer"

Action Anda:
1. Klik "Rokok Marlboro" - 1x
2. Klik BAYAR
3. Pilih "TRANSFER"
4. Input jumlah
5. Tunggu customer bayar via transfer
6. Manager verifikasi pembayaran
7. Klik CONFIRM kalau sudah terima transfer
```

---

## 📞 KONTAK SUPPORT

```
Manager Warung    : [Nama & Nomor Manager]
Support Odoo      : [Nomor IT Support jika ada]
Hotline Teknis    : [Nomor emergency support]

JIKA HANG/CRASH:
1. Restart browser
2. Hubungi manager
3. Jangan asal-asalan hapus data
```

---

## 📄 SIGNATURE TRAINING

Saya menyatakan sudah menerima training penggunaan sistem kasir:

```
Nama Karyawan     : _____________________
Tanda Tangan      : _____________________
Tanggal Training  : _____________________
Nama Manager      : _____________________
Tanda Tangan      : _____________________

---
Panduan ini diberikan tanggal: _____________________
Karyawan menyetujui untuk mengikuti prosedur: ___
```

---

**📌 SIMPAN PANDUAN INI!**
- Print dan tempel di dekat kasir
- Simpan juga versi digital
- Tanya manager jika ada yang tidak paham
- Jangan malu bertanya!

---

*Panduan dibuat untuk kemudahan karyawan warung.*  
*Version: 1.0 | Odoo 18.0 POS*
