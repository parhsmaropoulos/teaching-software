import axios from 'axios';

function getusers() {
    axios.get('http://localhost:5000/')
    .then(function (response) {
        console.log(response)
    })
    .catch(function (error) {
        console.log(error)
    })
    .then(function () {
        
    });
}

export default getusers();
