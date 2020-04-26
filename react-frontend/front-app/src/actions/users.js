import axios from 'axios';

export const getUsers = () => async() => {
    try {
        const res = await axios.get('http://localhost:5000/users')
        console.log(res);
        
    } catch(err) {
        console.log(err);
    }
};
