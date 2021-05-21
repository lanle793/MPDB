var poster = document.getElementById("poster"),
    preview = document.getElementById("preview");
    
poster.addEventListener("change", function() {
    displayImage(this);
});

function displayImage(input) {
    var reader;

    if (input.files && input.files[0]) {
        reader = new FileReader();

        reader.onload = function(e) {
            preview.setAttribute('src', e.target.result);
        }

        reader.readAsDataURL(input.files[0]);
    }
}