import { TodoList } from './todo.js';

const todoList = new TodoList();

todoList.addTask('Task 1');
todoList.addTask('Task 2');
todoList.addTask('Task 3');
todoList.markTaskComplete(1);

const tasks = todoList.listTasks();
console.log('Tasks:', tasks);