create table if not exists User (
    userid integer primary key autoincrement,
    username text not null,
    usertype text not null,
    date_joined datetime default current_timestamp
    oauth_token text not null,
);

create table if not exists in_group (
    groupid integer primary key autoincrement,
    groupname text not null,
    groupadmin integer not null,
    foreign key(groupadmin) references User(userid),
);

create table if not exists Contest (
    contestid integer primary key autoincrement,
    contestcode integer not null,
    contestname text not null,
    date_start datetime not null,
    date_end datetime,
    visible integer default 0,
    group integer not null,
    foreign key(group) references in_group(groupid),
);

create table if not exists Task (
    taskid integer primary key autoincrement,
    -- Json-stringified tags array
    tasktags text not null,
);

create table if not exists contains_task (
    contest integer primary key not null,
    task integer primary key not null,
    foreign key(contest) references Contest(contestid),
    foreign key(task) references Task(taskid),    
);
