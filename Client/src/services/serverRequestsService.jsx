import {config} from "../config/config";
import axios from "axios";

class ServerRequestsService {

    constructor() {
        this.serverUrl = config.serverUrl;
    }

    async getUserResults(userId) {
        console.log(userId);
        const body = {'user': userId};
        const results = await axios.post(this.serverUrl+ '/calculate', body);
        return results.data;
    }
}

export default ServerRequestsService;
