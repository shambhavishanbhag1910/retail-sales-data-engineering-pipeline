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
from {{ ref('stg_inventory') }} i
left join {{ ref('stg_products') }} p
    on i.product_id = p.product_id