--  En WS FINAL agregar campos
-- SET search_path=public;
-- use ejrocafuerte$public;
use ejrocafuerte$cpccs-ws;
-- LOS SECTORES NO HAN SIDO AGREGADOS.... CREO SECTORES CUALQUIERA PARA CUMPLIR CON LOS REQUISITOS
--  tabla provincia columnas id, nombre, regionid
INSERT INTO provincia VALUES (10, 'Azuay');
INSERT INTO provincia VALUES (1, 'Pichincha');
INSERT INTO provincia VALUES (2, 'Loja');
INSERT INTO provincia VALUES (3, 'Carchi');
INSERT INTO provincia VALUES (4, 'Imbabura');
INSERT INTO provincia VALUES (5, 'Cotopaxi');
INSERT INTO provincia VALUES (6, 'Tungurahua');
INSERT INTO provincia VALUES (7, 'Bolivar');
INSERT INTO provincia VALUES (8, 'Chimborazo');
INSERT INTO provincia VALUES (9, 'Cañar');
INSERT INTO provincia VALUES (11, 'El Oro');
INSERT INTO provincia VALUES (12, 'Esmeraldas');
INSERT INTO provincia VALUES (13, 'Santo Domingo de los Tsáchilas');
INSERT INTO provincia VALUES (14, 'Manabi');
INSERT INTO provincia VALUES (15, 'Los Rios');
INSERT INTO provincia VALUES (16, 'Santa Elena');
INSERT INTO provincia VALUES (17, 'Guayas');
INSERT INTO provincia VALUES (18, 'Sucumbios');
INSERT INTO provincia VALUES (19, 'Orellana');
INSERT INTO provincia VALUES (20, 'Pastaza');
INSERT INTO provincia VALUES (21, 'Morona Santiago');
INSERT INTO provincia VALUES (22, 'Zamora Chinchipe');
INSERT INTO provincia VALUES (23, 'Galapagos');
INSERT INTO provincia VALUES (24, 'Napo');
INSERT INTO provincia VALUES (25, 'otros');

