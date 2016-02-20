import psycopg2

conn = psycopg2.connect(user="sports_user", database="sports_stats")
cur = conn.cursor()
print("Welcome to the Boston Bruins 2010-2011 Database")

while True:

    def player_search():
        player_info = None

        user_input = '%' + input("Search for player by name: ") + '%'
        if user_input != "%%":
            cur.execute("SELECT * FROM player_stats WHERE LOWER(player_name) LIKE LOWER(%s);", (user_input,))
        else:
            player_search()

        player_info = cur.fetchall()

        if player_info:
            for player in player_info:
                print("\nName: " + player[2])
                print("Number: " + str(player[1]))
                print("Position: " + player[3])
                print("Age: " + str(player[4]))
                print("Height: " + player[5])
                print("Weight: " + str(player[6]))
                print("Shoots/Catches: " + player[7])
                print("Years Exp: " + player[8])
                print("Birthdate: " + player[9] + "\n")
        else:
            print("No records found.")
        input_prompt()

    def add_player():

        if input("Are you sure you would like to change history and add your own player? y/N").lower() == 'y':
            try:
                new_name = input("Player Name: ")[:30]
                new_number = int(input("Number: ")[:2])
                new_position = input("Position: ")[:2]
                new_age = int(input("Age: ")[:2])
                new_height = input("Height: ")[:5]
                new_weight = int(input("Weight: ")[:3])
                new_shoots_catches = input("Shoots/Catches L/R: ")[:3]
                new_years_exp = input("Years Exp: ")[:3]
                new_birthdate = input("Birthdate: ")[:30]
                insert_template = "INSERT INTO player_stats VALUES (DEFAULT, %s, %s, %s, %s, %s, %s, %s, %s, %s, DEFAULT)"
                insert_values = [(new_number,), (new_name,), (new_position,), (new_age,), (new_height,), (new_weight,), (new_shoots_catches,), (new_years_exp,), (new_birthdate,)]
                cur.execute(insert_template, insert_values)
                conn.commit()
                print("Player {} added to database.\n".format(new_name))
            except ValueError:
                print("Invalid input. Please try again.")
                add_player()

        else:
            if input("Would you like the main menu?").lower() == 'y':
                input_prompt()
            else:
                print("Goodbye.")

    def input_prompt():
        prompt = input("What would you like to do?\n"
                       "S - Search for player by name\n"
                       "A - Add an entry\n"
                       "Q - Quit"
                       ).lower()
        if prompt == 's':
            player_search()

        elif prompt == 'a':
            add_player()

        elif prompt == 'q':
            print("Goodbye.")
            return False

        else:
            print("Seriously, let's try this again.")
            input_prompt()
    input_prompt()


    break

cur.close()
conn.close()