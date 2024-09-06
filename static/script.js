document.getElementById('searchForm').addEventListener('submit', function(event) {
    event.preventDefault();
    var search = document.getElementById('search').value;
    var category = document.getElementById('category').value;
    var baseUrl;
    var url = '/ginsearch/view?query=' + encodeURIComponent(search) + '&category=' + encodeURIComponent(category);
    window.location.href = url;
});