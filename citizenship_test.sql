-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema citizenship_test
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema citizenship_test
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `citizenship_test` DEFAULT CHARACTER SET utf8 ;
USE `citizenship_test` ;

-- -----------------------------------------------------
-- Table `citizenship_test`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `citizenship_test`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(45) NULL,
  `email` VARCHAR(72) NULL,
  `password` VARCHAR(72) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `citizenship_test`.`test_results`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `citizenship_test`.`test_results` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `score` VARCHAR(45) NULL,
  `test_date` DATE NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_tests_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_tests_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `citizenship_test`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `citizenship_test`.`advice`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `citizenship_test`.`advice` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `advice` TINYTEXT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_advice_users1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_advice_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `citizenship_test`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `citizenship_test`.`questions_answers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `citizenship_test`.`questions_answers` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `question` TINYTEXT NULL,
  `answer_type` VARCHAR(45) NULL,
  `answer1` TINYTEXT NULL,
  `answer2` TINYTEXT NULL,
  `answer3` TINYTEXT NULL,
  `answer4` TINYTEXT NULL,
  `correct_answer` TINYTEXT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
