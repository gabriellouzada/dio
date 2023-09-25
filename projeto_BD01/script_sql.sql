-- Criação do banco de dados para o cenário de e-commerce.
BEGIN;


CREATE TABLE IF NOT EXISTS public."Produto"
(
    "idProduto" integer NOT NULL,
    "Categoria" "char" NOT NULL,
    PRIMARY KEY ("idProduto")
);

CREATE TABLE IF NOT EXISTS public."Disponibiliza"
(
    "idFornecedor" integer NOT NULL,
    "idProduto" integer NOT NULL
);

CREATE TABLE IF NOT EXISTS public."Fornecedor"
(
    "idFornecedor" integer NOT NULL,
    "Razão Social" "char" NOT NULL,
    "CNPJ" "char" NOT NULL,
    PRIMARY KEY ("idFornecedor")
);

CREATE TABLE IF NOT EXISTS public."Estoque"
(
    "idEstoque" integer NOT NULL,
    "Local" "char" NOT NULL,
    PRIMARY KEY ("idEstoque")
);

CREATE TABLE IF NOT EXISTS public."Em"
(
    "idProduto" integer NOT NULL,
    "idEstoque" integer NOT NULL,
    "Quantidade" integer NOT NULL
);

CREATE TABLE IF NOT EXISTS public."Vendedor"
(
    "idVendedor" integer NOT NULL,
    "Razão Social" "char" NOT NULL,
    "Local" "char" NOT NULL,
    PRIMARY KEY ("idVendedor")
);

CREATE TABLE IF NOT EXISTS public."Vendido"
(
    "idVendedor" integer NOT NULL,
    "idProduto" integer NOT NULL,
    "Quantidade" integer NOT NULL
);

CREATE TABLE IF NOT EXISTS public."Cliente"
(
    "idCliente" integer NOT NULL,
    "Nome" "char" NOT NULL,
    "Identificação" "char" NOT NULL,
    "Endereço" "char" NOT NULL,
    PRIMARY KEY ("idCliente")
);

CREATE TABLE IF NOT EXISTS public."Pedido"
(
    "idPedido" integer NOT NULL,
    "Status" "char" NOT NULL,
    "Descrição" "char" NOT NULL,
    "idCliente" integer NOT NULL,
    "Frete" money NOT NULL,
    PRIMARY KEY ("idPedido")
);

CREATE TABLE IF NOT EXISTS public."Produto/Pedido"
(
    "idPedido" integer NOT NULL,
    "idProduto" integer NOT NULL,
    "Quantidade" integer NOT NULL
);

ALTER TABLE IF EXISTS public."Disponibiliza"
    ADD CONSTRAINT "idFornecedor" FOREIGN KEY ("idFornecedor")
    REFERENCES public."Fornecedor" ("idFornecedor") MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public."Disponibiliza"
    ADD CONSTRAINT "idProduto" FOREIGN KEY ("idProduto")
    REFERENCES public."Produto" ("idProduto") MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public."Em"
    ADD CONSTRAINT "idProduto" FOREIGN KEY ("idProduto")
    REFERENCES public."Produto" ("idProduto") MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public."Em"
    ADD CONSTRAINT "idEstoque" FOREIGN KEY ("idEstoque")
    REFERENCES public."Estoque" ("idEstoque") MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public."Vendido"
    ADD CONSTRAINT "idVendedor" FOREIGN KEY ("idVendedor")
    REFERENCES public."Vendedor" ("idVendedor") MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public."Vendido"
    ADD CONSTRAINT "idProduto" FOREIGN KEY ("idProduto")
    REFERENCES public."Produto" ("idProduto") MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public."Pedido"
    ADD CONSTRAINT "idCliente" FOREIGN KEY ("idCliente")
    REFERENCES public."Cliente" ("idCliente") MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public."Produto/Pedido"
    ADD CONSTRAINT "idPedido" FOREIGN KEY ("idPedido")
    REFERENCES public."Pedido" ("idPedido") MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public."Produto/Pedido"
    ADD CONSTRAINT "idProduto" FOREIGN KEY ("idProduto")
    REFERENCES public."Produto" ("idProduto") MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;

END;