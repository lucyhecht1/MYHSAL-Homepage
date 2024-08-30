document.addEventListener('DOMContentLoaded', function () {
    const editTeamForm = document.getElementById("editTeamForm");
    const submitBtn = document.getElementById("edit-submit");
    const discardChangesBtn = document.getElementById("discardChanges");
    let isSubmitButtonFocused = false; // Flag to track if submit button is focused

    $(editTeamForm).on('keydown', function(e) {
        if (e.key === "Enter" && !isSubmitButtonFocused) {
            e.preventDefault(); 
            $(submitBtn).focus();
            isSubmitButtonFocused = true;
        } else if (e.key === "Enter" && isSubmitButtonFocused) {
            e.preventDefault();
            submitForm();
        }
    });

    function submitForm() {
        const formData = new FormData(editTeamForm);
        let teamId = $(submitBtn).data("team-id");
        let fetchUrl = '/edit/' + teamId;

        fetch(fetchUrl, {
            method: 'POST',
            body: formData
        }).then(response => {
            if (response.ok) {
                window.location.href = '/view/' + teamId;
            } else {
                alert('An error occurred while saving your changes.');
                isSubmitButtonFocused = false;
            }
        }).catch(() => {
            alert('An error occurred while saving your changes.');
            isSubmitButtonFocused = false; 
        });
    }
    // Handle discard changes button click
    discardChangesBtn.addEventListener("click", function () {
        const userConfirmed = confirm('Are you sure you want to discard changes?');
        if (userConfirmed) {
            let teamId = $(submitBtn).data("team-id");
            window.location.href = '/view/' + teamId;
        }
    });

    // Keydown event listener for discardChangesBtn
    discardChangesBtn.addEventListener("keydown", function (e) {
        if (e.key === "Enter") {
            e.preventDefault();
            const userConfirmed = confirm('Are you sure you want to discard changes?');
            if (userConfirmed) {
                let teamId = $(submitBtn).data("team-id");
                window.location.href = '/view/' + teamId;
            }
        }
    });
});