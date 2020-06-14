-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Apr 04, 2016 at 08:04 PM
-- Server version: 10.1.10-MariaDB
-- PHP Version: 5.5.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `iridium`
--

-- --------------------------------------------------------

--
-- Table structure for table `bank_acc`
--

CREATE TABLE `bank_acc` (
  `bank_id` int(5) NOT NULL,
  `busername` varchar(10) NOT NULL,
  `bpassword` varchar(10) NOT NULL,
  `bankname` text NOT NULL,
  `branch` text NOT NULL,
  `city` text NOT NULL,
  `pincode` int(7) NOT NULL,
  `banktype` int(10) NOT NULL,
  `cust_balance` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `cards`
--

CREATE TABLE `cards` (
  `cards_id` int(5) NOT NULL,
  `card_number` int(10) NOT NULL,
  `card_type` text NOT NULL,
  `cvv` int(3) NOT NULL,
  `pin` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `customer_id` int(5) NOT NULL,
  `username` varchar(10) NOT NULL,
  `password` varchar(10) NOT NULL,
  `customer_name` text NOT NULL,
  `age` int(2) NOT NULL,
  `mobile` int(10) NOT NULL,
  `address` varchar(250) NOT NULL,
  `city` text NOT NULL,
  `state` text NOT NULL,
  `pincode` int(7) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `cust_bank`
--

CREATE TABLE `cust_bank` (
  `c_account_no` int(10) NOT NULL,
  `bank_name` int(10) NOT NULL,
  `balance` float NOT NULL,
  `cards_id` int(5) NOT NULL,
  `customer_id` int(5) NOT NULL,
  `bank_type` text CHARACTER SET utf8 COLLATE utf8_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `merchant`
--

CREATE TABLE `merchant` (
  `merchant_id` int(5) NOT NULL,
  `musername` varchar(10) NOT NULL,
  `mpassword` varchar(10) NOT NULL,
  `metchant_name` text NOT NULL,
  `age` int(2) NOT NULL,
  `mobile` int(10) NOT NULL,
  `address` varchar(250) NOT NULL,
  `city` text NOT NULL,
  `state` text NOT NULL,
  `pincode` int(7) NOT NULL,
  `item` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `merch_bank`
--

CREATE TABLE `merch_bank` (
  `m_account_no` int(10) NOT NULL,
  `bank_name` text NOT NULL,
  `balance` float NOT NULL,
  `cards_id` int(5) NOT NULL,
  `merchant_id` int(5) NOT NULL,
  `bank_type` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `bank_acc`
--
ALTER TABLE `bank_acc`
  ADD PRIMARY KEY (`bank_id`),
  ADD UNIQUE KEY `bank_id` (`bank_id`);

--
-- Indexes for table `cards`
--
ALTER TABLE `cards`
  ADD PRIMARY KEY (`cards_id`);

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`customer_id`),
  ADD UNIQUE KEY `customer_id` (`customer_id`);

--
-- Indexes for table `cust_bank`
--
ALTER TABLE `cust_bank`
  ADD PRIMARY KEY (`c_account_no`),
  ADD UNIQUE KEY `c_account_no` (`c_account_no`),
  ADD UNIQUE KEY `c_account_no_2` (`c_account_no`);

--
-- Indexes for table `merch_bank`
--
ALTER TABLE `merch_bank`
  ADD PRIMARY KEY (`m_account_no`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
