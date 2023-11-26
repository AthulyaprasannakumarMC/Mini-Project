/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 8.0.34 : Database - hwmgmtapp
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`hwmgmtapp` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `hwmgmtapp`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_permission` */

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user` */

insert  into `auth_user`(`id`,`password`,`last_login`,`is_superuser`,`username`,`first_name`,`last_name`,`email`,`is_staff`,`is_active`,`date_joined`) values 
(1,'pbkdf2_sha256$260000$1KHijypJ9EqTnZWzlksvol$DazZ0TdLC+iZm2FR3DU2WT6hjrZBtHKiwRKW3I5ctS4=','2023-11-19 10:55:51.934827',1,'admin','','','admin@gmail.com',1,1,'2023-11-18 05:32:25.294957');

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `ch_app_category_table` */

DROP TABLE IF EXISTS `ch_app_category_table`;

CREATE TABLE `ch_app_category_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `ch_app_category_table` */

insert  into `ch_app_category_table`(`id`,`name`) values 
(1,'MOTHERBOARD');

/*Table structure for table `ch_app_complaint_table` */

DROP TABLE IF EXISTS `ch_app_complaint_table`;

CREATE TABLE `ch_app_complaint_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `complaint` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `reply` varchar(100) NOT NULL,
  `HARDWARESHOP_id` bigint NOT NULL,
  `USER_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `CH_App_complaint_tab_HARDWARESHOP_id_221d3f83_fk_CH_App_ha` (`HARDWARESHOP_id`),
  KEY `CH_App_complaint_table_USER_id_d01bf3ea_fk_CH_App_user_table_id` (`USER_id`),
  CONSTRAINT `CH_App_complaint_tab_HARDWARESHOP_id_221d3f83_fk_CH_App_ha` FOREIGN KEY (`HARDWARESHOP_id`) REFERENCES `ch_app_hardwareshops_table` (`id`),
  CONSTRAINT `CH_App_complaint_table_USER_id_d01bf3ea_fk_CH_App_user_table_id` FOREIGN KEY (`USER_id`) REFERENCES `ch_app_user_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `ch_app_complaint_table` */

insert  into `ch_app_complaint_table`(`id`,`complaint`,`date`,`reply`,`HARDWARESHOP_id`,`USER_id`) values 
(1,'aaaasse','2023-11-19','ghhhj',9,1);

/*Table structure for table `ch_app_feedback_table` */

DROP TABLE IF EXISTS `ch_app_feedback_table`;

CREATE TABLE `ch_app_feedback_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `feedback` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `rating` int NOT NULL,
  `USER_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `CH_App_feedback_table_USER_id_828ff29b_fk_CH_App_user_table_id` (`USER_id`),
  CONSTRAINT `CH_App_feedback_table_USER_id_828ff29b_fk_CH_App_user_table_id` FOREIGN KEY (`USER_id`) REFERENCES `ch_app_user_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `ch_app_feedback_table` */

insert  into `ch_app_feedback_table`(`id`,`feedback`,`date`,`rating`,`USER_id`) values 
(1,'good','2023-11-19',3,1);

/*Table structure for table `ch_app_hardwareshops_table` */

DROP TABLE IF EXISTS `ch_app_hardwareshops_table`;

CREATE TABLE `ch_app_hardwareshops_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `email` varchar(30) NOT NULL,
  `place` varchar(50) NOT NULL,
  `post` varchar(50) NOT NULL,
  `pin` int NOT NULL,
  `phone` bigint NOT NULL,
  `photo` varchar(100) NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `CH_App_hardwareshops_LOGIN_id_8a07daf2_fk_CH_App_lo` (`LOGIN_id`),
  CONSTRAINT `CH_App_hardwareshops_LOGIN_id_8a07daf2_fk_CH_App_lo` FOREIGN KEY (`LOGIN_id`) REFERENCES `ch_app_login_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `ch_app_hardwareshops_table` */

insert  into `ch_app_hardwareshops_table`(`id`,`name`,`email`,`place`,`post`,`pin`,`phone`,`photo`,`LOGIN_id`) values 
(8,'Athulya M C','athulyaathu229@gmail.com','qqq','qqqqqqqqqqq',987777,9179078996,'download_aamExQM.jpg',12),
(9,'AUStore','Au@gmail.com','Shornur','Shornur',679524,7012296076,'download_l1AaklN.jpg',13);

/*Table structure for table `ch_app_login_table` */

DROP TABLE IF EXISTS `ch_app_login_table`;

CREATE TABLE `ch_app_login_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `password` varchar(10) NOT NULL,
  `type` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `ch_app_login_table` */

