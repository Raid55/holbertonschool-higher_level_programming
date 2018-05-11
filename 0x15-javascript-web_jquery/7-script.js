$(() => {
  $.get('https://swapi.co/api/people/5/?format=json', res => {
    $('div#character').text(res.name);
  });
});
