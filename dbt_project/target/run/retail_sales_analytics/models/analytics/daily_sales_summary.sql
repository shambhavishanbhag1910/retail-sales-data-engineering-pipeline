
  
    

  create  table "retail_db"."analytics_analytics"."daily_sales_summary__dbt_tmp"
  
  
    as
  
  (
    select
    order_date,
    count(distinct order_id) as total_orders,
    count(distinct customer_id) as total_customers,
    sum(quantity) as total_quantity_sold,
    sum(gross_sales) as gross_revenue,
    sum(net_sales) as net_revenue
from "retail_db"."analytics_marts"."fact_sales"
group by order_date
order by order_date
  );
  