import {apiService} from "./apiService";
import {urls} from "../constants/urls";

const carService = {
    getAll:()=>apiService.get(urls.cars),
    create:(data)=>apiService.post(urls.cars, data)
}

export {
    carService
}