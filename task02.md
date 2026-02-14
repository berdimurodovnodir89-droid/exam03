# Task 2: Cinema Booking

## Loyiha Haqida

### Nima Qilamiz?
Siz kinoteattr uchun chipta bron qilish tizimini yozasiz. 

**Real hayotiy misol:**
- Kinoteatrda bitta film ko'rsatiladi (masalan: "Avatar 2")
- Zalda 5 ta o'rin bor (1, 2, 3, 4, 5 raqamli)
- Odamlar kelib o'rinlarni bron qilishadi
- Har bir o'rin faqat **bir marta** band qilinishi mumkin

### Tizim Qanday Ishlaydi?

```
1. Kinoteattr admin "Avatar 2" filmiga seans yaratadi (5 o'rinli)
2. Ali kelib 3-raqamli o'ringa chipta bron qiladi
3. Vali kelib 1-raqamli o'ringa chipta bron qiladi
4. Sardor 3-raqamga bron qilmoqchi → MUMKIN EMAS (Ali olgan)
5. Tizim bo'sh joylarni ko'rsatadi: [2, 4, 5]
```

### Klasslar Strukturasi

```
CinemaSession (Seans)
 ├── Seat (O'rin) - har bir stul/o'rin
 └── Ticket (Chipta) - kim qaysi o'ringa chipta olgan
```

**Nested Class Nima?**
`Seat` va `Ticket` classlarini `CinemaSession` **ichida** yozamiz. Chunki o'rinlar va chiптalar faqat seans mavjud bo'lganda kerak. Seans yo'q = o'rinlar ham yo'q.

---

## Umumiy Tavsif
Kinoteattr uchun oddiy chipta bron qilish tizimi. Faqat bron qilish va bo'sh joylarni ko'rish.

**Muhim:** Yordamchi classlar (`Seat`, `Ticket`) faqat `CinemaSession` **ichida** yoziladi.

---

## 1. Asosiy Class

```python
class CinemaSession:
    # Nested classlar shu yerda
```

### Constructor

```python
CinemaSession(movie_title: str, total_seats: int)
```

### Validatsiya
- `movie_title` - bo'sh emas → `ValueError`
- `total_seats` - 0 dan katta → `ValueError`

### Attributelar

| Nomi | Turi | Tavsif |
|------|------|--------|
| `movie_title` | str | Film nomi |
| `total_seats` | int | Jami o'rinlar |
| `seats` | list[Seat] | Barcha o'rinlar (1 dan total_seats gacha) |
| `bookings` | list[Ticket] | Bron qilingan chiптalar |

**Eslatma:** Constructor da `seats` listini yaratib, ichiga `Seat(1)`, `Seat(2)`, ... `Seat(total_seats)` qo'shish kerak.

---

## 2. Nested Classlar

### 2.1 `Seat` (Nested)

**Constructor:**
```python
Seat(number: int)
```

**Attributelar:**

| Nomi | Turi | Boshlang'ich | Tavsif |
|------|------|--------------|--------|
| `number` | int | constructordan | O'rin raqami |
| `is_taken` | bool | `False` | Bandmi? |

---

### 2.2 `Ticket` (Nested)

**Constructor:**
```python
Ticket(seat: Seat, owner: str)
```

**Attributelar:**

| Nomi | Turi | Tavsif |
|------|------|--------|
| `seat` | Seat | Qaysi o'rin |
| `owner` | str | Kim olgan |

---

## 3. Metodlar

### `available_seats() -> list[int]`

Bo'sh o'rinlar raqamini qaytaradi.

**Bajarilishi:**
- `self.seats` ichidan `is_taken == False` bo'lganlarning `number` ini listga yig'ish

---

### `book_seat(seat_number: int, user: str) -> Ticket`

Chipta bron qiladi.

**Bajarilishi:**
1. `seat_number` to'g'ri oraliqda borligini tekshirish (1 ≤ seat_number ≤ total_seats)
   - Agar yo'q bo'lsa → `ValueError`
2. `self.seats` dan tegishli `Seat` ni topish
3. Agar `seat.is_taken == True` → `RuntimeError` (allaqachon olingan)
4. `seat.is_taken = True` qilish
5. `Ticket(seat, user)` yaratish
6. `self.bookings` ga qo'shish
7. Ticket ni qaytarish

---

### `__str__() -> str`

```python
"CinemaSession: Avatar 2 (5 seats)"
```

Format: `CinemaSession: {movie_title} ({total_seats} seats)`

---

## 4. Foydalanish

```python
# Seans yaratish
session = CinemaSession("Avatar 2", 5)

# Bo'sh joylar
print(session.available_seats())  # [1, 2, 3, 4, 5]

# Bron qilish
ticket1 = session.book_seat(3, "Ali")
print(ticket1.owner)  # "Ali"
print(ticket1.seat.number)  # 3

# Bo'sh joylar
print(session.available_seats())  # [1, 2, 4, 5]

# Yana bron
ticket2 = session.book_seat(1, "Vali")

# Bo'sh joylar
print(session.available_seats())  # [2, 4, 5]

# Olingan joyga yana bron (xato)
session.book_seat(3, "Sardor")  # RuntimeError

# String
print(session)  # CinemaSession: Avatar 2 (5 seats)
```

---

## 5. Muhim Nuqtalar

✅ **Seat va Ticket nested** - global emas, faqat CinemaSession ichida

✅ **Constructor seats yaratadi** - boshida barcha o'rinlar bo'sh

✅ **book_seat Ticket qaytaradi** - to'g'ri return type

✅ **Band o'ringa bron qilib bo'lmaydi** - RuntimeError

✅ **available_seats to'g'ri ishlaydi** - faqat bo'sh joylar
