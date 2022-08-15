let total_income_url = 'http://127.0.0.1:8000/api/total-income/'
let get_total_income = () => {

    fetch(total_income_url)
    .then(response => response.json())
    .then(data => {
        console.log(data)
        build_total_income_card(data)
    })
}

let build_total_income_card = (total_income) => {
    let card = document.getElementById('total-income')
    card.innerHTML = `<h1>${total_income.total_income}</h1>`
}

let orders_url = 'http://127.0.0.1:8000/api/orders/'
let get_orders = () => {

    fetch(orders_url)
    .then(response => response.json())
    .then(data => {
        console.log(data)
        build_orders_table(data)
    })
}

let build_orders_table = (orders) => {
    let ordersWrapper = document.getElementById('table')
    ordersWrapper.innerHTML = `
                <tr>
                    <th>№</th>
                    <th>№ заказа</th>
                    <th>стоимость, $</th>
                    <th>стоимость, руб</th>
                    <th>дата доставки</th>
                </tr>
    `
    
    for (let i = 0; i < orders.length; i++){
        let order = orders[i]
        
        let order_raw = `
                <tr>
                    <td>${order.number}</td>
                    <td>${order.order}</td>
                    <td>${order.price_in_dollars}</td>
                    <td>${order.price_in_rubles}</td>
                    <td>${order.delivery_date}</td>
                </tr>
        `
        ordersWrapper.innerHTML += order_raw
    }
}

get_total_income()
get_orders()