const taskInput = document.getElementById('task-input');
const addBtn = document.getElementById('add-btn');
const taskList = document.getElementById('task-list');

function createTaskElement(taskText) {
    const li = document.createElement('li');
    li.className = 'task-item';

    const checkbox = document.createElement('input');
    checkbox.type = 'checkbox';

    const label = document.createElement('label');
    label.textContent = taskText;

    checkbox.addEventListener('change', function() {
        if (checkbox.checked) {
            li.classList.add('completed');
        } else {
            li.classList.remove('completed');
        }
    });

    const deleteBtn = document.createElement('button');
    deleteBtn.className = 'delete-btn';
    deleteBtn.title = 'Delete task';
    deleteBtn.innerHTML = '&times;';

    deleteBtn.addEventListener('click', function() {
        taskList.removeChild(li);
    });

    label.addEventListener('click', function() { checkbox.click(); });

    li.appendChild(checkbox);
    li.appendChild(label);
    li.appendChild(deleteBtn);

    return li;
}

function addTask() {
    const text = taskInput.value.trim();
    if (text) {
        const taskEl = createTaskElement(text);
        taskList.appendChild(taskEl);
        taskInput.value = '';
        taskInput.focus();
    }
}

addBtn.addEventListener('click', addTask);
taskInput.addEventListener('keydown', function(e) {
    if (e.key === 'Enter') addTask();
});

taskInput.focus();

