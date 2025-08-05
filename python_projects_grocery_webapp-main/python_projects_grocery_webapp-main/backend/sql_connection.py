import psycopg2

class DatabaseConnection:
    def __init__(self, dbname, user, password, host, port):
            print("Constructor called")
            self.dbname = dbname
            self.user = user
            self.password = password
            self.host = host
            self.port = port
            self.connection = None
            
    def get_connection(self):
        if self.connection is not None:
            return self.connection
        else:
            try:
                self.connection = psycopg2.connect(
                    dbname = self.dbname,
                    user = self.user,
                    password = self.password,
                    host =  self.host,
                    port = self.port                    
                )
                print("Connection to database successful")
                return self.connection
            except psycopg2.Error as e:
                print(f"Error connecting to database: {e}")
                return None
