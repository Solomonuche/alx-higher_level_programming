$(document).ready(function () {
    function fetchTranslation() {
        $.ajax({
            url: 'https://www.fourtonfish.com/hellosalut/hello/',
            data: {'data': $('INPUT#language_code').val()},
            success: function (data) {
                $('DIV#hello').text(data.hello);
            }
        });
    }

    // Listen for click event on the translation button
    $('INPUT#btn_translate').click(fetchTranslation);

    // Listen for keypress event on the input field
    $('INPUT#language_code').keypress(function(event) {
        // Check if the pressed key is ENTER (key code 13)
        if (event.which === 13) {
            fetchTranslation();
        }
    });
});