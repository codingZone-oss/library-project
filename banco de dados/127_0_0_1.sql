-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 12-Jan-2026 às 07:00
-- Versão do servidor: 10.4.28-MariaDB
-- versão do PHP: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `livraria`
--
CREATE DATABASE IF NOT EXISTS `livraria` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `livraria`;

-- --------------------------------------------------------

--
-- Estrutura da tabela `autores`
--

CREATE TABLE `autores` (
  `id` int(11) NOT NULL,
  `nome` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Extraindo dados da tabela `autores`
--

INSERT INTO `autores` (`id`, `nome`) VALUES
(1, 'Gabriel García Márquez'),
(2, 'Jane Austen'),
(3, 'William Shakespeare'),
(4, 'J.K. Rowling'),
(5, 'George Orwell'),
(6, 'Leo Tolstoy'),
(7, 'Fyodor Dostoevsky'),
(8, 'Ernest Hemingway'),
(9, 'Mark Twain'),
(10, 'Virginia Woolf'),
(11, 'Charles Dickens'),
(12, 'Franz Kafka'),
(13, 'Haruki Murakami'),
(14, 'J.R.R. Tolkien'),
(15, 'Agatha Christie'),
(16, 'Stephen King'),
(17, 'Albert Camus'),
(18, 'José Saramago'),
(19, 'Clarice Lispector'),
(20, 'Paulo Coelho'),
(21, 'Fernando Pessoa'),
(22, 'Jorge Amado'),
(23, 'Machado de Assis'),
(24, 'Eça de Queirós'),
(25, 'Italo Calvino'),
(26, 'Umberto Eco'),
(27, 'Oscar Wilde'),
(28, 'Emily Brontë'),
(29, 'Bram Stoker'),
(30, 'H.G. Wells'),
(31, 'Mary Shelley'),
(32, 'Philip K. Dick'),
(33, 'Isaac Asimov'),
(34, 'Ray Bradbury'),
(35, 'Aldous Huxley'),
(36, 'Jules Verne'),
(37, 'Victor Hugo'),
(38, 'Honoré de Balzac'),
(39, 'Marcel Proust'),
(40, 'Herman Melville'),
(41, 'James Joyce'),
(42, 'Toni Morrison'),
(43, 'Chinua Achebe'),
(44, 'Salman Rushdie'),
(45, 'Margaret Atwood'),
(46, 'Kurt Vonnegut'),
(47, 'George R.R. Martin'),
(48, 'Neil Gaiman'),
(49, 'Zadie Smith'),
(50, 'Colson Whitehead'),
(51, 'Don DeLillo'),
(52, 'Cormac McCarthy'),
(53, 'Thomas Pynchon'),
(54, 'Jonathan Franzen'),
(55, 'Ian McEwan'),
(56, 'Kazuo Ishiguro'),
(57, 'Mario Vargas Llosa'),
(58, 'Julio Cortázar'),
(59, 'Isabel Allende'),
(60, 'Roberto Bolaño');

-- --------------------------------------------------------

--
-- Estrutura da tabela `categorias`
--

CREATE TABLE `categorias` (
  `id` int(11) NOT NULL,
  `nome` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Extraindo dados da tabela `categorias`
--

INSERT INTO `categorias` (`id`, `nome`) VALUES
(1, 'Romance'),
(2, 'Ficção'),
(3, 'Drama'),
(4, 'Acção'),
(5, 'Comédia'),
(6, 'Religioso');

-- --------------------------------------------------------

--
-- Estrutura da tabela `clientes`
--

CREATE TABLE `clientes` (
  `id` int(11) NOT NULL,
  `nome` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `telefone` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Extraindo dados da tabela `clientes`
--

INSERT INTO `clientes` (`id`, `nome`, `email`, `telefone`) VALUES
(1, 'Ana Silva', 'ana@gmail.com', '98888'),
(2, 'estanislau dos santos', 'estanislauhilario60@gmail.com', '930676256'),
(3, 'Germano Rogerio', 'germano@gmail.com', '941791095'),
(4, 'Ema Franco', 'Ema@gmail.com', '941695266'),
(5, 'Miguel Kibala', 'Kibala@gmail.com', '94422567'),
(6, 'Francisco Makuntima', 'francisco@gmail.com', '921112523'),
(7, 'Beatriz Bravo', 'Bravo@gmail.com', '945993405'),
(8, 'Termo Nóbrega', 'termo@gmail.com', '92345678'),
(9, 'Panzo Bungadas', 'panzadas@gmail.com', '938047823'),
(10, 'Graciano Neto', 'graciano@gmail.com', '935555500'),
(11, 'Esperança Bernanrdo', 'esperança@gmail.com', '9380423423'),
(12, 'Manuel Lucas', 'manuel@gmail.com', '93801233'),
(13, 'Benjamim Andrade', 'benjamim@gmail.com', '923458235'),
(14, 'Estrela Mukenje', 'estrela@gmail.com', '9323456782'),
(15, 'isabel makaya', 'aculpaéda@gmail.com', '976543223'),
(16, 'Febo Francisco', 'febadas@gmail.com', '932987823'),
(17, 'Januario Janeiro', 'dejaná@gmail.com', '938232323'),
(18, 'Felismina Guilherme', 'tiafelí@gmail.com', '938098723'),
(19, 'Damião akatsuki', 'anime@gmail.com', '938047438'),
(20, 'José Lopes', 'jose@gmail.com', '931147823'),
(21, 'Daniel Álves', 'barça@gmail.com', '912247823'),
(22, 'Cristiano Ronaldo', 'cris@gmail.com', '955555555'),
(23, 'C4 Pedro', 'lilsaint@gmail.com', '911111111'),
(24, 'Jorge Paulo', 'pegrande@gmail.com', '932222222'),
(25, 'Pedro Viégas', 'pedradas@gmail.com', '933333333'),
(26, 'Vinícios Jr', 'hallamadrid@gmail.com', '934444444'),
(27, 'venâncio Gaspar', 'devená@gmail.com', '955555553'),
(28, 'Mickey Mouse', 'borro@gmail.com', '955555553'),
(29, 'Manuel gonçalves', 'manuel@gmail.com', '936666666'),
(30, 'Kassongo yeye', 'mobalinanga@gmail.com', '977777777'),
(31, 'Jaqueline Brasil', 'jaqui@gmail.com', '988888888'),
(32, 'Anselmo Ralph', 'fimdomundo@gmail.com', '999999999'),
(33, 'Lamine Yamal', 'viscabarça@gmail.com', '911111111'),
(34, 'Pedro Agostinho', 'neto@gmail.com', '912121212'),
(35, 'João Lourenço', 'anação@gmail.com', '913131313'),
(36, 'Rainha jinga', 'chocotera@gmail.com', '9123123123'),
(37, 'Fernado da piedade dias dos santos', 'burlador@gmail.com', '913456782'),
(38, 'Joana Palácio Camilo', 'joana@gmail.com', '998765433'),
(39, 'Tia Cátia', '24kitchen@gmail.com', '932342343'),
(40, 'Filipa Gomes', 'Cozinhacomtwistgmail.com', '939494949'),
(41, 'Virínia francisco', 'virgi@gmail.com', '998765432'),
(42, 'Celestino Ngunza', 'cele@gmail.com', '945456456'),
(43, 'Bob Marley Farai', 'jamaica@gmail.com', '938047823'),
(44, 'Tia Madó', 'madalena@gmail.com', '998876543'),
(45, 'António gilberto', 'rabi@gmail.com', '936393939'),
(46, 'aquele wi que náo aparece', 'nãotemamigo@gmail.com', '932222222'),
(47, 'Lil Mac', 'yongfamily@gmail.com', '931111111'),
(48, 'Xuxu Bower', 'mobbers@gmail.com', '977777777'),
(49, 'Puquila Bea', 'agenteBAI@gmail.com', '959800000'),
(50, 'Luís Suáres ', 'elpitchitxi@gmail.com', '980234123'),
(51, 'Panzo Bungadas', 'panzadas@gmail.com', '938047823'),
(52, 'Mano Chaba', 'quemtemandouirnailha@gmail.com', '938047123'),
(53, 'Rita Fernandes', 'rita@gmail.com', '930676633'),
(54, 'Arsenal Inglaterra', 'noreal@gmail.com', '938057823'),
(55, 'Laurindo Firmino', 'lau@gmail.com', '924047823'),
(56, 'Lauricleny Carlos', 'lau@gmail.com', '928057823'),
(57, 'Siantos António', 'ten@gmail.com', '939044723'),
(58, 'Valdimiro Ribeiro', 'val@gmail.com', '938047457'),
(59, 'Volodimir Zelensky', 'ucrania@gmail.com', '9983762733'),
(60, 'Vladimir Putin', 'fudido@gmail.com', '926047823'),
(61, 'Jorge Neto', 'jorge@gmail.com', '912247823'),
(62, 'Moisés do Egito', 'cristão@gmail.com', '932222223'),
(63, 'Feleciano Tchindavela', 'fininho@gmail.com', '938047325'),
(64, 'Papa Francisco', 'vaimorrer@gmail.com', '938047874'),
(65, 'Emenegildo duas Horas', 'damanha@gmail.com', '838047823');

-- --------------------------------------------------------

--
-- Estrutura da tabela `compras`
--

CREATE TABLE `compras` (
  `id` int(11) NOT NULL,
  `id_cliente` int(11) DEFAULT NULL,
  `id_livro` int(11) DEFAULT NULL,
  `quantidade` int(11) DEFAULT NULL,
  `data_compra` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `editoras`
--

CREATE TABLE `editoras` (
  `id` int(11) NOT NULL,
  `nome` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Extraindo dados da tabela `editoras`
--

INSERT INTO `editoras` (`id`, `nome`) VALUES
(1, 'Nova Página Editora'),
(2, 'Verso & Prosa'),
(3, 'Editora Horizonte'),
(4, 'Raiz Editorial'),
(5, 'LetraViva'),
(6, 'Palavrare'),
(7, 'Inktacto'),
(8, 'Foco na Página'),
(9, 'Nuvem de Letras'),
(10, 'Tinta Brava'),
(11, 'Mundo Miúdo'),
(12, 'Borboleta Azul'),
(13, 'Pequeno Gênio'),
(14, 'Contos Coloridos'),
(15, 'Editora Brincaletras'),
(16, 'Estória & Alma'),
(17, 'Sombras & Palavras'),
(18, 'Círculo Literário'),
(19, 'Narrativa Pura'),
(20, 'Luz & Letra'),
(21, 'Editora Saber'),
(22, 'Códice Técnico'),
(23, 'Lexis Publicações'),
(24, 'Ponto Científico'),
(25, 'Atlas do Saber'),
(26, 'Ruptura Editorial'),
(27, 'Voz Marginal'),
(28, 'Selva de Papel'),
(29, 'Outros Olhares'),
(30, 'Editora Subverso'),
(31, 'Letras do Tempo'),
(32, 'Palavra Aberta'),
(33, 'Editora Alfa & Ômega'),
(34, 'Caminho da Página'),
(35, 'Sabedoria Editorial'),
(36, 'Mestre Livro'),
(37, 'Impressão Livre'),
(38, 'Chama Literária'),
(39, 'Nova Geração'),
(40, 'Paginação Final'),
(41, 'Farol das Letras'),
(42, 'Ideia Impressa'),
(43, 'Publicações Aurora'),
(44, 'Livro Sagrado'),
(45, 'Editorial Essência'),
(46, 'Tempo de Ler'),
(47, 'Palavra & Espírito'),
(48, 'Expressão Escrita'),
(49, 'Palavra Nossa'),
(50, 'Editora Harmonia'),
(51, 'Raízes da Palavra'),
(52, 'Manuscrito Real'),
(53, 'Nova Era Editorial'),
(54, 'Editora AlfaNova'),
(55, 'Casa do Livro'),
(56, 'Editora Vida Plena'),
(57, 'Publicações Alvorada'),
(58, 'Editora Ponto & Vírgula'),
(59, 'Editora Mundo Aberto'),
(60, 'Fonte Literária'),
(61, 'Editora Palavra Solta');

-- --------------------------------------------------------

--
-- Estrutura da tabela `livros`
--

CREATE TABLE `livros` (
  `id` int(11) NOT NULL,
  `titulo` varchar(150) DEFAULT NULL,
  `ano_publicacao` year(4) NOT NULL,
  `id_autor` int(11) DEFAULT NULL,
  `id_editora` int(11) DEFAULT NULL,
  `id_categoria` int(11) DEFAULT NULL,
  `preco` decimal(10,2) DEFAULT NULL,
  `estoque` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Extraindo dados da tabela `livros`
--

INSERT INTO `livros` (`id`, `titulo`, `ano_publicacao`, `id_autor`, `id_editora`, `id_categoria`, `preco`, `estoque`) VALUES
(1, 'O Último Amanhecer', '2021', NULL, NULL, NULL, NULL, NULL),
(2, 'A Luz da Tempestade', '2020', NULL, NULL, NULL, 16.34, 1),
(3, 'Segredos do Deserto', '2019', NULL, NULL, NULL, 23.15, 8),
(4, 'No Coração da Floresta', '2022', NULL, NULL, NULL, 80.40, 2),
(5, 'Entre Sombras e Sonhos', '2018', NULL, NULL, NULL, 79.70, 5),
(6, 'O Código de Cristal', '2023', NULL, NULL, NULL, 65.90, 8),
(7, 'Ventos do Norte', '2021', NULL, NULL, NULL, 43.21, 6),
(8, 'A Canção dos Antigos', '2017', NULL, NULL, NULL, 56.90, 4),
(9, 'Caminhos de Esperança', '2016', NULL, NULL, NULL, 84.23, 9),
(10, 'O Olhar do Abismo', '2015', NULL, NULL, NULL, 45.76, 1),
(11, 'Sombras da Noite', '2022', NULL, NULL, NULL, 90.34, 6),
(12, 'Asas de Liberdade', '2019', NULL, NULL, NULL, 55.77, 3),
(13, 'O Refúgio Secreto', '2020', NULL, NULL, NULL, 65.90, 7),
(14, 'A Profecia Perdida', '2021', NULL, NULL, NULL, 55.69, 8),
(15, 'Fragmentos do Infinito', '2018', NULL, NULL, NULL, 23.15, 7),
(16, 'Vidas Paralelas', '2017', NULL, NULL, NULL, 43.76, 8),
(17, 'A Jornada do Herói', '2016', NULL, NULL, NULL, 17.65, 9),
(18, 'Noite de Estrelas', '2023', NULL, NULL, NULL, 78.30, 6),
(19, 'Lágrimas de Fogo', '2022', NULL, NULL, NULL, 45.76, 1),
(20, 'O Espelho do Tempo', '2021', NULL, NULL, NULL, 58.80, 5),
(21, 'Pelas Ruas da Alma', '2020', NULL, NULL, NULL, 78.12, 3),
(22, 'Códigos do Vento', '2019', NULL, NULL, NULL, 90.14, 9),
(23, 'Além das Palavras', '2023', NULL, NULL, NULL, 75.23, 4),
(24, 'A Ilha Desconhecida', '2022', NULL, NULL, NULL, 89.45, 9),
(25, 'Céus de Setembro', '2021', NULL, NULL, NULL, 100.45, 5),
(26, 'Som do Silêncio', '2020', NULL, NULL, NULL, 120.45, 7),
(27, 'O Reino de Cinzas', '2019', NULL, NULL, NULL, 145.56, 3),
(28, 'Caminho das Estações', '2018', NULL, NULL, NULL, 200.80, 9),
(29, 'O Voo das Borboletas', '2017', NULL, NULL, NULL, 300.34, 5),
(30, 'O Labirinto das Almas', '2016', NULL, NULL, NULL, 230.76, 8),
(31, 'O Diário Esquecido', '2023', NULL, NULL, NULL, 220.67, 4),
(32, 'Além da Memória', '2022', NULL, NULL, NULL, 120.65, 5),
(33, 'O Despertar dos Deuses', '2021', NULL, NULL, NULL, 450.98, 3),
(34, 'Chamas da Verdade', '2020', NULL, NULL, NULL, 345.87, 5),
(35, 'A Marca do Destino', '2019', NULL, NULL, NULL, 213.67, 2),
(36, 'Paz em Meio ao Caos', '2018', NULL, NULL, NULL, 321.76, 5),
(37, 'Horizonte Perdido', '2017', NULL, NULL, NULL, 321.89, 9),
(38, 'Filhos do Sol', '2016', NULL, NULL, NULL, 45.89, 8),
(39, 'Vozes da Floresta', '2023', NULL, NULL, NULL, 14.10, 4),
(40, 'O Eco do Vazio', '2022', NULL, NULL, NULL, 10.50, 5),
(41, 'Estrelas Caídas', '2021', NULL, NULL, NULL, 5.23, 6),
(42, 'No Fim da Estrada', '2020', NULL, NULL, NULL, 14000.00, 1),
(43, 'O Livro dos Dias', '2019', NULL, NULL, NULL, 15000.00, 2),
(44, 'Lendas de Areia', '2018', NULL, NULL, NULL, 20000.00, 3),
(45, 'A Casa dos Sonhos', '2017', NULL, NULL, NULL, 5000.00, 3),
(46, 'O Guardião da Palavra', '2016', NULL, NULL, NULL, 7000.00, 2),
(47, 'Sob o Céu Vermelho', '2023', NULL, NULL, NULL, 17000.00, 4),
(48, 'A Dança dos Ventos', '2022', NULL, NULL, NULL, 3000.00, 2),
(49, 'O Enigma da Montanha', '2021', NULL, NULL, NULL, 3000.00, 1),
(50, 'No Silêncio da Noite', '2020', NULL, NULL, NULL, 4000.00, 2),
(51, 'Caminho de Luz', '2019', NULL, NULL, NULL, 13000.00, 3),
(52, 'Entre Dois Mundos', '2018', NULL, NULL, NULL, 17000.00, 5),
(53, 'Histórias de Outono', '2017', NULL, NULL, NULL, 18000.00, 10),
(54, 'As Quatro Estações', '2016', NULL, NULL, NULL, 29000.00, 50),
(55, 'Sombras da Alma', '2023', NULL, NULL, NULL, 100.00, 2),
(56, 'A Rosa e o Espinho', '2022', NULL, NULL, NULL, 20000.00, 3),
(57, 'A Lenda do Mar', '2021', NULL, NULL, NULL, 30000.00, 4),
(58, 'Raízes do Tempo', '2020', NULL, NULL, NULL, 35000.00, 4),
(59, 'Memórias do Amanhã', '2019', NULL, NULL, NULL, 50000.00, 18),
(60, 'A Ponte Invisível', '2018', NULL, NULL, NULL, 25000.00, 45);

-- --------------------------------------------------------

--
-- Estrutura da tabela `user`
--

CREATE TABLE `user` (
  `cod` int(11) NOT NULL,
  `user_name` varchar(30) NOT NULL,
  `pass_word` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Extraindo dados da tabela `user`
--

INSERT INTO `user` (`cod`, `user_name`, `pass_word`) VALUES
(1, 'lary_123', 'est@nislau30'),
(2, 'davi#', 'davizin'),
(3, 'antonio#', 'anto');

-- --------------------------------------------------------

--
-- Estrutura da tabela `worker`
--

CREATE TABLE `worker` (
  `id` int(11) NOT NULL,
  `name_worker` varchar(30) NOT NULL,
  `number_identity_card` varchar(14) NOT NULL,
  `funtion_type` varchar(30) NOT NULL,
  `phone_number` varchar(15) NOT NULL,
  `city` varchar(30) NOT NULL,
  `district` varchar(30) NOT NULL,
  `avenue` varchar(30) NOT NULL,
  `neighborhood` varchar(30) NOT NULL,
  `street` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Extraindo dados da tabela `worker`
--

INSERT INTO `worker` (`id`, `name_worker`, `number_identity_card`, `funtion_type`, `phone_number`, `city`, `district`, `avenue`, `neighborhood`, `street`) VALUES
(1, 'Estanislauu dos Santos', '009130284LA040', 'bibliotecario', '930676256', 'Launda', 'Cazenga', 'Aven. Fidel de castro', 'Samba', 'None');

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `autores`
--
ALTER TABLE `autores`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `categorias`
--
ALTER TABLE `categorias`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `compras`
--
ALTER TABLE `compras`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_cliente` (`id_cliente`),
  ADD KEY `id_livro` (`id_livro`);

--
-- Índices para tabela `editoras`
--
ALTER TABLE `editoras`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `livros`
--
ALTER TABLE `livros`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_autor` (`id_autor`),
  ADD KEY `id_editora` (`id_editora`),
  ADD KEY `id_categoria` (`id_categoria`);

--
-- Índices para tabela `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`cod`);

--
-- Índices para tabela `worker`
--
ALTER TABLE `worker`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `number_identity_card` (`number_identity_card`),
  ADD UNIQUE KEY `phone_number` (`phone_number`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `autores`
--
ALTER TABLE `autores`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=61;

--
-- AUTO_INCREMENT de tabela `categorias`
--
ALTER TABLE `categorias`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de tabela `clientes`
--
ALTER TABLE `clientes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=66;

--
-- AUTO_INCREMENT de tabela `compras`
--
ALTER TABLE `compras`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `editoras`
--
ALTER TABLE `editoras`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=62;

--
-- AUTO_INCREMENT de tabela `livros`
--
ALTER TABLE `livros`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=61;

--
-- AUTO_INCREMENT de tabela `user`
--
ALTER TABLE `user`
  MODIFY `cod` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de tabela `worker`
--
ALTER TABLE `worker`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Restrições para despejos de tabelas
--

--
-- Limitadores para a tabela `compras`
--
ALTER TABLE `compras`
  ADD CONSTRAINT `compras_ibfk_1` FOREIGN KEY (`id_cliente`) REFERENCES `clientes` (`id`),
  ADD CONSTRAINT `compras_ibfk_2` FOREIGN KEY (`id_livro`) REFERENCES `livros` (`id`);

--
-- Limitadores para a tabela `livros`
--
ALTER TABLE `livros`
  ADD CONSTRAINT `livros_ibfk_1` FOREIGN KEY (`id_autor`) REFERENCES `autores` (`id`),
  ADD CONSTRAINT `livros_ibfk_2` FOREIGN KEY (`id_editora`) REFERENCES `editoras` (`id`),
  ADD CONSTRAINT `livros_ibfk_3` FOREIGN KEY (`id_categoria`) REFERENCES `categorias` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
