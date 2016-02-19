import psycopg2

conn = psycopg2.connect(user="sports_user", database="sports_stats")
cur = conn.cursor()
print("Welcome to the Boston Bruins 2010-2011 Database")
while True:
    user_input = input("Search for player by name: ")

    cur.execute("SELECT * FROM player_stats WHERE LOWER(player_name) = LOWER(%s);", (user_input,))
    print(cur.fetchall())



cur.close()
conn.close()