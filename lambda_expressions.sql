set global local_infile = 1;
update revisions SET FileName = CONCAT('/',FileName) where project='guava';
USE generics;

DROP TABLE IF EXISTS lambda_expressions, lambda_expressions_changed;

CREATE TABLE lambda_expressions (
    id INT NOT NULL AUTO_INCREMENT, 
    project VARCHAR(100),
    module VARCHAR(100),
    filename VARCHAR(255),
    revision VARCHAR(50),
    container VARCHAR(255), 
    container_granularity VARCHAR(255), 
    type VARCHAR(255), 
    count INT default 1,
    PRIMARY KEY (id)
);

CREATE TABLE lambda_expressions_changed (
    id INT NOT NULL AUTO_INCREMENT, 
    project VARCHAR(100),
    module VARCHAR(100),
    filename VARCHAR(255),
    revision VARCHAR(50),
    added boolean,
    container VARCHAR(255), 
    container_granularity VARCHAR(255),
    type VARCHAR(255), 
    count INT default 1, 
    PRIMARY KEY (id)
);