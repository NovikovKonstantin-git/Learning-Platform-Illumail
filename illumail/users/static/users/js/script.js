function handleFileSelect(evt) {
    var photo = evt.target.files;
    var p = photo[0];

    if (!p.type.match('image.*')) {
        alert("Image only please....");
    }
    var reader = new FileReader();

    reader.onload = (function(theFile) {
        return function(e) {

            var span = document.createElement('span');
            span.innerHTML = ['<img class="thumb" width="200" title="', escape(theFile.name), '" src="', e.target.result, '" />'].join('');
            document.getElementById('output').insertBefore(span, null);
        };
    })(p);

    reader.readAsDataURL(p);
}
document.getElementById('id_photo').addEventListener('change', handleFileSelect, false);



