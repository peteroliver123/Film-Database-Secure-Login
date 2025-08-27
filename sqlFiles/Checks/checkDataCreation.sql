ALTER TABLE users
DROP CHECK check_dates;

ALTER TABLE users
DROP CHECK check_is_locked;

ALTER TABLE users
DROP CHECK check_num_lockouts;

ALTER TABLE users
DROP CHECK check_admin;

ALTER TABLE users
DROP CHECK check_failed_entry;

ALTER TABLE attic
DROP CHECK check_attic;

ALTER TABLE kitchen
DROP CHECK check_kitchen;

ALTER TABLE lounge
DROP CHECK check_lounge;

ALTER TABLE users
ADD CONSTRAINT check_dates
CHECK (
	is_locked = "True" OR date_created = date_unlock
);

ALTER TABLE users
ADD CONSTRAINT check_is_locked
CHECK (
	is_locked = "True" OR is_locked = "False"
);

ALTER TABLE users
ADD CONSTRAINT check_num_lockouts
CHECK (
	num_lockouts >= 0 AND num_lockouts <= 1000
);

ALTER TABLE users
ADD CONSTRAINT check_admin
CHECK (
	username = "ADMIN" AND is_admin = "True" OR is_admin = "False"
);

ALTER TABLE users
ADD CONSTRAINT check_failed_entry
CHECK (
	failed_entry >= 0 AND failed_entry <= 3
);

ALTER TABLE attic
ADD CONSTRAINT check_attic
CHECK (
	age_rating IN ('U', 'PG', '12', '12A', '15', '18', 'BLANK') and location = "attic"
);

ALTER TABLE kitchen
ADD CONSTRAINT check_kitchen
CHECK (
	age_rating IN ('U', 'PG', '12', '12A', '15', '18', 'BLANK') and location = "kitchen"
);

ALTER TABLE lounge
ADD CONSTRAINT check_lounge
CHECK (
	age_rating IN ('U', 'PG', '12', '12A', '15', '18', 'BLANK') and location = "lounge"
);