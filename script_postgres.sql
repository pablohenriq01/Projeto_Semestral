create database db_adega;

create table Bebidas (
    id SERIAL PRIMARY KEY,
    tipo_produto VARCHAR(100),
    nome_produto VARCHAR(200),
    marca_produto VARCHAR(150),
    preco_produto FLOAT
)
