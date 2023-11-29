var updateBtns = document.getElementsByClassName('update-cart')


for (var i=0; i<updateBtns.length;i++) {
    updateBtns[i].addEventListener('click', function () {
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId:',productId, 'Action:',action)

        // changing what happens depending on user authentication

        console.log('USER:', user)
        if (user == 'AnonymousUser'){
            console.log('User is not authenticated')
        }else{
            updateUserOrder(productId, action)
        }

    })
}

function updateUserOrder(productId, action){
    console.log('User is authenticated, sending data.....')
    // url for sending our data
    var url = '/update_item/'
    // to send POST data we use fetch API
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'productId':productId,'action':action })
    })
        .then((response) =>{
            return response.json();
        })
        .then((data) => {
            console.log('data:', data)
        });

}