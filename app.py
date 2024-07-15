import pymysql.cursors

from flask import Flask, render_template, request

import config


connection = pymysql.connect(
    host=config.DATABASE_HOST,
    port=config.DATABASE_PORT,
    user=config.DATABASE_USER,
    password=config.DATABASE_PASSWORD,
    database=config.DATABASE_NAME,
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)
app = Flask(__name__)

app.config['MYSQL_UNIX_SOCKET'] = 'TCP'
#Especifica que a conexão é remota, para poder conseguir conectar ao WSL (https://superuser.com/questions/1354350/how-to-connect-to-mysql-running-on-xampp-through-wsl-terminal)


@app.route("/")
def worldcups():
    with connection.cursor() as cursor:
        query_args = []
        if request.args.get("search"):
            sql = """ SELECT * FROM `WorldCup` WHERE LOWER(`host`) LIKE LOWER(%s) or `cupYear` LIKE (%s) ORDER BY 'cupYear' DESC """
            search = "%{}%".format(request.args["search"])
            query_args = [search, search]
        else:
            sql = "SELECT * FROM `WorldCup`"
        cursor.execute(sql, query_args)
        worldcups = cursor.fetchall()

    return render_template("index.html", worldcups=worldcups, search=request.args.get("search"))


@app.route("/teams")
def teams():
    with connection.cursor() as cursor:
        query_args = []
        if request.args.get("search"):
            sql = "SELECT * FROM `Team` WHERE LOWER(`teamName`) LIKE LOWER(%s) ORDER BY 'numCupsWon' DESC"
            search = "%{}%".format(request.args["search"])
            query_args = [search]
        else:
            sql = "SELECT * FROM `Team` ORDER BY `numCupsWon` DESC"
        cursor.execute(sql, query_args)
        teams = cursor.fetchall()

    return render_template("teams.html", teams=teams, search=request.args.get("search"))


@app.route("/gamegoals")
def gamegoals():
    with connection.cursor() as cursor:
        query_args = []
        if request.args.get("search"):
            sql = """
                SELECT
                    `Game`.`gameDate`,`Game`.`city`,`Game`.`homeTeamName`, `Game`.`homeScore`, `Game`.`awayTeamName`, `Game`.`awayScore`, `Goal`.`scorer`, `Goal`.`goalMinute`
                FROM
                    `Game`
                LEFT JOIN
                    `Goal` ON `Game`.`gameDate` = `Goal`.`gameDate` AND (`Game`.`homeTeamName` = `Goal`.`teamName` OR `Game`.`awayTeamName` = `Goal`.`teamName`)
                WHERE `Goal`.`scorer` LIKE LOWER(%s) ORDER BY Game.gameDate DESC;
                """
            search = "%{}%".format(request.args["search"])
            query_args = [search]
        else:
            sql = """
                SELECT
                    `Game`.`gameDate`,`Game`.`city`,`Game`.`homeTeamName`, `Game`.`homeScore`, `Game`.`awayTeamName`, `Game`.`awayScore`, `Goal`.`scorer`, `Goal`.`goalMinute`
                FROM
                    `Game`
                LEFT JOIN
                    `Goal` ON `Game`.`gameDate` = `Goal`.`gameDate` AND (`Game`.`homeTeamName` = `Goal`.`teamName` OR `Game`.`awayTeamName` = `Goal`.`teamName`) ORDER BY Game.gameDate DESC;
                """
        cursor.execute(sql, query_args)
        gamegoals = cursor.fetchall()
    return render_template("gamegoals.html", gamegoals=gamegoals, search=request.args.get("search"))

@app.route("/totalgoals")
def totalgoals():
    with connection.cursor() as cursor:
        query_args = []
        if request.args.get("search"):
            sql = """
            SELECT 
                `teamName`, 
                COUNT(*) AS `totalGoals` 
            FROM 
                `Goal`
            WHERE 
                `teamName` LIKE LOWER(%s)
            GROUP BY 
                `teamName`
            ORDER BY 
                `totalGoals` DESC;
            """
            search = "%{}%".format(request.args["search"])
            query_args = [search]
        else:
            sql = """
            SELECT 
                `teamName`, 
                COUNT(*) AS `totalGoals` 
            FROM 
                `Goal`
            GROUP BY 
                `teamName`
            ORDER BY 
                `totalGoals` DESC;
            """
        cursor.execute(sql, query_args)
        totalgoals = cursor.fetchall()

    return render_template("totalgoals.html", totalgoals=totalgoals, search=request.args.get("search"))

@app.route("/neverwon")
def neverwons():
    with connection.cursor() as cursor:
        query_args = []
        if request.args.get("search"):
            sql = """
            SELECT 
                `teamName` 
            FROM 
                `Team` 
            WHERE 
                `numCupsWon`= '0'  AND (`teamName` LIKE (%s))
            ORDER BY 
                `teamName` ASC;
            """
            search = "%{}%".format(request.args["search"])
            query_args = [search]
        else:
            sql = """
            SELECT 
                `teamName` 
            FROM 
                `Team` 
            WHERE 
                `numCupsWon`= '0'
            ORDER BY 
                `teamName` ASC;
            """
        cursor.execute(sql, query_args)
        neverwons = cursor.fetchall()

    return render_template("neverwon.html", neverwons=neverwons, search=request.args.get("search"))

if __name__ == "__main__":
    app.run(debug=config.DEGUB)
