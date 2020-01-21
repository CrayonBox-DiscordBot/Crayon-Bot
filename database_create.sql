create table action
(
    actionID    int           not null,
    action_name varchar(2000) not null,
    constraint action_actionID_uindex
        unique (actionID)
);

alter table action
    add primary key (actionID);

create table phrase
(
    phraseID int auto_increment
        primary key,
    phrase   varchar(2000) not null
);

create table server
(
    serverID bigint                  not null,
    prefix   varchar(5) default 'c!' not null,
    constraint server_server_ID_uindex
        unique (serverID)
);

alter table server
    add primary key (serverID);

create table channel
(
    channelID bigint               not null,
    server_ID bigint               not null,
    ignored   tinyint(1) default 0 not null,
    used      int        default 0 not null,
    constraint channel_channelID_uindex
        unique (channelID),
    constraint channel_server_serverID_fk
        foreign key (server_ID) references server (serverID)
            on delete cascade
);

alter table channel
    add primary key (channelID);

create table channel_limitations
(
    channel_ID  bigint                  not null,
    length_min  int        default 0    not null,
    length_max  int        default 2000 not null,
    atachements tinyint(1) default 1    not null,
    constraint channel_limitations_channel_ID_uindex
        unique (channel_ID),
    constraint channel_limitations_channel_channelID_fk
        foreign key (channel_ID) references channel (channelID)
            on delete cascade
);

create table channel_special_phrases
(
    channel_ID   bigint                       not null,
    phrase_ID    int                          not null,
    special_type enum ('ignore', 'forbidden') not null,
    constraint channel_special_phrases_channel_ID_phrase_ID_uindex
        unique (channel_ID, phrase_ID),
    constraint channel_special_phrases_channel_channelID_fk
        foreign key (channel_ID) references channel (channelID)
            on delete cascade,
    constraint channel_special_phrases_phrase_phraseID_fk
        foreign key (phrase_ID) references phrase (phraseID)
            on delete cascade
);

create table channel_special_users
(
    channel_ID   bigint                       not null,
    user_ID      bigint                       not null,
    special_type enum ('ignore', 'forbidden') not null,
    constraint channel_special_users_channel_ID_user_ID_uindex
        unique (channel_ID, user_ID),
    constraint channel_special_users_channel_channelID_fk
        foreign key (channel_ID) references channel (channelID)
            on delete cascade
);

create table channel_verification
(
    channel_ID  bigint                 not null,
    phrase_ID   int                    not null,
    role_action enum ('add', 'remove') not null,
    role_ID     bigint                 not null,
    constraint verification_channel_channelID_fk
        foreign key (channel_ID) references channel (channelID)
            on delete cascade,
    constraint verification_phrase_phraseID_fk
        foreign key (phrase_ID) references phrase (phraseID)
            on delete cascade
);

create table server_log
(
    server_ID                   bigint not null,
    verification_log_channel_ID bigint not null,
    constraint server_log_server_ID_uindex
        unique (server_ID),
    constraint server_log_channel_channelID_fk
        foreign key (verification_log_channel_ID) references channel (channelID)
            on delete cascade
);


