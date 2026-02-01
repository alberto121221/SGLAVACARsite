/*Código para el boton tipo hamburguesa en disposivos móviles*/

document.addEventListener('DOMContentLoaded', () => {
    const burger = document.querySelector('.burger');
    const navLinks = document.querySelector('.nav-links');

    if (!burger || !navLinks) {
        console.error('Burger o nav-links no encontrados');
        return;
    }

    burger.addEventListener('click', () => {
        navLinks.classList.toggle('active');
        burger.classList.toggle('active');
        console.log('Burger clickeada'); // 👈 prueba
    });
});


    /* Loading del formulario SIN bloquear envío */
    const form = document.getElementById('contact-form');
    if (form) {
        form.addEventListener('submit', () => {
            const submitButton = form.querySelector('button[type="submit"]');
            submitButton.classList.add('loading');
            submitButton.disabled = true;
        });
    }



function showFlashMessage(message, category) {
    const flashContainer = document.getElementById('flash-messages');
    const flashMessage = document.createElement('div');
    flashMessage.className = `alert ${category}`;
    flashMessage.textContent = message;

    flashContainer.appendChild(flashMessage);

   
    setTimeout(() => {
        flashMessage.remove();
    }, 5000);
}