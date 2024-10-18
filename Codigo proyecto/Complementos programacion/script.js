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
    ];

    const productContainer = document.getElementById('productContainer');
    const buscador = document.getElementById('buscador');

    function mostrarProductos(productosFiltrados) {
        productContainer.innerHTML = '';
        productosFiltrados.forEach(producto => {
            const productElement = document.createElement('div');
            productElement.classList.add('product');
            productElement.innerHTML = `
                <img src="${producto.imagen}" alt="${producto.nombre}">
                <h2>${producto.nombre}</h2>
                <p>${producto.descripcion}</p>
                <button class="detalle-btn">Más Detalles</button>
                <div class="detalles-producto" style="display: none;">
                    <p>Vendedor: ${producto.vendedor}</p>
                    <p>Teléfono: ${producto.telefono}</p>
                    <p>Lugar: ${producto.lugar}</p>
                    <p>Correo: ${producto.correo}</p>
                </div>
            `;

            const detalleBtn = productElement.querySelector('.detalle-btn');
            const detallesProducto = productElement.querySelector('.detalles-producto');

            detalleBtn.addEventListener('click', () => {
                if (detallesProducto.style.display === 'none') {
                    detallesProducto.style.display = 'block';
                    detalleBtn.textContent = 'Ocultar Detalles';
                } else {
                    detallesProducto.style.display = 'none';
                    detalleBtn.textContent = 'Más Detalles';
                }
            });

            productContainer.appendChild(productElement);
        });
    }

    buscador.addEventListener('input', (e) => {
        const texto = e.target.value.toLowerCase();
        const productosFiltrados = productos.filter(producto =>
            producto.nombre.toLowerCase().includes(texto) ||
            producto.descripcion.toLowerCase().includes(texto)
        );
        mostrarProductos(productosFiltrados);
    });

    mostrarProductos(productos);
});