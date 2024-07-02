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
    goalMinute INTEGER,
    scorer VARCHAR(255),
    penalty BOOLEAN,
    ownGoal BOOLEAN,
    teamName VARCHAR(255),
    gameDate DATE,
    PRIMARY KEY (goalMinute, teamName, gameDate)
);

CREATE TABLE Game (
    city VARCHAR(255),
    gameDate DATE,
    homeTeamName VARCHAR(255),
    homeScore INTEGER,
    awayTeamName VARCHAR(255),
    awayScore INTEGER,
    PRIMARY KEY (gameDate, homeTeamName, awayTeamName)
);

CREATE TABLE Team_WorldCup (
    teamName VARCHAR(255),
    worldCupYear INTEGER,
    numGames INTEGER,
    wins INTEGER DEFAULT 0,
    placedAt INTEGER,
    losses INTEGER DEFAULT 0,
    draws INTEGER DEFAULT 0
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