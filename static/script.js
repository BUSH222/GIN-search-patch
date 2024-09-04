document.getElementById('searchForm').addEventListener('submit', function(event) {
    event.preventDefault();
    var search = document.getElementById('search').value;
    var category = document.getElementById('category').value;
    var baseUrl;

    if (category === 'content') {
        baseUrl = 'https://example.com/content';
    } else if (category === 'person') {
        baseUrl = 'https://example.com/person';
    }

    var url = baseUrl + '?query=' + encodeURIComponent(search);
    window.location.href = url;
});