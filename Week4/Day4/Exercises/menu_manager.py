import psycopg2
from menu_item import MenuItem


class MenuManager:
    @classmethod
    def get_by_name(cls, item_name):
        try:
            connection = psycopg2.connect(
                host="localhost",
                database="restaurant",
                user="itay",
                password="root"
            )
            cursor = connection.cursor()

            select_query = "SELECT * FROM Menu_Items WHERE item_name = %s;"
            data = (item_name,)
            cursor.execute(select_query, data)

            item = cursor.fetchone()

            cursor.close()
            connection.close()

            if item:
                item_id, item_name, item_price = item
                return MenuItem(item_name, item_price)
            else:
                return None
        except Exception as e:
            print("Error:", e)

    @classmethod
    def all_items(cls):
        try:
            connection = psycopg2.connect(
                host="localhost",
                database="restaurant",
                user="itay",
                password="root"
            )
            cursor = connection.cursor()

            select_query = "SELECT * FROM Menu_Items;"
            cursor.execute(select_query)

            items = cursor.fetchall()

            cursor.close()
            connection.close()

            menu_items = []
            for item in items:
                item_id, item_name, item_price = item
                menu_items.append(MenuItem(item_name, item_price))

            return menu_items
        except Exception as e:
            print("Error:", e)


item = MenuItem('Burger', 35)
item.save()
item.delete()
item.update('Veggie Burger', 37)
item2 = MenuManager.get_by_name('Beef Stew')
items = MenuManager.all_items()

