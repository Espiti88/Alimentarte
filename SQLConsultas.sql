use parcialalimentarte;

/*1) Listado de Clientes*/

SELECT nombre AS Nombre, telefono AS Teléfono, correo AS Correo
FROM clientes
ORDER BY nombre;

/*2) Listado de Platos que contengan la palabra "Arroz" en su descripción*/

SELECT platos.nombre AS Nombre, platos.descripcion AS Descripción, restaurantes.nombre AS Restaurante
FROM (platos INNER JOIN restaurantes
ON restaurantes.idRestaurante = platos.restaurante)
WHERE platos.descripcion LIKE '%Arroz%'
ORDER BY platos.nombre;

/*3) Menú de la Feria*/

SELECT platos.nombre AS Nombre, platos.descripcion AS Descripción, restaurantes.nombre AS Restaurante, platos.precio AS Precio
FROM (platos INNER JOIN restaurantes
ON restaurantes.idRestaurante = platos.restaurante)
ORDER BY platos.nombre;

/*4) Listado de Restaurantes*/

SELECT categorias.nombre AS Categoría, restaurantes.nombre AS Restaurante
FROM (categorias INNER JOIN restaurantes
ON categorias.idCategoria = restaurantes.categoria)
ORDER BY categorias.nombre;

/*5) Listado de Compras*/

SELECT pedidos.fecha_hora AS Fecha, clientes.nombre AS Cliente, platos.nombre AS Plato, platos.precio AS Costo
FROM (pedidos INNER JOIN clientes
ON pedidos.idCliente = clientes.idCliente) INNER JOIN platos
ON pedidos.idPlato = platos.idPlato
ORDER BY pedidos.fecha_hora;