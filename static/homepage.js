$(document).ready(function () {

    $('#searchForm').on('submit', function(event) {
        event.preventDefault(); 

        let query = $("#searchInput").val().trim();
        
        if (!query) {
            $("#searchInput").val('').focus();
            return;
        }
        window.location.href = '/search?query=' + encodeURIComponent(query);
    });
});
