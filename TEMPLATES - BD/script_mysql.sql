create database db_adega;
use db_adega;

create table Bebidas (
    id INT AUTO_INCREMENT,
    tipo_produto VARCHAR(100),
    nome_produto VARCHAR(200),
    marca_produto VARCHAR(150),
    preco_produto FLOAT,
    PRIMARY KEY (id)
);

INSERT INTO Bebidas (tipo_produto, nome_produto, marca_produto, preco_produto)
VALUES
('Whisky', 'Johnnie Walker Black Label', 'Johnnie Walker', 180.00),
('Whisky', 'Jameson Irish Whiskey', 'Jameson', 120.00),
('Whisky', 'Jack Daniels Old No. 7', 'Jack Daniel', 150.00);

create table login(
    id int AUTO_INCREMENT,
    nome varchar(250),
    email VARCHAR(150),
    senha varchar(30), 
    PRIMARY KEY (id)
);