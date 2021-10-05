// https://stackoverflow.com/a/17901198/2773311
function load(url, element) {
	fetch(url).then(html => { document.getElementById(element).innerHTML = html; });
}
