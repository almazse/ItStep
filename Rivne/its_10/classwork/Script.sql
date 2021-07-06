--select count(*)
--from employee e 
--where city_id in
--(select id from city c where c.city_name = 'London')

--select first_name, last_name from employee e
--where date_of_birth in 
--(select min(date_of_birth) from employee e2 group by city_id) 

--select first_name, last_name, date_of_birth from employee e
--where extract (month from date_of_birth) =
--extract(month from now())

select first_name, last_name from employee e
where id in 
(select employee_id from orders o where city_id in
(select id from city c where c.city_name = 'Madrid')) 