
  
    

  create  table "retail_db"."analytics_marts"."dim_dates__dbt_tmp"
  
  
    as
  
  (
    select distinct
    order_date as date_key,
    extract(year from order_date)::int as year,
    extract(month from order_date)::int as month,
    extract(day from order_date)::int as day,
    extract(quarter from order_date)::int as quarter
from "retail_db"."analytics_staging"."stg_orders"
where order_date is not null
  );
  