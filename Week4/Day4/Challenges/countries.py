import requests
import psycopg2
import random

DB_HOST = 'localhost'
DB_NAME = 'countries_db'
DB_USER = 'itay'
DB_PASSWORD = 'root'


def create_connection():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        return conn
    except Exception as e:
        print("Error: Unable to connect to the database")
        print(e)
        return None


def insert_country(conn, country):
    sql = """
        INSERT INTO countries (name, capital, flag, subregion, population)
        VALUES (%s, %s, %s, %s, %s);
    """
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql, country)
        conn.commit()
    except Exception as e:
        print("Error: Unable to insert data into the database")
        print(e)


def get_random_countries():
    api_url = "https://restcountries.com/v3.1/all"
    try:
        response = requests.get(api_url)
        countries_data = response.json()
        random_countries = random.sample(countries_data, 10)
        return random_countries
    except Exception as e:
        print("Error: Unable to fetch data from the API")
        print(e)
        return []


def main():
    conn = create_connection()
    if conn is not None:
        countries = get_random_countries()
        for country in countries:
            name = country['name']['common']
            capital = country['capital'][0] if 'capital' in country else None
            flag = country['flags']['png'] if 'flags' in country else None
            subregion = country['subregion'] if 'subregion' in country else None
            population = country['population'] if 'population' in country else None
            insert_country(conn, (name, capital, flag, subregion, population))

        conn.close()


# for country in get_random_countries():
#     n = country['name']['common']
#     c = country['capital'][0] if 'capital' in country else None
#     f = country['flags']['png'] if 'flags' in country else None
#     s = country['subregion'] if 'subregion' in country else None
#     p = country['population'] if 'population' in country else None
#     print(
#         f"Country name: {n}\nCapital: {c}\nFlag: {f}\nSubregion: {s}\nPopulation: {p}\n\n\n")

if __name__ == "__main__":
    main()
