import vk_api
import time
import sqlite3


def createDB():
    rouletDB = sqlite3.connect('test.db')
    rouletDB.execute('''CREATE TABLE TASK
                        (ID         INT    NOT NULL,
                        NAME           TEXT     NOT NULL,
                        SECS       INT    NOT NULL);''')

    rouletDB.close()

#Сюда  ID
idfriends = [167772346, 347023208, 402970340, 191457944, 473652730, 253371424, 332102905, 183608248, 158681103,
228498504, 164308993, 202550436, 153238948, 155275281, 72935439, 202875104, 185987139, 364721967,
243793532, 119567107, 325801846, 194986080, 227615183, 200692546, 359438622, 199960277, 173736337,
309922374, 195248716, 175359492]


def appendFriends():
    friendDB = sqlite3.connect("test.db")

    login, password = '8ggggggg', 'ggggggg'
    vk_session = vk_api.VkApi(login, password)

    try:
        vk_session.auth()
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return

    vk = vk_session.get_api()

    friend = []

    for i in range(len(idfriends)):
        friend.append(vk.users.get(user_id = idfriends[i], fields = "online"))

    friend[i][0] = dict(friend[i][0])

    for i in range(len(friend)):

        params = (i, friend[i][0]["first_name"] + " " + friend[i][0]["last_name"], 0)

        friendDB.execute("INSERT INTO TASk VALUES (?, ?, ?)", params)
        friendDB.commit()

    print("FINE")
    friendDB.close()


def plus_secs(user):

    friendDB = sqlite3.connect("test.db")

    cursorTask = friendDB.execute("SELECT id, name, secs from TASK")

    for row in cursorTask:
        if row[1] == user:
            params = (row[2] + 45, row[0])
            friendDB.execute("UPDATE TASK set SECS = ? where ID = ?", params)
            friendDB.commit()

    friendDB.close()


createDB()
appendFriends()



def main():

    login, password = 'ппппп', 'пппппп'
    vk_session = vk_api.VkApi(login, password)

    try:
        vk_session.auth()
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return

    vk = vk_session.get_api()

    friend = []

    for i in range(len(idfriends)):
        friend.append(vk.users.get(user_id = idfriends[i], fields = "online"))

    for i in range(len(friend)):
        friend[i][0] = dict(friend[i][0])

        if friend[i][0]["online"]:
            print(friend[i][0]["online"], friend[i][0]["first_name"])

            user_name = friend[i][0]["first_name"] + " " + friend[i][0]["last_name"]

            plus_secs(user_name)

    print("\n work - fine")

while True:
    n = time.time()
    main()
    time.sleep(15)
    print(time.time() - n)
