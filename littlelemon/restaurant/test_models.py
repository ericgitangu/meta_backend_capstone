from django.test import TestCase
from .models import Menu, Booking, User


class MenuModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("\n\n---- 2. Test Setup Menu Model----")
        Menu.objects.create(
            title='Burger',
            inventory=10,
            price=9.99,
            description='Delicious burger'
        )
        print('\tSetup complete for Menu Model ✅')

    def test_get_item(self):
        print("\n---- 2. Testing get_item method (Menu Model)----")
        menu = Menu.objects.get(title='Burger')
        expected_item = 'Burger : 9.99'
        self.assertEqual(str(menu), expected_item)
        print('\tPassed get_item method ✅')

    def test_get_all_items(self):
        print("\n---- 2. Testing get_all_items method (Menu Model)----")
        menu1 = Menu.objects.create(title='Pizza', inventory=5, price=12.99)
        menu2 = Menu.objects.create(title='Salad', inventory=8, price=7.99)
        menu3 = Menu.objects.create(title='Pasta', inventory=3, price=10.99)

        expected_items = ['Burger', 'Pasta', 'Pizza', 'Salad']
        actual_items = sorted(Menu.objects.values_list('title', flat=True))
        self.assertEqual(actual_items, expected_items)
        print('\tPassed get_all_items method ✅')

    def test_ordering(self):
        print("\n---- 2. Testing menu items ordering (Menu Model)----")
        menu1 = Menu.objects.create(title='Pizza', inventory=5, price=12.99)
        menu2 = Menu.objects.create(title='Salad', inventory=8, price=7.99)
        menu3 = Menu.objects.create(title='Pasta', inventory=3, price=10.99)

        expected_ordering = ['Burger', 'Pasta', 'Pizza', 'Salad']
        actual_ordering = list(Menu.objects.values_list('title', flat=True))
        self.assertEqual(actual_ordering, expected_ordering)
        print('\tPassed menu items ordering ✅')
    
    def test_verbose_name_plural(self):
        print("\n---- 2. Testing verbose_name_plural (Menu Model)----")
        self.assertEqual(str(Menu._meta.verbose_name_plural), 'Menu')
        print('\tPassed verbose_name_plural ✅')
    
    def test_string_representation(self):
        print("\n---- 2. Testing string representation (Menu Model)----")
        menu = Menu.objects.get(title='Burger')
        self.assertEqual(str(menu), 'Burger : 9.99')
        print('\tPassed string representation ✅')
    
    def test_title_max_length(self):
        print("\n---- 2. Testing title max length (Menu Model)----")
        menu = Menu.objects.get(title='Burger')
        max_length = menu._meta.get_field('title').max_length
        self.assertEqual(max_length, 255)
        print('\tPassed title max length ✅')
    
    def test_inventory_default(self):
        print("\n---- 2. Testing inventory default value (Menu Model)----")
        menu = Menu.objects.get(title='Burger')
        self.assertEqual(menu.inventory, 10)
        print('\tPassed inventory default value ✅')

    def test_price_max_digits(self):
        print("\n---- 2. Testing price max digits (Menu Model)----")
        menu = Menu.objects.get(title='Burger')
        max_digits = menu._meta.get_field('price').max_digits
        self.assertEqual(max_digits, 5)
        print('\tPassed price max digits ✅')
    
    def test_price_decimal_places(self):
        print("\n---- 2. Testing price decimal places (Menu Model)----")
        menu = Menu.objects.get(title='Burger')
        decimal_places = menu._meta.get_field('price').decimal_places
        self.assertEqual(decimal_places, 2)
        print('\tPassed price decimal places ✅')
    
    def test_description_null(self):
        print("\n---- 2. Testing description null (Menu Model)----")
        menu = Menu.objects.get(title='Burger')
        self.assertEqual(menu.description, 'Delicious burger')
        print('\tPassed description null ✅')

    def test_description_blank(self):
        print("\n---- 2. Testing description blank (Menu Model)----")
        menu = Menu.objects.get(title='Burger')
        self.assertEqual(menu.description, 'Delicious burger')
        print('\tPassed description blank ✅')
    
    def test_description_max_length(self):
        print("\n---- 2. Testing description max length (Menu Model)----")
        menu = Menu.objects.get(title='Burger')
        max_length = menu._meta.get_field('description').max_length
        self.assertIsNone(max_length)
        print('\tPassed description max length ✅')
    
    def test_update_menu_item(self):
        print("\n---- 2. Testing update menu item (Menu Model)----")
        menu = Menu.objects.get(title='Burger')
        menu.title = 'Cheeseburger'
        menu.price = 10.99
        menu.save()

        updated_menu = Menu.objects.get(id=menu.id)
        self.assertEqual(updated_menu.title, 'Cheeseburger')
        self.assertEqual(str(updated_menu.price), '10.99')
        print('\tPassed update menu item ✅')
    
    def test_delete_menu_item(self):
        print("\n---- 2. Testing delete menu item (Menu Model)----")
        menu = Menu.objects.get(title='Burger')
        menu.delete()
        self.assertEqual(Menu.objects.count(), 0)
        print('\tPassed delete menu item ✅')


