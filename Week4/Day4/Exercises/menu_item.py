import psycopg2


class MenuItem:
    def __init__(self, item_name, item_price):
        self.item_name = item_name
        self.item_price = item_price

    def save(self):
        try:
            connection = psycopg2.connect(
                host="localhost",
                database="restaurant",
                user="itay",
                password="root"
            )
            cursor = connection.cursor()

            insert_query = f"INSERT INTO Menu_Items (item_name, item_price) VALUES (%s, %s);"
            data = (self.item_name, self.item_price)
            cursor.execute(insert_query, data)

            connection.commit()
            cursor.close()
            connection.close()

            print("Item saved successfully!")
        except Exception as e:
            print("Error:", e)

    def delete(self):
        try:
            connection = psycopg2.connect(
                host="localhost",
                database="restaurant",
                user="itay",
                password="root"
            )
            cursor = connection.cursor()

            delete_query = "DELETE FROM Menu_Items WHERE item_name = %s;"
            data = (self.item_name,)
            cursor.execute(delete_query, data)

            connection.commit()
            cursor.close()
            connection.close()

            print("Item deleted successfully!")
        except Exception as e:
            print("Error:", e)

    def update(self, new_item_name, new_item_price):
        try:
            connection = psycopg2.connect(
                host="localhost",
                database="restaurant",
                user="itay",
                password="root"
            )
            cursor = connection.cursor()

            update_query = "UPDATE Menu_Items SET item_name = %s, item_price = %s WHERE item_name = %s;"
            data = (new_item_name, new_item_price, self.item_name)
            cursor.execute(update_query, data)

            connection.commit()
            cursor.close()
            connection.close()

            print("Item updated successfully!")
        except Exception as e:
            print("Error:", e)
