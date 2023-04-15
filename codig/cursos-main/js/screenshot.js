function myAlert(icon_alert, title_alert, text_alert) {
    Swal.fire({
        icon: icon_alert,
        title: title_alert,
        text: text_alert,
        backdrop: true,
        allowOutsideClick: false,
        allowEscapeKey: false
    });
}

/** PERSONALIZACION DE CONSOLA ANTE ACCESO DE HERRAMIENTAS PARA DESARROLLADOR (F12) **/

/** PARA DESHABILITAR CLIC DERECHO **/
document.oncontextmenu = function() {
    myAlert('warning', 'Clic derecho deshabilitado!', 'Trabajamos en mejorar el nivel de seguridad de nuestro sitio.');
    return false;
};

/** PARA DESHABILITAR CAPTURA DE PANTALLA **/
document.addEventListener('keyup', (e) => {
    if (e.key == 'PrintScreen') {
        navigator.clipboard.writeText('');
        myAlert('error', 'Capturas de pantalla deshabilitadas!', 'Solicitamos no intentarlo de nuevo o su acceso será interrumpido y reportado');
    }
});

/** PARA DESHABILITAR IMPRESIONES o EXPORTAR A PDF CON EL COMANDO (CTRL+P) Y DESHABILITAR RECORTES DE PANTALLA (CTRL+SHIFT+S)**/
document.addEventListener('keydown', (e) => {
    if (e.ctrlKey && e.key == 'p') {
        myAlert('error', 'Esta sección no se permite imprimir o exportar en PDF', 'Solicitamos no intentarlo de nuevo o su acceso será interrumpido y reportado');
        e.cancelBubble = true;
        e.preventDefault();
        e.stopImmediatePropagation();
    } else if (e.metaKey && e.shiftKey) {
        Swal.fire({
            imageUrl: 'https://www.soy502.com/sites/default/files/styles/full_node/public/2018/Mar/08/screen_shot_2018-03-08_at_7.31.17_am.png',
            imageAlt: 'imagen de así te queria agarrar puerco',
            imageWidth: '50%',
            title: 'Recortes de pantalla detectados!',
            text: 'Solicitamos no intentarlo de nuevo o su acceso será interrumpido y reportado',
            backdrop: true,
            allowOutsideClick: false,
            allowEscapeKey: false,
            width: '90%'
        });
    }
});