from database.db_connection import get_connection
from models.team import Team
from models.player import Player
from models.tournament import Tournament


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS team (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        region TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS player (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nickname TEXT,
        role TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tournament (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        prize_pool INTEGER
    )
    """)

    conn.commit()
    conn.close()


# 🔹 FITUR LIHAT DAFTAR TEAM
def lihat_daftar_team():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, region FROM team")
    teams = cursor.fetchall()

    conn.close()

    print("\n=== DAFTAR TEAM ===")
    if not teams:
        print("Belum ada data team")
    else:
        for team in teams:
            print(f"ID: {team[0]} | Nama: {team[1]} | Region: {team[2]}")


def main_menu():
    create_tables()

    while True:
        print("\n=== MENU E-SPORT ===")
        print("1. Tambah Team")
        print("2. Tambah Player")
        print("3. Tambah Tournament")
        print("4. Lihat Daftar Team")
        print("5. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            name = input("Nama Team: ")
            region = input("Region: ")
            team = Team(name, region)

            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO team (name, region) VALUES (?, ?)",
                (team.name, team.region)
            )
            conn.commit()
            conn.close()
            print("Team berhasil ditambahkan")

        elif pilihan == "2":
            nickname = input("Nickname Player: ")
            role = input("Role Player: ")
            player = Player(nickname, role)

            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO player (nickname, role) VALUES (?, ?)",
                (player.nickname, player.role)
            )
            conn.commit()
            conn.close()
            print("Player berhasil ditambahkan")

        elif pilihan == "3":
            title = input("Nama Tournament: ")
            prize = int(input("Prize Pool: "))
            tournament = Tournament(title, prize)

            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO tournament (title, prize_pool) VALUES (?, ?)",
                (tournament.title, tournament.prize_pool)
            )
            conn.commit()
            conn.close()
            print("Tournament berhasil ditambahkan")

        elif pilihan == "4":
            lihat_daftar_team()

        elif pilihan == "5":
            print("Program selesai")
            break

        else:
            print("Pilihan tidak valid")
