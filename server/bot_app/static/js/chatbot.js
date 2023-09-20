async function fetchResponse() {
    try{
        const response = await fetch('/bot/fetch_response/');
        if(!response.ok){
            data = 'Failed to fetch reponse. Please retry.';
            const table = document.getElementById('data-table');
            const queryRow = table.insertRow();
            queryRow.id = 'chat-bubble';
            const query_cell = queryRow.insertCell(0);
            query_cell.innerHTML = data; 
        }else{
            const data = await response.json();
            const table = document.getElementById('data-table');
            const queryRow = table.insertRow();
            queryRow.id = 'chat-bubble';
            const query_cell = queryRow.insertCell(0);
            query_cell.innerHTML = data.question_text;
            const responseRow = table.insertRow();
            responseRow.id = 'bot-bubble';
            const response_cell = responseRow.insertCell(0);
            response_cell.innerHTML = data.query_response;   
        }
    }catch(error){
        console.error('There was a error with fetching the response : ', error);
        return '';
    }
}

window.onload = function(){
    const form = document.getElementById('form-query');
    form.addEventListener('submit', function(event){
        event.preventDefault();
        fetchResponse();
    })
    const fetchBtn = document.getElementById('query-box');
    fetchBtn.addEventListener('keydown', function(event){
        if(event.key === 'Enter'){
            event.preventDefault();
            form.submit();
        }
    })
}