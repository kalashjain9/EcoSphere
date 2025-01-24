CREATE DATABASE energy_monitor;

USE energy_monitor;

CREATE TABLE consumption (
    id INT AUTO_INCREMENT PRIMARY KEY,
    electricity FLOAT NOT NULL,
    gas FLOAT NOT NULL,
    water FLOAT NOT NULL,
    carbon_footprint FLOAT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
