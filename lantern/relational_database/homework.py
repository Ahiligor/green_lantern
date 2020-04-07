from typing import List


def task_1_add_new_record_to_db(con) -> None:
    """
    Add a record for a new customer from Singapore
    {
        'customer_name': 'Thomas',
        'contactname': 'David',
        'address': 'Some Address',
        'city': 'London',
        'postalcode': '774',
        'country': 'Singapore',
    }

    Args:
        con: psycopg connection

    Returns: 92 records

    """
    new_customer = {
        'customer_name': 'Thomas',
        'contactname': 'David',
        'address': 'Some Address',
        'city': 'London',
        'postalcode': '774',
        'country': 'Singapore',
    }
    cursor = con.cursor()
    cursor.execute(
        "INSERT INTO customers (customername, contactname, address, city, postalcode, country)"
        "VALUES (%(customer_name)s, %(contactname)s, %(address)s, %(city)s, %(postalcode)s, %(country)s);",
        {**new_customer}
    )
    con.commit()
    cursor.execute(
        "SELECT * "
        "FROM customers;"
    )
    return cursor.fetchall()


def task_2_list_all_customers(cur) -> list:
    """
    Get all records from table Customers

    Args:
        cur: psycopg cursor

    Returns: 91 records

    """
    cur.execute(
        "SELECT * FROM customers;"
    )
    return cur.fetchall()


def task_3_list_customers_in_germany(cur) -> list:
    """
    List the customers in Germany

    Args:
        cur: psycopg cursor

    Returns: 11 records
    """
    cur.execute(
        "SELECT * FROM customers WHERE country='Germany'"
    )
    return cur.fetchall()


def task_4_update_customer(con):
    """
    Update first customer's name (Set CustomerName equal to  'Johnny Depp')
    Args:
        cur: psycopg cursor

    Returns: 91 records with updated customer

    """
    cursor = con.cursor()
    cursor.execute(
        "UPDATE customers SET CustomerName='Johnny Depp' WHERE CustomerID=1;"
    )
    con.commit()
    cursor.execute(
        "SELECT * "
        "FROM customers;"
    )
    return cursor.fetchall()


def task_5_delete_the_last_customer(con) -> None:
    """
    Delete the last customer

    Args:
        con: psycopg connection
    """
    cursor = con.cursor()
    cursor.execute(
        "DELETE FROM customers WHERE CustomerID=(SELECT MAX(CustomerID) FROM customers)"
    )
    con.commit()


def task_6_list_all_supplier_countries(cur) -> list:
    """
    List all supplier countries

    Args:
        cur: psycopg cursor

    Returns: 29 records

    """
    cur.execute(
        "SELECT country FROM suppliers;"
    )
    return cur.fetchall()


def task_7_list_supplier_countries_in_desc_order(cur) -> list:
    """
    List all supplier countries in descending order

    Args:
        cur: psycopg cursor

    Returns: 29 records in descending order

    """
    cur.execute(
        "SELECT country FROM suppliers ORDER BY country DESC;"
    )
    return cur.fetchall()


def task_8_count_customers_by_city(cur):
    """
    List the number of customers in each city

    Args:
        cur: psycopg cursor

    Returns: 69 records in descending order

    """
    cur.execute(
        "SELECT COUNT(city), City FROM customers GROUP BY city ORDER BY COUNT(city) DESC, City;"
    )
    return cur.fetchall()


def task_9_count_customers_by_country_with_than_10_customers(cur):
    """
    List the number of customers in each country. Only include countries with more than 10 customers.

    Args:
        cur: psycopg cursor

    Returns: 3 records
    """
    cur.execute(
        "SELECT COUNT(Country), Country "
        "FROM customers "
        "GROUP BY Country "
        "HAVING COUNT(Country) > 10;"
    )
    return cur.fetchall()


def task_10_list_first_10_customers(cur):
    """
    List first 10 customers from the table

    Results: 10 records
    """
    cur.execute(
        "SELECT * FROM Customers " 
        "ORDER BY CustomerID LIMIT 10;"
    )
    return cur.fetchall()


def task_11_list_customers_starting_from_11th(cur):
    """
    List all customers starting from 11th record

    Args:
        cur: psycopg cursor

    Returns: 11 records
    """
    cur.execute(
        "SELECT * FROM Customers " 
        "WHERE CustomerID>11;"
    )
    return cur.fetchall()


def task_12_list_suppliers_from_specified_countries(cur):
    """
    List all suppliers from the USA, UK, OR Japan

    Args:
        cur: psycopg cursor

    Returns: 8 records
    """
    cur.execute(
        "SELECT SupplierID, SupplierName, ContactName, city, country "
        "FROM suppliers "
        "WHERE country IN ('USA', 'UK', 'Japan')"
    )
    return cur.fetchall()


def task_13_list_products_from_sweden_suppliers(cur):
    """
    List products with suppliers from Sweden.

    Args:
        cur: psycopg cursor

    Returns: 3 records
    """
    cur.execute(
        "SELECT ProductName "
        "FROM products "
        "WHERE SupplierID "
        "IN (SELECT SupplierID FROM suppliers WHERE country='Sweden');"
    )
    return cur.fetchall()


def task_14_list_products_with_supplier_information(cur):
    """
    List all products with supplier information

    Args:
        cur: psycopg cursor

    Returns: 77 records
    """
    cur.execute(
        "SELECT p.ProductID, p.ProductName, p.Unit, p.Price, "
        "s.Country, s.City, s.SupplierName "
        "FROM products as p "
        "INNER JOIN suppliers as s "
        "ON  p.SupplierId = s.SupplierId;"
    )
    return cur.fetchall()


def task_15_list_customers_with_any_order_or_not(cur):
    """
    List all customers, whether they placed any order or not.

    Args:
        cur: psycopg cursor

    Returns: 213 records
    """
    cur.execute(
        "SELECT c.CustomerName, c.ContactName, c.country, o.OrderID "
        "FROM customers AS c "
        "LEFT JOIN orders AS o "
        "ON c.CustomerID = o.CustomerID;"
    )
    return cur.fetchall()


def task_16_match_all_customers_and_suppliers_by_country(cur):
    """
    Match all customers and suppliers by country

    Args:
        cur: psycopg cursor

    Returns: 194 records
    """
    cur.execute(
        "SELECT c.CustomerName, c.Address, c.Country AS CustomerCountry, "
        "s.Country AS SupplierCountry, s.SupplierName "
        "FROM customers AS c "
        "FULL JOIN suppliers AS s "
        "ON c.Country = s.Country "
        "ORDER BY CustomerCountry, SupplierCountry;"
    )
    return cur.fetchall()
