--
-- File generated with SQLiteStudio v3.0.6 on Sat Jul 25 15:47:37 2015
--
-- Text encoding used: windows-1252
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: reviews
CREATE TABLE `reviews` (
  `rid` int(11)  PRIMARY KEY,
  `place_id` int(11) NOT NULL,
  `rating` int(11) NOT NULL,
  `review` varchar(140) NOT NULL
  
);

-- Table: bucketlist
CREATE TABLE `bucketlist` (
  `uid` int(11) NOT NULL,
  `place_id` int(11) NOT NULL,
  `user_comments` varchar(140) NOT NULL
);

-- Table: places
CREATE TABLE `places` (
  `place_id` int(11) NOT NULL PRIMARY KEY,
  `name` varchar(50) NOT NULL,
  `category` varchar(50) NOT NULL
  
);

-- Table: followers
CREATE TABLE `followers` (
  `uid` int(11) NOT NULL,
  `fid` int(11) NOT NULL
);

-- Table: place_tags
CREATE TABLE `place_tags` (
  `place_id` int(11) NOT NULL,
  `tag_id` int(11) NOT NULL
);

-- Table: tags
CREATE TABLE `tags` (
  `tag_id` int(11) NOT NULL,
  `tag` int(11) NOT NULL
);

-- Table: visited
CREATE TABLE `visited` (
  `uid` int(11) NOT NULL,
  `place_id` int(11) NOT NULL
);

-- Table: users
CREATE TABLE users (uid INTEGER PRIMARY KEY, gid INTEGER, fname VARCHAR (30), lname VARCHAR (30), gender VARCHAR (10), email VARCHAR (30));

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
