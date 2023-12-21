// Update quantity on click

document.querySelectorAll('.update-link').forEach(function (link) {
    link.addEventListener('click', function (e) {
        const form = this.previousElementSibling;
        form.submit();
    });

});

// Remove item and reload on click

$('.remove-item').click(function (e) {
    var csrfToken = "{{ csrf_token }}";
    var itemId = $(this).attr('id').split('remove_')[1];
    var size = $(this).data('product_size');
    var url = `/bag/remove/${itemId}/`;
    var data = {
        'csrfmiddlewaretoken': csrfToken,
        'product_size': size
    };

    $.post(url, data)
        .done(function () {
            location.reload();
        });
})