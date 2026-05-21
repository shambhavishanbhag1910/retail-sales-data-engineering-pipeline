
    
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select order_date
from "retail_db"."analytics_analytics"."daily_sales_summary"
where order_date is null



  
  
      
    ) dbt_internal_test