--  tabla ciudad columnas id, nombre, provinciaid
INSERT INTO ciudad VALUES (180, 'Chordeleg', 10);
INSERT INTO ciudad VALUES (181, 'El Pan', 10);
INSERT INTO ciudad VALUES (182, 'Girón', 10);
INSERT INTO ciudad VALUES (183, 'Guachapala', 10);
INSERT INTO ciudad VALUES (184, 'Gualaceo', 10);
INSERT INTO ciudad VALUES (185, 'Nabón', 10);
INSERT INTO ciudad VALUES (186, 'Oña', 10);
INSERT INTO ciudad VALUES (187, 'Paute', 10);
INSERT INTO ciudad VALUES (188, 'Ponce Enríquez', 10);
INSERT INTO ciudad VALUES (189, 'Pucará', 10);
INSERT INTO ciudad VALUES (190, 'San Fernando', 10);
INSERT INTO ciudad VALUES (191, 'Santa Isabel', 10);
INSERT INTO ciudad VALUES (192, 'Sevilla de Oro', 10);
INSERT INTO ciudad VALUES (193, 'Sígsig', 10);
INSERT INTO ciudad VALUES (194, 'Caluma', 7);
INSERT INTO ciudad VALUES (195, 'Chillanes', 7);
INSERT INTO ciudad VALUES (196, 'Chimbo', 7);
INSERT INTO ciudad VALUES (197, 'Las Naves', 7);
INSERT INTO ciudad VALUES (198, 'Gualaceo', 7);
INSERT INTO ciudad VALUES (199, 'San Miguel', 7);
INSERT INTO ciudad VALUES (200, 'Biblián', 9);
INSERT INTO ciudad VALUES (201, 'Déleg', 9);
INSERT INTO ciudad VALUES (202, 'El Tambo', 9);
INSERT INTO ciudad VALUES (203, 'La Troncal', 9);
INSERT INTO ciudad VALUES (204, 'Suscal', 9);
INSERT INTO ciudad VALUES (205, 'Bolívar', 3);
INSERT INTO ciudad VALUES (206, 'Espejo', 3);
INSERT INTO ciudad VALUES (207, 'Mira', 3);
INSERT INTO ciudad VALUES (208, 'San Pedro de Huaca', 3);
INSERT INTO ciudad VALUES (209, 'Alausí', 8);
INSERT INTO ciudad VALUES (210, 'Chambo', 8);
INSERT INTO ciudad VALUES (211, 'Chunchi', 8);
INSERT INTO ciudad VALUES (212, 'Colta', 8);
INSERT INTO ciudad VALUES (213, 'Cumandá', 8);
INSERT INTO ciudad VALUES (215, 'Pallatanga', 8);
INSERT INTO ciudad VALUES (216, 'Penipe', 8);
INSERT INTO ciudad VALUES (217, 'Guamote', 8);
INSERT INTO ciudad VALUES (360, 'La Maná', 5);
INSERT INTO ciudad VALUES (361, 'Pangua', 5);
INSERT INTO ciudad VALUES (362, 'Salcedo', 5);
INSERT INTO ciudad VALUES (363, 'Saquisilí', 5);
INSERT INTO ciudad VALUES (364, 'Sigchos', 5);
INSERT INTO ciudad VALUES (365, 'Pujilí', 5);
INSERT INTO ciudad VALUES (366, 'Arenillas', 11);
INSERT INTO ciudad VALUES (367, 'Atahualpa', 11);
INSERT INTO ciudad VALUES (368, 'Balsas', 11);
INSERT INTO ciudad VALUES (218, 'Chilla', 11);
INSERT INTO ciudad VALUES (219, 'El Guabo', 11);
INSERT INTO ciudad VALUES (220, 'Huaquillas', 11);
INSERT INTO ciudad VALUES (221, 'Las Lajas', 11);
INSERT INTO ciudad VALUES (222, 'Marcabelí', 11);
INSERT INTO ciudad VALUES (223, 'Pasaje', 11);
INSERT INTO ciudad VALUES (224, 'Piñas', 11);
INSERT INTO ciudad VALUES (225, 'Portovelo', 11);
INSERT INTO ciudad VALUES (226, 'Santa Rosa', 11);
INSERT INTO ciudad VALUES (227, 'Zaruma', 11);
INSERT INTO ciudad VALUES (228, 'Atacames', 12);
INSERT INTO ciudad VALUES (229, 'Eloy Alfaro', 12);
INSERT INTO ciudad VALUES (230, 'Muisne', 12);
INSERT INTO ciudad VALUES (231, 'Quinindé', 12);
INSERT INTO ciudad VALUES (232, 'Río Verde', 12);
INSERT INTO ciudad VALUES (233, 'San Lorenzo', 12);
INSERT INTO ciudad VALUES (235, 'Isabela', 23);
INSERT INTO ciudad VALUES (236, 'San Cristóbal', 23);
INSERT INTO ciudad VALUES (237, 'Santa Cruz', 23);
INSERT INTO ciudad VALUES (238, 'Alfredo Baquerizo Moreno', 17);
INSERT INTO ciudad VALUES (239, 'Balao', 17);
INSERT INTO ciudad VALUES (240, 'Balzar', 17);
INSERT INTO ciudad VALUES (241, 'Colimes', 17);
INSERT INTO ciudad VALUES (242, 'Coronel Marcelino Maridueña', 17);
INSERT INTO ciudad VALUES (103, 'Guayaquil', 17);
INSERT INTO ciudad VALUES (104, 'Portoviejo', 14);
INSERT INTO ciudad VALUES (105, 'Loja', 2);
INSERT INTO ciudad VALUES (106, 'Tena', 24);
INSERT INTO ciudad VALUES (107, 'Manta', 14);
INSERT INTO ciudad VALUES (108, 'Ibarra', 4);
INSERT INTO ciudad VALUES (110, 'Machala', 11);
INSERT INTO ciudad VALUES (112, 'Ambato', 6);
INSERT INTO ciudad VALUES (113, 'Riobamba', 8);
INSERT INTO ciudad VALUES (114, 'Quevedo', 15);
INSERT INTO ciudad VALUES (115, 'Milagro', 17);
INSERT INTO ciudad VALUES (116, 'Esmeraldas', 12);
INSERT INTO ciudad VALUES (117, 'La Libertad', 16);
INSERT INTO ciudad VALUES (118, 'Babahoyo', 15);
INSERT INTO ciudad VALUES (119, 'Latacunga', 5);
INSERT INTO ciudad VALUES (121, 'Pasaje', 11);
INSERT INTO ciudad VALUES (122, 'Chone', 14);
INSERT INTO ciudad VALUES (123, 'Santa Rosa', 11);
INSERT INTO ciudad VALUES (124, 'Huaquillas', 11);
INSERT INTO ciudad VALUES (125, 'Nueva Loja', 18);
INSERT INTO ciudad VALUES (126, 'El Carmen', 14);
INSERT INTO ciudad VALUES (127, 'Jipijapa', 14);
INSERT INTO ciudad VALUES (128, 'Ventanas', 15);
INSERT INTO ciudad VALUES (129, 'Daule', 17);
INSERT INTO ciudad VALUES (130, 'Cayambe', 1);
INSERT INTO ciudad VALUES (131, 'Otavalo', 4);
INSERT INTO ciudad VALUES (132, 'Velasco Ibarra', 1);
INSERT INTO ciudad VALUES (133, 'Azogues', 9);
INSERT INTO ciudad VALUES (134, 'Santa Elena', 16);
INSERT INTO ciudad VALUES (135, 'Salinas', 16);
INSERT INTO ciudad VALUES (136, 'La Troncal', 9);
INSERT INTO ciudad VALUES (137, 'Buena Fé', 15);
INSERT INTO ciudad VALUES (138, 'Durán', 17);
INSERT INTO ciudad VALUES (139, 'Las Naves', 7);
INSERT INTO ciudad VALUES (141, 'Shushufindi', 18);
INSERT INTO ciudad VALUES (142, 'Zamora Chinchipe', 22);
INSERT INTO ciudad VALUES (144, 'Orellana', 19);
INSERT INTO ciudad VALUES (145, 'Francisco de Orellana', 19);
INSERT INTO ciudad VALUES (146, 'Bolivar', 7);
INSERT INTO ciudad VALUES (147, 'Biblian', 9);
INSERT INTO ciudad VALUES (148, 'Guano', 8);
INSERT INTO ciudad VALUES (149, 'Montalvo', 15);
INSERT INTO ciudad VALUES (150, 'Azuay', 10);
INSERT INTO ciudad VALUES (151, 'Cañar', 9);
INSERT INTO ciudad VALUES (153, 'Chimborazo', 8);
INSERT INTO ciudad VALUES (154, 'Cotopaxi', 5);
INSERT INTO ciudad VALUES (155, 'El Oro', 11);
INSERT INTO ciudad VALUES (156, 'Galapagos', 23);
INSERT INTO ciudad VALUES (157, 'Guaranda', 7);
INSERT INTO ciudad VALUES (158, 'Guayas', 17);
INSERT INTO ciudad VALUES (159, 'Imbabura', 4);
INSERT INTO ciudad VALUES (160, 'Macas', 21);
INSERT INTO ciudad VALUES (161, 'Manabí', 14);
INSERT INTO ciudad VALUES (162, 'Mejia', 1);
INSERT INTO ciudad VALUES (163, 'Napo', 24);
INSERT INTO ciudad VALUES (164, 'Pastaza', 20);
INSERT INTO ciudad VALUES (166, 'Puerto Baquerizo Moreno', 23);
INSERT INTO ciudad VALUES (167, 'Puerto Francisco de Orellana', 19);
INSERT INTO ciudad VALUES (168, 'Puyo', 20);
INSERT INTO ciudad VALUES (170, 'Sucumbios', 18);
INSERT INTO ciudad VALUES (171, 'Tungurahua', 6);
INSERT INTO ciudad VALUES (172, 'Zamora', 22);
INSERT INTO ciudad VALUES (173, 'Carchi', 3);
INSERT INTO ciudad VALUES (101, 'Quito', 1);
INSERT INTO ciudad VALUES (244, 'Eloy Alfaro', 17);
INSERT INTO ciudad VALUES (245, 'El Empalme', 17);
INSERT INTO ciudad VALUES (111, 'Sangolquí', 1);
INSERT INTO ciudad VALUES (120, 'Tulcán', 3);
INSERT INTO ciudad VALUES (143, 'Los Ríos', 15);
INSERT INTO ciudad VALUES (246, 'El Triunfo', 17);
INSERT INTO ciudad VALUES (169, 'Santo Domingo de los Tsáchilas', 25);
INSERT INTO ciudad VALUES (247, 'Bucay', 17);
INSERT INTO ciudad VALUES (248, 'Isidro Ayora', 17);
INSERT INTO ciudad VALUES (249, 'Lomas de Sargentillo', 17);
INSERT INTO ciudad VALUES (251, 'Naranjal', 17);
INSERT INTO ciudad VALUES (252, 'Naranjito', 17);
INSERT INTO ciudad VALUES (253, 'Nobol', 17);
INSERT INTO ciudad VALUES (254, 'Palestina', 17);
INSERT INTO ciudad VALUES (255, 'Pedro Carbo', 17);
INSERT INTO ciudad VALUES (256, 'Playas', 17);
INSERT INTO ciudad VALUES (257, 'Samborondón', 17);
INSERT INTO ciudad VALUES (258, 'Salitre', 17);
INSERT INTO ciudad VALUES (259, 'San Jacinto de Yaguachi', 17);
INSERT INTO ciudad VALUES (260, 'Santa Lucía', 17);
INSERT INTO ciudad VALUES (261, 'Simón Bolívar', 17);
INSERT INTO ciudad VALUES (262, 'Antonio Ante', 4);
INSERT INTO ciudad VALUES (263, 'Cotacachi', 4);
INSERT INTO ciudad VALUES (264, 'Otavalo', 4);
INSERT INTO ciudad VALUES (265, 'Pimampiro', 4);
INSERT INTO ciudad VALUES (266, 'San Miguel de Urcuquí', 4);
INSERT INTO ciudad VALUES (267, 'Calvas', 2);
INSERT INTO ciudad VALUES (268, 'Catamayo', 2);
INSERT INTO ciudad VALUES (269, 'Celica', 2);
INSERT INTO ciudad VALUES (270, 'Chaguarpamba', 2);
INSERT INTO ciudad VALUES (271, 'Espíndola', 2);
INSERT INTO ciudad VALUES (272, 'Gonzanamá', 2);
INSERT INTO ciudad VALUES (273, 'Macará', 2);
INSERT INTO ciudad VALUES (274, 'Paltas', 2);
INSERT INTO ciudad VALUES (275, 'Pindal', 2);
INSERT INTO ciudad VALUES (276, 'Puyango', 2);
INSERT INTO ciudad VALUES (277, 'Quilanga', 2);
INSERT INTO ciudad VALUES (278, 'Saraguro', 2);
INSERT INTO ciudad VALUES (279, 'Sozoranga', 2);
INSERT INTO ciudad VALUES (280, 'Zapotillo', 2);
INSERT INTO ciudad VALUES (281, 'Baba', 15);
INSERT INTO ciudad VALUES (282, 'Buena Fe', 15);
INSERT INTO ciudad VALUES (283, 'Mocache', 15);
INSERT INTO ciudad VALUES (284, 'Montalvo', 15);
INSERT INTO ciudad VALUES (285, 'Palenque', 15);
INSERT INTO ciudad VALUES (286, 'Pueblo Viejo', 15);
INSERT INTO ciudad VALUES (287, 'Quevedo', 15);
INSERT INTO ciudad VALUES (288, 'Urdaneta', 15);
INSERT INTO ciudad VALUES (289, 'Ventanas', 15);
INSERT INTO ciudad VALUES (290, 'Vinces', 15);
INSERT INTO ciudad VALUES (369, 'Valencia', 15);
INSERT INTO ciudad VALUES (291, 'Bolívar', 14);
INSERT INTO ciudad VALUES (292, 'Chone', 14);
INSERT INTO ciudad VALUES (293, 'El Carmen', 14);
INSERT INTO ciudad VALUES (294, 'Flavio Alfaro', 14);
INSERT INTO ciudad VALUES (295, 'Jama', 14);
INSERT INTO ciudad VALUES (296, 'Jaramijó', 14);
INSERT INTO ciudad VALUES (297, 'Jipijapa', 14);
INSERT INTO ciudad VALUES (298, 'Junín', 14);
INSERT INTO ciudad VALUES (299, 'Manta', 14);
INSERT INTO ciudad VALUES (300, 'Montecristi', 14);
INSERT INTO ciudad VALUES (301, 'Olmedo', 14);
INSERT INTO ciudad VALUES (302, 'Paján', 14);
INSERT INTO ciudad VALUES (303, 'Pedernales', 14);
INSERT INTO ciudad VALUES (304, 'Pichincha', 14);
INSERT INTO ciudad VALUES (305, 'Portoviejo', 14);
INSERT INTO ciudad VALUES (306, 'Puerto Lopéz', 14);
INSERT INTO ciudad VALUES (307, 'Rocafuerte', 14);
INSERT INTO ciudad VALUES (308, 'San Vicente', 14);
INSERT INTO ciudad VALUES (371, 'Santa Ana', 14);
INSERT INTO ciudad VALUES (372, 'Sucre', 14);
INSERT INTO ciudad VALUES (373, 'Tosagua', 14);
INSERT INTO ciudad VALUES (374, 'Veinticuatro de Mayo', 14);
INSERT INTO ciudad VALUES (309, 'Gualaquiza', 21);
INSERT INTO ciudad VALUES (310, 'Huamboya', 21);
INSERT INTO ciudad VALUES (311, 'Limón Indanza', 21);
INSERT INTO ciudad VALUES (312, 'Logroño', 21);
INSERT INTO ciudad VALUES (314, 'Pablo Sexto', 21);
INSERT INTO ciudad VALUES (315, 'Palora', 21);
INSERT INTO ciudad VALUES (316, 'San Juan Bosco', 21);
INSERT INTO ciudad VALUES (317, 'Santiago', 21);
INSERT INTO ciudad VALUES (318, 'Sucúa', 21);
INSERT INTO ciudad VALUES (319, 'Taisha', 21);
INSERT INTO ciudad VALUES (320, 'Tiwintza', 21);
INSERT INTO ciudad VALUES (321, 'Archidona', 24);
INSERT INTO ciudad VALUES (322, 'Carlos Julio Arosemena Tola', 24);
INSERT INTO ciudad VALUES (323, 'El Chaco', 24);
INSERT INTO ciudad VALUES (324, 'Quijos', 24);
INSERT INTO ciudad VALUES (325, 'Aguarico', 19);
INSERT INTO ciudad VALUES (326, 'Joya de los Sachas', 19);
INSERT INTO ciudad VALUES (327, 'Loreto', 19);
INSERT INTO ciudad VALUES (328, 'Arajuno', 20);
INSERT INTO ciudad VALUES (329, 'Mera', 20);
INSERT INTO ciudad VALUES (330, 'Santa Clara', 20);
INSERT INTO ciudad VALUES (332, 'Mejía', 1);
INSERT INTO ciudad VALUES (333, 'Pedro Moncayo', 1);
INSERT INTO ciudad VALUES (334, 'Pedro Vicente Maldonado', 1);
INSERT INTO ciudad VALUES (335, 'Puerto Quito', 1);
INSERT INTO ciudad VALUES (336, 'Rumiñahui', 1);
INSERT INTO ciudad VALUES (337, 'San Miguel de los Bancos', 1);
INSERT INTO ciudad VALUES (339, 'Cascales', 18);
INSERT INTO ciudad VALUES (340, 'Cuyabeno', 18);
INSERT INTO ciudad VALUES (341, 'Gonzalo Pizarro', 18);
INSERT INTO ciudad VALUES (342, 'Lago Agrio', 18);
INSERT INTO ciudad VALUES (343, 'Putumayo', 18);
INSERT INTO ciudad VALUES (344, 'Baños', 6);
INSERT INTO ciudad VALUES (345, 'Cevallos', 6);
INSERT INTO ciudad VALUES (346, 'Mocha', 6);
INSERT INTO ciudad VALUES (347, 'Patate', 6);
INSERT INTO ciudad VALUES (348, 'Pelileo', 6);
INSERT INTO ciudad VALUES (349, 'Píllaro', 6);
INSERT INTO ciudad VALUES (350, 'Quero', 6);
INSERT INTO ciudad VALUES (351, 'Tisaleo', 6);
INSERT INTO ciudad VALUES (352, 'Centinela del Cóndor', 22);
INSERT INTO ciudad VALUES (353, 'Chinchipe', 22);
INSERT INTO ciudad VALUES (354, 'El Pangui', 22);
INSERT INTO ciudad VALUES (355, 'Nangaritza', 22);
INSERT INTO ciudad VALUES (356, 'Palanda', 22);
INSERT INTO ciudad VALUES (357, 'Paquisha', 22);
INSERT INTO ciudad VALUES (358, 'Yacuambi', 22);
INSERT INTO ciudad VALUES (359, 'Yantzaza', 22);
INSERT INTO ciudad VALUES (234, 'La Concordia', 13);
INSERT INTO ciudad VALUES (140, 'Morona Santiago', 21);
INSERT INTO ciudad VALUES (109, 'Santo Domingo de los Tsáchilas', 13);
INSERT INTO ciudad VALUES (102, 'Cuenca', 10);

