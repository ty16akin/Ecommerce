CREATE DATABASE chbs;

--
-- Create model Customer
--
CREATE TABLE `CHBS_customer` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `name` varchar(200) NULL, `email` varchar(200) NULL, `user_id` integer NULL UNIQUE);
--
-- Create model Order
--
CREATE TABLE `CHBS_order` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `date_ordered` datetime(6) NOT NULL, `complete` bool NOT NULL, `transaction_id` varchar(100) NULL, `customer_id` bigint NULL);
--
-- Create model Product
--
CREATE TABLE `CHBS_product` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `name` varchar(200) NOT NULL, `price` double precision NOT NULL, `digital` bool NULL);
--
-- Create model ShippingAddress
--
CREATE TABLE `CHBS_shippingaddress` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `address` varchar(200) NOT NULL, `city` varchar(200) NOT NULL, `postalcode` varchar(200) NOT NULL, `date_added` datetime(6) NOT NULL, `customer_id` bigint NULL, `order_id` bigint NULL);
--
-- Create model OrderItem
--
CREATE TABLE `CHBS_orderitem` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `quantity` integer NULL, `date_added` datetime(6) NOT NULL, `order_id` bigint NULL, `product_id` bigint NULL);
ALTER TABLE `CHBS_customer` ADD CONSTRAINT `CHBS_customer_user_id_31f59f78_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
ALTER TABLE `CHBS_order` ADD CONSTRAINT `CHBS_order_customer_id_ec44488d_fk_CHBS_customer_id` FOREIGN KEY (`customer_id`) REFERENCES `CHBS_customer` (`id`);
ALTER TABLE `CHBS_shippingaddress` ADD CONSTRAINT `CHBS_shippingaddress_customer_id_2b11adbd_fk_CHBS_customer_id` FOREIGN KEY (`customer_id`) REFERENCES `CHBS_customer` (`id`);
ALTER TABLE `CHBS_shippingaddress` ADD CONSTRAINT `CHBS_shippingaddress_order_id_b1abb9a3_fk_CHBS_order_id` FOREIGN KEY (`order_id`) REFERENCES `CHBS_order` (`id`);
ALTER TABLE `CHBS_orderitem` ADD CONSTRAINT `CHBS_orderitem_order_id_9ac29b9c_fk_CHBS_order_id` FOREIGN KEY (`order_id`) REFERENCES `CHBS_order` (`id`);
ALTER TABLE `CHBS_orderitem` ADD CONSTRAINT `CHBS_orderitem_product_id_6817a16f_fk_CHBS_product_id` FOREIGN KEY (`product_id`) REFERENCES `CHBS_product` (`id`);