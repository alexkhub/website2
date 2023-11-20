$.ajax({
    type: 'PUT',
    url: '/profile_update',
    data: { pk: pk },
    success: function() {
        alert('Object deleted!')
    }
});