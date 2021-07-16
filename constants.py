from selenium.webdriver.common.by import By

DEFAULT_WAIT = 89

MAIN_SEARCH_BAR__SEARCH_ICON = (By.CSS_SELECTOR, 'span[data-testid="search"]')
QR_CODE = (By.CSS_SELECTOR, 'div[data-ref]')

SETUP_INDEXEDDB = """

function getResultFromRequest(request) {
    return new Promise((resolve, reject) => {
        request.onsuccess = function(event) {
            resolve(request.result);
        };
    })
}

async function getDB() {
    var request = window.indexedDB.open("wawc");
    return await getResultFromRequest(request);
}

"""
EXTRACT_SESSION = SETUP_INDEXEDDB + """

async function readAllKeyValuePairs() {
    var db = await getDB();
    var objectStore = db.transaction("user").objectStore("user");
    var request = objectStore.getAll();
    return await getResultFromRequest(request);
}

return await readAllKeyValuePairs();

"""

INJECT_SESSION = SETUP_INDEXEDDB + """

async function injectSession(SESSION_STRING) {
    var session = eval(SESSION_STRING);
    var db = await getDB();
    var objectStore = db.transaction("user", "readwrite").objectStore("user");
    for(var keyValue of session) {
        var request = objectStore.put(keyValue);
        await getResultFromRequest(request);
    }
}

// we can pass "arguments" from python to javascript
var SESSION_STRING = arguments[0]; 
await injectSession(SESSION_STRING);

"""
