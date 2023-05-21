# masxmenos


# Universidad del Norte


### Integrantes
- Aaron Cabrales Contreras
- Juan Pablo Guzman Restrepo
- Juan Miguel González Pérez
- Julian Alberto Florez Meyer

Barranquilla, Colombia
Mayo – 2023
# Introducción

En tiempos recientes, se ha observado un aumento en la popularidad de múltiples cadenas de supermercados en el país, lo cual ha generado diversos cambios en los hábitos de compra de las personas. Uno de los desafíos más significativos que ha surgido es la determinación del establecimiento con el precio más competitivo. Sin embargo, elegir una cadena simplemente en base a su economía no siempre resulta una tarea sencilla, ya que una cadena de supermercados no necesariamente superará a otra en todos los aspectos de precios. A menudo, aquellos que organizan cuidadosamente sus gastos y visitan diferentes tiendas se percatan de que ninguna cadena se mantiene consistentemente más barata que las demás en todos los productos. Por lo tanto, el objetivo de este proyecto consiste en desarrollar una solución que permita identificar qué tienda ofrece el mejor precio para cada producto.

La empresa ColEcono propone el desarrollo de la aplicación "MasxMenos". Esta aplicación permitirá a los usuarios comparar los precios de diversos productos en una amplia variedad de tiendas, recibiendo una actualización constante de los mismos y asegurándose de no perderse los mejores precios en las principales cadenas de supermercados a nivel nacional.

## Metodología

La metodología utilizada en el desarrollo de la aplicación "MasxMenos" se basó en un enfoque iterativo e incremental, que permitió un desarrollo eficiente y adaptativo. A continuación, se detallan las etapas principales del proceso de desarrollo:

1. Análisis de requerimientos: Se realizó un estudio detallado de los requerimientos funcionales y no funcionales de la aplicación, estableciendo los objetivos y alcances del proyecto.

2. Diseño de la arquitectura: Se definió la estructura de la aplicación, incluyendo la selección de tecnologías y frameworks adecuados para su implementación.

3. Desarrollo del backend: Se implementó la lógica de negocio y las funcionalidades principales de la aplicación utilizando el lenguaje de programación Python y el framework Django.

4. Desarrollo del frontend: Se creó la interfaz de usuario utilizando HTML, CSS y JavaScript, asegurando una experiencia de usuario intuitiva y atractiva.

5. Pruebas y depuración: Se llevaron a cabo pruebas exhaustivas para identificar y corregir cualquier error o fallo en la aplicación, garantizando su correcto funcionamiento.

6. Despliegue y lanzamiento: Se configuró un entorno de producción para la aplicación y se realizó su despliegue en un servidor web, asegurando su accesibilidad para los usuarios.

7. Mantenimiento y mejoras: Se estableció un plan de mantenimiento continuo para la aplicación, incluyendo la implementación de actualizaciones y mejoras basadas en la retroalimentación de los usuarios.

La metodología utilizada permitió un desarrollo ágil y eficiente de la aplicación "MasxMenos", asegurando la entrega de un producto de calidad que cumple con los requerimientos establecidos.

## Requerimientos Funcionales

- Mostrar un listado completo de todos los productos disponibles en cada tienda.
- Actualizar los precios de los productos de manera regular para brindar información actualizada.
- Generar una lista de los productos más económicos en cada categoría, permitiendo al usuario encontrar fácilmente las mejores ofertas.
- Implementar un carrito de compra que permita al usuario seleccionar y organizar los productos deseados para facilitar su proceso de compra.

## Requerimientos No Funcionales

- Diseñar una interfaz de usuario intuitiva y estéticamente agradable que brinde una experiencia de uso agradable.
- Garantizar la integridad y precisión de la información de los productos, evitando cualquier tipo de falla o inconsistencia en los datos.
- Asegurar la disponibilidad y accesibilidad de la aplicación para los usuarios, minimizando los tiempos de carga y ofreciendo un alto rendimiento.

# Diagrama de Clases UML

Para la creación de esta aplicación, se elaboró un diagrama de clases con el objetivo de lograr una organización eficiente durante la implementación del aplicativo web. A continuación, se presenta el diagrama UML correspondiente:

