console.log("Hello")
var updateBtns = document.getElementsByClassName('update-cart')

for (i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function() {
        var bookId = this.dataset.book
        var action = this.dataset.action

        console.log('bookId', bookId, 'action', action)
        console.log('user: ', user)

        if (user != "AnonymousUser") {
            userUpdateOrder(bookId, action)
        }
    })

}


async function userUpdateOrder(bookId, action) {
    var url = '/update_item/'
    fetch(url, {
        method: 'POST',
        mode: "cors",
        cache: "no-cache",
        credentials: "same-origin",
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        redirect: "follow",
        referrerPolicy: "no-referrer",
        body: JSON.stringify({ 'bookId': bookId, 'action': action })
    })

    // return response.json();

    .then((response) => {
        if (!response.ok) {
            // error processing
            throw 'Error';
        }
        return response.json()
    })

    .then((data) => {
        console.log('data', data)
        location.reload()
    })

    .catch(error => console.log('Failed:', error));
}

// console.log("Hello")
// var updateBtns = document.getElementsByClassName('update-cart')

// for (i = 0; i < updateBtns.length; i++) {
//     updateBtns[i].addEventListener('click', function() {
//         var bookId = this.dataset.book
//         var action = this.dataset.action

//         console.log('bookId', bookId, 'action', action)
//         console.log('user: ', user)

//         if (user != "AnonymousUser") {
//             userUpdateOrder(bookId, action)
//         }
//     })

// }


// async function userUpdateOrder(bookId, action) {

//     var url = '/update_item/'
//     fetch(url, {
//         method: 'POST',
//         mode: "cors",
//         cache: "no-cache",
//         credentials: "same-origin",
//         headers: {
//             'Content-Type': 'application/json',
//             'X-CSRFToken': csrftoken
//         },
//         redirect: "follow",
//         referrerPolicy: "no-referrer",
//         body: JSON.stringify({ 'bookId': bookId, 'action': action })
//     })

//     // return response.json();

//     .then((response) => {
//         if (!response.ok) {
//             // error processing
//             throw 'Error';
//         }
//         return response.json()
//     })

//     .then((data) => {
//         console.log('data', data)
//     })
// }