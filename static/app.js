// get the button to show the add task form

let addTaskBtn = document.querySelector('#add_task')
let doneBtn = document.querySelector('#done')

// get the task creation form

let createTask = document.querySelector('.create-container')

addTaskBtn.addEventListener("click", function() {
    createTask.classList.toggle('show');
});



