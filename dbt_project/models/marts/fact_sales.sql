select
    oi.order_item_id,
    o.order_id,
    o.customer_id,
    oi.product_id,
    o.order_date,
    o.order_status,
    o.payment_method,
    oi.quantity,
    oi.unit_price,
    oi.discount,
    (oi.quantity * oi.unit_price) as gross_sales,
    ((oi.quantity * oi.unit_price) - oi.discount) as net_sales
from {{ ref('stg_orders') }} o
inner join {{ ref('stg_order_items') }} oi
    on o.order_id = oi.order_id
where o.order_status = 'completed'