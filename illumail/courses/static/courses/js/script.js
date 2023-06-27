function handleFileSelect(evt) {
    var course_photo = evt.target.files;
    var cp = course_photo[0];

    if (!cp.type.match('image.*')) {
        alert("Image only please....");
    }
    var reader = new FileReader();

    reader.onload = (function(theFile) {
        return function(e) {

            var span = document.createElement('span');
            span.innerHTML = ['<img class="thumb" width="350" title="', escape(theFile.name), '" src="', e.target.result, '" />'].join('');
            document.getElementById('output').insertBefore(span, null);
        };
    })(cp);

    reader.readAsDataURL(cp);
}
document.getElementById('id_course_photo').addEventListener('change', handleFileSelect, false);


document.getElementById('public').onclick = function() {
      document.getElementById('text2').hidden = true;
    }
document.getElementById('paid').onclick = function() {
      document.getElementById('text2').hidden = false;
    }



/* DROPDOWN */

const dropdowns = document.querySelectorAll('.dropdown');
dropdowns.forEach(dropdown => {
    const select = dropdown.querySelector('.select');
    const caret = dropdown.querySelector('.caret');
    const menu = dropdown.querySelector('.menu');
    const options = dropdown.querySelectorAll('.menu li');
    const selected = dropdown.querySelector('.selected');

    selected.addEventListener('click', () => {
        select.classList.toggle('select-clicked');
        caret.classList.toggle('caret-rotate');
        menu.classList.toggle('menu-open');
    });

    options.forEach(option => {
        option.addEventListener('click', () => {
            selected.innerText = option.innerText;
            select.classList.remove('select-clicked');
            caret.classList.remove('caret-rotate');
            menu.classList.remove('menu-open');
            option.forEach(option => {
                option.classList.remove('active');
            });
            option.classList.add('active');
        });
    });
});