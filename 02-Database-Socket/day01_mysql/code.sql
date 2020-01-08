

create table orders(
  order_id varchar(32), -- 订单编号
  cust_id varchar(32),  -- 客户编号
  order_date datetime,  -- 下单时间,日期时间
  status int,           -- 状态
  products_num int,     -- 商品数量，整数
  amt decimal(16,2)     -- 订单总金额
                        -- 最长１６位，小数２位
) default charset=utf8;

-- 查询
select * from orders;

-- 插入记录
-- 1所有字段都插入值
insert into orders VALUES
('201801010001','c0001',now(),1,1,100.00);
-- 2向表中插入指定字段值
insert into orders(order_id, cust_id)
values('201801010002','c0002');
-- 3一个ｓｑｌ语句插入多笔数据
insert into orders VALUES
('201801010003','c0003',now(),1,1,200.00),
('201801010004','c0004',now(),1,1,200.00);

-- 查询记录
-- 语法格式
-- select * from 表名 [where 条件];
-- select 字段1, 字段2...
-- from 表名 [where 条件];

-- 实例
-- 查询表中所有数据
-- select * from orders;
-- 查询订单编号，客户编号
-- select order_id,cust_id from orders;
-- 查询指定字段，给每个字段起个别名
-- select order_id "订单编号",
--        cust_id "客户编号"
-- from orders;
-- 带一个条件的查询
-- select * from orders
-- where order_id = '201801010003';
-- 带多个条件的查询
-- select * from orders
-- where order_id = '201801010003'
-- and status = 1;
-- and表示两个条件同事满足
-- or表示满足其中一个条件