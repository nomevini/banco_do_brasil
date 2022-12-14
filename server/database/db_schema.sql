-- MySQL Script generated by MySQL Workbench
-- dom 14 ago 2022 09:39:07
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema banco_do_brasil
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `banco_do_brasil` ;

-- -----------------------------------------------------
-- Schema banco_do_brasil
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `banco_do_brasil` ;
SHOW WARNINGS;
USE `banco_do_brasil` ;

-- -----------------------------------------------------
-- Table `banco_do_brasil`.`Pessoa`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `banco_do_brasil`.`Pessoa` (
  `idUsuario` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NULL,
  `cpf` VARCHAR(20) NULL,
  `data_nascimento` VARCHAR(20) NULL,
  PRIMARY KEY (`idUsuario`))
ENGINE = InnoDB;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `banco_do_brasil`.`Conta`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `banco_do_brasil`.`Conta` (
  `idConta` INT NOT NULL AUTO_INCREMENT,
  `senha` VARCHAR(45) NULL,
  `numeroConta` VARCHAR(45) NULL,
  `saldo` FLOAT NULL,
  `Pessoa_idUsuario` INT NOT NULL,
  PRIMARY KEY (`idConta`),
  INDEX `fk_Conta_Pessoa1_idx` (`Pessoa_idUsuario` ASC) VISIBLE)
ENGINE = InnoDB;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `banco_do_brasil`.`Historico`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `banco_do_brasil`.`Historico` (
  `idHistorico` INT NOT NULL AUTO_INCREMENT,
  `data` VARCHAR(20) NULL,
  `operacao` VARCHAR(200) NULL,
  `Conta_idConta` INT NOT NULL,
  PRIMARY KEY (`idHistorico`),
  INDEX `fk_Historico_Conta1_idx` (`Conta_idConta` ASC) VISIBLE)
ENGINE = InnoDB;

SHOW WARNINGS;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
