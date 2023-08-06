$(document).ready(function() {
  var apiUrl = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
  $.ajax({
    url: apiUrl,
    type: 'GET',
    dataType: 'json',
    success: function(data) {
      var characterName = data.name;
      $('#character').text(characterName);
    },
    error: function(error) {
      console.error(error);
    }
  });
});