insert  into `ch_app_login_table`(`id`,`username`,`password`,`type`) values 
(1,'admin','Admin@123','admin'),
(2,'Athulya','Athu@123','user'),
(12,'Q@123qqq','Q@123qqq','hardwareshop'),
(13,'AUStore','Au@123789','hardwareshop');

/*Table structure for table `ch_app_notification_table` */

DROP TABLE IF EXISTS `ch_app_notification_table`;

CREATE TABLE `ch_app_notification_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `notification` varchar(100) NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `ch_app_notification_table` */

insert  into `ch_app_notification_table`(`id`,`notification`,`date`) values 
(1,'sdfsfs','2023-11-18'),
(3,'bad service','2023-11-19');

/*Table structure for table `ch_app_offer_table` */

DROP TABLE IF EXISTS `ch_app_offer_table`;

CREATE TABLE `ch_app_offer_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `fromdate` varchar(50) NOT NULL,
  `todate` varchar(50) NOT NULL,
  `offer` varchar(100) NOT NULL,
  `details` varchar(100) NOT NULL,
  `PRODUCTID_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `CH_App_offer_table_PRODUCTID_id_3140a0d0_fk_CH_App_pr` (`PRODUCTID_id`),
  CONSTRAINT `CH_App_offer_table_PRODUCTID_id_3140a0d0_fk_CH_App_pr` FOREIGN KEY (`PRODUCTID_id`) REFERENCES `ch_app_products_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `ch_app_offer_table` */

insert  into `ch_app_offer_table`(`id`,`fromdate`,`todate`,`offer`,`details`,`PRODUCTID_id`) values 
(1,'2023-11-06','2023-11-18','hjkkk','dddf',1);

/*Table structure for table `ch_app_order_table` */

DROP TABLE IF EXISTS `ch_app_order_table`;

CREATE TABLE `ch_app_order_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `amount` int NOT NULL,
  `status` varchar(100) NOT NULL,
  `USER_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `CH_App_order_table_USER_id_3064e0ba_fk_CH_App_user_table_id` (`USER_id`),
  CONSTRAINT `CH_App_order_table_USER_id_3064e0ba_fk_CH_App_user_table_id` FOREIGN KEY (`USER_id`) REFERENCES `ch_app_user_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `ch_app_order_table` */

insert  into `ch_app_order_table`(`id`,`date`,`amount`,`status`,`USER_id`) values 
(15,'2023-11-19',450,'paid',1),
(16,'2023-11-19',450,'paid',1),
(17,'2023-11-19',120,'paid',1),
(18,'2023-11-19',120,'paid',1),
(19,'2023-11-19',1020,'paid',1),
(20,'2023-11-19',120,'pending',1);

/*Table structure for table `ch_app_orderitem_table` */

DROP TABLE IF EXISTS `ch_app_orderitem_table`;

CREATE TABLE `ch_app_orderitem_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `offer` varchar(100) NOT NULL,
  `quantity` int NOT NULL,
  `ORDER_id` bigint NOT NULL,
  `PRODUCT_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `CH_App_orderitem_tab_ORDER_id_13998626_fk_CH_App_or` (`ORDER_id`),
  KEY `CH_App_orderitem_tab_PRODUCT_id_c6822eef_fk_CH_App_pr` (`PRODUCT_id`),
  CONSTRAINT `CH_App_orderitem_tab_ORDER_id_13998626_fk_CH_App_or` FOREIGN KEY (`ORDER_id`) REFERENCES `ch_app_order_table` (`id`),
  CONSTRAINT `CH_App_orderitem_tab_PRODUCT_id_c6822eef_fk_CH_App_pr` FOREIGN KEY (`PRODUCT_id`) REFERENCES `ch_app_products_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `ch_app_orderitem_table` */

