function handleFileSelect(evt) {
    var group_photo = evt.target.files;
    var gp = group_photo[0];

    if (!gp.type.match('image.*')) {
        alert("Image only please....");
    }
    var reader = new FileReader();

    reader.onload = (function(theFile) {
        return function(e) {

            var span = document.createElement('span');
            span.innerHTML = ['<img class="thumb" width="350" title="', escape(theFile.name), '" src="', e.target.result, '" />'].join('');
            document.getElementById('output').insertBefore(span, null);
        };
    })(gp);

    reader.readAsDataURL(gp);
}
document.getElementById('id_group_photo').addEventListener('change', handleFileSelect, false);



