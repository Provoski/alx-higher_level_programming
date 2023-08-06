$(document).ready(function() {
  var apiUrl = 'https://fourtonfish.com/hellosalut/?lang=fr';
  $.ajax({
    url: apiUrl,
    method: 'GET',
    dataType: 'json',
    success: function(data) {
      $('#hello').text(data.hello);
    },
    error: function(error) {
      console.error(error);
    }
  });
});