[![Whats-App-Image-2023-05-20-at-7-11-41-PM.jpg](https://i.postimg.cc/6pMFzh5V/Whats-App-Image-2023-05-20-at-7-11-41-PM.jpg)](https://postimg.cc/tsVr4W67)

# Implementación y tecnologías relevantes en la implementación

## Aplicativo Web
Este proyecto consiste en el desarrollo de un aplicativo web que permite a los usuarios ver los precios en cada tienda y generar un comparativo entre ellos. Además, brinda la opción de añadir productos a un listado organizado en un carrito de compra.

## Tecnologías Utilizadas
Durante la implementación de este aplicativo web, se utilizaron las siguientes tecnologías:

- [**Python**](https://docs.python.org/3/reference/index.html): Uno de los lenguajes más utilizados a la hora de hacer Scripts. En este proyecto, se aprovechó su flexibilidad y las numerosas librerías disponibles para hacer Web Scraping, lo que nos permitió recolectar la información de las páginas de las diferentes tiendas objetivo para la comparación.

- **Selenium**: Una herramienta que permite manejar páginas web con un headless browser. Fue utilizada para interactuar con el contenido dinámico de las tiendas en línea y extraer la información necesaria.

- **Requests**: Una librería de Python que facilita la realización de peticiones HTTP. Se utilizó para obtener los datos de las páginas web de las tiendas y acceder a la información de precios y productos.

- [**Django**](https://docs.djangoproject.com/): Un framework potente para el desarrollo web con Python. Se eligió debido a su amplia documentación, herramientas integradas y una comunidad de desarrolladores activa que brinda soporte y recursos adicionales.

Estas tecnologías fueron seleccionadas cuidadosamente para garantizar una implementación eficiente y efectiva del aplicativo web "MasxMenos".

# Resultados
Se presentarán los resultados obtenidos a lo largo del desarrollo de la aplicación Web “MasxMenos” en lo que al apartado visual e interfaz de usuario se refiere:

### Registro

[![registro.jpg](https://i.postimg.cc/DzZ0Y5Q7/registro.jpg)](https://postimg.cc/PCgdCWF7)
Al momento de iniciar la aplicación web, se requiere iniciar sesión. Por lo tanto, si el usuario no cuenta con una sesión previa en nuestra aplicación, es importante realizar el proceso de *“registro”* para crear una cuenta.

### Inicio de sesión

[![inicio-sesion.jpg](https://i.postimg.cc/nhMfyWWS/inicio-sesion.jpg)](https://postimg.cc/75vR7KwS)
Una vez creada la cuenta, es posible acceder a *“iniciar sesión”* utilizando los datos proporcionados durante el proceso de registro.

### Inicio

[![menu.jpg](https://i.postimg.cc/xdHhYV35/menu.jpg)](https://postimg.cc/mcL8Nqq1)
La pestaña de *“inicio”* es la sección principal de la página web, donde los usuarios pueden familiarizarse con "MasxMenos" y obtener información completa sobre el funcionamiento de la aplicación y sus beneficios.

### Listado de productos

[![Listado-de-productos.jpg](https://i.postimg.cc/QxwfMnty/Listado-de-productos.jpg)](https://postimg.cc/fJ7c2CYc)
La sección de *“listado de productos”* brinda al usuario la posibilidad de acceder a una amplia variedad de productos disponibles en múltiples tiendas de cadena de forma simultánea. Esta pestaña ofrece opciones de filtrado por tipo de producto, tienda e incluso orden de precios, con el objetivo de facilitar la búsqueda y permitir al usuario añadir los productos deseados a un carrito.

### Carrito

[![carrito.jpg](https://i.postimg.cc/3rbBLbgx/carrito.jpg)](https://postimg.cc/JtZZ0x6f)
Para concluir, el usuario puede acceder a la pestaña *"Carrito"*, la cual le permite visualizar los productos previamente agregados y conocer el precio individual de cada uno, así como el precio total de su compra. En todo momento se mostrará la información correspondiente a la tienda a la que pertenecen los productos y el tipo de producto al que corresponden.

# Conclusiones

En vista de los resultados obtenidos, la aplicación web "MasxMenos" logra abordar la problemática planteada de manera efectiva. Esta aplicación cuenta con una amplia selección de tiendas de cadena, lo que le permite comparar una variedad extensa de productos. De esta forma, brinda a los usuarios la seguridad de obtener precios competitivos en relación con la competencia. "MasxMenos" se posiciona como una propuesta destacada en el sector de las aplicaciones, al ofrecer una solución a una pregunta común: ¿Dónde puedo encontrar un determinado producto al mejor precio? Esto le augura un futuro prometedor en comparación con otras aplicaciones similares.

Sin embargo, es importante mencionar que "MasxMenos" presenta ciertas limitaciones. Por ejemplo, no considera la ubicación geográfica del usuario ni la disponibilidad de productos en las tiendas cercanas, lo que impide conocer si el producto deseado está disponible en la tienda más cercana. Además, la aplicación no permite realizar compras directamente. Estas funcionalidades que actualmente no están disponibles se consideran para futuras actualizaciones, incluyendo la implementación de aplicaciones móviles a través de las tiendas virtuales [App Store](https://www.apple.com/app-store/) y [Play Store](https://play.google.com/store/games), respectivamente.

# Referencias bibliográficas

Sanchez. L.A(2019). El impacto de los establecimientos Hard Discount o tiendas de
descuento en el sector comercial de Colombia.Universidad de La Salle, Bogotá. Recuperado de: [https://ciencia.lasalle.edu.co/cgi/viewcontent.cgi?article=2592&context=administracion_de_empresas](https://ciencia.lasalle.edu.co/cgi/viewcontent.cgi?article=2592&context=administracion_de_empresas)

Python Software Foundation. (2021). The Python Language Reference. Recuperado de [https://docs.python.org/3/reference/index.html](https://docs.python.org/3/reference/index.html)

Django Software Foundation. (2021). Django documentation. Recuperado de [https://docs.djangoproject.com/](https://docs.djangoproject.com/)

McKinney, W., & Pandas Development Team. (2021). Pandas: Powerful data analysis toolkit. Recuperado de [https://pandas.pydata.org/docs/](https://pandas.pydata.org/docs/)

Crummy, L. (n.d.). BeautifulSoup Documentation. Recuperado de 
[https://www.crummy.com/software/BeautifulSoup/bs4/doc/](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

Gracias por su interés en *"MasxMenos"*
