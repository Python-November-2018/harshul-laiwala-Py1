-- Return all users who are friends with Kermit, make sure their names are displayed in results.
SELECT concat(u1.first_name, u1.last_name) as user_ , concat(u2.first_name , u2.last_name) as friend_name FROM users u1
JOIN friendships f ON u1.id=f.friend_1_id 
join users u2 on u2.id=f.friend_2_id
 where u1.first_name ='Kermit';

--  Return the count of all friendships
Select count(*) from friendships;

-- Find out who has the most friends and return the count of their friends.
SELECT count(*) as NumberOfFriends , concat(u1.first_name , u1.last_name) as user_ FROM users u1
LEFT JOIN friendships f ON u1.id=f.friend_1_id 
LEFT JOIN users as u2 ON u2.id = f.friend_2_id group by u1.id order by count(*) Desc;

-- Create a new user and make them friends with Eli Byers, Kermit The Frog, and Marky Mark
Insert into users Values( 6 ,'Eli', 'Byers', now());
Insert into friendships Values 
(6, 4,now()),
(6, 2,now()), 
(6,5,now());

-- Return the friends of Eli in alphabetical order
SELECT concat(u1.first_name, u1.last_name) as user_ , concat(u2.first_name , u2.last_name) as friend_name FROM users u1
JOIN friendships f ON u1.id=f.friend_1_id 
join users u2 on u2.id=f.friend_2_id
 where u1.first_name ='Eli' order by u2.first_name asc;

-- Remove Marky Mark from Eli’s friends.
Delete from friendships where friendships.friend_2_id IN (select id from users where first_name='Marky' and last_name='Mark');

-- Return all friendships, displaying just the first and last name of both friends
SELECT concat(u1.first_name, u1.last_name) as user_ , concat(u2.first_name , u2.last_name) as friend_name FROM users u1
JOIN friendships f ON u1.id=f.friend_1_id 
join users u2 on u2.id=f.friend_2_id;