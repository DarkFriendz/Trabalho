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

function editTarefa(x, id) {
    const form = document.getElementById("editForm")
    if (x == 0) {
        document.getElementById("editId").value = id
        document.getElementById("editTitle").value = document.getElementById(id+"T").textContent
        document.getElementById("editDescription").value = document.getElementById(id+"D").textContent
        prazo = document.getElementById(id+"P").textContent.replace("/", "-")
        prazo = prazo.replace("/", "-")
        prazo = prazo.replace(" ", "T")
        document.getElementById("editPrazo").value = prazo
        //form.style.display = "Block"
    } else {
        document.getElementById("editId").value = ""
        document.getElementById("editTitle").value = "Vazio"
        document.getElementById("editDescription").value = "Vazio"
        document.getElementById("editPrazo").value = ""
        //form.style.display = "none"
    }
}

function pesquisar(x) {
    alert(x)
}