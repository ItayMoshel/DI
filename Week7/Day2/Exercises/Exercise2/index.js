document.addEventListener('DOMContentLoaded', () => {
    const userForm = document.getElementById('userForm');
    console.log(userForm);

    const firstNameInput = document.getElementById('fname');
    const lastNameInput = document.getElementById('lname');
    console.log(firstNameInput);
    console.log(lastNameInput);

    const inputsByName = document.getElementsByName('firstname');
    inputsByName.forEach(input => {
        console.log(input);
    });

    userForm.addEventListener('submit', event => {
        event.preventDefault(); // Prevent form submission
        const firstNameValue = firstNameInput.value.trim();
        const lastNameValue = lastNameInput.value.trim();

        if (firstNameValue !== '' && lastNameValue !== '') {
            const usersAnswerList = document.querySelector('.usersAnswer');

            const firstNameLi = document.createElement('li');
            firstNameLi.textContent = `First name: ${firstNameValue}`;
            const lastNameLi = document.createElement('li');
            lastNameLi.textContent = `Last name: ${lastNameValue}`;

            usersAnswerList.appendChild(firstNameLi);
            usersAnswerList.appendChild(lastNameLi);

            firstNameInput.value = '';
            lastNameInput.value = '';
        }
    });
});
