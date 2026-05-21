
  
    

  create  table "retail_db"."analytics_analytics"."customer_revenue_summary__dbt_tmp"
  
  
    as
  
  (
    select
    c.customer_id,
    c.customer_name,
    c.city,
    c.state,
    count(distinct f.order_id) as total_orders,
    sum(f.net_sales) as total_revenue
from "retail_db"."analytics_marts"."fact_sales" f
left join "retail_db"."analytics_marts"."dim_customers" c
    on f.customer_id = c.customer_id
group by
    c.customer_id,
    c.customer_name,
    c.city,
    c.state
order by total_revenue desc
  );
  