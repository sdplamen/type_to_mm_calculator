function convert() {
    const conversionType = $('#conversionType').val();
    const value = $('#value').val();

    $.ajax({
        url: '/convert/',
        type: 'POST',
        data: {
            conversion_type: conversionType,
            value: value,
            csrfmiddlewaretoken: '{{ csrf_token }}'
        },
        success: function(response) {
            $('#result').text(response.result);
        },
        error: function() {
            $('#result').text('Error in conversion');
        }
    });
}