create database db_adega;

create table Bebidas (
    id SERIAL PRIMARY KEY,
    tipo_produto VARCHAR(100),
    nome_produto VARCHAR(200),
    marca_produto VARCHAR(150),
    preco_produto FLOAT
);

INSERT INTO Bebidas (tipo_produto, nome_produto, marca_produto, preco_produto)
VALUES
('Whisky', 'Johnnie Walker Black Label', 'Johnnie Walker', 180.00),
('Whisky', 'Jameson Irish Whiskey', 'Jameson', 120.00),
('Whisky', 'Jack Daniels Old No. 7', 'Jack Daniel', 150.00);