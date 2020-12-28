from selenium.webdriver.common.by import By


class SELECTORS(object):
    QR_CODE = (By.CSS_SELECTOR, 'div[data-ref]')
    MAIN_SEARCH_BAR = (By.CSS_SELECTOR, '#side [contenteditable="true"]')


class STRINGS(object):
    CHECK_CHAR = '✔'
    CROSS_CHAR = '❌'


class INTEGERS(object):
    DEFAULT_WAIT = 89


_SETUP_SESSION = '''
window.indexedDB = window.indexedDB || window.mozIndexedDB ||
    window.webkitIndexedDB || window.msIndexedDB; 
window.IDBTransaction = window.IDBTransaction ||
    window.webkitIDBTransaction || window.msIDBTransaction;
window.IDBKeyRange = window.IDBKeyRange || window.webkitIDBKeyRange ||
    window.msIDBKeyRange
if (!window.indexedDB) {
    window.alert("Your browser doesn't support a stable version of IndexedDB.")
}
var db = await new Promise((resolve, reject) => {
    var request = window.indexedDB.open("wawc");
    request.onerror = function(event) {
        console.log(event);
        resolve(0);
    };

    request.onsuccess = function(event) {
        resolve(request.result);
    };

    request.onupgradeneeded = function(event) {
        resolve(event.target.result)
    }

});
'''

GET_SESSION = _SETUP_SESSION + '''
function readAll() {
    return new Promise((resolve, reject) => {
        res = [];
        var objectStore = db.transaction("user").objectStore("user");
        objectStore.openCursor().onsuccess = function(event) {
            var cursor = event.target.result;
            if (cursor) {
                res.push(cursor.value);
                cursor.continue();
            } else {
                resolve(res);
            }
        };
    });
}
session = await readAll();
res = "";
for (i in session) {
    res += session[i].key + "\\nnavi" + session[i].value + "\\nnavi";
}
return res;
'''

PUT_SESSION = _SETUP_SESSION + '''
await new Promise((resolve, reject) => {
   var request = db.transaction(["user"], "readwrite")
   .objectStore("user")
   .clear();
   request.onsuccess = function(event) {
      resolve(1);
   };
});
function add(key, value) {
    return new Promise((resolve, reject) => {
        var request = db.transaction(["user"], "readwrite")
            .objectStore("user")
            .add({
                key: key,
                value: value
            });
        request.onsuccess = function(event) {
            resolve(0);
        };
        request.onerror = function(event) {
            resolve(1);
        }
    });
}
a = arguments[0].split("\\nnavi");
for (i = 0; i < a.length - 1; i += 2) {
    await add(a[i], a[i + 1]);
}
localStorage.clear();
for (i = 0; i < a.length - 1; i += 2) {
    localStorage.setItem(a[i], a[i+1])
}
'''