--  tabla estadocivil columnas id descripcion
INSERT INTO estadocivil VALUES (1, 'Soltero');
INSERT INTO estadocivil VALUES (2, 'Casado');
INSERT INTO estadocivil VALUES (3, 'Divorciado');
INSERT INTO estadocivil VALUES (4, 'Unión Libre');
INSERT INTO estadocivil VALUES (5, 'Viudo');

-- tabla nivel de educacion columnas id, descripcion, nombre
INSERT INTO niveleducacion VALUES (1, 'Primaria', 'Primaria');
INSERT INTO niveleducacion VALUES (2, 'Secundaria', 'Secundaria');
INSERT INTO niveleducacion VALUES (3, 'Tercer Nivel', 'Tercer Nivel');
INSERT INTO niveleducacion VALUES (4, 'Cuarto Nivel', 'Cuarto Nivel');

-- tabla nivel de genero columnas id, nombre
INSERT INTO genero VALUES (1,'MASCULINO');
INSERT INTO genero VALUES (2,'FEMENINO');
INSERT INTO genero VALUES (3,'LGBTI');

-- tabla etnia columnas id, nombre
INSERT INTO etnia VALUES (1,'Mestizo');
INSERT INTO etnia VALUES (2,'Indígena');
INSERT INTO etnia VALUES (3,'Afroecuatoriano');
INSERT INTO etnia VALUES (4,'Montubio');
INSERT INTO etnia VALUES (5,'Blanco');

-- tabla tipo requerimiento columnas id, nombre
INSERT INTO tiporrequerimiento VALUES (1,'DENUNCIA');
INSERT INTO tiporrequerimiento VALUES (2,'PEDIDO');
