module ParentalTesting where

{- Usar o tipo sanguíneo para determinar se uma pessoa é filha de outras duas.
 - Devemos criar uma função chamada validParents. Ela deve receber os tipos
 - sanguíneos dos pais e do possível filho e responder se a combinação é ou não
 - possível.
 -
 - A tabela abaixo mostra os tipos sanguíneos possíveis de um filho para cada
 - combinação de pais.
 -
 -
 - ### |      A      |       B      |      AB      |      O       |
 - ----------------------------------------------------------------
 -  A  |    A, O     |  A, B, AB, O |   A, B, AB   |     A, O     |
 -  B  | A, B, AB, O |     B, O     |   A, B, AB   |     B, O     |
 -  AB |   A, B, AB  |   A, B, AB   |   A, B, AB   |     A, B     |
 -  O  |    A, O     |     B, O     |     A, B     |      O       |
 - ----------------------------------------------------------------
 -
 - Genes por tipo sanguíneo:
 - A -> AA ou AO
 - B -> BB ou BO
 - AB -> AB
 - O -> OO
 -
 - Um cruzamento entre AA e AO pode resultar em AA ou AO (ou seja, só pessoas do
 - tipo sanguíneo A). Já um cruzamento entre AO e AO pode dar AA, AO ou OO (ou
 - seja, pessoas com tipo sanguíneo A e O.)
 -}

data BloodType = A | B | AB | O deriving (Show, Eq, Ord)


cross :: BloodType -> BloodType -> [BloodType]
cross A A = [A, O]
cross A O = [A, O]
cross B B = [B, O]
cross O B = [B, O]
cross AB _ = [A, B, AB]
cross A B = [A, B, AB, O]
cross O O = [O]
cross x y = cross y x

validParents child mom dad = child `elem` cross mom dad
