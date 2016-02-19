import psycopg2

conn = psycopg2.connect(user="sports_user", database="sports_stats")
cur = conn.cursor()
print("Welcome to the Boston Bruins 2010-2011 Database")
while True:
    user_input = input("Search for player by name: ")

    cur.execute("SELECT * FROM player_stats WHERE LOWER(player_name) = LOWER(%s);", (user_input,))

    player_info = cur.fetchall()[0]
    print("\nName: " + player_info[2])
    print("Number: " + str(player_info[1]))
    print("Position: " + player_info[3])
    print("Age: " + str(player_info[4]))
    print("Height: " + player_info[5])
    print("Weight: " + str(player_info[6]))
    print("Shoots/Catches: " + player_info[7])
    print("Years Exp: " + player_info[8])
    print("Birthdate: " + player_info[9] + "\n")



cur.close()
conn.close()