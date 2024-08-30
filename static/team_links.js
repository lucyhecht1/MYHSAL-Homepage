$(document).ready(function () {

    document.querySelectorAll('.team-link').forEach(function(link) {
        link.addEventListener('click', function(event) {
            event.preventDefault();

            var teamId = this.getAttribute('data-team-id');

            console.log("Redirecting to team ID: ", teamId);

            window.location.href = '/view/' + teamId;
        });
    });
});