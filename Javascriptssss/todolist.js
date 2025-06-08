const todolist = [
  { name: "make dinner", duedate: "2022-12-22" },
  {
    name: "wash dishes",
    duedate: "2022-12-22",
  },
];
renderTodoList();

function renderTodoList() {
  let todolistHTML = "";

  todolist.forEach((todo, index) => {
    const { name, duedate } = todo;
    const html = `
    <div> ${name}</div>
    <div> ${duedate}</div>
    <button onclick=
      "todolist.splice(${index},1);
      renderTodoList();"
      class="delete-todo-button">Delete</button> 
    </div> `;
    todolistHTML += html;
  });

  document.querySelector(".js-todo-list").innerHTML = todolistHTML;
}

function addTodo() {
  inputElement = document.querySelector(".js-name-input");
  const name = inputElement.value;
  const dateinputelement = document.querySelector(".js-due-date-input");
  const duedate = dateinputelement.value;

  todolist.push({
    name,
    duedate,
  });
  inputElement.value = "";
  renderTodoList();
}
