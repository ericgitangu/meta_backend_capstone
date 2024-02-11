# Backend Capstone - META Certification Capstone Project for the Backend Specialization

## Project objectives

1. Using Djoser and DRF for Authentication on the project level using a router, api is the root API endpoint

2. User Endpoints note only admins can change users, menu items, and bookings, users can view the menu items and need to be authenticated to make a reservation.

3. API throttling implemented for unauthenticated users to 10 calls/min and 20 calls/mins for authenticated uses.

4. Filtering, pagination and search features for the APIs implemented.

5. Endpoints - Users, Menu-items, Bookings, Managers with granular access, users, managers and admins

This repository contains the backend code for the capstone project.

## Endpoints

### Profile View

- URL: `/profile`
- Method: GET
- Description: Displays the user profile.
- Authentication: Requires the user to be logged in.
- Template: `profile.html`

### Home View

- URL: `/`
- Method: GET
- Description: Renders the index page.
- Template: `index.html`

### About View

- URL: `/about`
- Method: GET
- Description: Renders the about page.
- Template: `about.html`

### Reservations View

- URL: `api/reservations`
- Method: GET
- Description: Retrieves the reservations for a specific date and renders them in a template.
- Template: `bookings.html`

### Reservations Item View

- URL: `api/reservations/{pk}`
- Method: GET
- Description: Retrieves a specific reservation or all reservations.
- Parameters:
  - `pk` (optional): The primary key of the reservation to retrieve.
- Template: `booking_item.html`

### Book View (Reservations)

- URL: `api/book`
- Method: GET
- Description: Renders the booking form if the user is authenticated, otherwise redirects to the login page.
- Authentication: Requires the user to be logged in.
- Template: `book.html`

- URL: `/apibook`
- Method: POST
- Description: Saves the booking if the user is authenticated and the form is valid, otherwise renders the booking form or the login page.
- Authentication: Requires the user to be logged in.
- Template: `book.html` or `login.html`

### Booking Item View

- URL: `api/bookings/{pk}`
- Method: GET
- Description: Retrieves a specific booking or all bookings.
- Parameters:
  - `pk` (optional): The primary key of the booking to retrieve.
- Template: `booking_item.html`

### Menu View

- URL: `api/menu`
- Method: GET
- Description: Renders the menu page with the menu data.
- Template: `menu.html`

### Menu Item View

- URL: `api/menu/{pk}`
- Method: GET
- Description: Retrieves a specific menu item or all menu items.
- Parameters:
  - `pk` (optional): The primary key of the menu item to retrieve.
- Template: `menu_item.html`

## Templates

1. Base - from which other templates extend from.
2. About - a view about the restaurant Littlelemon.
3. Index - a view that renders the home/ landing page
4. Bookings - a view that uses the booking api endpoint to get and post bookings (Reservations) [requires authentication]
5. Booking-item - a view that uses the booking<int:pk> specifier for crudly operations
6. Menu - a view that uses the menu api endpoint to get all menu item listings
7. Menu-item - a view that uses the menu<int:pk> specifier for crudly operations
8. Profile -  a view that captures the redirect from djsoers redirection from a successful authentication

## Models

1. Bookings - verbose_name_plural 'Bookings'
2. User - verbose_name_plural 'Users'
3. Menu - verbose_name_plutal 'Menu'

## Databases

1. sqlite
2. MySQL (use --database mysql to migrate to your mysql instance)

## Project URLs

1. admin
2. api
3. api-auth - (rest_framework endpoints)
4. auth - (djoser - urls, authtokens)
5. api/token - (JWT, obtain an access & refresh token)
6. api/token/refresh - (Renew an access token using a refresh token)
7. api/token/verify - Takes a token and indicates if it is valid.
8. api/accounts/signout/ - Destroys a token and signing out a user and ends their session
9. api/accounts/login - Logs in a user and they can use their JWT token for subsequent API calls.

## Tests

## Python Unit Tests

### MenuModelTest

- `setUpTestData`: Sets up test data for the Menu Model.
- `test_get_item`: Tests the `get_item` method of the Menu Model.
- `test_get_all_items`: Tests the `get_all_items` method of the Menu Model.
- `test_ordering`: Tests the ordering of menu items in the Menu Model.
- `test_verbose_name_plural`: Tests the `verbose_name_plural` attribute of the Menu Model.
- `test_string_representation`: Tests the string representation of the Menu Model.
- `test_title_max_length`: Tests the maximum length of the `name` field in the Menu Model.
- `test_inventory_default`: Tests the default value of the `inventory` field in the Menu Model.
- `test_price_max_digits`: Tests the maximum number of digits in the `price` field of the Menu Model.
- `test_price_decimal_places`: Tests the number of decimal places in the `price` field of the Menu Model.
- `test_description_null`: Tests the `description` field of the Menu Model for null values.
- `test_description_blank`: Tests the `description` field of the Menu Model for blank values.
- `test_description_max_length`: Tests the maximum length of the `description` field in the Menu Model.
- `test_update_menu_item`: Tests updating a menu item in the Menu Model.
- `test_delete_menu_item`: Tests deleting a menu item from the Menu Model.

### BookingModelTest

- `setUp`: Sets up the test data for the Booking Model.
- `tearDown`: Cleans up the test data after running the tests.
- `test_string_representation`: Tests the string representation of the Booking Model.
- `test_update_reservation`: Tests updating a reservation in the Booking Model.
- `test_delete_reservation`: Tests deleting a reservation from the Booking Model.

## Project

- littlelemon

## App

- restaurant

## Set up

1. cd littlelemon
2. pipenv shell
3. pipenv install
4. make migrations
5. migrate (you can use the sqlite DB or change the credential settings to use your mysql instance using the --database switch and your db credentials)
6. create a super user 'createsuper', you will need this to explore APIs that have restrictions
7. run server
8. Test the endpoints as documented above, note the super user has priviledges to make changes to models as you would using the admin panel.
