CREATE DATABASE wear_fit;
\c wear_fit
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    middle_name VARCHAR(50),
    phone_number VARCHAR(15),
    country VARCHAR(50),
    region VARCHAR(50),
    city VARCHAR(50),
    street VARCHAR(100),
    postal_code VARCHAR(10),
    email VARCHAR(100) NOT NULL,
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    employee_status BOOLEAN DEFAULT FALSE,
    active_status BOOLEAN DEFAULT TRUE
);
CREATE TABLE product_category (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    slug VARCHAR(100) NOT NULL
);
CREATE TABLE product (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    category_id INT NOT NULL,
    slug VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    update_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    in_stock BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (category_id) REFERENCES product_category(id)
);
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
CREATE TABLE order_product_link (
    id SERIAL PRIMARY KEY,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(id),
    FOREIGN KEY (product_id) REFERENCES product(id)
);


-- Заполнение таблицы users
INSERT INTO users (username, first_name, last_name, middle_name, phone_number, country, region, city, street, postal_code, email, registration_date, employee_status, active_status)
VALUES
('user1', 'Иван', 'Иванов', 'Иванович', '79001234567', 'Россия', 'Московская область', 'Москва', 'Ленина', '101000', 'ivan.ivanov@example.com', '2024-01-01', FALSE, TRUE),
('user2', 'Петр', 'Петров', 'Петрович', '79007654321', 'Россия', 'Ленинградская область', 'Санкт-Петербург', 'Невский проспект', '190000', 'petr.petrov@example.com', '2024-01-02', FALSE, TRUE),
('user3', 'Сергей', 'Сергеев', 'Сергеевич', '79003456789', 'Россия', 'Новосибирская область', 'Новосибирск', 'Красный проспект', '630000', 'sergey.sergeev@example.com', '2024-01-03', FALSE, TRUE),
('user4', 'Алексей', 'Алексеев', 'Алексеевич', '79005678901', 'Россия', 'Свердловская область', 'Екатеринбург', 'Ленина', '620000', 'alexey.alexeev@example.com', '2024-01-04', FALSE, TRUE),
('user5', 'Мария', 'Морозова', 'Алексеевна', '79009876543', 'Россия', 'Татарстан', 'Казань', 'Пушкина', '420000', 'maria.morozova@example.com', '2024-01-05', FALSE, TRUE),
('user6', 'Наталья', 'Николаева', 'Ивановна', '79001239876', 'Россия', 'Ростовская область', 'Ростов-на-Дону', 'Садовая', '344000', 'natalya.nikolaeva@example.com', '2024-01-06', FALSE, TRUE),
('user7', 'Ольга', 'Орлова', 'Сергеевна', '79007651234', 'Россия', 'Краснодарский край', 'Краснодар', 'Красная', '350000', 'olga.orlova@example.com', '2024-01-07', FALSE, TRUE),
('user8', 'Анна', 'Александрова', 'Петровна', '79003459876', 'Россия', 'Самарская область', 'Самара', 'Московское шоссе', '443000', 'anna.alexandrova@example.com', '2024-01-08', FALSE, TRUE),
('user9', 'Владимир', 'Владимиров', 'Иванович', '79005673421', 'Россия', 'Челябинская область', 'Челябинск', 'Кирова', '454000', 'vladimir.vladimirov@example.com', '2024-01-09', FALSE, TRUE),
('user10', 'Екатерина', 'Егорова', 'Сергеевна', '79009871234', 'Россия', 'Тюменская область', 'Тюмень', 'Республики', '625000', 'ekaterina.egorova@example.com', '2024-01-10', FALSE, TRUE);

-- Заполнение таблицы product_category
INSERT INTO product_category (name, slug)
VALUES
('Футболки', 'futbolki'),
('Свитшоты/Худи', 'svitshoty-hudi'),
('Штаны/Шорты', 'shtany-shorty'),
('Шапки', 'shapki'),
('Рюкзаки/Сумки', 'ryukzaki-sumki'),
('Тестовые товары', 'testovye-tovary');

-- Заполнение таблицы product
INSERT INTO product (name, category_id, slug, description, price, creation_date, update_date, in_stock)
VALUES
('Базовая футболка', 1, 'bazovaya-futbolka', 'Удобная базовая футболка', 1499.99, '2024-01-01', '2024-01-01', TRUE),
('Худи с принтом', 2, 'hudi-s-printom', 'Стильное худи с принтом', 3499.99, '2024-01-02', '2024-01-02', TRUE),
('Джинсы', 3, 'dzhinsy', 'Классические джинсы', 2999.99, '2024-01-03', '2024-01-03', TRUE),
('Спортивные шорты', 3, 'sportivnye-shorty', 'Удобные спортивные шорты', 1999.99, '2024-01-04', '2024-01-04', TRUE),
('Бейсболка', 4, 'bejsbolka', 'Повседневная бейсболка', 999.99, '2024-01-05', '2024-01-05', TRUE),
('Рюкзак', 5, 'ryukzak', 'Просторный рюкзак', 3999.99, '2024-01-06', '2024-01-06', TRUE),
('Кроссовки', 6, 'krossovki', 'Легкие кроссовки', 4999.99, '2024-01-07', '2024-01-07', TRUE),
('Тестовый товар 1', 6, 'testovyi-tovar-1', 'Описание тестового товара 1', 100.00, '2024-01-08', '2024-01-08', TRUE),
('Тестовый товар 2', 6, 'testovyi-tovar-2', 'Описание тестового товара 2', 200.00, '2024-01-09', '2024-01-09', TRUE),
('Тестовый товар 3', 6, 'testovyi-tovar-3', 'Описание тестового товара 3', 300.00, '2024-01-10', '2024-01-10', TRUE);

-- Заполнение таблицы orders
INSERT INTO orders (user_id)
VALUES
(1), (2), (3), (4), (5), (6), (7), (8), (9), (10);

-- Заполнение таблицы order_product_link
INSERT INTO order_product_link (order_id, product_id)
VALUES
(1, 1), (1, 2), (2, 3), (2, 4), (3, 5), (3, 6), (4, 7), (4, 8), (5, 9), (5, 10),
(6, 1), (6, 3), (7, 2), (7, 4), (8, 5), (8, 7), (9, 6), (9, 8), (10, 9), (10, 10);
