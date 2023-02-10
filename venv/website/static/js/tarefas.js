function lineSelect(checkbox, id) {
    const Select = document.getElementById("Select")
    if(checkbox.checked == true) {
        if(Select.value == "None") {
            Select.value = ""+id+":"
        } else {
            Select.value = Select.value+id+":"
        }
    } else {
        if (Select.value[1] != 'undefined') {
            value = Select.value.replace(id+".", "")
            if (value == "") {
                Select.value = "None"
            } else {
                Select.value = value
            }
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

const Filter = document.getElementById("Filter")
const Pesquisar = document.getElementById("Pesquisar")
const PesquisarDate = document.getElementById("PesquisarDate")

Filter.addEventListener("change", function() {
    const all = document.getElementById("All").value.split(":")
    for (line in all) {
        if (line != 0) {
            select = document.getElementById(line+"L")
            select.style.display = "table-row"
        }
    }

    Pesquisar.value = ""
    PesquisarDate.value = ""

    switch (Filter.value) {
        case "0":
            Pesquisar.style.display = "block"
            PesquisarDate.style.display = "None"
        break;
        case "1":
            Pesquisar.style.display = "block"
            PesquisarDate.style.display = "None"
        break;
        case "2":
            Pesquisar.style.display = "None"
            PesquisarDate.style.display = "block"
        break;
        case "3":
            Pesquisar.style.display = "None"
            PesquisarDate.style.display = "block"
        break;
        case "4":
            Pesquisar.style.display = "None"
            PesquisarDate.style.display = "block"
        break;
        case "5":
            Pesquisar.style.display = "None"
            PesquisarDate.style.display = "None"
            for (line in all) {
                if (line != 0) {
                    select = document.getElementById(line+"L")
                    if (select.className != "lineFeita") {
                        select.style.display = "None"
                    }
                }
            }
        break;
        case "6":
            Pesquisar.style.display = "None"
            PesquisarDate.style.display = "None"
            for (line in all) {
                if (line != 0) {
                    select = document.getElementById(line+"L")
                    if (select.className != "lineExpired") {
                        select.style.display = "None"
                    }
                }
            }
        break;
        default:
            Pesquisar.style.display = "block"
            PesquisarDate.style.display = "None"
        break;
    }
})

Pesquisar.addEventListener("input", function () {
    const all = document.getElementById("All").value.split(":")
    switch (Filter.value) {
        case '0':
            value = Pesquisar.value.toLowerCase()
            for (line in all) {
                if (line != 0) {
                    select = document.getElementById(line+"T").textContent.toLowerCase()
                    select = select.split(value)
                    if (!select[1]) {
                        document.getElementById(line+"L").style.display = "None"
                    }
                    else {
                        document.getElementById(line+"L").style.display = "table-row"
                    }
                }
            }
        break;
        case '1':
            value = Pesquisar.value.toLowerCase()
            for (line in all) {
                if (line != 0) {
                    select = document.getElementById(line+"D").textContent.toLowerCase()
                    select = select.split(value)
                    if (!select[1]) {
                        document.getElementById(line+"L").style.display = "None"
                    }
                    else {
                        document.getElementById(line+"L").style.display = "table-row"
                    }
                }
            }
        break;
    }
})

PesquisarDate.addEventListener("input", function () {
    const all = document.getElementById("All").value.split(":")
    switch (Filter.value) {
        case '2':
            for (line in all) {
                if (line != 0) {
                    select = PesquisarDate.value.split("T")
                    select = select[0].replace("-", "/")
                    select = select.replace("-", "/")
                    value = document.getElementById(line+"C").textContent.split(" ")
                    if (select != value[0]) {
                        select = document.getElementById(line+"L")
                        select.style.display = "none"
                    } else {
                        select = document.getElementById(line+"L")
                        select.style.display = "table-row"
                    }
                }
            }
        break;
        case '3':
            for (line in all) {
                if (line != 0) {
                    select = PesquisarDate.value.split("T")
                    select = select[0].replace("-", "/")
                    select = select.replace("-", "/")
                    value = document.getElementById(line+"P").textContent.split(" ")
                    if (select != value[0]) {
                        select = document.getElementById(line+"L")
                        select.style.display = "none"
                    } else {
                        select = document.getElementById(line+"L")
                        select.style.display = "table-row"
                    }
                }
            }
        break;
        case '4':
            for (line in all) {
                if (line != 0) {
                    select = PesquisarDate.value.split("T")
                    select = select[0].replace("-", "/")
                    select = select.replace("-", "/")
                    value = document.getElementById(line+"E").textContent.split(" ")
                    if (select != value[0]) {
                        select = document.getElementById(line+"L")
                        select.style.display = "none"
                    } else {
                        select = document.getElementById(line+"L")
                        select.style.display = "table-row"
                    }
                }
            }
        break;
    }
})