document.addEventListener("DOMContentLoaded", function() {
    const element = document.getElementById("number");
    const startButton = document.getElementById("startButton");
    const stopButton = document.getElementById("stopButton");
    let isTwo = true;
    let interval;

    const updateNumber = () => {
        element.textContent = isTwo ? 2 : 12;
        element.classList.remove('visible');

        setTimeout(() => {
            element.classList.add('visible');
        }, 100);

        isTwo = !isTwo;
    };

    startButton.addEventListener('click', function() {
        startButton.disabled = true;
        stopButton.disabled = false;
        interval = setInterval(updateNumber, 1000);
        updateNumber();
    });

    stopButton.addEventListener('click', function() {
        clearInterval(interval);
        startButton.disabled = false;
        stopButton.disabled = true;
    });
});
