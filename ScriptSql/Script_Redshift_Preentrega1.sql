drop table if exists juansaobento_coderhouse.juansaobento_cocktailsapi;
create table juansaobento_coderhouse.juansaobento_cocktailsapi (
idDrink int primary key,
Cocktail varchar (200),
Categoria varchar (200),
Alcoholico varchar (200),
Cristaleria varchar (200),
Instrucciones varchar (1000),
Ingredientes SUPER,
strFecha_Obtencion datetime default (current_timestamp));

