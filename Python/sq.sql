select 3+5;
select 3-5;

select upper('deepanshu');

create database cetpa;
use cetpa;

create table class(name varchar(255),
age int,
course varchar(255),
fees int);

show tables;


select * from class;
 insert into class (name,age,course,fees)values
 ('deepanshu',45,'ai',50000),('abc',465873,'ml',4573);


select * from class;
select course, fees from class;

use weekend;
show tables;

select * from employee;
select * from employee where age=30;
select * from employee where age>30 and city='DELHI';

select * from class;
# alter, drop a column, add column, reanme
alter table class drop column course;
alter table class add column course varchar(255);
alter table class rename column fees to amount;


# update
update  class set name='xyz' where name='abc';
update  class set age=1 where amount=50000;

SET SQL_SAFE_UPDATES = 0;
delete from class   where age=1;




truncate table class;
drop table class;




