/* eslint-disable linebreak-style */
function addTask() {
  const taskInput = document.getElementById('taskInput');
  const taskText = taskInput.value.trim();
  if (taskText !== '') {
    const taskList = document.getElementById('taskList');
    const newTask = document.createElement('li');
    newTask.classList.add('task');
    newTask.innerHTML = `<span>${taskText}</span>`
                            + '<select onchange="setPriority(this)">'
                            + '<option value="low">Low</option>'
                            + '<option value="medium">Medium</option>'
                            + '<option value="high">High</option>'
                            + '</select>'
                            + '<span class="delete-btn" onclick="deleteTask(this)">Delete</span>';
    taskList.appendChild(newTask);
    taskInput.value = '';
  } else {
    alert('Please enter a task!');
  }
}

function deleteTask(deleteBtn) {
  const taskList = document.getElementById('taskList');
  const taskItem = deleteBtn.parentNode;
  taskList.removeChild(taskItem);
}

function setPriority(prioritySelect) {
  const taskItem = prioritySelect.parentNode;
  const priorityValue = prioritySelect.value;
  taskItem.className = `task ${priorityValue}`;
}
