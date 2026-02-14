# Python OOP Final Exam

## Exam Haqida

Ushbu exam Python OOP (Object-Oriented Programming) bo'yicha bilimingizni tekshirish uchun mo'ljallangan. Exam 3 ta mustaqil taskdan iborat bo'lib, har biri turli OOP konsepsiyalarini qamrab oladi.

**Umumiy vaqt:** 3-4 soat  
**Jami ballar:** 100 ball  
**O'tish balli:** 60 ball

---

## 📋 Tasklar

| # | Mavzu | Ball | Qiyinlik | Fayl |
|---|-------|------|----------|------|
| 1 | Book Class - Attributes & Methods | 35 | ⭐⭐ | [task01.md](task01.md) |
| 2 | Cinema Booking - Nested Classes | 30 | ⭐⭐⭐ | [task02.md](task02.md) |
| 3 | Random Image Bot - Architecture | 35 | ⭐⭐⭐ | [task03.md](task03.md) |

---

## 📚 Task Tavsifi

### [Task 1: Book Class](task01.md)
Kutubxona tizimi uchun kitob klassini yarating.

**O'rganiladi:**
- Class va Constructor
- Public attributes
- Instance methods
- Dunder methods (`__str__`, `__repr__`, `__eq__`, `__len__`, `__bool__`)
- Input validation
- State management

---

### [Task 2: Cinema Booking](task02.md)
Kinoteattr uchun chipta bron qilish tizimi.

**O'rganiladi:**
- Nested classes
- Composition
- Object relationships
- Lifecycle management
- Encapsulation

---

### [Task 3: Random Image Bot](task03.md)
Telegram bot - random hayvon rasmlari.

**O'rganiladi:**
- Code architecture
- Separation of concerns
- External API integration
- Telegram bot development
- Class design

---

## ⚙️ Texnik Talablar

### Muhit
- Python 3.8+
- Virtual environment ishlatish tavsiya etiladi

### Kutubxonalar

**Task 1 & 2:**
```bash
# Faqat standart kutubxonalar
from datetime import datetime
```

**Task 3:**
```bash
pip install python-telegram-bot==13.15
pip install requests
```

---

## 📝 Umumiy Qoidalar

### 1. Kod Sifati
- ✅ To'g'ri Python naming conventions
- ✅ Docstring yozish (ixtiyoriy, lekin tavsiya etiladi)
- ✅ Clean code printsiplari
- ❌ Commented code qoldirmaslik
- ❌ Keraksiz print() statements

### 2. Strukturaviy Talablar
- ✅ Har bir task alohida fayl/papkada
- ✅ Classlar to'g'ri tuzilishi
- ✅ Method signatures task tavsifiga mos
- ❌ Global o'zgaruvchilar (agar zarur bo'lmasa)

### 3. Error Handling
- ✅ To'g'ri exception typelar (`ValueError`, `RuntimeError`)
- ✅ Validation qoidalariga rioya qilish
- ❌ Try-except bilan xatolarni yashirish

### 4. Testing
Har bir task uchun o'zingizning test kodlarini yozing:
```python
# test_book.py misoli
book = Book(1, "Clean Code", "Robert Martin", 464)
book.borrow("Ali")
assert book.is_borrowed == True
assert book.borrower == "Ali"
print("✅ Test passed")
```

---

## 🎯 Baholash Mezonlari

### Task 1: Book Class (35 ball)
- Constructor va validation: 5 ball
- Attributes to'g'ri: 5 ball
- Core methods (`borrow`, `return_book`, `change_title`, `archive`): 12 ball
- Dunder methods: 8 ball
- `info()` method: 5 ball

### Task 2: Cinema Booking (30 ball)
- Nested classes to'g'ri joylashgan: 10 ball
- Constructor va initialization: 5 ball
- `book_seat()` to'g'ri ishlaydi: 10 ball
- `available_seats()` to'g'ri: 3 ball
- `__str__()` mavjud: 2 ball

### Task 3: Random Image Bot (35 ball)
- Arxitektura to'g'ri (3 class): 12 ball
- API integration ishlaydi: 10 ball
- Telegram handlers to'g'ri: 8 ball
- Inline keyboard mavjud: 3 ball
- `send_photo()` ishlatilgan: 2 ball

---

## 📤 Topshirish

### Fayl Tuzilishi
```
exam03/
├── README.md (ushbu fayl)
├── task01/
│   ├── book.py
│   └── test_book.py (ixtiyoriy)
├── task02/
│   ├── cinema.py
│   └── test_cinema.py (ixtiyoriy)
└── task03/
    ├── api_client.py
    ├── image_service.py
    ├── handlers.py
    ├── main.py
    └── requirements.txt
```

### Git Orqali Topshirish
```bash
# Repository yaratish
git init
git add .
git commit -m "Final exam solution"
git remote add origin <your-repo-url>
git push -u origin main
```

---

## ❓ Ko'p So'raladigan Savollar

**Q: Barcha taskni bajarishim shartmi?**  
A: Ha, 60 ball olish uchun kamida 2 ta taskni to'liq bajarishingiz kerak.

**Q: Internet'dan kod ko'chirsam bo'ladimi?**  
A: Yo'q. Plagiarism aniqlansa 0 ball.

**Q: Task qiyinroq bo'lsa nima qilaman?**  
A: Task 1 dan boshlang - u eng oson. Keyin Task 2 yoki 3 ni tanlang.

**Q: Test yozish majburiyatmi?**  
A: Yo'q, lekin kodingiz ishlashini tekshirish uchun yozishni tavsiya etamiz.

**Q: Qo'shimcha kutubxona ishlatsa bo'ladimi?**  
A: Faqat task tavsifida ko'rsatilganlarni ishlating.

---

## 🚀 Boshlash

1. **Task fayllarini o'qing:**
   - [task01.md](task01.md) - Book Class
   - [task02.md](task02.md) - Cinema Booking
   - [task03.md](task03.md) - Random Image Bot

2. **Virtual environment yarating:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. **Kodlashni boshlang!**

---

**Omad tilaymiz! 🎓**
