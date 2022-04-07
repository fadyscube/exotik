const selected = document.querySelector('.selected');
const typesContainer = document.querySelector('.types-container');

const typesList = document.querySelectorAll('.type');

selected.addEventListener('click', () => {
    typesContainer.classList.toggle('active');
})

typesList.forEach(t => {
    t.addEventListener('click', () => {
        selected.innerHTML = t.querySelector('label').innerHTML;
        selected.id = t.querySelector('input').id;
        typesContainer.classList.remove('active');
    })
})

const randomButton = document.querySelector('.random-btn .btn');
const randomActivity = document.querySelector('.activity-parent');
randomButton.addEventListener('click', () => {
    fetch(`https://www.boredapi.com/api/activity?type=${selected.id}`)
        .then(response => response.json())
        .then(data => {
            randomActivity.innerHTML = `<p>${data.activity}</p>`;
            randomActivity.style.display = 'block';
        });
})