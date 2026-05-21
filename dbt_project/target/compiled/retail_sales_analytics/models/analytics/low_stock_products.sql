select
    product_id,
    product_name,
    category,
    stock_quantity,
    reorder_level,
    last_updated
from "retail_db"."analytics_marts"."fact_inventory"
where is_low_stock = true
order by stock_quantity asc