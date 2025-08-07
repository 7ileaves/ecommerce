from datetime import datetime

# Testing purpose only.
from sql_connection import DatabaseConnection

def insert_order(db_connection, order):    
    try:
        with db_connection.cursor() as cursor:
            order_query = ("INSERT INTO orders (customer_id, order_date, status) VALUES (%s, %s, %s)")
            order_data = (order['customer_id'], datetime.now(), order['status'])

            cursor.execute(order_query, order_data)
            order_id = cursor.lastrowid
                        
            db_connection.commit()

            return order_id
    except Exception as e:
            db_connection.rollback()
            raise e
        
def insert_order_item(db_connection, order_item):    
    try:
        with db_connection.cursor() as cursor:

            order_details_query = ("INSERT INTO order_items (order_id, product_id, quantity, unit_price) VALUES (%s, %s, %s, %s)") 
            item = [order_item['order_id'], order_item['product_id'], order_item['quantity'], order_item['unit_price']]
            
            cursor.execute(order_details_query, item)
            db_connection.commit()            
            order_item_id = cursor.lastrowid
            
            order_id = order_item['order_id']
            update_order(order_id, {'total_cost': int(order_item['unit_price']) * int(order_item['quantity'])})
            return order_item_id
    except Exception as e:
            db_connection.rollback()
            raise e
        
def update_order(db_connection, order_id, data):
    try:
        with db_connection.cursor() as cursor:
            query = "UPDATE orders SET total_cost = %s WHERE order_id = %s"
            cursor.execute(query, (data['total_cost'], order_id))
            db_connection.commit()
    except Exception as e:          
        db_connection.rollback()
        raise e
    
def get_order_details(order_id):     
    pass


# Given a customer id, i should get the order details.
def get_all_orders():
    pass

if __name__ == '__main__':
    
    postgres_connection = DatabaseConnection('grocerydb', 'postgres', 'root123#', 'localhost', 5432)
    connection = postgres_connection.get_connection()
    
    order_id = insert_order(connection, {
                'customer_id': 1, 
                'order_date': datetime.now(),                
                'status': 'completed'               
                 })
    
    print(order_id)
        
    print(insert_order_item(connection, {
                'order_id': 15,
                'product_id': '5', 
                'quantity': '2',
                'unit_price': '300'
                 }))