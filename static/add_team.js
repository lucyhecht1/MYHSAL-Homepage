$(document).ready(function () {
    const addTeamForm = document.getElementById("addTeamForm");
    const errorMessage = document.getElementById("error-message");
    const successMessage = document.getElementById("success-message");

    // Function to display error message near the input field
    function showError(element, message) {
        $(element).next('.error-message').remove();
        const errorDiv = $("<div class='error-message' style='color: red;'></div>").text(message);
        $(element).after(errorDiv);
        $(element).focus(); // Refocus on the field with the error
    }

    // Remove error message when user starts typing in an input field
    $(addTeamForm).find('.form-input').on('input', function() {
        $(this).next('.error-message').remove();
    });

    addTeamForm.addEventListener("submit", function (event) {
        event.preventDefault();

        errorMessage.textContent = '';
        successMessage.textContent = '';
        $(".error-message").remove();

        let isFormValid = true; // Flag to check if form inputs are valid

        $(addTeamForm).find('.form-input').each(function() {
            const trimmedValue = this.value.trim();
            if (trimmedValue === '' && !$(this).hasClass('allow-empty')) {
                showError(this, "Field cannot be left empty.");
                isFormValid = false;
                return false;
            }
        });

        // If form is not valid (empty fields), prevent submission
        if (!isFormValid) {
            return;
        }

        const formData = new FormData(addTeamForm);

        // Proceed with form submission if validation passed
        fetch('/add', {
            method: 'POST',
            body: formData
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok.');
            }
            return response.json();
        })
        .then(data => {
            if (!data.success) {
                errorMessage.innerHTML = data.errors.join('<br>');
            } else {
                successMessage.textContent = "Entry successfully added.";
                successMessage.style.display = "block";
                addTeamForm.reset();

                let viewButton = document.getElementById("viewEntryButton");
                if (!viewButton) {
                    viewButton = document.createElement("button");
                    viewButton.id = "viewEntryButton";
                    viewButton.textContent = "View Entry";
                    viewButton.classList.add("view-button");
                    viewButton.addEventListener("click", function () {
                        window.location.href = "/view/" + data.id;
                    });
                    successMessage.appendChild(viewButton);
                    $(addTeamForm).find('.form-input').first().focus();
                }
            }
        })
        .catch(error => {
            console.error('Error:', error);
            errorMessage.textContent = 'An error occurred while processing your request.';
            $(addTeamForm).find('.form-input').first().focus(); // Ensure focus is set back to the first field for correction
        });
    });

    // Keyboard navigation for form inputs
    $('#addTeamForm').on('keydown', '.form-input', function(e) {
        if (e.key === "Enter") {
            e.preventDefault();
            const currentIndex = $('.form-input').index(this);
            const nextIndex = currentIndex + 1;

            if (nextIndex < $('.form-input').length - $('.allow-empty').length) {
                $('.form-input').eq(nextIndex).focus(); // Move focus to next field
            } else {
                $('#addTeamForm button[type="submit"]').focus(); // Or focus the submit button if it's the last field before 'allow-empty' fields
            }
        }
    });
});
