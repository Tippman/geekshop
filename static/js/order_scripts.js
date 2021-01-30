window.onload = function () {
    var _quantity, _price, orderitem_num, delta_quantity, orderitem_quantity, delta_cost;
    var quantity_arr = [];
    var price_arr = [];

    var TOTAL_FORMS = parseInt($('input[name=orderitems-TOTAL_FORMS]').val());

    var order_total_quantity = parseInt($('.order_total_quantity').text()) || 0
    var order_total_price = parseFloat($('.order_total_cost').text().replace(',', '.').replace(/\s*/g, '')) || 0

    for (let i = 0; i < TOTAL_FORMS; i++) {
        _quantity = parseInt($('input[name=orderitems-' + i + '-quantity]').val());
        _price = parseFloat($('span.orderitems-' + i + '-price').text().replace(',', '.').replace(/\s*/g, ''));

        quantity_arr[i] = _quantity;
        if (_price) {
            price_arr[i] = _price;
        } else {
            price_arr[i] = 0;
        }
    }

    $('.order_form').on('change', 'input[type=number]', function () {
        let target = event.target;
        orderitem_num = parseInt(target.name.replace(/orderitems-(\d*)-quantity/, '$1'));
        if (price_arr[orderitem_num]) {
            orderitem_quantity = parseInt(target.value);
            delta_quantity = orderitem_quantity - quantity_arr[orderitem_num];
            quantity_arr[orderitem_num] = orderitem_quantity;
            orderSummaryUpdate(price_arr[orderitem_num], delta_quantity);
        }
    });

    $('.order_form').on('click', 'input[type=checkbox]', function () {
        let target = event.target;
        orderitem_num = parseInt(target.name.replace(/orderitems-(\d*)-DELETE/, '$1'));
        if (target.checked) {
            delta_quantity = -quantity_arr[orderitem_num];
        } else {
            delta_quantity = quantity_arr[orderitem_num];
        }
        orderSummaryUpdate(price_arr[orderitem_num], delta_quantity);
    });

    $('.order_form').on('change', 'select', function () {
        let product_id = event.target.value;
        orderitem_num = parseInt(event.target.name.replace(/orderitems-(\d*)-product/, '$1'));

        $.ajax({
            url: `/order/get-price/`,
            data: {
                'product_id': product_id
            },
            success: (data) => {
                $(`span.orderitems-${orderitem_num}-price`).html(data);
                price_arr[orderitem_num] = parseFloat($('span.orderitems-' + orderitem_num + '-price').text().replace(',', '.').replace(/\s*/g, ''));
            },
        });
        event.preventDefault();

    });


    function orderSummaryUpdate(orderitem_price, delta_quantity) {
        delta_cost = orderitem_price * delta_quantity;
        order_total_price = Number((order_total_price + delta_cost).toFixed(2));
        order_total_quantity = order_total_quantity + delta_quantity;

        $('.order_total_quantity').html(order_total_quantity.toString());
        $('.order_total_cost').html(order_total_price.toString());
    };
}
