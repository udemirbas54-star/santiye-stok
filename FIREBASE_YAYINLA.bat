@echo off
chcp 65001 >nul
echo ========================================================
echo   ŞANTİYE STOK, ZİMMET VE FATURA SİSTEMİ - FIREBASE YAYINLAMA
echo   Proje: santiye-stok (https://santiye-stok.web.app)
echo ========================================================
echo.
cd /d "%~dp0"
echo 1. Firebase hesabınız kontrol ediliyor...
call npx -y firebase-tools login
echo.
echo 2. Uygulama ve Firestore kuralları santiye-stok projesine yükleniyor...
call npx -y firebase-tools deploy --project santiye-stok
echo.
echo ========================================================
echo   İşlem tamamlandı! Uygulamanıza şu adresten erişebilirsiniz:
echo   https://santiye-stok.web.app
echo ========================================================
pause
