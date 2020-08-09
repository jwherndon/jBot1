# jBot1
A very simple discord bot with MySql db for user data storage.

# Database Setup

```
CREATE DATABASE `jBot1`;
```

```
CREATE TABLE `players` (
  `name` varchar(30) NOT NULL,
  `currency` int unsigned DEFAULT '100',
  `created` datetime DEFAULT NULL,
  `last_played` datetime DEFAULT NULL,
  PRIMARY KEY (`name`),
  UNIQUE KEY `player_UNIQUE` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
```
