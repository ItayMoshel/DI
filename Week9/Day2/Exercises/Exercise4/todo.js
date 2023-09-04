export class TodoList {
    constructor() {
      this.tasks = [];
    }
  
    // Method to add a task
    addTask(task) {
      this.tasks.push({ task, completed: false });
    }
  
    // Method to mark a task as complete
    markTaskComplete(index) {
      if (index >= 0 && index < this.tasks.length) {
        this.tasks[index].completed = true;
      }
    }
  
    // Method to list all tasks
    listTasks() {
      return this.tasks;
    }
  }