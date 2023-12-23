//var form = document.getElementById('update_profile');
//// form указывает на форму
//
//var params = new FormData(form);
//
//fetch('#', {
//   method: 'PUT',
//    headers: {
//
//            'X-CSRFToken': csrftoken,
//        },
//   body: params,
//});
//document.getElementById('update_profile').addEventListener('submit', function(event) {
//  event.preventDefault(); // Предотвращает отправку формы по умолчанию
//
//  var form = event.target;
//  var formData = new FormData(form);
//
//  fetch('#', {
//    method: 'PATCH',
//    headers: {
//      'X-Requested-With': 'XMLHttpRequest' // Добавьте заголовок, чтобы указать, что это AJAX-запрос
//    },
//    body: formData
//  })
//  .then(function(response) {
//    if (response.ok) {
//      // Обработка успешного ответа
//      return response.text();
//    } else {
//      // Обработка ошибки
//      throw new Error(response.status + ": " + response.statusText);
//    }
//  })
//  .then(function(data) {
//    console.log(data);
//  })
//  .catch(function(error) {
//    console.error(error);
//  });
//});

$("#confirm").on("click",function() {
        var url = document.location.pathname
         form = $(this).closest("form"),
         formData  = form.serialize()
         $.ajax({
             type:'PATCH',
             url: url,
             data: formData,
             success: function (data) {

            },
              headers: {'X_METHODOVERRIDE': 'PUT',
              {'X-CSRFToken': csrftoken}
              }
         });
    });