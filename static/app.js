document.addEventListener('DOMContentLoaded', function () {
    // Fetch transactions when the DOM is loaded.
    fetchTransactions();

    // Handle the form submission for adding a transaction.
    document.getElementById('Transaction').addEventListener('submit', function (e) {
        e.preventDefault();
        addTransaction();
    });
});

function addTransaction() {
    const description = document.getElementById('description').value;
    const amount = parseFloat(document.getElementById('amount').value);
    const date = document.getElementById('date').value;
    const type = document.getElementById('type').value;

    const data = { description, amount, date, type };

    fetch('/api/transactions', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        fetchTransactions(); // Refresh the list of transactions.
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

function fetchTransactions() {
    fetch('/api/transactions')
        .then(response => response.json())
        .then(data => {
            displayTransactions(data);
        })
        .catch((error) => {
            console.error('Error:', error);
        });
}

function displayTransactions(transactions) {
    const transactionsList = document.getElementById('transactionList');
    // Clear the list before displaying new data
    transactionsList.innerHTML = '';

    transactions.forEach(transaction => {
        // Create transaction element
        const transactionElement = document.createElement('div');
        transactionElement.innerHTML = `
            <div>
                <span>${transaction.description}</span>
                <span>${transaction.amount}</span>
                <span>${transaction.date}</span>
                <span>${transaction.type}</span>
                <button onclick="deleteTransaction(${transaction.id})">Delete</button>
            </div>
        `;
        transactionsList.appendChild(transactionElement);
    });
}

function deleteTransaction(id) {
    fetch(`/api/transactions/${id}`, {
        method: 'DELETE',
    })
    .then(response => response.json())
    .then(data => {
        console.log('Delete Success:', data);
        fetchTransactions(); // Refresh the list of transactions.
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}
