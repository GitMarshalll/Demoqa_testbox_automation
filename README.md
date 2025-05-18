# DemoQA Form Automation Tests (Selenium + Pytest)

Bu loyiha [DemoQA Text Box formasi](https://demoqa.com/text-box) uchun yozilgan "avtomatlashtirilgan testlar" to‘plamidir. Testlar `Selenium WebDriver` va `Pytest` yordamida ishlab chiqilgan.

## Maqsad

Formani to‘ldirishdagi quyidagi holatlarni avtomatik sinash:
1. To‘g‘ri (valid) ma’lumotlar bilan yuborish
2. Noto‘g‘ri email (invalid email) yuborish (negative test)
3. Kirill yozuvida yuborilgan ma’lumotlarga sayt qanday munosabatda bo‘lishini tekshirish

## Test Fayllari

| Fayl nomi | Tavsifi |
|-----------|---------|
| `test_valid_input_latin.py` | Lotin yozuvidagi to‘g‘ri ma’lumotlar bilan forma yuboriladi |
| `test_invalid_input_negative_case.py` | Email noto‘g‘ri formatda yuboriladi (masalan: `$` ishlatiladi) |
| `test_cyrillic_input.py` | Kirill yozuvlar (`Али`, `Тошкент`, `Юнусобод`) bilan forma to‘ldiriladi |

## Talablar
- Python 3.11
- Google Chrome (eng so‘ngi versiya)


## Testlarni Ishga Tushirish

```bash
pytest test_valid_input_latin.py
pytest test_invalid_input_negative_case.py
pytest test_cyrillic_input.py
```

Yoki barchasini birgalikda:

```bash
pytest
```

## Eslatma

- `time.sleep()` faqatgina testlarda elementlar to‘liq yuklanishini kutish uchun ishlatilgan.
- Har bir test `assert` yordamida tekshiriladi — agar test muvaffaqiyatli o‘tsa, konsolda ✅ chiqadi.

## Muallif

QA Automation Tester: Usmonkhojayev Mokhirkhoja
Email: usmonxojayv@gmail.com

