
  
    

  create  table "retail_db"."analytics_analytics"."low_stock_products__dbt_tmp"
  
  
    as
  
  (
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
  );
  