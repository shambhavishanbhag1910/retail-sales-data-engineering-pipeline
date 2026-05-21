select
    i.product_id,
    p.product_name,
    p.category,
    i.stock_quantity,
    i.reorder_level,
    case
        when i.stock_quantity <= i.reorder_level then true
        else false
    end as is_low_stock,
    i.last_updated
from "retail_db"."analytics_staging"."stg_inventory" i
left join "retail_db"."analytics_staging"."stg_products" p
    on i.product_id = p.product_id