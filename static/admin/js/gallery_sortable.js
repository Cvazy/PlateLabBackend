document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('changelist-form');
    if (!form) return;
    
    if (!window.Sortable) {
        const script = document.createElement('script');
        script.src = 'https://cdn.jsdelivr.net/npm/sortablejs@1.15.0/Sortable.min.js';
        document.head.appendChild(script);
        
        script.onload = initSortable;
    } else {
        initSortable();
    }
    
    function initSortable() {
        const tableBody = document.querySelector('#result_list tbody');
        if (!tableBody) return;
        
        Sortable.create(tableBody, {
            animation: 150,
            ghostClass: 'bg-gray-100',
            handle: 'td',
            onEnd: function(evt) {
                const positions = Array.from(tableBody.querySelectorAll('tr'))
                    .map(row => row.querySelector('.action-checkbox input[type="checkbox"]').value);
                
                let csrftoken = null;
                const csrfInput = document.querySelector('input[name="csrfmiddlewaretoken"]');
                if (csrfInput) {
                    csrftoken = csrfInput.value;
                } else {
                    const cookies = document.cookie.split(';');
                    for (let cookie of cookies) {
                        const [name, value] = cookie.trim().split('=');
                        if (name === 'csrftoken') {
                            csrftoken = value;
                            break;
                        }
                    }
                }
                
                const formData = new FormData();
                positions.forEach((position) => {
                    formData.append('positions[]', position);
                });
                
                fetch('/admin/gallery/gallery/update-order/', {
                    method: 'POST',
                    body: formData,
                    credentials: 'include',
                    headers: {
                        'X-CSRFToken': csrftoken || '',
                        'X-Requested-With': 'XMLHttpRequest'
                    }
                })
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Response not OK: ' + response.statusText);
                    }
                    return response.json();
                })
                .then(data => {
                    if (data.status === 'ok') {
                        const rowsWithInputs = document.querySelectorAll('#result_list tbody tr');
                        rowsWithInputs.forEach((row, index) => {
                            const orderInput = row.querySelector('input[name$="-order"]');
                            if (orderInput) orderInput.value = index;
                        });
                    } else {
                        console.error('Error in server response:', data);
                        alert('Произошла ошибка при сохранении порядка!');
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                    alert('Произошла ошибка при сохранении порядка!');
                });
            }
        });
        
        const rows = document.querySelectorAll('#result_list tbody tr');
        rows.forEach(row => {
            row.style.cursor = 'move';
            row.title = 'Перетащите для изменения порядка';
        });
    }
}); 