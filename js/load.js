// https://stackoverflow.com/a/17901198/2773311
// https://stackoverflow.com/a/63519229/2773311
function load(url, element) {
	fetch(url)
		.then(res => { return res.text(); })
		.then(html => { document.getElementById(element).innerHTML = html; });
}
