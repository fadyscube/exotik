const randomButton = document.querySelector('.random-btn');
const randomFact = document.querySelector('.fact');
randomButton.addEventListener('click', () => {
    fetch('https://api.api-ninjas.com/v1/facts', {
        headers: {
            'X-Api-Key': 'ojGt8FQxsfAA0B29nHaUiA==OLU5TXZ2DWDPrHEe',
        }
    })
        .then(response => response.json())
        .then(data => {
            console.log(data.activity);
            randomFact.innerHTML = `
                <p>${data[0].fact}</p>
            `;
        });
})