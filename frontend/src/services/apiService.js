import axios from "axios";
import {baseURL} from "../constants/urls";
import {authService} from "./authService";

const apiService = axios.create({baseURL})


apiService.interceptors.request.use(request => {
    const token = localStorage.getItem('access');

    if (token) {
        request.headers.Authorization = `Bearer ${token}`
    }

    return request
})
export {
    apiService
}