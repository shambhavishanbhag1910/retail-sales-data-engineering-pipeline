
  
    

  create  table "retail_db"."analytics_marts"."dim_customers__dbt_tmp"
  
  
    as
  
  (
    select
    customer_id,
    customer_name,
    email,
    city,
    state,
    created_date
from "retail_db"."analytics_staging"."stg_customers"
  );
  