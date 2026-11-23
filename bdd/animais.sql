CREATE DATABASE Animais;

USE Animais;

CREATE TABLE animal (
    nomeCientifico VARCHAR(100) PRIMARY KEY,
    nome VARCHAR(100),
    habitat VARCHAR(255),
    nivelPerigo VARCHAR(50),
    descricao TEXT,
    caracterFisic TEXT,
    sobre TEXT
);