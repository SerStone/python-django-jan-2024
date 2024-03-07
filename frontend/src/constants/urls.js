const baseURL = '/api'

const auth = '/auth';
const cars = '/cars';

const urls = {
    auth: {
        login: `${auth}/login`,
        socket: `${auth}/socket`
    },
    cars
}

export {
    baseURL,
    urls
}