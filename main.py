import psycopg2

conn = psycopg2.connect(user="sports_user", database="sports_stats")
cur = conn.cursor()
print("Welcome to the Boston Bruins 2010-2011 Database")
player_info = None
while True:
    user_input = input("Search for player by name: ")

    cur.execute("SELECT * FROM player_stats WHERE LOWER(player_name) = LOWER(%s);", (user_input,))
    try:
        player_info = cur.fetchall()[0]
    except:
        print("No data found")

    if player_info:
        print("\nName: " + player_info[2])
        print("Number: " + str(player_info[1]))
        print("Position: " + player_info[3])
        print("Age: " + str(player_info[4]))
        print("Height: " + player_info[5])
        print("Weight: " + str(player_info[6]))
        print("Shoots/Catches: " + player_info[7])
        print("Years Exp: " + player_info[8])
        print("Birthdate: " + player_info[9] + "\n")

    if input("Would you like to change history and add your own player? y/N").lower() == 'y':
        new_name = input("Player Name: ")
        new_number = input("Number: ")
        new_position = input("Position: ")
        new_age = input("Age: ")
        new_height = input("Height: ")
        new_weight = input("Weight: ")
        new_shoots_catches = input("Shoots/Catches L/R: ")
        new_years_exp = input("Years Exp: ")
        new_birthdate = input("Birthdate: ")
        insert_template = "INSERT INTO player_stats VALUES (DEFAULT, %s, %s, %s, %s, %s, %s, %s, %s, %s, DEFAULT)"
        insert_values = [new_number, new_name, new_position, new_age, new_height, new_weight, new_shoots_catches, new_years_exp, new_birthdate]
        cur.execute(insert_template, insert_values)
        conn.commit()
    else:
        if input("Would you like to search again? Y/n").lower() == 'y':
            continue
        else:
            print("Goodbye.")
            break

cur.close()
conn.close()