# MongoDB assignments
<b>lab2_1.py</b>

Implement the storage of the following information: 
(1) Football teams: name, city, full name of the coach, starting lineup of players (name, position), substitute players. 
(2) Games: date, score, violations of the rules (yellow and red cards, to whom and at what minute they were issued, for what), goals scored (from what position it was scored, minute, author, transfer), penalties (similarly), number shots on goal (similarly). 

Create a windowed application containing two text input fields for a key and its value for the properties of the current document; for nested keys, the dot operator is used; all nested elements are a list of documents; three buttons: "Add key-value", "Save document", "Show documents"; field for displaying a list of documents. The application implements the following functions:
When you click on the "Add key-value" button, it adds a new key-value pair to the current document;
When you click on the "Save Document" button, it creates a new document in the database with the previously entered key-value set and clears the variable that stores the current set;
When you click on the "Show Documents" button, it generates a database query that returns all documents in the collection and displays them in a list.

![image](https://user-images.githubusercontent.com/67418401/208235198-e5beb888-f17a-4cd7-9dc9-305ee2e46b6a.png)



<b>lab2_2.py</b>

Create a collection of documents for an online store. Each document describes one product and includes: the name of the product, its manufacturer, price and its special characteristics in the form of an attached document, as well as information about the buyers of this product in the form of many documents, including data on the names of buyers, when they bought the product, reviews, service name delivery, etc. Choose 4 categories of goods with different characteristics. Populate the database with at least 20 documents. Create database queries:
Get a list of product names related to a given category;
Get a list of product characteristics of a given category;
Get a list of names and prices of goods purchased by a given customer;
Get a list of names, manufacturers and prices for goods that have a given color;
Get the total amount of goods sold;
Get the number of products in each category;
Get a list of names of buyers of a given product;
Get a list of names of buyers of a given product, with a delivery company with a given name.

![image](https://user-images.githubusercontent.com/67418401/208235247-cb583bce-fa0f-46d7-b028-c00cfaa1ba73.png)
