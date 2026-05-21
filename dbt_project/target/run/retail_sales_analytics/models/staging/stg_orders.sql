
  create view "retail_db"."analytics_staging"."stg_orders__dbt_tmp"
    
    
  as (
    select
    order_id::int as order_id,
    customer_id::int as customer_id,
    cast(order_date as date) as order_date,
    lower(trim(order_status)) as order_status,
    lower(trim(payment_method)) as payment_method
from "retail_db"."public"."raw_orders"
where order_id is not null
  );