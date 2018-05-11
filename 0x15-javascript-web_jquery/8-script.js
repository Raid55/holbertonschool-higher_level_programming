$(() => {
  $.get('https://swapi.co/api/films/?format=json', res => {
    res.results.forEach(movie => {
      $('ul#list_movies').append(`<li>${movie.title}</li>`);
    });
  });
});
