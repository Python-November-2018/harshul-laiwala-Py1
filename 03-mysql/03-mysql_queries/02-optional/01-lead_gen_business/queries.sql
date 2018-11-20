-- 1. What query would you run to get the total revenue for March of 2012?
select sum(amount) , count(charged_datetime) from billing where charged_datetime > '2012-03-01 00:00:00' and charged_datetime < '2012-04-01 00:00:00';

-- 2. What query would you run to get total revenue collected from the client with an id of 2?
select sum(amount) as Total_revenue from billing where client_id = 2;

-- 3. What query would you run to get all the sites that client=10 owns?
select domain_name from sites where client_id=10;

-- 4. What query would you run to get total # of sites created per month per year for the client with an id of 1? What about for client=20?
select count(site_id) , month(created_datetime), created_datetime from sites where client_id=1  group by month(created_datetime), year(created_datetime);

-- 5. What query would you run to get the total # of leads generated for each of the sites between January 1, 2011 to February 15, 2011?
select count(leads_id) from leads where registered_datetime between '2011-01-01' and '2011-02-15';

-- 6. What query would you run to get a list of client names and the total # of leads we've generated for each of our clients between January 1, 2011 to December 31, 2011?
select concat(clients.first_name,' ',clients.last_name) as client_name , count(leads.leads_id) from clients
join sites on clients.client_id = sites.client_id 
join leads on sites.site_id = leads.site_id 
where leads.registered_datetime between '2011-01-01' and '2011-12-31' group by clients.client_id;

-- 7. What query would you run to get a list of client names and the total # of leads we've generated for each client each month between months 1 - 6 of Year 2011?
select concat(clients.first_name,' ',clients.last_name) as client_name , count(leads.leads_id) from clients
join sites on clients.client_id = sites.client_id 
join leads on sites.site_id = leads.site_id 
where leads.registered_datetime between '2011-01-01' and '2011-06-31' group by clients.client_id;


-- 8. What query would you run to get a list of client names and the total # of leads we've generated for each of our clients' sites between January 1, 2011 to December 31, 2011? Order this query by client id.  Come up with a second query that shows all the clients, the site name(s), and the total number of leads generated from each site for all time.
select clients.client_id,concat(clients.first_name,' ',clients.last_name) as client_name,  count(leads.leads_id) from clients
join sites on clients.client_id = sites.client_id 
join leads on sites.site_id = leads.site_id 
where leads.registered_datetime between '2011-01-01' and '2011-12-31' group by clients.client_id order by clients.client_id;

select clients.client_id,concat(clients.first_name,' ',clients.last_name) as client_name,  count(leads.leads_id) , sites.domain_name from clients
join sites on clients.client_id = sites.client_id 
join leads on sites.site_id = leads.site_id 
group by clients.client_id order by clients.client_id;


-- 9. Write a single query that retrieves total revenue collected from each client for each month of the year. Order it by client id.

-- 10. Write a single query that retrieves all the sites that each client owns. Group the results so that each row shows a new client. It will become clearer when you add a new field called 'sites' that has all the sites that the client owns. (HINT: use GROUP_CONCAT)