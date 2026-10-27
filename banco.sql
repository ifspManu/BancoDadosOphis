DROP DATABASE IF EXISTS Animais;
CREATE DATABASE Animais;
USE Animais;

CREATE TABLE animal(
    nomeCientifico VARCHAR(50) NOT NULL,
    nome VARCHAR(50) NOT NULL,
    habitat VARCHAR(100) NOT NULL,
    nivelPerigo VARCHAR(20) NOT NULL,
    descricao VARCHAR(255) NOT NULL,
    caracterFisic VARCHAR(255) NOT NULL,
    sobre VARCHAR(255) NOT NULL,
    PRIMARY KEY(nomeCientifico)
);

INSERT INTO animal VALUES(
    'Micrurus corallinus',
    'Cobra-coral',
    'Florestas e áreas úmidas',
    'Alto',
    'Serpente peçonhenta, conhecida por suas cores vibrantes.',
    'Corpo fino com anéis vermelhos, pretos e brancos.',
    'Possui veneno neurotóxico e geralmente evita humanos.'
);