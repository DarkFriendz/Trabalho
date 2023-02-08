function lineSelect(checkbox, id) {
    const Select = document.getElementById("Select")
    if(checkbox.checked == true) {
        if(Select.value == "None") {
            Select.value = ""+id+":"
        } else {
            Select.value = Select.value+id+":"
        }
        console.log(Select.value)
    } else {
        if (Select.value[1] != 'undefined') {
            value = Select.value.replace(id+".", "")
            if (value == "") {
                Select.value = "None"
            } else {
                Select.value = value
            }
            console.log(Select.value)
        } else {
            Select.value = "None"
        }
    }
}

function addTarefas(x) {
    const form = document.getElementById("addForm")
    if (x == 0) {
        form.style.display = "block"
    } else {
        form.style.display = "none"
    }
}

function pesquisar(x) {
    alert(x)
}