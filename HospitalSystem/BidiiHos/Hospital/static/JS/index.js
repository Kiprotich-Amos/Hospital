$(document).ready(function() {
    $("#patients-form-button").on("click", function() {
        // Show the patients form pop-up
        $("#patients-form-popup").show();
    });

    $("#close-patients-form").on("click", function() {
        // Close the patients form pop-up
        $("#patients-form-popup").hide();
    });

    // Handle form submission
    $("#submit-patients-form").on("click", function() {
        // Add your form submission logic here
        
        // After successful submission, show the success message and close the pop-up
        $("#success-message").show();
        $("#patients-form-popup").hide();
    });

    // Close the success message when clicked
    $("#success-message").on("click", function() {
        $(this).hide();
    });
});
