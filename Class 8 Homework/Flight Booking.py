class Flight:
    def __init__(self,flight_num,destination,seats,base_price):
        self.flight_num = flight_num
        self.destination = destination
        self.seats_available = seats
        self.base_price = base_price

    def book_ticket(self,passenger_name):
        if self.seats_available >= 1:
            self.seats_available -= 1
            confirmation = input(f"Dear {passenger_name}, do you confirm a booking for {self.flight_num} to {self.destination}?(yes/no) ")
            if confirmation.lower() == "yes":
                print(f"Dear {passenger_name}, a booking has been made under your name.")
            else:
                print("Booking has been canceled.")

        else:
            print("This flight doesn't have enough seats left.")

    def ticket_price(self):
        pass
    
    def display_flight_info(self):
        pass

class Domestic_flight(Flight):
    def __init__(self,flight_num,destination,seats,base_price):
        super().__init__(flight_num,destination,seats,base_price)

    def ticket_price(self):
        price = self.base_price + (self.base_price*0.05)
        print(f"Price = {price}")

class International_flight(Flight):
    def __init__(self,flight_num,destination,seats,base_price):
        super().__init__(flight_num,destination,seats,base_price)

    def ticket_price(self):
        price = self.base_price + (self.base_price*0.10) + (self.base_price*0.20)
        print(f"Price = {price}")

class Passenger:
    def __init__(self, name, passport_number):
        self.passenger_name = name
        self.passport_num = passport_number

    def book_flight(self,flight):
        Flight.book_ticket(self.passenger_name)