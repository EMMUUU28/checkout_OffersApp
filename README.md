# checkout_OffersApp
Project Documentation: Discount Offers Selection

Introduction:

This project is aimed at providing a platform for users to select discount offers
from a list of available options. The selected offers will be stored in the Django
admin database for further processing. This documentation provides an
overview of the project, its features, and how to use it effectively.

Table of Contents:
1. Project Overview
2. Features
3. Installation and Setup
4. Usage Guide
5. Admin Interface
6. Conclusion

<h2>Project Overview:</h2>

The Discount Offers Selection project allows users to choose from a variety of
	discount offers. These offers are stored in the Django admin database and
	can be dynamically displayed to the users. Users can select the offers they
	want to avail by checking the corresponding checkboxes. The selected offers
	are then stored in the database for further processing.

<h2>Features:</h2>

● Displaying a list of discount offers: The project provides a user interface to
		display the available discount offers.
		
● Checkbox selection: Users can select the offers they want to avail by
checking the checkboxes associated with each offer.

● Storing selected offers: The selected offers are stored in the Django admin
database using a custom Result model.

● Admin interface integration: The Django admin interface allows easy
management and retrieval of the selected offers.
         
<h2>Installation and Setup:</h2>
  To set up the Discount Offers Selection project, follow these steps:
  
  ● Clone the project repository from the provided source.

● Install the required dependencies using the pip install -r requirements.txt
  command.

● Set up the Django database configuration in the project's settings file.

● Run the necessary migrations using the python manage.py migrate
  command.

● Create a superuser account using the python manage.py createsuperuser
  command.

● Start the development server using the python manage.py runserver
  command.
  
<h2>Usage Guide:</h2>

 ● Once the project is set up and the development server is running, users can
  access the application through a web browser. They will be presented with a
  list of available discount offers.

● Selecting offers: Users can choose the offers they want to avail by checking
  the checkboxes associated with each offer.

● Submitting the selection: After selecting the desired offers, users can click the
  "Checkout" button to submit their selection.

● Confirmation: Users will receive a confirmation message indicating that their
  selection has been successfully stored.

<h2>Admin Interface:</h2>

 The Django admin interface provides access to the stored selections and
 offers additional management capabilities. To access the admin interface:
 Open a web browser and navigate to the admin URL(e.g.
 http://127.0.0.1:8000/admin).
 Log in using the superuser account created during setup.

 In the admin interface, navigate to the "Results" section to view the stored
 selections.
 From the admin interface, you can perform actions such as editing, deleting,
 or exporting the selections.

<h2>Conclusion:</h2>

 The Discount Offers Selection project provides a convenient way for users to
 select discount offers and store their selections in the Django admin
 database. By following the installation and usage instructions provided in this
 documentation, users can effectively utilise the project's features and manage
 the selected offers seamlessly.
 
<h2>Result:</h2> 
![Screenshot 2023-06-05 220959](https://github.com/EMMUUU28/checkout_OffersApp/assets/97393911/8d23cb4e-c15f-4cd7-affb-22dee42616ed)
