CREATE SCHEMA `ring` ;

CREATE TABLE `ring`.`ringdata` (
  `idRingData` INT NOT NULL,
  `ringsize` VARCHAR(45) BINARY NULL,
  `ringindex` VARCHAR(45) NULL,
  `block` VARCHAR(45) NULL,
  `chain` VARCHAR(45) NULL,
  `ringhash` VARCHAR(45) NULL,
  `mineraddress` VARCHAR(45) NULL,
  `order1hash` VARCHAR(45) NULL,
  `order1lrcReward` VARCHAR(45) NULL,
  `order1lrcFeeState` VARCHAR(45) NULL,
  `order1splitS` VARCHAR(45) NULL,
  `order1splitB` VARCHAR(45) NULL,
  `order2hash` VARCHAR(45) NULL,
  `order2lrcReward` VARCHAR(45) NULL,
  `order2lrcFeeState` VARCHAR(45) NULL,
  `order2splitS` VARCHAR(45) NULL,
  `order2splitB` VARCHAR(45) NULL,
  `order3hash` VARCHAR(45) NULL,
  `order3lrcReward` VARCHAR(45) NULL,
  `order3lrcFeeState` VARCHAR(45) NULL,
  `order3splitS` VARCHAR(45) NULL,
  `order3splitB` VARCHAR(45) NULL,
  PRIMARY KEY (`idRingData`));
