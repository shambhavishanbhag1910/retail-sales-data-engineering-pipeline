select
    p.product_id,
    p.product_name,
    p.category,
    sum(f.quantity) as total_quantity_sold,
    sum(f.net_sales) as total_revenue
from "retail_db"."analytics_marts"."fact_sales" f
left join "retail_db"."analytics_marts"."dim_products" p
    on f.product_id = p.product_id
group by
    p.product_id,
    p.product_name,
    p.category
order by total_revenue desc