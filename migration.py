import psycopg2

conn = psycopg2.connect(user="sports_user", database="sports_stats")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS player_stats;")

create_table_string = """
    CREATE TABLE player_stats (
    id SERIAL PRIMARY KEY,
    number NUMERIC(2),
    player_name VARCHAR(30),
    position VARCHAR(2),
    age NUMERIC(2),
    height VARCHAR(5),
    weight NUMERIC(3),
    shoots_catches VARCHAR(3),
    years_exp VARCHAR(3),
    birthdate VARCHAR(30),
    summary VARCHAR(30)
    )
    """
cur.execute(create_table_string)
conn.commit()
insert_template = "INSERT INTO player_stats VALUES (DEFAULT, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
with open("player_roster.csv") as roster:
    team_data = []
    for items in roster.readlines():
        team_data.append(items.split(','))
for player in team_data:
    cur.execute(insert_template, player)
    conn.commit()

cur.close()
conn.close()