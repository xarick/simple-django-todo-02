//https://docs.djangoproject.com/en/3.0/ref/csrf/

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

//end scrf token

//for update
var activeItem = null

listStudent()
function listStudent(){
    var studentTable = document.getElementById('student-table')
    studentTable.innerHTML = ''

    var url = 'http://127.0.0.1:8000/api/student-list/'

    fetch(url)
    .then((resp) => resp.json())
    .then(function(data){

        var st = data
        for (var i in st){
            var item = `
                <tr>
                  <th scope="row">${st[i].id}</th>
                  <td>${st[i].name}</td>
                  <td>${st[i].email}</td>
                  <td>${st[i].group}</td>
                  <td>${st[i].completed}</td>
                  <td>
                      <a href="#" class="btn btn-outline-warning btn-sm edit">Edit</a>
                  </td>
                  <td>
                      <button class="btn btn-outline-danger btn-sm delete">Delete</button>
                  </td>
                </tr>
            `
            studentTable.innerHTML += item
        }

        for (var i in st){
            var editBtn = document.getElementsByClassName('edit')[i]
            var deleteBtn = document.getElementsByClassName('delete')[i]

            // update function
            editBtn.addEventListener('click', (function(item){
                return function(){
                    editStudent(item)
                }
            })(st[i]))

            // delete function
            deleteBtn.addEventListener('click', (function(item){
                return function(){
                    deleteStudent(item)
                }
            })(st[i]))
        }
    })
}

function clearStudentsTable(){
    document.getElementById('form').reset()
}

var form = document.getElementById('student-form')
form.addEventListener('submit', function(e){
    e.preventDefault()
    console.log("Form submitted.")

    var url = 'http://127.0.0.1:8000/api/student-create/'

    if (activeItem != null){
        var url = `http://127.0.0.1:8000/api/student-update/${activeItem.id}/`
        activeItem = null
    }

    var name        = document.getElementById('name').value
    var email       = document.getElementById('email').value
    var group       = document.getElementById('group').value
    var completed   = document.getElementById('completed').value

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({
            'name': name,
            'email': email,
            'group': group,
            'completed': completed
        })
    }).then(function(response){
        listStudent()
        clearStudentsTable()
    })
})

function editStudent(item){
    activeItem = item
    document.getElementById('name').value = activeItem.name
    document.getElementById('email').value = activeItem.email
    document.getElementById('group').value = activeItem.group

    var select = document.getElementById('completed')
    if(activeItem.completed == true){
        select[1].selected = true;
    } else {
        select[2].selected = true;
    }
}

function deleteStudent(item){
    fetch(`http://127.0.0.1:8000/api/student-delete/${item.id}/`, {
        method: 'DELETE',
        headers: {
            'Content-type': 'application/json',
            'X-CSRFToken': csrftoken,
        }
    }).then((response) => {
        listStudent()
    })
}