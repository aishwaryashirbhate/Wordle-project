import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
        while true:
            ( )

    return conn

def create_table(tablename):
    conn = sqlite3.connect('logs db')
    if tablename == "gameplay":
        cur = conn.cursor()
        try:
            cur.execute('''CREATE TABLE IF NOT EXISTS GAMEPLAY
                           (game_id text primary key,ip_address text,date_of_play datetime) ''')
            conn.commit()
            conn.close()
        except Error as e:
            print(e)
            return





    elif tablename=='game_data':
        cur = conn.cursor()
        try:
            cur.execute('pragma foreign_keys=ON')
            cur.execute('''CREATE TABLE IF NOT EXISTS GAMEDATA
                                   (id text  ,input_words text,answer text,win_percentage text,number_of_wins text)  ''')
            conn.commit()

        except Error as e :
            print(e)
            return



def create_project( game_data):
    """
    Create a new project into the projects table
    :param conn:
    :param game_data:
    :return: project id
    """
    try:
        conn = sqlite3.connect('logs db')
        sql = ''' INSERT INTO GAMEDATA(id,input_words,answer,win_percentage,number_of_wins)
                  VALUES(?,?,?,?,?) '''
        cur = conn.cursor()
        cur.execute(sql,game_data)
        conn.commit()
        conn.close()
    except Error as e:
        print(e)


def create_task( gameplay):
    """
    Create a new task

    :param gameplay:
    :return:
    """

    try:
        conn = sqlite3.connect('logs db')
        sql = ''' INSERT INTO GAMEPLAY(game_id,ip_address,date_of_play)
                  VALUES(?,?,?) '''
        cur = conn.cursor()
        cur.execute(sql,gameplay)

        conn.commit()

        conn.close()
    except Error as e :
        print(e)

def game_report(start,end):
    """
    Create a new task
    :param :
    :param :
    :return:
    """

    try:
      for row in curr.execute('''SELECT a.id,b.date_of_play,b.ip_address,a.input_words,a.answer,a.win_percentage,a.number_of_wins FROM GAMEDATA a join GAMEPLAY b on a.ID = b.GAME_ID WHERE date_of_play>=? and date_of_play<=?''',[start,end]):
        print(list(row))

    except Error as e :
        print(e)

if __name__ == '__main__':
    # PRINT DATA

    conn=sqlite3.connect('logs db')
    curr= conn.cursor()
    # for row in curr.execute('''SELECT * FROM GAMEPLAY'''):
    #     print(list(row))

    # for row in curr.execute('''SELECT * FROM GAMEPLAY'''):
    #     print(row)

    # CHECK GAME REPORT DATA
    game_report('04/28/2022, 00:25:44', '04/28/2022, 02:00:47')
