-- The script creates a new database as well as
-- a new user who should only have select privileges.
-- The database:
CREATE DATABASE IF  NOT EXISTS `hbtn_0d_2`;
-- The new user:
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
-- Grant select privilege:
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
