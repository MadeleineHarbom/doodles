


function toggleClass(clickedButton) {
    // Get all buttons
    console.log("clicky click")
    const buttons = document.querySelectorAll('nav-link');

    // Remove the class 'active' from all buttons
    buttons.forEach(button => {
        button.classList.remove('active');
    });

    // Add the class 'active' to the clicked button
    clickedButton.classList.add('active');
}
