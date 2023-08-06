$(document).ready(function() {
  var apiUrl = 'https://swapi-api.alx-tools.com/api/films/?format=json';
  $.ajax({
    url: apiUrl,
    type: 'GET',
    dataType: 'json',
    success: function(data) {
      $('#list_movies').empty();
      data.results.forEach(function(film) {
        var movieTitle = film.title;
        $('#list_movies').append('<li>' + movieTitle + '</li>');
      });
    },
    error: function(error) {
      console.error(error);
    }
  });
});