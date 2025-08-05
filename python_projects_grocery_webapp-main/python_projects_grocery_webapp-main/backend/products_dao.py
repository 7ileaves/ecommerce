import pandas as pd
from sql_connection import DatabaseConnection
postgres_connection = DatabaseConnection('grocerydb', 'postgres', 'root123#', 'localhost', 5432)
db_connection = postgres_connection.get_connection()

def get_all_products():
    try:
        with db_connection.cursor() as cursor:
            #query = ("SELECT * FROM products INNER JOIN uom USING(uom_id)")
            query = ("SELECT * FROM products")
            cursor.execute(query)
            response = []
            for (product_id, name, description, price, uom_id) in cursor:
                response.append({
                    'product_id': product_id,
                    'name': name,
                    'description': description,
                    'price': price,
                    'uom_id': uom_id                          
            })
            return response
    except Exception as e:
        postgres_connection.connection.rollback()
        raise e

def insert_new_product(product):
    try:
        with db_connection.cursor() as cursor:
    
            query = ("INSERT INTO products "
                 "(name, description, price, uom_id)"
                 "VALUES (%s, %s, %s, %s)")
            data = (product['name'], product['description'], product['price'], product['uom_id'])

            cursor.execute(query, data)
            postgres_connection.connection.commit()
            

            return cursor.lastrowid
    except Exception as e:
        postgres_connection.connection.rollback()
        raise e

def delete_product(product_id):
    try:
        with db_connection.cursor() as cursor:
            query = ("DELETE FROM products where product_id=" + str(product_id))
            cursor.execute(query)
            postgres_connection.connection.commit()
            return cursor.lastrowid
    except Exception as e:
        postgres_connection.connection.rollback()
        raise e
    cursor = db_connection.cursor()

if __name__ == '__main__':    
    # Testing purpose
    # print(get_all_products(connection))
    #print(insert_new_product({
    #    'name':'Puzzle Books for kids','description':'Educational','price': 500, 'uom_id':1  
    #}))
    
    '''
    response = get_all_products()
    #print(response)
    df = pd.DataFrame(response)
    print(df)
    '''
    delete_product(200)
    response = get_all_products() 
    df = pd.DataFrame(response)
    print(df)