-- MySQL Script generated by MySQL Workbench
-- Sat Jun 17 23:24:45 2017
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema wall
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema wall
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `wall` DEFAULT CHARACTER SET utf8 ;
USE `wall` ;

-- -----------------------------------------------------
-- Table `wall`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `wall`.`users` (
  `user_id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NULL,
  `last_name` VARCHAR(255) NULL,
  `email` VARCHAR(255) NULL,
  `password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`user_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `wall`.`messages`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `wall`.`messages` (
  `message_id` INT NOT NULL AUTO_INCREMENT,
  `message` TEXT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `users_id` INT NOT NULL,
  PRIMARY KEY (`message_id`),
  INDEX `fk_messages_users_idx` (`users_id` ASC),
  CONSTRAINT `fk_messages_users`
    FOREIGN KEY (`users_id`)
    REFERENCES `wall`.`users` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `wall`.`comments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `wall`.`comments` (
  `comment_id` INT NOT NULL AUTO_INCREMENT,
  `comment` TEXT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `users_id` INT NOT NULL,
  `messages_id` INT NOT NULL,
  PRIMARY KEY (`comment_id`),
  INDEX `fk_comments_users1_idx` (`users_id` ASC),
  INDEX `fk_comments_messages1_idx` (`messages_id` ASC),
  CONSTRAINT `fk_comments_users1`
    FOREIGN KEY (`users_id`)
    REFERENCES `wall`.`users` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_comments_messages1`
    FOREIGN KEY (`messages_id`)
    REFERENCES `wall`.`messages` (`message_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
