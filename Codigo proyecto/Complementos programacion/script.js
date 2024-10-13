document.addEventListener('DOMContentLoaded', () => {
    const productos = [{
            nombre: 'Marranos de tiesto',
            imagen: 'imagenes/producto1.jpg',
            descripcion: 'Objeto decorado de diferentes tipos',
            telefono: '123456789',
            lugar: 'Raquira',
            correo: 'vendedor1@correo.com',
            vendedor: 'Vendedor 1'
        },
        {
            nombre: 'Hamacas',
            imagen: 'imagenes/producto2.jpg',
            descripcion: 'Objeto para descansar, tejido a mano',
            telefono: '987654321',
            lugar: 'Raquira',
            correo: 'vendedor2@correo.com',
            vendedor: 'Vendedor 2'
        },
        // Añade más productos aquí
    ];

    // Mostrar detalles del producto
    const params = new URLSearchParams(window.location.search);
    const nombreProducto = params.get('nombre');
    const productoEncontrado = productos.find(producto => producto.nombre === nombreProducto);

    if (productoEncontrado) {
        document.getElementById('nombreProducto').innerText = productoEncontrado.nombre;
        document.getElementById('imagenProducto').src = productoEncontrado.imagen;
        document.getElementById('descripcionProducto').innerText = productoEncontrado.descripcion;
        document.getElementById('vendedorProducto').innerText = `Vendedor: ${productoEncontrado.vendedor}`;
        document.getElementById('telefonoProducto').innerText = `Teléfono: ${productoEncontrado.telefono}`;
        document.getElementById('lugarProducto').innerText = `Lugar: ${productoEncontrado.lugar}`;
        document.getElementById('correoProducto').innerText = `Correo: ${productoEncontrado.correo}`;
    } else {
        document.getElementById('detalleProducto').innerText = 'Producto no encontrado.';
    }
});