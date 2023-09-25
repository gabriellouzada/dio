BEGIN;

SELECT * FROM "Produto";
INSERT INTO public."Produto" 
	VALUES (01, 'casa',
		   02, 'banho',
		   03, 'cozinha',
		   04, 'eletronicos');