select
    date_trunc('month', order_date)::date as sales_month,
    count(distinct order_id) as total_orders,
    sum(net_sales) as monthly_revenue
from "retail_db"."analytics_marts"."fact_sales"
group by date_trunc('month', order_date)::date
order by sales_month