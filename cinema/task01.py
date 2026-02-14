class Seat:
    def __init__(self, number: int):
        self.number = number
        self.is_taken = False


class Ticket:
    def __init__(self, seat: Seat, owner: str):
        self.seat = seat
        self.owner = owner


class CinemaSession:
    def __init__(self, movie_title: str, total_seats: int):
        if movie_title.strip() == "":
            raise ValueError("movie_title bo'sh bo'lmasligi kerak")
        if total_seats <= 0:
            raise ValueError("total_seats 0 dan katta bo'lishi kerak")

        self.movie_title = movie_title
        self.total_seats = total_seats
        self.seats = []
        self.bookings = []

        for i in range(1, total_seats + 1):
            self.seats.append(Seat(i))

    def available_seats(self):
        result = []
        for seat in self.seats:
            if not seat.is_taken:
                result.append(seat.number)
        return result

    def book_seat(self, seat_number: int, user: str):
        if seat_number < 1 or seat_number > self.total_seats:
            raise ValueError("Bunday o'rin mavjud emas")

        seat = self.seats[seat_number - 1]

        if seat.is_taken:
            raise RuntimeError("O'rin allaqachon olingan")

        seat.is_taken = True
        ticket = Ticket(seat, user)
        self.bookings.append(ticket)
        return ticket

    def __str__(self):
        return f"CinemaSession: {self.movie_title} ({self.total_seats} seats)"


session = CinemaSession("Avatar 2", 5)


print(session.available_seats())

ticket1 = session.book_seat(3, "Ali")
print(ticket1.owner)
print(ticket1.seat.number)
print(ticket1.seat.is_taken)


print(session.available_seats())


ticket2 = session.book_seat(1, "Vali")
print(session.available_seats())

try:
    session.book_seat(3, "Sardor")
except RuntimeError:
    print("Xato: O'rin allaqachon olingan!")


print(session)

print(len(session.bookings))


for ticket in session.bookings:
    print(f"O'rin {ticket.seat.number}: {ticket.owner}")
