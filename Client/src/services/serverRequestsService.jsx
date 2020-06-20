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

    async searchUsers(text_to_search) {
        console.log(text_to_search);
        const body = {'search_text': text_to_search};
        const results = await axios.post(this.serverUrl+ '/searchUsers', body);
        return results.data;
    }
}

export default ServerRequestsService;
