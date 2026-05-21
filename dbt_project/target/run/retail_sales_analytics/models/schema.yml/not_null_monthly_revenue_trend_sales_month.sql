
    
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select sales_month
from "retail_db"."analytics_analytics"."monthly_revenue_trend"
where sales_month is null



  
  
      
    ) dbt_internal_test