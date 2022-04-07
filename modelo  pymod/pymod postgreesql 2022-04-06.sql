CREATE TABLE "IMOVEL"(
    "id" INTEGER NULL,
    "logradouro" VARCHAR(255) NOT NULL,
    "cep" INTEGER NOT NULL,
    "bairro" VARCHAR(255) NOT NULL,
    "cidade" VARCHAR(255) NOT NULL,
    "estado" VARCHAR(255) NOT NULL,
    "valor" DOUBLE PRECISION NOT NULL
);
ALTER TABLE
    "IMOVEL" ADD PRIMARY KEY("id");
CREATE TABLE "INQUILINO"(
    "id" INTEGER NULL,
    "nome" VARCHAR(255) NOT NULL,
    "data_nascimento" DATE NOT NULL,
    "telefone" VARCHAR(255) NOT NULL,
    "e-mail" VARCHAR(255) NOT NULL,
    "cpf" INTEGER NOT NULL
);
ALTER TABLE
    "INQUILINO" ADD PRIMARY KEY("id");
ALTER TABLE
    "INQUILINO" ADD CONSTRAINT "inquilino_telefone_unique" UNIQUE("telefone");
ALTER TABLE
    "INQUILINO" ADD CONSTRAINT "inquilino_e_mail_unique" UNIQUE("e-mail");
ALTER TABLE
    "INQUILINO" ADD CONSTRAINT "inquilino_cpf_unique" UNIQUE("cpf");
CREATE TABLE "PROPRIETARIO"(
    "id" INTEGER NULL,
    "nome" VARCHAR(255) NOT NULL,
    "data_nascimento" DATE NOT NULL,
    "telefone" VARCHAR(255) NULL,
    "e-mail" VARCHAR(255) NULL,
    "cpf" VARCHAR(255) NULL
);
ALTER TABLE
    "PROPRIETARIO" ADD PRIMARY KEY("id");
ALTER TABLE
    "PROPRIETARIO" ADD CONSTRAINT "proprietario_telefone_unique" UNIQUE("telefone");
ALTER TABLE
    "PROPRIETARIO" ADD CONSTRAINT "proprietario_cpf_unique" UNIQUE("cpf");
CREATE TABLE "CORRETOR"(
    "id" INTEGER NULL,
    "nome" INTEGER NOT NULL,
    "data_nascimento" INTEGER NOT NULL,
    "telefone" INTEGER NULL,
    "e-mail" INTEGER NULL,
    "cpf" INTEGER NULL,
    "cofeci" INTEGER NULL
);
ALTER TABLE
    "CORRETOR" ADD PRIMARY KEY("id");
ALTER TABLE
    "CORRETOR" ADD CONSTRAINT "corretor_telefone_unique" UNIQUE("telefone");
ALTER TABLE
    "CORRETOR" ADD CONSTRAINT "corretor_e_mail_unique" UNIQUE("e-mail");
ALTER TABLE
    "CORRETOR" ADD CONSTRAINT "corretor_cpf_unique" UNIQUE("cpf");
ALTER TABLE
    "CORRETOR" ADD CONSTRAINT "corretor_cofeci_unique" UNIQUE("cofeci");
COMMENT
ON COLUMN
    "CORRETOR"."cofeci" IS 'Conselho Federal de Corretores de Imóveis- numero de atuação do corretor';
CREATE TABLE "ALUGUEL"(
    "id" INTEGER NULL,
    "id imovel" INTEGER NULL,
    "id proprietário" INTEGER NULL,
    "id inquilino" INTEGER NULL,
    "id corretor" INTEGER NULL
);
ALTER TABLE
    "ALUGUEL" ADD PRIMARY KEY("id");
CREATE INDEX "aluguel_id imovel_index" ON
    "ALUGUEL"("id imovel");
CREATE INDEX "aluguel_id proprietário_index" ON
    "ALUGUEL"("id proprietário");
CREATE INDEX "aluguel_id inquilino_index" ON
    "ALUGUEL"("id inquilino");
CREATE INDEX "aluguel_id corretor_index" ON
    "ALUGUEL"("id corretor");
CREATE TABLE "CONTRATO"(
    "id" INTEGER NULL,
    "id aluguel" INTEGER NULL,
    "data fechamento" DATE NOT NULL,
    "fechado" BOOLEAN NOT NULL
);
ALTER TABLE
    "CONTRATO" ADD PRIMARY KEY("id");
CREATE INDEX "contrato_id aluguel_index" ON
    "CONTRATO"("id aluguel");
CREATE TABLE "IMOVEL_PROPRIETARIO"(
    "id" INTEGER NULL,
    "id proprietario" INTEGER NULL,
    "id imovel" INTEGER NULL
);
ALTER TABLE
    "IMOVEL_PROPRIETARIO" ADD PRIMARY KEY("id");
ALTER TABLE
    "IMOVEL_PROPRIETARIO" ADD CONSTRAINT "imovel_proprietario_id imovel_unique" UNIQUE("id imovel");
ALTER TABLE
    "ALUGUEL" ADD CONSTRAINT "aluguel_id inquilino_foreign" FOREIGN KEY("id inquilino") REFERENCES "INQUILINO"("id");
ALTER TABLE
    "ALUGUEL" ADD CONSTRAINT "aluguel_id proprietário_foreign" FOREIGN KEY("id proprietário") REFERENCES "PROPRIETARIO"("id");
ALTER TABLE
    "IMOVEL_PROPRIETARIO" ADD CONSTRAINT "imovel_proprietario_id proprietario_foreign" FOREIGN KEY("id proprietario") REFERENCES "PROPRIETARIO"("id");
ALTER TABLE
    "ALUGUEL" ADD CONSTRAINT "aluguel_id imovel_foreign" FOREIGN KEY("id imovel") REFERENCES "IMOVEL"("id");
ALTER TABLE
    "IMOVEL_PROPRIETARIO" ADD CONSTRAINT "imovel_proprietario_id imovel_foreign" FOREIGN KEY("id imovel") REFERENCES "IMOVEL"("id");
ALTER TABLE
    "ALUGUEL" ADD CONSTRAINT "aluguel_id corretor_foreign" FOREIGN KEY("id corretor") REFERENCES "CORRETOR"("id");
ALTER TABLE
    "CONTRATO" ADD CONSTRAINT "contrato_id aluguel_foreign" FOREIGN KEY("id aluguel") REFERENCES "ALUGUEL"("id");