insert  into `ch_app_orderitem_table`(`id`,`offer`,`quantity`,`ORDER_id`,`PRODUCT_id`) values 
(14,'0',0,17,1),
(15,'0',1,18,1),
(17,'0',0,19,1),
(18,'0',1,20,1);

/*Table structure for table `ch_app_payment_table` */

DROP TABLE IF EXISTS `ch_app_payment_table`;

CREATE TABLE `ch_app_payment_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `amount` int NOT NULL,
  `ORDER_id` bigint NOT NULL,
  `USER_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `CH_App_payment_table_ORDER_id_50c6e379_fk_CH_App_order_table_id` (`ORDER_id`),
  KEY `CH_App_payment_table_USER_id_550096f0_fk_CH_App_user_table_id` (`USER_id`),
  CONSTRAINT `CH_App_payment_table_ORDER_id_50c6e379_fk_CH_App_order_table_id` FOREIGN KEY (`ORDER_id`) REFERENCES `ch_app_order_table` (`id`),
  CONSTRAINT `CH_App_payment_table_USER_id_550096f0_fk_CH_App_user_table_id` FOREIGN KEY (`USER_id`) REFERENCES `ch_app_user_table` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `ch_app_payment_table` */

/*Table structure for table `ch_app_pro_return_table` */

DROP TABLE IF EXISTS `ch_app_pro_return_table`;

CREATE TABLE `ch_app_pro_return_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` varchar(50) NOT NULL,
  `reason` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `ORDERITEM_id` bigint NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `ch_app_pro_return_table` */

insert  into `ch_app_pro_return_table`(`id`,`date`,`reason`,`status`,`ORDERITEM_id`) values 
(4,'2023-11-19 13:26:38.189117','gg','sorry',14),
(5,'2023-11-19 15:20:02.285447','mkjhjgnhfbgv','ok',17);

/*Table structure for table `ch_app_products_table` */

DROP TABLE IF EXISTS `ch_app_products_table`;

CREATE TABLE `ch_app_products_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `price` int NOT NULL,
  `quantity` int NOT NULL,
  `photo` varchar(100) NOT NULL,
  `CATEGORY_id` bigint NOT NULL,
  `SHOPID_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `CH_App_products_tabl_CATEGORY_id_1ae0590f_fk_CH_App_ca` (`CATEGORY_id`),
  KEY `CH_App_products_tabl_SHOPID_id_9bb767db_fk_CH_App_ha` (`SHOPID_id`),
  CONSTRAINT `CH_App_products_tabl_CATEGORY_id_1ae0590f_fk_CH_App_ca` FOREIGN KEY (`CATEGORY_id`) REFERENCES `ch_app_category_table` (`id`),
  CONSTRAINT `CH_App_products_tabl_SHOPID_id_9bb767db_fk_CH_App_ha` FOREIGN KEY (`SHOPID_id`) REFERENCES `ch_app_hardwareshops_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `ch_app_products_table` */

insert  into `ch_app_products_table`(`id`,`name`,`price`,`quantity`,`photo`,`CATEGORY_id`,`SHOPID_id`) values 
(1,'ASRock A620M Pro RS WiFi Motherboard A620M-PRO-RS-WIFI',120,99,'download_d7f2OCm.jpg',1,9);

/*Table structure for table `ch_app_return_table` */

DROP TABLE IF EXISTS `ch_app_return_table`;

CREATE TABLE `ch_app_return_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `quantity` varchar(100) NOT NULL,
  `date` varchar(50) NOT NULL,
  `reason` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `TRANSACTION_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `CH_App_return_table_TRANSACTION_id_09b0dbdb_fk_CH_App_tr` (`TRANSACTION_id`),
  CONSTRAINT `CH_App_return_table_TRANSACTION_id_09b0dbdb_fk_CH_App_tr` FOREIGN KEY (`TRANSACTION_id`) REFERENCES `ch_app_transaction` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `ch_app_return_table` */

insert  into `ch_app_return_table`(`id`,`quantity`,`date`,`reason`,`status`,`TRANSACTION_id`) values 
(5,'5','2023-11-19','defect','pending',4);

/*Table structure for table `ch_app_transaction` */

DROP TABLE IF EXISTS `ch_app_transaction`;

CREATE TABLE `ch_app_transaction` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `cname` varchar(100) NOT NULL,
  `quantity` varchar(100) NOT NULL,
  `date` varchar(50) NOT NULL,
  `bill_no` int NOT NULL,
  `status` varchar(100) NOT NULL,
  `PRODUCT_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `CH_App_transaction_PRODUCT_id_aded6a76_fk_CH_App_pr` (`PRODUCT_id`),
  CONSTRAINT `CH_App_transaction_PRODUCT_id_aded6a76_fk_CH_App_pr` FOREIGN KEY (`PRODUCT_id`) REFERENCES `ch_app_products_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `ch_app_transaction` */

insert  into `ch_app_transaction`(`id`,`cname`,`quantity`,`date`,`bill_no`,`status`,`PRODUCT_id`) values 
(4,'      pavi','34','2023-11-19',266778,'pending',1);

/*Table structure for table `ch_app_user_table` */

DROP TABLE IF EXISTS `ch_app_user_table`;

CREATE TABLE `ch_app_user_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `lastname` varchar(100) NOT NULL,
  `email` varchar(30) NOT NULL,
  `place` varchar(50) NOT NULL,
  `post` varchar(50) NOT NULL,
  `pin` int NOT NULL,
  `phone` bigint NOT NULL,
  `photo` varchar(100) NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `CH_App_user_table_LOGIN_id_de6babe9_fk_CH_App_login_table_id` (`LOGIN_id`),
  CONSTRAINT `CH_App_user_table_LOGIN_id_de6babe9_fk_CH_App_login_table_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `ch_app_login_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `ch_app_user_table` */

