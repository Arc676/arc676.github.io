// https://stackoverflow.com/a/17901198/2773311
// https://stackoverflow.com/a/63519229/2773311
function load(doc, url, element) {
	fetch(url)
		.then(res => { res.text(); })
		.then(html => { doc.getElementById(element).innerHTML = html; });
}
