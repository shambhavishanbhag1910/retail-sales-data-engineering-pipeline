select
    product_id::int as product_id,
    stock_quantity::int as stock_quantity,
    reorder_level::int as reorder_level,
    cast(last_updated as date) as last_updated
from {{ source('raw', 'raw_inventory') }}
where product_id is not null