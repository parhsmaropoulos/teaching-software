
drop table if exists students;
	create table students (
		id integer primary key autoincrement,
		firstname text not null,
		lastname text not null
	);
