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
const addRandomForm = document.querySelector('.add-random-form');
const addTodoForm = document.querySelector('.add-todo-form');
randomButton.addEventListener('click', () => {
    fetch(`/activities/random_api?type=${selected.id}`)
        .then(response => response.json())
        .then(data => {
            console.log(data.activity);
            randomActivity.innerHTML = `
                <a href="https://duckduckgo.com/?q=!ducky+${data.activity}" target="_blank">${data.activity}</a>
            `;
            addRandomForm.value = data.activity;
            addTodoForm.style.display = 'block';
            randomActivity.style.display = 'block';
        });
})