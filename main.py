import psycopg2

conn = psycopg2.connect(user="sports_user", database="sports_stats")
cur = conn.cursor()
print("Welcome to the Boston Bruins 2010-2011 Database")


def player_db():
    while True:

        def player_edit():

            print("Pick a player by entry number for editing. "
                  "Use player search to find correct entry. Q to quit.")
            edit_input = input("-> ")
            if edit_input.lower() == 'q':
                main_menu()

            else:
                cur.execute("SELECT * FROM player_stats WHERE id = %s;", (edit_input,))
            player_edit_info = cur.fetchall()
            if player_edit_info:
                player_nfo_display(player_edit_info)

            else:
                print("Record not found.")
                player_edit()

        def player_search():

            user_input = '%' + input("\nSearch for player by name: ") + '%'
            if user_input != "%%":
                cur.execute("SELECT * FROM player_stats WHERE LOWER(player_name) LIKE LOWER(%s);", (user_input,))
            else:
                player_search()

            player_info = cur.fetchall()

            if player_info:
                player_nfo_display(player_info)
            else:
                print("No records found.")
            main_menu()

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
                    insert_template = """INSERT INTO player_stats VALUES (
                                      DEFAULT, %s, %s, %s, %s, %s, %s, %s, %s, %s, DEFAULT
                                      )"""
                    insert_values = [(new_number,), (new_name,), (new_position,), (new_age,), (new_height,),
                                     (new_weight,), (new_shoots_catches,), (new_years_exp,), (new_birthdate,)]
                    cur.execute(insert_template, insert_values)
                    conn.commit()
                    print("Player {} added to database.\n".format(new_name))
                    main_menu()

                except ValueError:
                    print("Invalid input. Please try again.")
                    add_player()
            else:
                main_menu()

        def player_nfo_display(player_info):
            for player in player_info:
                print("\nEntry No: " + str(player[0]))
                print("\tName: " + player[2])
                print("\tNumber: " + str(player[1]))
                print("\tPosition: " + player[3])
                print("\tAge: " + str(player[4]))
                print("\tHeight: " + player[5])
                print("\tWeight: " + str(player[6]))
                print("\tShoots/Catches: " + player[7])
                print("\tYears Exp: " + player[8])
                print("\tBirthdate: " + player[9] + "\n")

        def main_menu():
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
                print("\nGoodbye.")
                return False

            else:
                print("Seriously, let's try this again.")
                main_menu()
        break

    main_menu()


player_db()

cur.close()
conn.close()
