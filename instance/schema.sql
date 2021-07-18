DROP TABLE IF EXISTS user;

create table user(
    id integer primary key autoincrement,
    email text unique not null,
    password text not null,
    first_name text not null,
    last_name text not null,
    middle_name text,
    phone text,
    year int,
    month int,
    day int, 
    occupation text,
    created timespan default current_timespan
);