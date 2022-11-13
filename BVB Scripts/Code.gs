function bvbCurrentPrice(symbol) {
    var url = 'https://price.easybiny.com/price.php?sym=' + symbol;
    var response = UrlFetchApp.fetch(url, {'muteHttpExceptions': true});
    const responseAsJson = JSON.parse(response);
    return responseAsJson.RON;
}
