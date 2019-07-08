import configparser


# CONFIG
config = configparser.ConfigParser()
config.read('dwh.cfg')

# DROP TABLES

staging_events_table_drop = "DROP TABLE IF EXISTS staging_events"
staging_songs_table_drop = "DROP TABLE IF EXISTS staging_songs"
songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

staging_events_table_create= ("""
    CREATE TABLE staging_events(
        event_id BIGINT IDENTITY(0,1) PRIMARY KEY,
        artist VARCHAR(255),
        auth VARCHAR(255),
        first_name VARCHAR(255),
        gender VARCHAR(1),
        item_in_session INT,
        last_name VARCHAR(255),
        length DOUBLE PRECISION, 
        level VARCHAR(255),
        location VARCHAR(255),	
        method VARCHAR(25),
        page VARCHAR(255),	
        registration DOUBLE PRECISION,	
        session_id BIGINT,
        song VARCHAR(255),
        status INT,	
        ts DOUBLE PRECISION,
        user_agent VARCHAR(255),
        user_id INT);
""")

staging_songs_table_create = ("""
    CREATE TABLE staging_songs(
        song_id VARCHAR(100) PRIMARY KEY,
        num_songs INT,
        artist_id VARCHAR(100),
        artist_latitude DOUBLE PRECISION,
        artist_longitude DOUBLE PRECISION,
        artist_location VARCHAR(255),
        artist_name VARCHAR(255),
        title VARCHAR(255),
        duration DOUBLE PRECISION,
        year INT);
""")

songplay_table_create = ("""
    CREATE TABLE IF NOT EXISTS songplays (
        songplay_id BIGINT IDENTITY(0,1),
        start_time TIMESTAMP NOT NULL,
        user_id INT NOT NULL,
        level VARCHAR(255),
        song_id VARCHAR(255),
        artist_id VARCHAR(255),
        session_id INT, 
        location VARCHAR(255),
        user_agent VARCHAR(255),
        PRIMARY KEY (songplay_id));
""")

user_table_create = ("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INT, 
        first_name VARCHAR(255), 
        last_name VARCHAR(255), 
        gender VARCHAR(255), 
        level VARCHAR(255),
        PRIMARY KEY (user_id));
""")

song_table_create = ("""
    CREATE TABLE IF NOT EXISTS songs (
        song_id VARCHAR(255), 
        title VARCHAR(255), 
        artist_id VARCHAR(255), 
        year INT, 
        duration DOUBLE PRECISION,
        PRIMARY KEY (song_id));
""")

artist_table_create = ("""
    CREATE TABLE IF NOT EXISTS artists (
        artist_id VARCHAR(255), 
        name VARCHAR(255), 
        location VARCHAR(255), 
        lattitude DOUBLE PRECISION, 
        longitude DOUBLE PRECISION,
        PRIMARY KEY (artist_id));
""")

time_table_create = ("""
    CREATE TABLE IF NOT EXISTS time (
        start_time BIGINT, 
        hour INT, 
        day INT, 
        week INT, 
        month INT, 
        year INT, 
        weekday INT,
        PRIMARY KEY (start_time));
""")

# STAGING TABLES

staging_events_copy = ("""
""").format()

staging_songs_copy = ("""
""").format()

# FINAL TABLES

songplay_table_insert = ("""
""")

user_table_insert = ("""
""")

song_table_insert = ("""
""")

artist_table_insert = ("""
""")

time_table_insert = ("""
""")

# QUERY LISTS

create_table_queries = [staging_events_table_create, staging_songs_table_create, songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [staging_events_table_drop, staging_songs_table_drop, songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
copy_table_queries = [staging_events_copy, staging_songs_copy]
insert_table_queries = [songplay_table_insert, user_table_insert, song_table_insert, artist_table_insert, time_table_insert]
