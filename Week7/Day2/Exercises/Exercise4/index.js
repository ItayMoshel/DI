document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('MyForm');
    const radiusInput = document.getElementById('radius');
    const volumeInput = document.getElementById('volume');

    form.addEventListener('submit', event => {
        event.preventDefault();
        
        const radius = parseFloat(radiusInput.value);
        if (!isNaN(radius)) {
            const volume = calculateSphereVolume(radius);
            volumeInput.value = volume.toFixed(2);
        } else {
            volumeInput.value = '';
        }
    });
});

function calculateSphereVolume(radius) {
    return (4 / 3) * Math.PI * Math.pow(radius, 3);
}
