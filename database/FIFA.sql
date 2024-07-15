/* Lógico_1: */

CREATE TABLE WorldCup (
    cupYear INTEGER PRIMARY KEY,
    host VARCHAR(255),
    numTeams INTEGER,
    numTotalGames INTEGER,
    goalsScored INTEGER,
    champion VARCHAR(255)
);

CREATE TABLE Team (
    teamName VARCHAR(255) PRIMARY KEY,
    numCupsWon INTEGER DEFAULT 0
);

CREATE TABLE Goal (
    gameDate DATE,
    teamName VARCHAR(255),
    scorer VARCHAR(255),
    goalMinute INTEGER,
    ownGoal BOOLEAN,
    penalty BOOLEAN,
    PRIMARY KEY (goalMinute, teamName, gameDate)
);

CREATE TABLE Game (
    gameDate DATE,
    homeTeamName VARCHAR(255),
    awayTeamName VARCHAR(255),
    homeScore INTEGER,
    awayScore INTEGER,
    city VARCHAR(255),
    PRIMARY KEY (gameDate, homeTeamName, awayTeamName)
);

CREATE TABLE Team_WorldCup (
    placedAt INTEGER,
    teamName VARCHAR(255),
    numGames INTEGER,
    wins INTEGER DEFAULT 0,
    draws INTEGER DEFAULT 0,
    losses INTEGER DEFAULT 0,
    worldCupYear INTEGER
);
 
ALTER TABLE Goal ADD CONSTRAINT FK_Goal_2
    FOREIGN KEY (teamName)
    REFERENCES Team (teamName)
    ON DELETE CASCADE;
 
ALTER TABLE Goal ADD CONSTRAINT FK_Goal_3
    FOREIGN KEY (gameDate)
    REFERENCES Game (gameDate)
    ON DELETE CASCADE;
 
ALTER TABLE Game ADD CONSTRAINT FK_Game_2
    FOREIGN KEY (homeTeamName)
    REFERENCES Team (teamName)
    ON DELETE CASCADE;

ALTER TABLE Game ADD CONSTRAINT FK_Game_3
    FOREIGN KEY (awayTeamName)
    REFERENCES Team (teamName)
    ON DELETE CASCADE;
 
ALTER TABLE Team_WorldCup ADD CONSTRAINT FK_Team_WorldCup_1
    FOREIGN KEY (teamName)
    REFERENCES Team (teamName)
    ON DELETE RESTRICT;
 
ALTER TABLE Team_WorldCup ADD CONSTRAINT FK_Team_WorldCup_2
    FOREIGN KEY (worldCupYear)
    REFERENCES WorldCup (cupYear)
    ON DELETE RESTRICT;
    

LOAD DATA LOCAL INFILE 'WorldCup.csv'
INTO TABLE WorldCup
FIELDS TERMINATED BY ';'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;

LOAD DATA LOCAL INFILE 'Team.csv'
INTO TABLE Team
FIELDS TERMINATED BY ';'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;

LOAD DATA LOCAL INFILE 'Goal2.csv'
INTO TABLE Goal
FIELDS TERMINATED BY ';'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;

LOAD DATA LOCAL INFILE 'Game.csv'
INTO TABLE Game
FIELDS TERMINATED BY ';'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;

LOAD DATA LOCAL INFILE 'Team_WorldCup.csv'
INTO TABLE Team_WorldCup
FIELDS TERMINATED BY ';'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;