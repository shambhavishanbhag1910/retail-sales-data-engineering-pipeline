
  create view "retail_db"."analytics_staging"."stg_customers__dbt_tmp"
    
    
  as (
    select
    customer_id::int as customer_id,
    trim(customer_name) as customer_name,
    lower(trim(email)) as email,
    trim(city) as city,
    trim(state) as state,
    cast(created_at as date) as created_date
from "retail_db"."public"."raw_customers"
where customer_id is not null
  );