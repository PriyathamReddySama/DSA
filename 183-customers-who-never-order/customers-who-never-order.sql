# Write your MySQL query statement below
SELECT c.name as customers
from customers c
left join orders o
    on c.id = o.customerId
WHERE o.customerId is NULL;