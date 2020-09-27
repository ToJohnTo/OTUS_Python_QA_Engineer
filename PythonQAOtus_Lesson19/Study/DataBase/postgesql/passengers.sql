CREATE TABLE IF NOT EXISTS passenger_info
(
    id                SERIAL PRIMARY KEY,
    name              VARCHAR(30) NOT NULL,
    surname           VARCHAR(30) NOT NULL,
    patronymic        VARCHAR(30),
    phone             VARCHAR(30) NOT NULL,
    flight_num        INTEGER     NOT NULL,
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
