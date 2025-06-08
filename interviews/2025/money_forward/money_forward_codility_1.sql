create table hotels (
    id integer PRIMARY KEY AUTOINCREMENT,
    name varchar NOT NULL,
    created_at timestamp NOT NULL,
    updated_at timestamp NOT NULL
);

create table plans (
    id integer PRIMARY KEY AUTOINCREMENT,
    name varchar NOT NULL,
    period_from timestamp NOT NULL,
    period_to timestamp NOT NULL,
    enable boolean NOT NULL DEFAULT false,
    hotel_id integer NOT NULL,
    created_at timestamp NOT NULL,
    updated_at timestamp NOT NULL,
    FOREIGN KEY (hotel_id) REFERENCES hotels(id)
);

create table rooms (
    id integer PRIMARY KEY AUTOINCREMENT,
    name varchar NOT NULL,
    enable boolean NOT NULL DEFAULT false,
    created_at timestamp NOT NULL,
    updated_at timestamp NOT NULL,
    FOREIGN KEY (hotel_id) REFERENCES hotels(id)
);

create table prices (
    id integer PRIMARY KEY AUTOINCREMENT,
    date timestamp NOT NULL,
    price decimal NOT NULL,
    plan_id integer,
    room_id integer NOT NULL,
    created_at timestamp NOT NULL,
    updated_at timestamp NOT NULL,
    FOREIGN KEY (plan_id) REFERENCES plans(id),
    FOREIGN KEY (room_id) REFERENCES rooms(id)
);


create table roomstocks (
    id integer PRIMARY KEY AUTOINCREMENT,
    date timestamp NOT NULL,
    amount integer NOT NULL,
    room_id integer NOT NULL,
    created_at timestamp NOT NULL,
    updated_at timestamp NOT NULL,
    FOREIGN KEY (room_id) REFERENCES rooms(id)
);
