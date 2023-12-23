function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');


$(function() {
    $('#update_profile').on('submit', function(event) {
        function updateTodo(url, payload) {
          $.ajax({
            url: url,
            type: "PUT",
            dataType: "json",
            data: JSON.stringify({payload: payload,}),
            headers: {
              "X-Requested-With": "XMLHttpRequest",
              "X-CSRFToken": getCookie("csrftoken"),
            },
            success: (data) => {
              console.log(data);
            },
            error: (error) => {
              console.log(error);
            }
          });
        };
       };

