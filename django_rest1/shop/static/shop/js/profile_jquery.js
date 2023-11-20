$(document).ready(function() {
  $('#update_profile').submit(function(event) {
    event.preventDefault();

    var formData = $(this).serialize();

    $.ajax({
      url: 'profile/',
      type: 'PATCH',
      data: formData,
      success: function(response) {

        console.log(response);
      },
      error: function(xhr, errmsg, err) {

        console.log(xhr.status + ": " + xhr.responseText);
      }
    });
  });
});

