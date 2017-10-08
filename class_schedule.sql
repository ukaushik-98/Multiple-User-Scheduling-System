create table class_schedule(id integer,
class_id integer,
class_name text,
professor_name text,
class_time text,
final text);

insert into class_schedule (id, class_id, class_name, professor_name, class_time, final) values (10, 16213, 'cse 132 disc','staff', '4:00-4:50p MW', 'NA'); 

update class_schedule
set class_id = 47459, class_name = 'physics 20e disc', professor_name = 'staff', class_time = '4:00-4:50pm W', final = 'NA'
where id = 10;

create table udit.test1 as 
select * from world.class_schedule order by class_time desc;
alter table class_schedule
add primary key (id);


SET SQL_SAFE_UPDATES = 0;