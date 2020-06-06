import {config} from "../config/config";
import axios from "axios";

class ServerRequestsService {

    constructor() {
        this.serverUrl = config.serverUrl;
    }

    async getUserResults(userId) {
        const results = await axios.get(this.serverUrl+ '/calculate');
        return results.data;
    }
}

export default ServerRequestsService;
