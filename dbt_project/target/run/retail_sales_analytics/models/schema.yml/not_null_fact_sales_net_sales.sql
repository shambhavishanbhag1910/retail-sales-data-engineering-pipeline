
    
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select net_sales
from "retail_db"."analytics_marts"."fact_sales"
where net_sales is null



  
  
      
    ) dbt_internal_test