"""
create database if not exists exemplo_crud_python;
use exemplo_crud_python;

create table if not exists produto
(
	id int not null auto_increment primary key,
	nome varchar(50) not null,
	valor decimal(10,2) not null,
	estoque int not null
);

create table if not exists fornecedor
(
	id int not null auto_increment primary key,
	razao_social varchar(50) not null,
	nome_fantasia varchar(50) not null,
	cnpj decimal(20,2) not null,
	email varchar(50) not null
);

create table if not exists clientes
(
	id int not null auto_increment primary key,
	nome varchar(50) not null,
	cpf varchar(50) not null,
	email varchar(50) not null,
	renda decimal(10,2) not null
);

CREATE TABLE if not exists movimentacao (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_produto INT NOT NULL,
    tipo ENUM('Entrada', 'Saída') NOT NULL,
    quantidade INT NOT NULL,
    data_movimentacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_produto_mov FOREIGN KEY (id_produto) 
        REFERENCES produto(id) ON DELETE CASCADE
);

create table if not exists enderecos
(
	id int not null auto_increment primary key,
	id_cliente int not null,
	cep varchar(10) not null,
	logradouro varchar(10) not null,
	cidade varchar(50) not null,
	tipo ENUM('Comercial', 'Residencial', 'Entrega') not null,
	constraint fk_id_cliente foreign key (id_cliente)
		references clientes(id) on delete cascade
);

create table if not exists contatos
(
	id int not null auto_increment primary key,
	id_fornecedor int not null,
	nome varchar(50) not null,
	telefone varchar(20) not null,
	email varchar(50) not null,
	tipo enum('Vendas', 'Suporte'),
	constraint fk_id_fornecedor foreign key (id_fornecedor)
		references fornecedor(id) on delete cascade
);
"""