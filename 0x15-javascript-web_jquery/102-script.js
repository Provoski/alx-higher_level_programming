$(document).ready(function() {
  var apiUrl = 'https://www.fourtonfish.com/hellosalut/hello/';
  language = $('#language_code').val()
  $('#btn_translate').click(function () {
    $.ajax({
      url: apiUrl + language,
      type: 'GET',
      dataType: 'json',
      success: function(response) {
        $('#hello').text(response.hello);
      },
      error: function(error) {
        console.error(error);
      }
    });
  });
});