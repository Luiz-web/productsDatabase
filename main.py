import sqlite3


class ProductsDB:
    def __init__(self, file):
        self.conn = sqlite3.connect(file)
        self.cursor = self.conn.cursor()

    
    def insert_product(self, name, price):
        consult = 'INSERT INTO productlist (name, price) VALUES(?, ?)'
        self.cursor.execute(consult, (name, price))
        self.conn.commit()
    
    def edit_product(self, name, price, id):
        consult = 'UPDATE productlist SET name=?, price=? WHERE id=?'
        self.cursor.execute(consult, (name, price, id))
        self.conn.commit()

    def delete_product(self, id):
        consult = 'DELETE FROM productlist WHERE id=?'
        self.cursor.execute(consult, (id,))
        self.conn.commit()
    
    def show_products(self):
        self.cursor.execute('SELECT * FROM productlist')

        for line in self.cursor.fetchall():
            print(line)

    def search_products(self, value):
        consult = 'SELECT * FROM productlist WHERE name LIKE ? '
        self.cursor.execute(consult, (f'%{value}%',))

        for line in self.cursor.fetchall():
            print(line)

    def close(self):
        self.conn.close()
        self.cursor.close()


if __name__ == '__main__':
    productlist = ProductsDB('productlist.db')
   # productlist.insert('Name', 0.00)
   # productlist.edit_product('Name', 0.00, 0)
   # productlist.delete_product(0)
   # productlist.show_products()
   # productlist.search_products('Name')

