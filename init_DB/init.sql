----- DROP TABLE IF EXISTS users_language;
DROP TABLE IF EXISTS users;

----- USERS TABLE;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    user_id BIGINT UNIQUE NOT NULL,
    username TEXT NOT NULL,
    language TEXT NOT NULL,
    timestamp DATE NOT NULL
);

----- LANGUAGE TABLE; 

----- joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
----- something to add on later maybe atm just from datetime import DATE ---> date.today()...
