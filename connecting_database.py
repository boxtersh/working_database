def connecting_database():
    host='109.206.169.221'
    user='seschool_01'
    password='seschool_01'
    database='seschool_01_RP12_TYA'
    return host, user, password, database

def creating_tables():
    requests = """
    SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
    SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
    SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';
    
    CREATE TABLE IF NOT EXISTS seschool_01_RP12_TYA.habits (
    id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    name TINYTEXT NOT NULL,
    frequency ENUM('ежедневно', 'еженедельно', 'ежемесячно', 'ежегодно', 'произвольно') NULL,
    created_at DATE NOT NULL,
    PRIMARY KEY (id))
    ENGINE = InnoDB;
    
    CREATE TABLE IF NOT EXISTS seschool_01_RP12_TYA.habit_checks(
    id INT NOT NULL AUTO_INCREMENT,
    habits_id INT NOT NULL,
    check_date DATE NOT NULL,
    note VARCHAR(45) NULL,
    INDEX fk_habit_checks_habits_idx (habits_id ASC),
    PRIMARY KEY (id),
    CONSTRAINT fk_habit_checks_habits
    FOREIGN KEY (habits_id)
    REFERENCES seschool_01_RP12_TYA.habits (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
    ENGINE = InnoDB;

    SET SQL_MODE=@OLD_SQL_MODE;
    SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
    SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
    """
    sql_generator = (request.strip() for request in requests.split(';'))
    return sql_generator


dict_query = {'Показать все записи':'SELECT * FROM ZootopiaCharacters',
              'Название животного на Л' : 'SELECT * FROM ZootopiaCharacters WHERE Species LIKE "%ал"'
              }