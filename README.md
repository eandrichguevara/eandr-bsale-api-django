<h2>Inicio</h2>
<p>Esta solución consiste en el desarrollo de una API (Back-End), para el desarrollo de esta se utilizo Django, la cual debe consultar una base de datos MySql proporcionada por BSale en conjunto con una Applicacion Web (Front-End) desarrollada con vanilla javascript y compañado de Bootstrap para mejorar la UI.</p>
<p>El despliegue de la API se hizo con Heroku, fue desplegada en el siguiente <a href="https://radiant-wave-78267.herokuapp.com/api/products">link</a> </p>
<p>El despliegue del Front-End se realizo con Netlify, desplegandose en el siguiente <a href="https://starlit-licorice-628a63.netlify.app"></a></p>

<h2>API</h2>
<p>La API creada cuenta con 4 endpoints.</p>
<ul>
    <li>
        <strong>GET:</strong> 
        <span>/api/categories/</span>
        <p>Este endpoint nos devuelve un json con todas las categorias en la DB.</p>
    </li>
    <li>
        <strong>GET:</strong> 
        <span>/api/products/</span>
        <p>Este endpoint nos devuelve un json con todas los productos en la DB.</p>
    </li>
    <li>
        <strong>GET:</strong> 
        <span>/api/products/category/*id</span>
        <p>* 'id' es una variable de tipo entero, representa la columna category_id de la tabla product en la DB.</p>
        <p>Este endpoint nos devuelve un json con todas los productos en la DB filtrados por category_id.</p>
    </li>
    <li>
        <strong>GET:</strong> 
        <span>/api/search/*search</span>
        <p>* 'search' es una variable de tipo string, esta variable se compara con la columna name de la tabla product en la DB.</p>
        <p>Este endpoint nos devuelve un json con todas los productos en la DB filtrados por las coincidencias encontradas en la columna name.</p>
    </li>
</ul>

<h2>Aplicacion Web</h2>
<p>El Front_End cuenta con una UI simple creada principalmente con Bootstrap.</p>
<ul>
    <li>
        <p>Contiene una barra de navegacion que cuenta con un buscador que compara la el texto ingresado con las coincidencias en los nombres de los produtos.</p>
    </li>
    <li>
        <p>Debajo de la barra de navegacion nos encontramos con un filtro por categoria.</p>
        <ul>
            <li>
                <p>Al hacer click sobre el se despliega un menu con las categorias disponibles para filtrar.</p>
            </li>
        </ul>
    </li>
    <li>
        <p>Posee un despliegue de productos simple.</p>
        <ul>
            <li>
                <p>Los productos se presentan en una tarjeta que incluye su nombre, precio y un boton para comprar.</p>
            </li>
        </ul>
    </li>
</ul>