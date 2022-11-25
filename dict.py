import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="dict",
    user="postgres",
    password="SuperElla2020")
 
# Reads the dictionary in a list
def read_dict(C):
    cur = C.cursor()
    cur.execute("SELECT id, word, translation FROM dictionary;")
    rows = cur.fetchall()
    cur.close()
    return rows
# Add words to dictionary
def add_word(C, word, translation):
    cur = C.cursor()
    cur.execute(f"INSERT INTO dictionary (word, translation) VALUES ('{word}', '{translation}');")
    cur.close()
# Delete words from dictionary
def delete_word(C, ID):
    cur = C.cursor()
    cur.execute(f"DELETE FROM dictionary WHERE id = '{ID}';")
    cur.close()
# Save the current/updated version of the dictionary and quits the program
def save_dict(C):
    cur = C.cursor()
    cur.execute("COMMIT;")
    cur.close()

while True: ## REPL - Read Execute Program Loop
    print("These commands are available: list, add, delete, quit:")
    cmd = input("Command: ").strip().lower()
    if cmd == "list":
        print("Current list:\n")
        print(read_dict(conn))
    elif cmd == "add":
        name = input("  Word: ")
        phone = input("  Translation: ")
        add_word(conn, name, phone)
        print(f"Added word: {name}")
    elif cmd == "delete":
        ID = input("  ID: ")
        delete_word(conn, ID)
        print(f"Deleted word: {ID}")
    elif cmd == "quit":
        save_dict(conn)
        print("Quits program")
        exit()
