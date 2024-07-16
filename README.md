# Restaurant-Database-Management-System
## Description:
This project is a web-based application developed using Flask and WTForms to manage restaurant orders. The application allows users to select meals, drinks, and desserts from predefined lists and place orders. The application connects to a MySQL database to store and retrieve order details.
## Code Overview:
### Database Connection:
* Establishes a connection to the MySQL database and fetches data for meals, drinks, and desserts.

### Forms:
* `MyForm`: Form to add new meals, drinks, and desserts.
* `OrderForm`: Form to place an order, selecting meals, drinks, and desserts.
### Routes:
Home route renders the main page:
* /deserts.html, /drink.html, and /food.html routes handle adding new items to the database.
* /menu.html handles order placement and displays the bill.
* Additional routes for static pages like Thanks and Contact.
### Templates: 
* Renders HTML templates for each route using Flask's render_template.
### Database Operations:
* Fetching Data: Queries to fetch meal, drink, and dessert details to populate forms.
* Inserting Data: Queries to insert new meals, drinks, and desserts into the database.
* Updating Data: Queries to update order details in the database when an order is placed.
## Note:
Ensure that the MySQL database is running and accessible before starting the application. Adjust the database schema and queries as needed to fit your specific requirements.
