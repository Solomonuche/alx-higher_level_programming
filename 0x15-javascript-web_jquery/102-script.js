$(document).ready(function () {
  $('INPUT#btn_translate').click( function () {
    $.ajax({
      url: 'https://www.fourtonfish.com/hellosalut/hello/',
      data: {lang: $('INPUT#language_code').val()},
      success: function (data) {
        $('DIV#hello').html(data.hello)
      }
      });
  });
});