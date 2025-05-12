document.addEventListener('DOMContentLoaded', function() {
    if (!window.Sortable) {
        const script = document.createElement('script');
        script.src = 'https://cdn.jsdelivr.net/npm/sortablejs@1.15.0/Sortable.min.js';
        document.head.appendChild(script);
        
        script.onload = initSortable;
    } else {
        initSortable();
    }

    function initSortable() {
        const urlParts = window.location.pathname.split('/');
        const caseIdIndex = urlParts.indexOf('case') + 1;
        if (caseIdIndex >= urlParts.length) return;
        
        const caseId = urlParts[caseIdIndex];
        console.log('Case ID:', caseId);
        
        const inlineGroup = document.querySelector('.inline-group');
        if (!inlineGroup) return;
        
        const tbody = inlineGroup.querySelector('tbody');
        if (!tbody) return;
        
        const lastRow = tbody.querySelector('tr.add-row');
        
        Sortable.create(tbody, {
            handle: 'td:first-child',
            animation: 150,
            ghostClass: 'bg-gray-100',
            filter: '.empty-form, .add-row',
            onEnd: function(evt) {
                const rows = Array.from(tbody.querySelectorAll('tr:not(.empty-form):not(.add-row)'));
                console.log('Found rows:', rows.length);
                
                const positions = [];
                for (let i = 0; i < rows.length; i++) {
                    const row = rows[i];
                    const idInput = row.querySelector('input[type="hidden"][name$="-id"]');
                    if (idInput && idInput.value) {
                        positions.push(idInput.value);
                    } else {
                        console.warn('No ID found for row', i, row);
                    }
                }
                
                console.log('Positions to update:', positions);
                
                if (positions.length === 0) {
                    console.error('No positions to update!');
                    return;
                }
                
                let csrftoken = null;
                const csrfInput = document.querySelector('input[name="csrfmiddlewaretoken"]');
                if (csrfInput) {
                    csrftoken = csrfInput.value;
                    console.log('Found CSRF token in form');
                } else {
                    const cookies = document.cookie.split(';');
                    for (let cookie of cookies) {
                        const [name, value] = cookie.trim().split('=');
                        if (name === 'csrftoken') {
                            csrftoken = value;
                            console.log('Found CSRF token in cookies');
                            break;
                        }
                    }
                }
                
                if (!csrftoken) {
                    console.warn('No CSRF token found!');
                }
                
                const requestURL = `/admin/cases/case/${caseId}/update-image-order/`;
                console.log('Request URL:', requestURL);
                
                fetch(requestURL, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': csrftoken || '',
                        'X-Requested-With': 'XMLHttpRequest'
                    },
                    body: JSON.stringify({positions: positions}),
                    credentials: 'include'
                })
                .then(response => {
                    console.log('Response status:', response.status);
                    if (!response.ok) {
                        return response.text().then(text => {
                            console.error('Error response body:', text);
                            throw new Error('Response not OK: ' + response.statusText);
                        });
                    }
                    return response.json();
                })
                .then(data => {
                    console.log('Response data:', data);
                    if (data.status === 'ok') {
                        rows.forEach((row, index) => {
                            const orderInput = row.querySelector('input[name$="-order"]');
                            if (orderInput) orderInput.value = index;
                        });
                    } else {
                        console.error('Error in server response:', data);
                        alert('Произошла ошибка при сохранении порядка изображений!');
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                    alert('Произошла ошибка при сохранении порядка изображений!');
                });
            }
        });
        
        const handleCells = tbody.querySelectorAll('tr:not(.empty-form):not(.add-row) td:first-child');
        handleCells.forEach(cell => {
            cell.style.cursor = 'move';
            cell.style.backgroundColor = '#f8f8f8';
            cell.setAttribute('title', 'Перетащите для изменения порядка');
            
            cell.addEventListener('mouseover', function() {
                this.style.backgroundColor = '#e8e8e8';
            });
            
            cell.addEventListener('mouseout', function() {
                this.style.backgroundColor = '#f8f8f8';
            });
        });
    }
}); 