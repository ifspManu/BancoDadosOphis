CREATE DATABASE Animais;

USE Animais;

CREATE TABLE animal (
    nomeCientifico VARCHAR(100) PRIMARY KEY,
    nome VARCHAR(100),
    habitat VARCHAR(255),
    nivelPerigo VARCHAR(50),
    descricao VARCHAR(100),
    caracterFisic VARCHAR(100),
    sobre VARCHAR(100)
);