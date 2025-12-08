from django.test import TestCase
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from .models import Airport, Route, AirplaneType, Airplane, Flight, Crew, Order, Ticket

class AirportModelTest(TestCase):
    def test_str(self):
        airport = Airport.objects.create(name="WAW", closest_big_city="Warsaw")
        self.assertEqual(str(airport), "WAW (Warsaw)")

class RouteModelTest(TestCase):
    def test_str(self):
        a1 = Airport.objects.create(name="GDN", closest_big_city="GDN")
        a2 = Airport.objects.create(name="ALC", closest_big_city="Alicante")
        route = Route.objects.create(source=a1, destination=a2, distance=2500)
        self.assertEqual(str(route), f"{a1} -> {a2}")

class AirplaneTypeModelTest(TestCase):
    def test_str(self):
        at = AirplaneType.objects.create(name="Boeing 737")
        self.assertEqual(str(at), "Boeing 737")

class AirplaneModelTest(TestCase):
    def test_str(self):
        at = AirplaneType.objects.create(name="Boeing 737")
        plane = Airplane.objects.create(name="Plane1", rows=20, seats_in_row=6, airplane_type=at)
        self.assertEqual(str(plane), "Plane1")

class FlightModelTest(TestCase):
    def test_str(self):
        a1 = Airport.objects.create(name="GDN", closest_big_city="GDN")
        a2 = Airport.objects.create(name="ALC", closest_big_city="Alicante")
        route = Route.objects.create(source=a1, destination=a2, distance=2500)
        airplane_type = AirplaneType.objects.create(name="B737")
        airplane = Airplane.objects.create(name="PlaneX", rows=10, seats_in_row=4, airplane_type=airplane_type)
        departure = datetime.now()
        arrival = departure + timedelta(hours=2)
        flight = Flight.objects.create(route=route, airplane=airplane, departure_time=departure, arrival_time=arrival)
        self.assertEqual(str(flight), f"{route} ({departure} -> {arrival})")

class CrewModelTest(TestCase):
    def test_str(self):
        crew = Crew.objects.create(first_name="John", last_name="Doe")
        self.assertEqual(str(crew), "John Doe")

class OrderModelTest(TestCase):
    def test_str(self):
        user = User.objects.create(username="user1")
        order = Order.objects.create(user=user)
        self.assertEqual(str(order), f"Order {order.id} by {user}")

class TicketModelTest(TestCase):
    def test_str(self):
        a1 = Airport.objects.create(name="GDN", closest_big_city="GDN")
        a2 = Airport.objects.create(name="ALC", closest_big_city="Alicante")
        route = Route.objects.create(source=a1, destination=a2, distance=2300)
        airplane_type = AirplaneType.objects.create(name="B737")
        airplane = Airplane.objects.create(name="Plane1", rows=10, seats_in_row=4, airplane_type=airplane_type)
        departure = datetime.now()
        arrival = departure + timedelta(hours=1)
        flight = Flight.objects.create(route=route, airplane=airplane, departure_time=departure, arrival_time=arrival)
        user = User.objects.create(username="user2")
        order = Order.objects.create(user=user)
        ticket = Ticket.objects.create(row=1, seat=2, flight=flight, order=order)
        self.assertEqual(str(ticket), f"Ticket {ticket.id} for {flight}")
