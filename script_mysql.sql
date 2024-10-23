create database db_adega;
use db_adega;

create table bebidas (
    id INT AUTO_INCREMENT,
    tipo_produto VARCHAR(100),
    nome_produto VARCHAR(200),
    marca_produto VARCHAR(150),
    preco_produto FLOAT
    PRIMARY KEY (id)
)
