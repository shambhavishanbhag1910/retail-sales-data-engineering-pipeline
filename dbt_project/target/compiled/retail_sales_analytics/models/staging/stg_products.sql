select
    product_id::int as product_id,
    trim(product_name) as product_name,
    trim(category) as category,
    unit_price::numeric(10,2) as unit_price,
    supplier_id::int as supplier_id
from "retail_db"."public"."raw_products"
where product_id is not null