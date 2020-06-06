export let config;

let docHost = document.location.host;
let originArr = docHost.split(".");
if(!docHost.includes('localhost') && isNaN(parseInt(originArr[0]))) {
    config = require('./config.prod.json');
} else {
    config = require('./config.dev.json');
}
