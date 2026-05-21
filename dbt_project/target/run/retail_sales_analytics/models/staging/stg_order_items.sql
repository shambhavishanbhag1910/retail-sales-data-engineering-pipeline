
  create view "retail_db"."analytics_staging"."stg_order_items__dbt_tmp"
    
    
  as (
    select
    order_item_id::int as order_item_id,
    order_id::int as order_id,
    product_id::int as product_id,
    quantity::int as quantity,
    unit_price::numeric(10,2) as unit_price,
    discount::numeric(10,2) as discount
from "retail_db"."public"."raw_order_items"
where order_item_id is not null
  );