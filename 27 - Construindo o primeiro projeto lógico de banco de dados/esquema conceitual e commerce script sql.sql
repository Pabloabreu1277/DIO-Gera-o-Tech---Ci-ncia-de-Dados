-- criação do bd para cenario e-commerce
create database ecommercee;
use ecommercee;

-- criar tabela clientes

create table client(
	idcliente int auto_increment primary key,
    Fnome varchar(10),
    Minit varchar(3),
    Lnome varchar(20),
    CPF char(11) not null,
    address varchar(30),
    constraint unique_cpf_client unique(CPF)
);

desc client;

-- criar tabela produto
create table product(
	idproduct int auto_increment primary key,
    Pname varchar(10) not null,
    classification_kids bool default false,
    category enum('eletronica','vestimento','brinquedos','alimentos','móveis') not null,
    avaliação float default 0,
    size varchar(10)
);

desc product;

create table payments(
	idclient int,
    idpayment int,
    typepayment enum('boleto','cartão','dois cartoes'),
    limitavaliable float,
    primary key(idclient, idpayment)
);

desc payments;

-- criar tabela pedido
create table orders(
	idorders int auto_increment primary key,
	idorderclient int,
	orderstatus enum('cancelado','confirmado','em processamento') default 'em processamento',
	orderdescription varchar(255),
	sendvalue float default 10,
    paymentcash bool default false,
    constraint fk_orders_client foreign key (idorderclient) references client(idcliente)
);

desc orders;
    
-- criar tabela de estoque
create table productstorage(
	idprodstorage int auto_increment primary key,
    storagelocation varchar(255),
    quantity int default 0
);

desc productstorage;

-- criar tabela fornecedor
 create table supplier(
	idsupplier int auto_increment primary key,
	Socialname varchar(255) not null,
    CNPJ char(15) not null,
    contact char(11) not null,
    constraint unique_supplier unique (CNPJ)
    );
    
    desc supplier;
    
    -- criar tabela vendedor
    create table saller(
		idsaller int auto_increment primary key,
        socialname varchar(255) not null,
        abstname varchar(255),
        CNPJ char(15),
        CPF char(9),
        location varchar(255),
        contact char(11) not null,
        constraint unique_cnpj_saller unique (CNPJ),
        constraint unique_cpf_saller unique (CPF)
	);
    
    desc saller;
    
    create table productsaller(
		idpsaller int,
        idproduct int,
        prodquantity int default 1,
        primary key (idpsaller,idproduct),
        constraint fk_product_saller foreign key (idpsaller) references saller(idsaller),
        constraint fk_product_product foreign key (idproduct) references product(idproduct)
	);
	
    desc productsaller;
    
    create table productorder(
		idpoproduct int,
        idpoorder int,
        poquantity int default 1,
        postatus enum('disponivel','sem estoque') default 'disponivel',
        primary key (idpoproduct,idpoorder),
        constraint fk_product_sallerorder foreign key (idpoproduct) references product (idproduct),
		constraint fk_product_productorder foreign key (idpoorder) references orders (idorders)
	);
    
    desc productorder;
    
    create table storagelocation(
		idlproduct int,
        idlstorage int,
        location varchar(255) not null,
        primary key (idlproduct,idlstorage),
        constraint fk_product_sallerstorage foreign key (idlproduct) references product (idproduct),
        constraint fk_product_productstorage foreign key (idlstorage) references productstorage (idprodstorage)
);
    
desc storagelocation;




