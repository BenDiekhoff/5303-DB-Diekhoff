-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Dec 10, 2019 at 07:49 PM
-- Server version: 5.7.28-0ubuntu0.18.04.4
-- PHP Version: 7.2.24-0ubuntu0.18.04.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `diekhoff`
--

-- --------------------------------------------------------

--
-- Table structure for table `a04_planes`
--

CREATE TABLE `a04_planes` (
  `planeID` int(11) NOT NULL,
  `name` varchar(128) NOT NULL,
  `iata_code` varchar(3) NOT NULL,
  `icao_code` varchar(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `a04_planes`
--

INSERT INTO `a04_planes` (`planeID`, `name`, `iata_code`, `icao_code`) VALUES
(1, 'Aerospatiale (Nord) 262', 'ND2', 'N262'),
(2, 'Aerospatiale (Sud Aviation) Se.210 Caravelle', 'CRV', 'S210'),
(3, 'Aerospatiale SN.601 Corvette', 'NDC', 'S601'),
(4, 'Aerospatiale/Alenia ATR 42-300', 'AT4', 'AT43'),
(5, 'Aerospatiale/Alenia ATR 42-500', 'AT5', 'AT45'),
(6, 'Aerospatiale/Alenia ATR 42-600', 'ATR', 'AT46'),
(7, 'Aerospatiale/Alenia ATR 72', 'AT7', 'AT72'),
(8, 'Airbus A300', 'AB3', 'A30B'),
(9, 'Airbus A300-600', 'AB6', 'A306'),
(10, 'Airbus A300-600ST Super Transporter / Beluga', 'ABB', 'A3ST'),
(11, 'Airbus A310', '310', 'A310'),
(12, 'Airbus A318', '318', 'A318'),
(13, 'Airbus A319', '319', 'A319'),
(14, 'Airbus A319neo', '31N', 'A19N'),
(15, 'Airbus A320', '320', 'A320'),
(16, 'Airbus A320neo', '32N', 'A20N'),
(17, 'Airbus A321', '321', 'A321'),
(18, 'Airbus A321neo', '32Q', 'A21N'),
(19, 'Airbus A330', '330', '\\N'),
(20, 'Airbus A330-200', '332', 'A332'),
(21, 'Airbus A330-300', '333', 'A333'),
(22, 'Airbus A330-700 Beluga XL', '\\N', 'A337'),
(23, 'Airbus A330-800neo', '338', 'A338'),
(24, 'Airbus A330-900neo', '339', 'A339'),
(25, 'Airbus A340', '340', '\\N'),
(26, 'Airbus A340-200', '342', 'A342'),
(27, 'Airbus A340-300', '343', 'A343'),
(28, 'Airbus A340-500', '345', 'A345'),
(29, 'Airbus A340-600', '346', 'A346'),
(30, 'Airbus A350', '350', '\\N'),
(31, 'Airbus A350-1000', '351', 'A35K'),
(32, 'Airbus A350-900', '359', 'A359'),
(33, 'Airbus A380', '380', '\\N'),
(34, 'Airbus A380-800', '388', 'A388'),
(35, 'Antonov AN-12', 'ANF', 'AN12'),
(36, 'Antonov AN-124 Ruslan', 'A4F', 'A124'),
(37, 'Antonov AN-140', 'A40', 'A140'),
(38, 'Antonov An-148', 'A81', 'A148'),
(39, 'Antonov An-158', 'A58', 'A158'),
(40, 'Antonov An-225 Mriya', 'A25', 'A225'),
(41, 'Antonov AN-24', 'AN4', 'AN24'),
(42, 'Antonov AN-26', 'A26', 'AN26'),
(43, 'Antonov AN-28', 'A28', 'AN28'),
(44, 'Antonov AN-30', 'A30', 'AN30'),
(45, 'Antonov AN-32', 'A32', 'AN32'),
(46, 'Antonov AN-72', 'AN7', 'AN72'),
(47, 'Avro RJ100', 'AR1', 'RJ1H'),
(48, 'Avro RJ70', 'AR7', 'RJ70'),
(49, 'Avro RJ85', 'AR8', 'RJ85'),
(50, 'BAe 146', '146', '\\N'),
(51, 'BAe 146-100', '141', 'B461'),
(52, 'BAe 146-200', '142', 'B462'),
(53, 'BAe 146-300', '143', 'B463'),
(54, 'Beechcraft 1900', 'BEH', 'B190'),
(55, 'Beechcraft Baron', '\\N', 'BE58'),
(56, 'Beechcraft Baron / 55 Baron', '\\N', 'BE55'),
(57, 'Bell 212', 'BH2', 'B212'),
(58, 'Boeing 707', '703', 'B703'),
(59, 'Boeing 717', '717', 'B712'),
(60, 'Boeing 720B', 'B72', 'B720'),
(61, 'Boeing 727', '727', '\\N'),
(62, 'Boeing 727-100', '721', 'B721'),
(63, 'Boeing 727-200', '722', 'B722'),
(64, 'Boeing 737', '737', '\\N'),
(65, 'Boeing 737 MAX 10', '7MJ', '\\N'),
(66, 'Boeing 737 MAX 7', '7M7', 'B37M'),
(67, 'Boeing 737 MAX 8', '7M8', 'B38M'),
(68, 'Boeing 737 MAX 9', '7M9', 'B39M'),
(69, 'Boeing 737-200', '732', 'B732'),
(70, 'Boeing 737-300', '733', 'B733'),
(71, 'Boeing 737-400', '734', 'B734'),
(72, 'Boeing 737-500', '735', 'B735'),
(73, 'Boeing 737-600', '736', 'B736'),
(74, 'Boeing 737-700', '73G', 'B737'),
(75, 'Boeing 737-800', '738', 'B738'),
(76, 'Boeing 737-900', '739', 'B739'),
(77, 'Boeing 747', '747', '\\N'),
(78, 'Boeing 747 LCF Dreamlifter', '74B', 'BLCF'),
(79, 'Boeing 747-100', '741', 'B741'),
(80, 'Boeing 747-200', '742', 'B742'),
(81, 'Boeing 747-300', '743', 'B743'),
(82, 'Boeing 747-400', '744', 'B744'),
(83, 'Boeing 747-400D', '74J', 'B74D'),
(84, 'Boeing 747-8', '748', 'B748'),
(85, 'Boeing 747SP', '74L', 'B74S'),
(86, 'Boeing 747SR', '74R', 'B74R'),
(87, 'Boeing 757', '757', '\\N'),
(88, 'Boeing 757-200', '752', 'B752'),
(89, 'Boeing 757-300', '753', 'B753'),
(90, 'Boeing 767', '767', '\\N'),
(91, 'Boeing 767-200', '762', 'B762'),
(92, 'Boeing 767-300', '763', 'B763'),
(93, 'Boeing 767-400', '764', 'B764'),
(94, 'Boeing 777', '777', '\\N'),
(95, 'Boeing 777-200', '772', 'B772'),
(96, 'Boeing 777-200LR', '77L', 'B77L'),
(97, 'Boeing 777-300', '773', 'B773'),
(98, 'Boeing 777-300ER', '77W', 'B77W'),
(99, 'Boeing 777-8', '778', 'B778'),
(100, 'Boeing 777-9', '779', 'B779'),
(101, 'Boeing 787', '787', '\\N'),
(102, 'Boeing 787-10', '78J', 'B78X'),
(103, 'Boeing 787-8', '788', 'B788'),
(104, 'Boeing 787-9', '789', 'B789'),
(105, 'Bombardier 415', '\\N', 'CL2T'),
(106, 'Bombardier BD-100 Challenger 300', '\\N', 'CL30'),
(107, 'Bombardier CS100', 'CS1', 'BCS1'),
(108, 'Bombardier CS300', 'CS3', 'BCS3'),
(109, 'Bombardier Global Express', 'CCX', 'GLEX'),
(110, 'British Aerospace (BAC) One Eleven', 'B11', 'BA11'),
(111, 'British Aerospace 125 series / Hawker/Raytheon 700/800/800XP/850/900', 'H25', 'H25B'),
(112, 'British Aerospace 125-1000 series / Hawker/Raytheon 1000', 'H25', 'H25C'),
(113, 'British Aerospace ATP', 'ATP', 'ATP'),
(114, 'British Aerospace Jetstream 31', 'J31', 'JS31'),
(115, 'British Aerospace Jetstream 32', 'J32', 'JS32'),
(116, 'British Aerospace Jetstream 41', 'J41', 'JS41'),
(117, 'Canadair Challenger', 'CCJ', 'CL60'),
(118, 'Canadair CL-44', 'CL4', 'CL44'),
(119, 'Canadair Regional Jet 100', 'CR1', 'CRJ1'),
(120, 'Canadair Regional Jet 1000', 'CRK', 'CRJX'),
(121, 'Canadair Regional Jet 200', 'CR2', 'CRJ2'),
(122, 'Canadair Regional Jet 700', 'CR7', 'CRJ7'),
(123, 'Canadair Regional Jet 900', 'CR9', 'CRJ9'),
(124, 'Cessna 152', '\\N', 'C152'),
(125, 'Cessna 172', 'CN1', 'C172'),
(126, 'Cessna 182 Skylane', 'CN1', 'C182'),
(127, 'Cessna 208 Caravan', 'CN1', 'C208'),
(128, 'Cessna 210 Centurion', 'CN1', 'C210'),
(129, 'Cessna Citation CJ3', 'CNJ', 'C25B'),
(130, 'Cessna Citation CJ4', 'CNJ', 'C25C'),
(131, 'Cessna Citation Excel', 'CNJ', 'C56X'),
(132, 'Cessna Citation I', 'CNJ', 'C500'),
(133, 'Cessna Citation II', 'CNJ', 'C550'),
(134, 'Cessna Citation Mustang', 'CNJ', 'C510'),
(135, 'Cessna Citation Sovereign', 'CNJ', 'C680'),
(136, 'Cessna Citation X', 'CNJ', 'C750'),
(137, 'COMAC C-919', '\\N', 'C919'),
(138, 'Concorde', 'SSC', 'CONC'),
(139, 'Dassault Falcon 2000', 'D20', 'F2TH'),
(140, 'Dassault Falcon 50', 'DF3', 'FA50'),
(141, 'Dassault Falcon 7X', 'DF7', 'FA7X'),
(142, 'Dassault Falcon 900', 'DF9', 'F900'),
(143, 'De Havilland Canada DHC-2 Beaver', 'DHP', 'DHC2'),
(144, 'De Havilland Canada DHC-2 Turbo-Beaver', 'DHR', 'DH2T'),
(145, 'De Havilland Canada DHC-3 Otter', 'DHL', 'DHC3'),
(146, 'De Havilland Canada DHC-4 Caribou', 'DHC', 'DHC4'),
(147, 'De Havilland Canada DHC-6 Twin Otter', 'DHT', 'DHC6'),
(148, 'De Havilland Canada DHC-7 Dash 7', 'DH7', 'DHC7'),
(149, 'De Havilland Canada DHC-8-100 Dash 8 / 8Q', 'DH1', 'DH8A'),
(150, 'De Havilland Canada DHC-8-200 Dash 8 / 8Q', 'DH2', 'DH8B'),
(151, 'De Havilland Canada DHC-8-300 Dash 8', 'DH3', 'DH8C'),
(152, 'De Havilland Canada DHC-8-400 Dash 8Q', 'DH4', 'DH8D'),
(153, 'De Havilland DH.104 Dove', 'DHD', 'DOVE'),
(154, 'De Havilland DH.114 Heron', 'DHH', 'HERN'),
(155, 'Douglas DC-10', 'D10', 'DC10'),
(156, 'Douglas DC-3', 'D3F', 'DC3'),
(157, 'Douglas DC-6', 'D6F', 'DC6'),
(158, 'Douglas DC-8-50', 'D8T', 'DC85'),
(159, 'Douglas DC-8-62', 'D8L', 'DC86'),
(160, 'Douglas DC-8-72', 'D8Q', 'DC87'),
(161, 'Douglas DC-9-10', 'D91', 'DC91'),
(162, 'Douglas DC-9-20', 'D92', 'DC92'),
(163, 'Douglas DC-9-30', 'D93', 'DC93'),
(164, 'Douglas DC-9-40', 'D94', 'DC94'),
(165, 'Douglas DC-9-50', 'D95', 'DC95'),
(166, 'Embraer 170', 'E70', 'E170'),
(167, 'Embraer 175', 'E75', '\\N'),
(168, 'Embraer 175 (long wing)', 'E7W', 'E75L'),
(169, 'Embraer 175 (short wing)', 'E7W', 'E75S'),
(170, 'Embraer 190', 'E90', 'E190'),
(171, 'Embraer 195', 'E95', 'E195'),
(172, 'Embraer E190-E2', '290', 'E290'),
(173, 'Embraer E195-E2', '295', 'E295'),
(174, 'Embraer EMB 110 Bandeirante', 'EMB', 'E110'),
(175, 'Embraer EMB 120 Brasilia', 'EM2', 'E120'),
(176, 'Embraer Legacy 450', '\\N', 'E545'),
(177, 'Embraer Legacy 600', 'ER3', 'E35L'),
(178, 'Embraer Phenom 100', 'EP1', 'E50P'),
(179, 'Embraer Phenom 300', 'EP3', 'E55P'),
(180, 'Embraer RJ135', 'ER3', 'E135'),
(181, 'Embraer RJ140', 'ERD', 'E135'),
(182, 'Embraer RJ145', 'ER4', 'E145'),
(183, 'Fairchild Dornier 328JET', 'FRJ', 'J328'),
(184, 'Fairchild Dornier Do.228', 'D28', 'D228'),
(185, 'Fairchild Dornier Do.328', 'D38', 'D328'),
(186, 'Fokker 100', '100', 'F100'),
(187, 'Fokker 50', 'F50', 'F50'),
(188, 'Fokker 70', 'F70', 'F70'),
(189, 'Fokker F27 Friendship', 'F27', 'F27'),
(190, 'Fokker F28 Fellowship', 'F21', 'F28'),
(191, 'Gulfstream Aerospace G-159 Gulfstream I', 'GRS', 'G159'),
(192, 'Gulfstream G280', 'GR3', 'G280'),
(193, 'Gulfstream G650', 'GJ6', 'GLF6'),
(194, 'Gulfstream IV', 'GJ4', 'GLF4'),
(195, 'Gulfstream V', 'GJ5', 'GLF5'),
(196, 'Gulfstream/Rockwell (Aero) Commander', 'ACP', 'AC68'),
(197, 'Gulfstream/Rockwell (Aero) Turbo Commander', 'ACT', 'AC90'),
(198, 'Harbin Yunshuji Y12', 'YN2', 'Y12'),
(199, 'Hawker Siddeley HS 748', 'HS7', 'A748'),
(200, 'Ilyushin IL114', 'I14', 'I114'),
(201, 'Ilyushin IL18', 'IL8', 'IL18'),
(202, 'Ilyushin IL62', 'IL6', 'IL62'),
(203, 'Ilyushin IL76', 'IL7', 'IL76'),
(204, 'Ilyushin IL86', 'ILW', 'IL86'),
(205, 'Ilyushin IL96', 'I93', 'IL96'),
(206, 'Learjet 35', 'LRJ', 'LJ35'),
(207, 'Learjet 60', 'LRJ', 'LJ60'),
(208, 'Lockheed L-1011 Tristar', 'L10', 'L101'),
(209, 'Lockheed L-1049 Super Constellation', 'L49', 'CONI'),
(210, 'Lockheed L-182 / 282 / 382 (L-100) Hercules', 'LOH', 'C130'),
(211, 'Lockheed L-188 Electra', 'LOE', 'L188'),
(212, 'McDonnell Douglas MD-11', 'M11', 'MD11'),
(213, 'McDonnell Douglas MD-81', 'M81', 'MD81'),
(214, 'McDonnell Douglas MD-82', 'M82', 'MD82'),
(215, 'McDonnell Douglas MD-83', 'M83', 'MD83'),
(216, 'McDonnell Douglas MD-87', 'M87', 'MD87'),
(217, 'McDonnell Douglas MD-88', 'M88', 'MD88'),
(218, 'McDonnell Douglas MD-90', 'M90', 'MD90'),
(219, 'NAMC YS-11', 'YS1', 'YS11'),
(220, 'Partenavia P.68', 'PN6', 'P68'),
(221, 'Pilatus Britten-Norman BN-2A Mk III Trislander', 'BNT', 'TRIS'),
(222, 'Pilatus Britten-Norman BN-2A/B Islander', 'BNI', 'BN2P'),
(223, 'Pilatus PC-12', 'PL2', 'PC12'),
(224, 'Pilatus PC-6 Turbo Porter', 'PL6', 'PC6T'),
(225, 'Piper PA-28 (above 200 hp)', '\\N', 'P28B'),
(226, 'Piper PA-28 (up to 180 hp)', '\\N', 'P28A'),
(227, 'Piper PA-31 Navajo', 'PA2', 'PA31'),
(228, 'Piper PA-44 Seminole', '\\N', 'PA44'),
(229, 'Piper PA-46', 'PAG', 'PA46'),
(230, 'Saab 2000', 'S20', 'SB20'),
(231, 'Saab SF340A/B', 'SF3', 'SF34'),
(232, 'Shorts SC-5 Belfast', 'SHB', 'BELF'),
(233, 'Shorts SC-7 Skyvan', 'SHS', 'SC7'),
(234, 'Shorts SD.330', 'SH3', 'SH33'),
(235, 'Shorts SD.360', 'SH6', 'SH36'),
(236, 'Sikorsky S-58T', 'S58', 'S58T'),
(237, 'Sikorsky S-61', 'S61', 'S61'),
(238, 'Sikorsky S-76', 'S76', 'S76'),
(239, 'Sikorsky S-92', 'S92', 'S92'),
(240, 'Sukhoi Superjet 100-95', 'SU9', 'SU95'),
(241, 'Tupolev Tu-134', 'TU3', 'T134'),
(242, 'Tupolev Tu-144', '\\N', 'T144'),
(243, 'Tupolev Tu-154', 'TU5', 'T154'),
(244, 'Tupolev Tu-204', 'T20', 'T204'),
(245, 'Yakovlev Yak-40', 'YK4', 'YK40'),
(246, 'Yakovlev Yak-42', 'YK2', 'YK42');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `a04_planes`
--
ALTER TABLE `a04_planes`
  ADD PRIMARY KEY (`planeID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `a04_planes`
--
ALTER TABLE `a04_planes`
  MODIFY `planeID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=247;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