class BookingModelTest(TestCase):

    def setUp(self):
        print("\n\n---- 3. Test Setup Booking Model ----")
        Booking.objects.create(
            name='John Doe',
            phone='1234567890',
            email= 'johndoe@email.com',
            reservation_date='2022-01-01',
            reservation_slot='12:00:00'
        )

        print("\tSetup complete for Booking ✅")
    
    def tearDown(self):
        print("---- 3. Test Teardown Booking Model----")
        Booking.objects.all().delete()
        print('\tTeardown complete ✅')

    def test_string_representation(self):
        print("\n---- 3. Testing string representation (Booking Model)----")
        booking = Booking.objects.create(
            name='John Doe',
            phone='1234567890',
            email='johndoe@example.com',
            reservation_date='2022-01-01',
            reservation_slot='12:00:00'
        )
        expected_string = 'John Doe : 2022-01-01 - 12:00:00'
        self.assertEqual(str(booking), expected_string)
        print('\tPassed string representation ✅')

    # def test_ordering(self):
    #     print("\n----Testing booking ordering----")
    #     Booking.objects.all().delete()
    #     booking1 = Booking.objects.create(
    #         name='John Doe',
    #         phone='1234567890',
    #         email='johndoe@example.com',
    #         reservation_date='2022-01-01',
    #         reservation_slot='12:00:00'
    #     )
    #     booking2 = Booking.objects.create(
    #         name='Jane Smith',
    #         phone='0987654321',
    #         email='janesmith@example.com',
    #         reservation_date='2022-01-02',
    #         reservation_slot='14:00:00'
    #     )
    #     booking3 = Booking.objects.create(
    #         name='Alice Johnson',
    #         phone='9876543210',
    #         email='alicejohnson@example.com',
    #         reservation_date='2022-01-01',
    #         reservation_slot='10:00:00'
    #     )

    #     expected_ordering = [
    #         f'Alice Johnson : {{datetime.str2022-01-01}} - 10:00:00',
    #         f'John Doe : 2022-01-01 - 12:00:00',
    #         f'Jane Smith : 2022-01-02 - 14:00:00'
    #     ]
    #     actual_ordering = list(Booking.objects.values_list('name', 'reservation_date', 'reservation_slot'))
    #     self.assertEqual(actual_ordering, expected_ordering)
    #     Booking.object().all().delete()
    #     print('\tPassed booking ordering ✅')

    def test_update_reservation(self):
        print("\n---- 3. Testing updating a reservation (Booking Model)----")
        # Create a booking
        booking = Booking.objects.create(
            name='John Doe',
            phone='1234567890',
            email='johndoe@example.com',
            reservation_date='2022-01-01',
            reservation_slot='12:00:00'
        )

        # Update the reservation
        booking.name = 'Jane Smith'
        booking.save()

        # Retrieve the updated reservation from the database
        updated_booking = Booking.objects.get(pk=booking.pk)

        # Check if the name has been updated
        self.assertEqual(updated_booking.name, 'Jane Smith')
        booking.delete()
        print('\tPassed updating a reservation ✅')

    def test_delete_reservation(self):
        print("\n---- 3. Testing deleting a reservation (Booking Model)----")
        # Create a booking
        booking = Booking.objects.create(
            name='John Doe',
            phone='1234567890',
            email='johndoe@email.com',
            reservation_date='2022-01-01',
            reservation_slot='12:00:00'
        )
        booking.delete()
        print("\t Passed deleting a reservation ✅")

    