insert  into `ch_app_user_table`(`id`,`name`,`lastname`,`email`,`place`,`post`,`pin`,`phone`,`photo`,`LOGIN_id`) values 
(1,'Athulya','M C','Athulyaathu229@gmail.com','Shornur','Shornur',679524,7907899637,'nptel[142]_1uVdd90.jpg',2);

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_content_type` */

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_migrations` */

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values 
('2hkg32i63x2gnnvrv1kq6yw8brzth9d1','.eJxVjsEOgyAQRP-Fc0PCKgg99t5vMMDuVlujEfRgmv57IfHibTLzZjJfMY0o7nATvd-3od8zpb46QomLF3z80FwDfPv5tci4zFsag6yIPNMsnwvS9DjZy8Dg81DaFlk3VmkCAnaBuCH0AK1FEymA4c4GNC16p5roNAMQa0fKBXStNl0ZTWs9qMrndd2Oon5_AMJAAw:1r4bly:OW46hSo0vQl7Ob_LjURaQ4troomgKSwVvGIzRqgtLrw','2023-12-03 06:59:14.986490'),
('exxhfwh711ck7len9v726rba9cbpvtrc','.eJxVjDsOwyAQBe9CHSGxfAwp0-cMCNglOLFAMnZl5e4Jkhu3M_PewZYZ2R1uzId9K37vtPpBmGAXFkP6UB0C36G-Gk-tbusc-Uj4aTt_NqTlcbaXgxJ6-a8tZi2t0AQE2UXKkjAAKIsmUQSTJxvRKAxOyOR0BqCsHQkX0SltJvb9AXTNOpw:1r4fSx:OSPO7MVwwR5D9BocOSld52KJM8vH7sR2mP_DiAO8Mdk','2023-12-03 10:55:51.939476'),
('u1jq2b57rang79lyyqgdezwgm30842y5','.eJxVjDsOwyAQBe9CHSGxfAwp0-cMCNglOLFAMnZl5e4Jkhu3M_PewZYZ2V3cmA_7VvzeafWDMMEuLIb0oToEvkN9NZ5a3dY58pHw03b-bEjL42wvByX08l9bzFpaoQkIsouUJWEAUBZNoggmTzaiURickMnpDEBZOxIuolPaTOz7A3QhOps:1r4b3f:fI-FZkuuhxpjyHvzrHyoaKwibdg38gNcGOWj9EBfq6Y','2023-12-03 06:13:27.334369');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
