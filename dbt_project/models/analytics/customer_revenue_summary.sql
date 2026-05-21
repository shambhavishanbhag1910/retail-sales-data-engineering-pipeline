select
    c.customer_id,
    c.customer_name,
    c.city,
    c.state,
    count(distinct f.order_id) as total_orders,
    sum(f.net_sales) as total_revenue
from {{ ref('fact_sales') }} f
left join {{ ref('dim_customers') }} c
    on f.customer_id = c.customer_id
group by
    c.customer_id,
    c.customer_name,
    c.city,
    c.state
order by total_revenue desc