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
	renda varchar(50) not null
);
"""