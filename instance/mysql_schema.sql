DROP TABLE IF EXISTS user;

create table user(
    id integer primary key auto_increment,
    email varchar(50) unique not null,
    password varchar(50) not null,
    first_name varchar(20) not null,
    last_name varchar(20) not null,
    middle_name varchar(20),
    phone varchar(20),
    occupation varchar(50),
    created datetime default current_timestamp()
);