$(document).ready(function() {
  function fetchTranslation() {
    var apiUrl = 'https://www.fourtonfish.com/hellosalut/hello/';
    language = $('#language_code').val()
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
  }
  
  $('#btn_translate').click(fetchTranslation);
  $('#language_code').on('keypress', function(e) {
    if (e.which === 13) {
      fetchTranslation();
    }
  });
});