import pandas as pd

# Testing purpose only.
from sql_connection import DatabaseConnection

def get_all_products(db_connection):
    try:
        with db_connection.cursor() as cursor:
            #query = ("SELECT * FROM products INNER JOIN uom USING(uom_id)")
            query = ("SELECT * FROM products")
            cursor.execute(query)
            response = []
            for (product_id, name, description, price, uom_id) in cursor:
                '''
                response.append({
                    'product_id': product_id,
                    'name': name,
                    'description': description,
                    'price': price,
                    'uom_id': uom_id                          
                })
            '''
                response.append([
                        product_id,
                        name,
                        description,
                        price,
                        uom_id                          
                ])
            return response
    except Exception as e:
        db_connection.rollback()
        raise e

def insert_new_product(db_connection, product):
    try:
        with db_connection.cursor() as cursor:
    
            query = ("INSERT INTO products "
                 "(name, description, price, uom_id)"
                 "VALUES (%s, %s, %s, %s)")
            data = (product['name'], product['description'], product['price'], product['uom_id'])

            cursor.execute(query, data)
            db_connection.commit()
            

            return cursor.lastrowid
    except Exception as e:
        db_connection.rollback()
        raise e

def delete_product(db_connection, product_id):
    try:
        with db_connection.cursor() as cursor:
            query = ("DELETE FROM products where product_id=" + str(product_id))
            cursor.execute(query)
            db_connection.commit()
            return cursor.lastrowid
    except Exception as e:
        db_connection.rollback()
        raise e
    cursor = db_connection.cursor()

if __name__ == '__main__':    
    # Testing purpose
    postgres_connection = DatabaseConnection('grocerydb', 'postgres', 'root123#', 'localhost', 5432)
    connection = postgres_connection.get_connection()
    print(get_all_products(connection))
    print(insert_new_product(connection, {
        'name':'OSHO for living','description':'Philosophy','price': 500, 'uom_id':1  
    }))
    
    '''
    response = get_all_products()
    #print(response)
    df = pd.DataFrame(response)
    print(df)
   
     
   

    delete_product(connection, 11)
    response = get_all_products(connection) 
    df = pd.DataFrame(response)
    print(df)
     '''