async function sendQuestion() {
    const question = document.getElementById('input-question').value;
    const model = document.getElementById('model-select').value;
    const responseBox = document.getElementById('response-box');
    const loading = document.getElementById('loading');

    if (!question) {
        alert('Por favor, digite uma pergunta!');
        return;
    }

    try {
        loading.style.display = 'block';
        responseBox.textContent = '';

        // Chamada real para a API
        const response = await fetch('http://localhost:5000/api/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                model: model,
                message: question
            })
        });
        console.log(response.body)
        if (!response.ok) {
            throw new Error(`Erro HTTP: ${response.message}`);
        }

        const data = await response.json();
        responseBox.textContent = data.answer;

    } catch (error) {
        responseBox.textContent = `Erro: ${error.message}`;
    } finally {
        loading.style.display = 'none';
    }
}

// Remover a função mockApiCall