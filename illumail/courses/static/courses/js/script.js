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
