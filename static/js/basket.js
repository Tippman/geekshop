window.onload = function () {
    $('.basket-list').on('click', 'input[type="number"]', (event) => {
        const elem = event.target;
        $.ajax({
            url: `/baskets/edit/${elem.name}/${elem.value}`,
            success: (data) => {
                $('.basket-list').html(data.result);
            },
        });
        event.preventDefault();
    });
}